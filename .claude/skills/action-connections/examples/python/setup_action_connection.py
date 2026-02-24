"""
Datadog Action Connection Setup

Provides functions to automate the setup of Datadog Action Connections for AWS.
Designed to be imported and used in Lambda functions or other Python code.

Main function: setup_datadog_action_connection()

Workflow:
1. Creates an application key with actions scope
2. Creates an AWS action connection in Datadog
3. Updates the IAM role trust policy with the external ID from Datadog

Example usage with XA_Session pattern:
    from datadog_helpers.setup_action_connection import setup_datadog_action_connection

    # Get XA session for AWS API calls (GameDay pattern)
    xa_session = quests_api_client.assume_team_ops_role(team_id)

    response = setup_datadog_action_connection(
        api_key=os.environ['DD_API_KEY'],
        app_key=os.environ['DD_APP_KEY'],
        role_arn=cfn_outputs['DatadogActionRoleArn'],
        aws_session=xa_session  # Pass session for STS/IAM calls
    )

    if response.success:
        external_id = response.data['external_id']
        connection_id = response.data['connection_id']
    else:
        logger.error(response.message)
"""

import os
import json
import time
import boto3
import requests
from datadog_helpers.datadog_helpers import DatadogResponse, build_headers, BASE_URL, DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES


# Datadog's AWS account ID for action connections
# This is the account that will assume the role in your AWS account
DATADOG_AWS_ACCOUNT_ID = "464622532012"


def create_app_key_with_actions_scope(
    api_key: str,
    app_key: str,
    key_name: str = "DatadogActionsKey",
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create a new Datadog application key with App Builder & Workflow Automation scopes.

    Scopes include:
    - connections_read: List and view available connections
    - connections_write: Create and delete connections
    - workflows_read: View workflows
    - workflows_run: Run workflows
    - workflows_write: Create, edit, and delete workflows
    - apps_run: View and run Apps in App Builder
    - apps_write: Create, edit, and delete Apps in App Builder

    Args:
        api_key: Datadog API key
        app_key: Existing Datadog application key (with permission to create keys)
        key_name: Name for the new application key
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with the new app key in data["key"]
    """
    headers = build_headers(api_key, app_key)

    # Add random suffix to ensure unique key name on every run
    import random
    random_suffix = random.randint(1000, 9999)
    unique_key_name = f"{key_name}_{random_suffix}"

    # App Builder & Workflow Automation scopes
    scopes = [
    "api_keys_delete",
    "api_keys_read",
    "api_keys_write",
    "apps_datastore_manage",
    "apps_datastore_read",
    "apps_datastore_write",
    "apps_run",
    "apps_write",
    "aws_configuration_edit",
    "aws_configuration_read",
    "aws_configurations_manage",
    "client_tokens_read",
    "client_tokens_write",
    "connection_groups_read",
    "connection_groups_write",
    "connections_read",
    "connections_resolve",
    "connections_write",
    "on_prem_runner_read",
    "on_prem_runner_use",
    "on_prem_runner_write",
    "org_app_keys_read",
    "org_app_keys_write",
    "user_app_keys",
    "workflows_read",
    "workflows_run",
    "workflows_write"
  ]

    payload = {
        "data": {
            "type": "application_keys",
            "attributes": {
                "name": unique_key_name,
                "scopes": scopes
            }
        }
    }

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/current_user/application_keys",
                headers=headers,
                json=payload,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 201:
                response_data = response.json()
                new_app_key = response_data.get("data", {}).get("attributes", {}).get("key", "")

                return DatadogResponse(
                    success=True,
                    status_code=201,
                    message=f"Created app key with actions scope: {unique_key_name}",
                    data={
                        "key": new_app_key,
                        "id": response_data.get("data", {}).get("id", ""),
                        "full_response": response_data
                    }
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to create app key: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error creating app key: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to create app key after {max_retries} retries"
    )


def create_aws_action_connection(
    api_key: str,
    app_key: str,
    connection_name: str,
    role_arn: str,
    aws_session=None,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create an AWS action connection in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key with actions scope
        connection_name: Name for the action connection
        role_arn: ARN of the AWS IAM role to assume (will extract role name)
        aws_session: Optional boto3 Session object (for XA_Session pattern)
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with connection details including external_id
    """
    headers = build_headers(api_key, app_key)

    # Get AWS account ID and region from execution context
    try:
        if aws_session:
            sts_client = aws_session.client('sts')
        else:
            sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Failed to get AWS account ID: {e}"
        )

    region = os.environ.get('AWS_REGION', os.environ.get('AWS_DEFAULT_REGION', 'us-east-1'))

    # Extract role name from ARN (e.g., "arn:aws:iam::123456789012:role/RoleName" -> "RoleName")
    role_name = role_arn.split('/')[-1] if '/' in role_arn else role_arn

    payload = {
        "data": {
            "type": "action_connection",
            "attributes": {
                "name": connection_name,
                "integration": {
                    "type": "aws",
                    "credentials": {
                        "type": "awsassumerole",
                        "role": role_name,
                        "account_id": account_id
                    }
                }
            }
        }
    }

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/actions/connections",
                headers=headers,
                json=payload,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 201:
                response_data = response.json()
                connection_id = response_data.get("data", {}).get("id", "")

                # External ID is in a different API endpoint: custom_connections
                # This is necessary because the public actions/connections API doesn't return the external_id
                try:
                    get_response = requests.get(
                        f"{BASE_URL}/api/v2/connection/custom_connections/{connection_id}",
                        headers=headers,
                        timeout=DEFAULT_TIMEOUT
                    )

                    if get_response.status_code == 200:
                        get_data = get_response.json()
                        # Path: data.attributes.data.aws.assumeRole.externalId
                        external_id = (get_data.get("data", {})
                                      .get("attributes", {})
                                      .get("data", {})
                                      .get("aws", {})
                                      .get("assumeRole", {})
                                      .get("externalId", ""))
                    else:
                        external_id = ""
                except Exception as e:
                    external_id = ""

                return DatadogResponse(
                    success=True,
                    status_code=201,
                    message=f"Created action connection: {connection_name}",
                    data={
                        "connection_id": connection_id,
                        "external_id": external_id,
                        "full_response": response_data
                    }
                )
            elif response.status_code == 409:
                return DatadogResponse(
                    success=True,
                    status_code=409,
                    message=f"Action connection already exists: {connection_name}"
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to create action connection: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error creating action connection: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to create action connection after {max_retries} retries"
    )


def set_connection_restriction_policy(
    api_key: str,
    app_key: str,
    connection_id: str,
    org_id: str,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Set restriction policy for an action connection to allow org-wide editor access.

    This makes the connection accessible to all users in the organization,
    not just the creator.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        connection_id: Action connection ID
        org_id: Datadog organization ID
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)

    payload = {
        "data": {
            "id": f"connection:{connection_id}",
            "type": "restriction_policy",
            "attributes": {
                "bindings": [
                    {
                        "relation": "editor",
                        "principals": [
                            f"org:{org_id}"
                        ]
                    }
                ]
            }
        }
    }

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/restriction_policy/connection:{connection_id}",
                headers=headers,
                json=payload,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code in [200, 201]:
                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"Set restriction policy for connection {connection_id}"
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to set restriction policy: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error setting restriction policy: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to set restriction policy after {max_retries} retries"
    )


def verify_connection_ready(
    api_key: str,
    app_key: str,
    connection_id: str,
    max_wait_seconds: int = 30
) -> DatadogResponse:
    """
    Poll the connection endpoint to verify it's fully created and accessible.

    This prevents race conditions where apps try to use a connection
    before it's fully propagated in Datadog's system.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key (with actions scope)
        connection_id: Action connection ID to verify
        max_wait_seconds: Maximum time to wait in seconds

    Returns:
        DatadogResponse indicating if connection is ready
    """
    headers = build_headers(api_key, app_key)

    start_time = time.time()
    wait_interval = 2  # Start with 2 seconds

    while (time.time() - start_time) < max_wait_seconds:
        try:
            response = requests.get(
                f"{BASE_URL}/api/v2/actions/connections/{connection_id}",
                headers=headers,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 200:
                return DatadogResponse(
                    success=True,
                    status_code=200,
                    message=f"Connection {connection_id} is ready",
                    data=response.json()
                )

            # If not ready yet, wait with exponential backoff
            time.sleep(wait_interval)
            wait_interval = min(wait_interval * 1.5, 8)  # Max 8 seconds between retries

        except Exception as e:
            # Continue polling even on exceptions
            time.sleep(wait_interval)
            wait_interval = min(wait_interval * 1.5, 8)

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Connection {connection_id} not ready after {max_wait_seconds}s"
    )


def ensure_iam_role(
    role_name: str,
    external_id: str = "placeholder",
    aws_session=None,
    datadog_account_id: str = DATADOG_AWS_ACCOUNT_ID
) -> DatadogResponse:
    """
    Ensure an IAM role exists for Datadog action connections.

    If the role already exists, returns it. If not, creates it with a trust
    policy allowing Datadog's AWS account to assume it.

    Args:
        role_name: Name for the IAM role
        external_id: External ID for the trust policy (placeholder until connection is created)
        aws_session: Optional boto3 Session object (for XA_Session pattern)
        datadog_account_id: Datadog's AWS account ID (default: 464622532012)

    Returns:
        DatadogResponse with role_name, role_arn, and created flag
    """
    try:
        if aws_session:
            iam_client = aws_session.client('iam')
        else:
            iam_client = boto3.client('iam')

        # Check if role already exists
        try:
            role = iam_client.get_role(RoleName=role_name)
            return DatadogResponse(
                success=True,
                status_code=200,
                message=f"IAM role already exists: {role_name}",
                data={
                    "role_name": role_name,
                    "role_arn": role["Role"]["Arn"],
                    "created": False
                }
            )
        except iam_client.exceptions.NoSuchEntityException:
            pass

        # Create the role with trust policy for Datadog
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{datadog_account_id}:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {
                            "sts:ExternalId": external_id
                        }
                    }
                }
            ]
        }

        role = iam_client.create_role(
            RoleName=role_name,
            Path="/datadog/",
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description=f"Datadog action connection role (auto-created)",
            MaxSessionDuration=3600
        )

        return DatadogResponse(
            success=True,
            status_code=201,
            message=f"Created IAM role: {role_name}",
            data={
                "role_name": role_name,
                "role_arn": role["Role"]["Arn"],
                "created": True
            }
        )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error ensuring IAM role: {e}"
        )


def update_role_permissions(
    role_name: str,
    permissions: list,
    policy_name: str = "DatadogActionPermissions",
    aws_session=None
) -> DatadogResponse:
    """
    Set the inline permissions policy on a dedicated IAM role.

    Each role is dedicated to one app/workflow, so this replaces (not merges)
    the policy with exactly the given permissions.

    Args:
        role_name: Name of the IAM role
        permissions: List of IAM permission strings (e.g., ["ec2:DescribeInstances"])
        policy_name: Name for the inline policy
        aws_session: Optional boto3 Session object

    Returns:
        DatadogResponse with role_name, policy_name, and permissions_count
    """
    try:
        if aws_session:
            iam_client = aws_session.client('iam')
        else:
            iam_client = boto3.client('iam')

        policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": sorted(permissions),
                    "Resource": "*"
                }
            ]
        }

        iam_client.put_role_policy(
            RoleName=role_name,
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )

        return DatadogResponse(
            success=True,
            status_code=200,
            message=f"Updated permissions for role: {role_name}",
            data={
                "role_name": role_name,
                "policy_name": policy_name,
                "permissions_count": len(permissions)
            }
        )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error updating role permissions: {e}"
        )


def update_role_trust_policy(
    role_name: str,
    external_id: str,
    aws_session=None,
    datadog_account_id: str = DATADOG_AWS_ACCOUNT_ID
) -> DatadogResponse:
    """
    Update the IAM role trust policy to include Datadog's external ID.

    Args:
        role_name: Name of the IAM role to update
        external_id: External ID from Datadog action connection
        aws_session: Optional boto3 Session object (for XA_Session pattern)
        datadog_account_id: Datadog's AWS account ID (default: 464622532012)

    Returns:
        DatadogResponse with operation result
    """
    try:
        if aws_session:
            iam_client = aws_session.client('iam')
        else:
            iam_client = boto3.client('iam')

        # Create the trust policy document
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{datadog_account_id}:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {
                            "sts:ExternalId": external_id
                        }
                    }
                }
            ]
        }

        # Update the role's trust policy
        iam_client.update_assume_role_policy(
            RoleName=role_name,
            PolicyDocument=json.dumps(trust_policy)
        )

        return DatadogResponse(
            success=True,
            status_code=200,
            message=f"Updated trust policy for role: {role_name}",
            data={
                "role_name": role_name,
                "external_id": external_id,
                "datadog_account_id": datadog_account_id
            }
        )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error updating role trust policy: {e}"
        )


def setup_datadog_action_connection(
    api_key: str,
    app_key: str,
    role_arn: str = None,
    aws_session=None,
    role_name: str = "DatadogActionRole",
    connection_name: str = "DatadogAWSConnection",
    app_key_name: str = "DatadogActionsKey",
    org_id: str = None,
    permissions: list = None
) -> DatadogResponse:
    """
    Complete setup workflow for Datadog action connection.

    This function orchestrates the setup process:
    Step 0:   Ensure IAM role exists (auto-creates if missing)
    Step 0.5: Scope role permissions (if permissions list provided)
    Step 1:   Creates an application key with actions scope
    Step 2:   Creates an AWS action connection in Datadog
    Step 3:   Updates the IAM role trust policy with the external ID
    Step 4:   Sets connection restriction policy (makes it org-wide accessible)
    Step 5:   Verifies connection is ready and accessible

    Args:
        api_key: Datadog API key
        app_key: Existing Datadog application key
        role_arn: ARN of the AWS IAM role (optional if role_name provided — will be constructed)
        aws_session: Optional boto3 Session object (for XA_Session pattern)
        role_name: Name of the IAM role (for trust policy update and auto-creation)
        connection_name: Name for the action connection
        app_key_name: Name for the new app key with actions scope
        org_id: Datadog organization ID (fetched automatically if not provided)
        permissions: Optional list of IAM permissions to scope the role to (least-privilege)

    Returns:
        DatadogResponse with complete setup results in data dict:
        {
            "steps_completed": List[str],
            "app_key_id": str,
            "actions_app_key": str,
            "connection_id": str,
            "external_id": str,
            "role_name": str,
            "role_arn": str,
            "org_id": str
        }
    """
    results = {
        "steps_completed": [],
        "app_key_id": None,
        "actions_app_key": None,
        "connection_id": None,
        "external_id": None,
        "role_name": role_name,
        "role_arn": role_arn,
        "org_id": org_id
    }

    # Step 0: Ensure IAM role exists
    role_response = ensure_iam_role(role_name, aws_session=aws_session)
    if not role_response.success:
        return DatadogResponse(
            success=False,
            status_code=role_response.status_code,
            message=f"Step 0 failed: {role_response.message}",
            data=results
        )

    results["role_arn"] = role_response.data["role_arn"]
    role_arn = role_response.data["role_arn"]
    if role_response.data["created"]:
        results["steps_completed"].append("iam_role_created")
    else:
        results["steps_completed"].append("iam_role_exists")

    # Step 0.5: Scope role permissions (if provided)
    if permissions:
        perm_response = update_role_permissions(
            role_name, permissions, aws_session=aws_session
        )
        if not perm_response.success:
            return DatadogResponse(
                success=False,
                status_code=perm_response.status_code,
                message=f"Step 0.5 failed: {perm_response.message}",
                data=results
            )
        results["steps_completed"].append("role_permissions_scoped")

    # Step 1: Create app key with actions scope
    app_key_response = create_app_key_with_actions_scope(api_key, app_key, app_key_name)

    if not app_key_response.success:
        return DatadogResponse(
            success=False,
            status_code=app_key_response.status_code,
            message=f"Step 1 failed: {app_key_response.message}",
            data=results
        )

    results["app_key_id"] = app_key_response.data["id"]
    results["actions_app_key"] = app_key_response.data["key"]
    results["steps_completed"].append("app_key_created")

    # Use the new app key for subsequent calls
    actions_app_key = app_key_response.data["key"]

    # Step 2: Create action connection
    connection_response = create_aws_action_connection(
        api_key,
        actions_app_key,
        connection_name,
        role_arn,
        aws_session=aws_session
    )

    if not connection_response.success:
        return DatadogResponse(
            success=False,
            status_code=connection_response.status_code,
            message=f"Step 2 failed: {connection_response.message}",
            data=results
        )

    # If connection already exists, retrieve its ID and external_id
    if connection_response.status_code == 409:
        results["steps_completed"].append("connection_already_exists")

        # Try to find the existing connection and retrieve external_id
        try:
            list_response = requests.get(
                f"{BASE_URL}/api/v2/actions/connections",
                headers=build_headers(api_key, actions_app_key),
                timeout=DEFAULT_TIMEOUT
            )

            if list_response.status_code == 200:
                connections = list_response.json().get("data", [])
                for conn in connections:
                    if conn.get("attributes", {}).get("name") == connection_name:
                        results["connection_id"] = conn.get("id")
                        break

                # If we found the connection, retrieve its external_id
                if results["connection_id"]:
                    try:
                        get_response = requests.get(
                            f"{BASE_URL}/api/v2/connection/custom_connections/{results['connection_id']}",
                            headers=build_headers(api_key, actions_app_key),
                            timeout=DEFAULT_TIMEOUT
                        )

                        if get_response.status_code == 200:
                            get_data = get_response.json()
                            # Path: data.attributes.data.aws.assumeRole.externalId
                            results["external_id"] = (get_data.get("data", {})
                                                     .get("attributes", {})
                                                     .get("data", {})
                                                     .get("aws", {})
                                                     .get("assumeRole", {})
                                                     .get("externalId", ""))
                    except Exception as e:
                        print(f"Warning: Could not retrieve external_id for existing connection: {e}")

        except Exception as e:
            print(f"Warning: Could not retrieve existing connection ID: {e}")

        # If we couldn't get the external_id, we cannot proceed safely
        if not results.get("external_id"):
            return DatadogResponse(
                success=False,
                status_code=409,
                message="Connection already exists but could not retrieve external_id. Manual trust policy configuration may be required.",
                data=results
            )

        # Continue to trust policy update instead of returning early
        # Fall through to Step 3 below
    else:
        # New connection created - set connection details from response
        results["connection_id"] = connection_response.data["connection_id"]
        results["external_id"] = connection_response.data["external_id"]
        results["steps_completed"].append("connection_created")

    # Step 3: Update IAM role trust policy
    trust_policy_response = update_role_trust_policy(
        role_name,
        results["external_id"],
        aws_session=aws_session
    )

    if not trust_policy_response.success:
        return DatadogResponse(
            success=False,
            status_code=trust_policy_response.status_code,
            message=f"Step 3 failed: {trust_policy_response.message}",
            data=results
        )

    results["steps_completed"].append("trust_policy_updated")

    # Step 4: Get org ID if not provided
    if not org_id:
        try:
            org_response = requests.get(
                f"{BASE_URL}/api/v2/current_user",
                headers=build_headers(api_key, app_key),
                timeout=DEFAULT_TIMEOUT
            )
            if org_response.status_code == 200:
                org_id = (org_response.json()
                         .get("data", {})
                         .get("relationships", {})
                         .get("org", {})
                         .get("data", {})
                         .get("id", ""))
                results["org_id"] = org_id
        except Exception as e:
            # Non-fatal - continue without setting restriction policy
            print(f"Warning: Could not fetch org ID: {e}")

    # Step 5: Set connection restriction policy (make it org-wide)
    # NOTE: As of this implementation, action connections may not support
    # restriction policies in the same way as app-builder apps.
    # Connections may be creator-scoped by default or use a different sharing mechanism.
    # This step attempts to set the policy but failures are non-fatal.
    if org_id:
        policy_response = set_connection_restriction_policy(
            api_key,
            app_key,
            results["connection_id"],
            org_id
        )

        if policy_response.success:
            results["steps_completed"].append("restriction_policy_set")
        else:
            # Non-fatal warning - connection may still work or may be creator-scoped
            # This is expected if action connections don't support restriction policies
            print(f"Info: Restriction policy not set - {policy_response.message}")

    # Step 6: Verify connection is ready
    verify_response = verify_connection_ready(
        api_key,
        actions_app_key,
        results["connection_id"],
        max_wait_seconds=30
    )

    if verify_response.success:
        results["steps_completed"].append("connection_verified")
    else:
        # Non-fatal warning - connection may still work
        print(f"Warning: Could not verify connection: {verify_response.message}")

    return DatadogResponse(
        success=True,
        status_code=200,
        message="Datadog action connection setup completed successfully",
        data=results
    )
