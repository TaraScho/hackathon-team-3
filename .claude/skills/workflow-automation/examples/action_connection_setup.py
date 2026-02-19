# Extracted from configure_datadog.py - only the AWS action connection setup functions.
# Original: aws-gameday-quest-development/walkup-quest-2026/team_lambda_source/configure_datadog.py

import urllib3
import json
import os
import boto3

DD_URL = "https://api.datadoghq.com/api"

http = urllib3.PoolManager()

# Datadog's AWS account ID for action connections
DATADOG_AWS_ACCOUNT_ID = "464622532012"


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
    response = http.request(
        method,
        url,
        headers=headers,
        body=json.dumps(body) if body else None,
    )
    return response


def create_aws_action_connection(app_key, role_arn, connection_name="DatadogWorkflowAutomationConnection"):
    """
    Create an AWS action connection in Datadog.

    Args:
        app_key: Datadog application key (must have actions API access enabled)
        role_arn: ARN of the AWS IAM role to assume
        connection_name: Name for the action connection

    Returns:
        dict with "connection_id" and "external_id", or None on failure
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": DD_API_KEY,
        "DD-APPLICATION-KEY": app_key,
    }

    # Get AWS account ID
    try:
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
    except Exception as e:
        print(f"Failed to get AWS account ID: {e}")
        return None

    # Extract role name from ARN
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

    try:
        response = make_request(f"{DD_URL}/v2/actions/connections", "POST", headers, payload)

        if response.status == 201:
            response_data = json.loads(response.data.decode("utf-8"))
            connection_id = response_data.get("data", {}).get("id", "")

            # Get external ID from custom_connections endpoint
            try:
                get_response = make_request(
                    f"{DD_URL}/v2/connection/custom_connections/{connection_id}",
                    "GET",
                    headers
                )
                if get_response.status == 200:
                    get_data = json.loads(get_response.data.decode("utf-8"))
                    external_id = (get_data.get("data", {})
                                  .get("attributes", {})
                                  .get("data", {})
                                  .get("aws", {})
                                  .get("assumeRole", {})
                                  .get("externalId", ""))
                else:
                    external_id = ""
            except Exception as e:
                print(f"Warning: Could not retrieve external_id: {e}")
                external_id = ""

            print(f"Created action connection: {connection_name} (ID: {connection_id}, External ID: {external_id})")
            return {"connection_id": connection_id, "external_id": external_id}

        elif response.status == 409:
            print(f"Action connection '{connection_name}' already exists, retrieving details...")

            # List all connections and find ours
            try:
                list_response = make_request(f"{DD_URL}/v2/actions/connections", "GET", headers)
                if list_response.status == 200:
                    connections = json.loads(list_response.data.decode("utf-8")).get("data", [])
                    for conn in connections:
                        if conn.get("attributes", {}).get("name") == connection_name:
                            connection_id = conn.get("id")

                            # Get external_id
                            get_response = make_request(
                                f"{DD_URL}/v2/connection/custom_connections/{connection_id}",
                                "GET",
                                headers
                            )
                            if get_response.status == 200:
                                get_data = json.loads(get_response.data.decode("utf-8"))
                                external_id = (get_data.get("data", {})
                                              .get("attributes", {})
                                              .get("data", {})
                                              .get("aws", {})
                                              .get("assumeRole", {})
                                              .get("externalId", ""))

                                print(f"Found existing connection: {connection_name} (ID: {connection_id}, External ID: {external_id})")
                                return {"connection_id": connection_id, "external_id": external_id}
            except Exception as e:
                print(f"Warning: Could not retrieve existing connection: {e}")

            print(f"Connection already exists but could not retrieve details")
            return None
        else:
            print(f"Failed to create action connection: {response.status} {response.data.decode('utf-8')}")
            return None
    except Exception as e:
        print(f"Error creating action connection: {e}")
        return None


def update_role_trust_policy(role_name, external_id):
    """
    Update the IAM role trust policy to allow Datadog workflow automation to assume the role.

    Args:
        role_name: Name of the IAM role
        external_id: External ID from Datadog action connection

    Returns:
        True on success, False on failure
    """
    try:
        iam_client = boto3.client('iam')

        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{DATADOG_AWS_ACCOUNT_ID}:root"
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

        iam_client.update_assume_role_policy(
            RoleName=role_name,
            PolicyDocument=json.dumps(trust_policy)
        )

        print(f"Updated trust policy for role: {role_name} with external ID: {external_id}")
        return True
    except Exception as e:
        print(f"Error updating role trust policy: {e}")
        return False


def setup_aws_action_connection(role_arn):
    """
    Complete workflow to set up AWS action connection for Datadog workflow automation.

    Args:
        role_arn: ARN of the DatadogActionRole IAM role

    Returns:
        True on success, False on failure
    """
    print("\n--- Setting up AWS Action Connection ---")

    role_name = role_arn.split('/')[-1] if '/' in role_arn else role_arn

    # Step 1: Create AWS action connection
    print("Step 1: Creating AWS action connection...")
    connection_data = create_aws_action_connection(DD_APP_KEY, role_arn)
    if not connection_data or not connection_data.get("external_id"):
        print("Failed to create action connection or retrieve external ID")
        return False

    # Step 2: Update role trust policy
    print("Step 2: Updating IAM role trust policy...")
    if not update_role_trust_policy(role_name, connection_data["external_id"]):
        print("Failed to update role trust policy")
        return False

    print("✓ AWS action connection setup completed successfully")
    return True
