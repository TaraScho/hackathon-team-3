# Copyright 2025 Amazon.com and its affiliates; all rights reserved.
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# Creates Datadog workflow automations for Stickerlandia quest challenges.
# Run locally: source .env && python walkup-quest-2026/team_lambda_source/create_workflows.py
# Integrated with configure_datadog.py for automated setup during quest deployment.

import urllib3
import json
import os
import boto3

DD_URL = "https://api.datadoghq.com/api"
http = urllib3.PoolManager()


def get_datadog_secrets():
    """Read DD API/APP keys from Secrets Manager, falling back to env vars for local testing."""
    api_key = os.getenv("DD_API_KEY")
    app_key = os.getenv("DD_APP_KEY")
    if api_key and app_key:
        return api_key, app_key

    sm = boto3.client("secretsmanager")
    try:
        api_key = sm.get_secret_value(SecretId="datadog/api-key")["SecretString"]
        app_key = sm.get_secret_value(SecretId="datadog/app-key")["SecretString"]
    except Exception as e:
        print(f"Failed to read Datadog secrets from Secrets Manager: {e}")
        raise
    return api_key, app_key


DD_API_KEY, DD_APP_KEY = get_datadog_secrets()


def make_request(url, method="GET", headers=None, body=None):
    """Make HTTP request using urllib3."""
    response = http.request(
        method,
        url,
        headers=headers,
        body=json.dumps(body) if body else None,
    )
    return response


def get_connection_id_by_name(api_key, app_key, connection_name):
    """
    Look up AWS action connection ID by name.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        connection_name: Name of the connection to find

    Returns:
        connection_id (string) or None if not found
    """
    headers = {
        "Accept": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }

    try:
        response = make_request(f"{DD_URL}/v2/actions/connections", "GET", headers)

        if response.status == 200:
            connections = json.loads(response.data.decode("utf-8")).get("data", [])
            for conn in connections:
                if conn.get("attributes", {}).get("name") == connection_name:
                    connection_id = conn.get("id")
                    print(f"Found connection '{connection_name}': {connection_id}")
                    return connection_id
            print(f"Connection '{connection_name}' not found")
            return None
        else:
            print(f"Failed to list connections: {response.status} {response.data.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"Error looking up connection: {e}")
        return None


def get_attach_iam_policy_workflow_spec(connection_id, action_id="com.datadoghq.aws.iam.attachRolePolicy", add_monitor_trigger=False, monitor_id=None):
    """
    Generate workflow specification for "Attach IAM Policy" workflow.

    This workflow accepts a policy ARN and IAM role name,
    and attaches the policy to the role using AWS IAM API.

    Args:
        connection_id: UUID of the AWS action connection
        action_id: Action ID for attach role policy (default: com.datadoghq.aws.iam.attach_role_policy)
        add_monitor_trigger: If True, add a monitor trigger in addition to manual trigger
        monitor_id: Monitor ID to trigger from (required if add_monitor_trigger=True)

    Returns:
        dict containing the complete workflow specification
    """
    # Monitor trigger configuration
    # Empty monitorTrigger {} allows manual execution from UI
    # With monitorId, it triggers on specific monitor alerts
    if add_monitor_trigger and monitor_id:
        trigger = {
            "monitorTrigger": {
                "monitorId": str(monitor_id)
            },
            "startStepNames": [
                "attach_policy_to_role"
            ]
        }
    else:
        # Default: manual trigger (empty monitorTrigger)
        trigger = {
            "monitorTrigger": {},
            "startStepNames": [
                "attach_policy_to_role"
            ]
        }

    triggers = [trigger]

    return {
        "steps": [
            # Single step: Attach policy to role
            {
                "name": "attach_policy_to_role",
                "actionId": action_id,
                "connectionLabel": "AWS_ACTION_CONNECTION",
                "display": {
                    "bounds": {
                        "y": 188
                    }
                },
                "parameters": [
                    {
                        "name": "roleName",
                        "value": "{{ Trigger.role_name }}"
                    },
                    {
                        "name": "policyArn",
                        "value": "{{ Trigger.policy_arn }}"
                    }
                ]
            }
        ],

        # Connection configuration
        "connectionEnvs": [
            {
                "env": "default",
                "connections": [
                    {
                        "label": "AWS_ACTION_CONNECTION",
                        "connectionId": connection_id
                    }
                ]
            }
        ],

        # Input parameters (accessed via Trigger.*)
        "inputSchema": {
            "parameters": [
                {
                    "name": "policy_arn",
                    "label": "Policy ARN",
                    "type": "STRING",
                    "description": "ARN of the managed IAM policy to attach"
                },
                {
                    "name": "role_name",
                    "label": "IAM Role Name",
                    "type": "STRING",
                    "description": "Name of the IAM role (not ARN, just the name)"
                }
            ]
        },

        # Triggers (manual by default, optionally add monitor trigger)
        "triggers": triggers
    }


def create_attach_iam_policy_workflow(api_key, app_key, connection_id, monitor_id=None):
    """
    Create "Attach IAM Policy" workflow in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        connection_id: UUID of the AWS action connection
        monitor_id: Optional monitor ID to trigger the workflow (in addition to manual trigger)

    Returns:
        Workflow ID on success, None on failure
    """
    workflow_spec = get_attach_iam_policy_workflow_spec(
        connection_id,
        add_monitor_trigger=(monitor_id is not None),
        monitor_id=monitor_id
    )

    # Payload structure for Datadog Workflow API
    payload = {
        "data": {
            "type": "workflows",
            "attributes": {
                "name": "Attach IAM Policy",
                "description": "Attaches an AWS IAM managed policy to a role, user, or group. Use this to grant additional permissions to IAM entities.",
                "spec": workflow_spec
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }

    try:
        response = make_request(
            f"{DD_URL}/v2/workflows",
            "POST",
            headers,
            payload
        )

        if response.status in (200, 201):
            workflow_data = json.loads(response.data.decode("utf-8"))
            workflow_id = workflow_data.get("data", {}).get("id")
            print(f"✓ Created 'Attach IAM Policy' workflow: {workflow_id}")
            return workflow_id
        elif response.status == 409:
            print("Workflow 'Attach IAM Policy' already exists (409)")
            # TODO: Could retrieve existing workflow ID here
            return None
        else:
            print(f"Failed to create workflow: {response.status} {response.data.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"Error creating workflow: {e}")
        return None


def get_ecs_rollback_workflow_spec(connection_id, region, add_monitor_trigger=False, monitor_id=None):
    """
    Generate workflow specification for "ECS Rollback Leaderboard" workflow.

    This workflow rolls back an ECS service to a specific image tag by:
    1. Describing the current task definition
    2. Transforming the image tag on the leaderboard container
    3. Registering a new task definition revision
    4. Updating the ECS service to use the new task definition

    Args:
        connection_id: UUID of the AWS action connection
        region: AWS region (e.g. 'us-east-1')
        add_monitor_trigger: If True, add a monitor trigger in addition to manual trigger
        monitor_id: Monitor ID to trigger from (required if add_monitor_trigger=True)

    Returns:
        dict containing the complete workflow specification
    """
    if add_monitor_trigger and monitor_id:
        trigger = {
            "monitorTrigger": {
                "monitorId": str(monitor_id)
            },
            "startStepNames": [
                "Describe_task_definition"
            ]
        }
    else:
        trigger = {
            "monitorTrigger": {},
            "startStepNames": [
                "Describe_task_definition"
            ]
        }

    triggers = [trigger]

    return {
        "steps": [
            {
                "name": "Describe_task_definition",
                "actionId": "com.datadoghq.aws.ecs.describeTaskDefinition",
                "connectionLabel": "AWS_ACTION_CONNECTION",
                "parameters": [
                    {
                        "name": "region",
                        "value": region
                    },
                    {
                        "name": "taskDefinition",
                        "value": "{{ Trigger.service_name }}"
                    }
                ],
                "outboundEdges": [
                    {
                        "nextStepName": "Transform_image_tag",
                        "branchName": "main"
                    }
                ],
                "display": {
                    "bounds": {
                        "x": 192,
                        "y": 192
                    }
                }
            },
            {
                "name": "Transform_image_tag",
                "actionId": "com.datadoghq.datatransformation.func",
                "parameters": [
                    {
                        "name": "script",
                        "value": "const taskDef = $.Steps.Describe_task_definition.taskDefinition;\nconst newTag = $.Trigger.image_tag;\nconst containerDefs = taskDef.containerDefinitions.map(container => {\n  if (container.name === 'leaderboard') {\n    const imageBase = container.image.split(':')[0];\n    container.image = imageBase + ':' + newTag;\n  }\n  return container;\n});\nreturn containerDefs;"
                    }
                ],
                "outboundEdges": [
                    {
                        "nextStepName": "Register_task_definition",
                        "branchName": "main"
                    }
                ],
                "display": {
                    "bounds": {
                        "x": 192,
                        "y": 384
                    }
                }
            },
            {
                "name": "Register_task_definition",
                "actionId": "com.datadoghq.aws.ecs.registerTaskDefinition",
                "connectionLabel": "AWS_ACTION_CONNECTION",
                "parameters": [
                    {
                        "name": "containerDefinitions",
                        "value": "{{ Steps.Transform_image_tag.data }}"
                    },
                    {
                        "name": "cpu",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.cpu }}"
                    },
                    {
                        "name": "ephemeralStorage",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.ephemeralStorage }}"
                    },
                    {
                        "name": "executionRoleArn",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.executionRoleArn }}"
                    },
                    {
                        "name": "family",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.family }}"
                    },
                    {
                        "name": "inferenceAccelerators",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.inferenceAccelerators }}"
                    },
                    {
                        "name": "ipcMode",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.ipcMode }}"
                    },
                    {
                        "name": "memory",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.memory }}"
                    },
                    {
                        "name": "networkMode",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.networkMode }}"
                    },
                    {
                        "name": "pidMode",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.pidMode }}"
                    },
                    {
                        "name": "placementConstraints",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.placementConstraints }}"
                    },
                    {
                        "name": "proxyConfiguration",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.proxyConfiguration }}"
                    },
                    {
                        "name": "region",
                        "value": region
                    },
                    {
                        "name": "requiresCompatibilities",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.requiresCompatibilities }}"
                    },
                    {
                        "name": "runtimePlatform",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.runtimePlatform }}"
                    },
                    {
                        "name": "taskRoleArn",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.taskRoleArn }}"
                    },
                    {
                        "name": "volumes",
                        "value": "{{ Steps.Describe_task_definition.taskDefinition.volumes }}"
                    }
                ],
                "outboundEdges": [
                    {
                        "nextStepName": "Update_ECS_service",
                        "branchName": "main"
                    }
                ],
                "display": {
                    "bounds": {
                        "x": 192,
                        "y": 504
                    }
                }
            },
            {
                "name": "Update_ECS_service",
                "actionId": "com.datadoghq.aws.ecs.updateEcsService",
                "connectionLabel": "AWS_ACTION_CONNECTION",
                "parameters": [
                    {
                        "name": "cluster",
                        "value": "{{ Trigger.service_name }}"
                    },
                    {
                        "name": "forceNewDeployment",
                        "value": True
                    },
                    {
                        "name": "region",
                        "value": region
                    },
                    {
                        "name": "serviceName",
                        "value": "{{ Trigger.service_name }}"
                    },
                    {
                        "name": "taskDefinition",
                        "value": "{{ Steps.Register_task_definition.taskDefinition.taskDefinitionArn }}"
                    }
                ],
                "display": {
                    "bounds": {
                        "x": 192,
                        "y": 720
                    }
                }
            }
        ],

        "connectionEnvs": [
            {
                "env": "default",
                "connections": [
                    {
                        "label": "AWS_ACTION_CONNECTION",
                        "connectionId": connection_id
                    }
                ]
            }
        ],

        "inputSchema": {
            "parameters": [
                {
                    "name": "service_name",
                    "label": "Service Name",
                    "description": "The ECS service name (used for task definition family, service name, and cluster)",
                    "type": "STRING"
                },
                {
                    "name": "image_tag",
                    "label": "Image Tag",
                    "description": "The image tag to deploy, e.g. 1.0.0",
                    "type": "STRING"
                }
            ]
        },

        "triggers": triggers
    }


def create_ecs_rollback_workflow(api_key, app_key, connection_id, region, monitor_id=None):
    """
    Create "ECS Rollback Leaderboard" workflow in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        connection_id: UUID of the AWS action connection
        region: AWS region for ECS API calls
        monitor_id: Optional monitor ID to trigger the workflow

    Returns:
        Workflow ID on success, None on failure
    """
    workflow_spec = get_ecs_rollback_workflow_spec(
        connection_id,
        region,
        add_monitor_trigger=(monitor_id is not None),
        monitor_id=monitor_id
    )

    payload = {
        "data": {
            "type": "workflows",
            "attributes": {
                "name": "ECS Rollback Leaderboard",
                "description": "Rolls back the leaderboard ECS service to a specified image tag by registering a new task definition revision and updating the service.",
                "spec": workflow_spec
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }

    try:
        response = make_request(
            f"{DD_URL}/v2/workflows",
            "POST",
            headers,
            payload
        )

        if response.status in (200, 201):
            workflow_data = json.loads(response.data.decode("utf-8"))
            workflow_id = workflow_data.get("data", {}).get("id")
            print(f"✓ Created 'ECS Rollback Leaderboard' workflow: {workflow_id}")
            return workflow_id
        elif response.status == 409:
            print("Workflow 'ECS Rollback Leaderboard' already exists (409)")
            return None
        else:
            print(f"Failed to create ECS rollback workflow: {response.status} {response.data.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"Error creating ECS rollback workflow: {e}")
        return None


def create_ecs_workflows(connection_name="DatadogWorkflowAutomationConnection", monitor_id=None):
    """
    Create Datadog workflow automations for ECS operations.
    Requires AWS action connection to already exist.

    Args:
        connection_name: Name of the AWS action connection
        monitor_id: Optional monitor ID to trigger the workflow automatically

    Returns:
        True on success, False on failure
    """
    print("\n--- Creating ECS Workflow Automations ---")

    connection_id = get_connection_id_by_name(
        DD_API_KEY,
        DD_APP_KEY,
        connection_name
    )

    if not connection_id:
        print(f"Error: Could not find connection '{connection_name}'")
        print("Make sure setup_aws_action_connection() has been called first")
        return False

    region = os.environ.get("AWS_REGION", "us-east-1")

    workflow_id = create_ecs_rollback_workflow(
        DD_API_KEY,
        DD_APP_KEY,
        connection_id,
        region,
        monitor_id=monitor_id
    )

    if workflow_id:
        print(f"✓ ECS workflow automation setup complete")
        return True
    else:
        print("Failed to create ECS workflows")
        return False


def create_iam_workflows(connection_name="DatadogWorkflowAutomationConnection", monitor_id=None):
    """
    Create Datadog workflow automations for IAM operations.
    Requires AWS action connection to already exist.

    Args:
        connection_name: Name of the AWS action connection
        monitor_id: Optional monitor ID to trigger the workflow automatically when monitor alerts

    Returns:
        True on success, False on failure

    Usage:
        # Create workflow with manual trigger only:
        create_iam_workflows()

        # Create workflow that triggers on a specific monitor:
        create_iam_workflows(monitor_id=12345678)

    Monitor Trigger:
        When a monitor_id is provided, the workflow will be triggered automatically when
        that monitor transitions to Alert state. The workflow will still support manual
        execution from the Datadog UI.

        To find your monitor ID:
        1. Go to Monitors in Datadog UI
        2. Click on the monitor you want to trigger from
        3. The monitor ID is in the URL: /monitors/{monitor_id}
    """
    print("\n--- Creating IAM Workflow Automations ---")

    # Step 1: Lookup connection ID
    connection_id = get_connection_id_by_name(
        DD_API_KEY,
        DD_APP_KEY,
        connection_name
    )

    if not connection_id:
        print(f"Error: Could not find connection '{connection_name}'")
        print("Make sure setup_aws_action_connection() has been called first")
        return False

    # Step 2: Create workflows
    workflow_id = create_attach_iam_policy_workflow(
        DD_API_KEY,
        DD_APP_KEY,
        connection_id,
        monitor_id=monitor_id
    )

    if workflow_id:
        print(f"✓ IAM workflow automation setup complete")
        return True
    else:
        print("Failed to create IAM workflows")
        return False


if __name__ == "__main__":
    import sys

    if not DD_API_KEY or not DD_APP_KEY:
        print("ERROR: DD_API_KEY and DD_APP_KEY must be set. Run: source .env")
        exit(1)

    iam_ok = create_iam_workflows()
    ecs_ok = create_ecs_workflows()
    exit(0 if (iam_ok and ecs_ok) else 1)
