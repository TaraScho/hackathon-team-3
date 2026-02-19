#!/usr/bin/env python3
"""
Standalone script to set up Datadog AWS Action Connection for Stickerlandia.

This script orchestrates the complete workflow:
1. Creates an AWS action connection in Datadog
2. Updates the IAM role trust policy with the external ID from Datadog

Usage:
    # Set environment variables
    export DD_API_KEY="your-api-key"
    export DD_APP_KEY="your-app-key"
    export AWS_PROFILE="gameday"

    # Run the script
    python walkup-quest-2026/setup_aws_action_connection.py

Prerequisites:
    - DatadogActionRole IAM role must exist in AWS
    - DD_API_KEY and DD_APP_KEY must be set (DD_APP_KEY must have actions API access enabled)
    - AWS credentials must be configured

This script mirrors the implementation from gameday-reinvent-2025/central_lambda_source/datadog_helpers/setup_action_connection.py
"""

import os
import sys
import json
import time
import boto3
import urllib3
from dataclasses import dataclass
from typing import Optional, Dict

# Datadog configuration
DD_SITE = "datadoghq.com"
BASE_URL = f"https://api.{DD_SITE}"
DEFAULT_TIMEOUT = 10
DEFAULT_MAX_RETRIES = 3

# Datadog's AWS account ID for action connections
DATADOG_AWS_ACCOUNT_ID = "464622532012"

# Connection configuration for Stickerlandia
ROLE_NAME = "DatadogActionRole"
CONNECTION_NAME = "DatadogWorkflowAutomationConnection"

http = urllib3.PoolManager()


@dataclass
class DatadogResponse:
    """Structured response from Datadog API operations."""
    success: bool
    status_code: int
    message: str
    data: Optional[Dict] = None


def build_headers(api_key: str, app_key: str) -> Dict[str, str]:
    """Build standard Datadog API headers."""
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }


def make_request(url: str, method: str = "GET", headers: dict = None, body: dict = None):
    """Make HTTP request using urllib3."""
    response = http.request(
        method,
        url,
        headers=headers,
        body=json.dumps(body) if body else None,
    )
    return response


def create_aws_action_connection(
    api_key: str,
    app_key: str,
    connection_name: str,
    role_arn: str,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create an AWS action connection in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key with actions scope
        connection_name: Name for the action connection
        role_arn: ARN of the AWS IAM role to assume
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with connection details including external_id
    """
    headers = build_headers(api_key, app_key)

    # Get AWS account ID from execution context
    try:
        sts_client = boto3.client('sts')
        account_id = sts_client.get_caller_identity()['Account']
    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Failed to get AWS account ID: {e}"
        )

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

    for attempt in range(max_retries + 1):
        try:
            response = make_request(
                f"{BASE_URL}/api/v2/actions/connections",
                "POST",
                headers,
                payload
            )

            if response.status == 201:
                response_data = json.loads(response.data.decode("utf-8"))
                connection_id = response_data.get("data", {}).get("id", "")

                # External ID is in a different API endpoint: custom_connections
                try:
                    get_response = make_request(
                        f"{BASE_URL}/api/v2/connection/custom_connections/{connection_id}",
                        "GET",
                        headers
                    )

                    if get_response.status == 200:
                        get_data = json.loads(get_response.data.decode("utf-8"))
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
                    print(f"Warning: Could not retrieve external_id: {e}")
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
            elif response.status == 409:
                # Connection already exists - try to get its details
                print(f"Connection '{connection_name}' already exists, retrieving details...")

                try:
                    list_response = make_request(
                        f"{BASE_URL}/api/v2/actions/connections",
                        "GET",
                        headers
                    )

                    if list_response.status == 200:
                        connections = json.loads(list_response.data.decode("utf-8")).get("data", [])
                        for conn in connections:
                            if conn.get("attributes", {}).get("name") == connection_name:
                                connection_id = conn.get("id")

                                # Get external_id
                                get_response = make_request(
                                    f"{BASE_URL}/api/v2/connection/custom_connections/{connection_id}",
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

                                    return DatadogResponse(
                                        success=True,
                                        status_code=409,
                                        message=f"Connection already exists: {connection_name}",
                                        data={
                                            "connection_id": connection_id,
                                            "external_id": external_id
                                        }
                                    )
                except Exception as e:
                    print(f"Warning: Could not retrieve existing connection details: {e}")

                return DatadogResponse(
                    success=False,
                    status_code=409,
                    message=f"Connection already exists but could not retrieve external_id: {connection_name}"
                )
            else:
                error_msg = json.loads(response.data.decode("utf-8")).get("errors", [response.data.decode("utf-8")]) if response.data else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status,
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


def update_role_trust_policy(
    role_name: str,
    external_id: str,
    datadog_account_id: str = DATADOG_AWS_ACCOUNT_ID
) -> DatadogResponse:
    """
    Update the IAM role trust policy to include Datadog's external ID.

    Args:
        role_name: Name of the IAM role to update
        external_id: External ID from Datadog action connection
        datadog_account_id: Datadog's AWS account ID (default: 464622532012)

    Returns:
        DatadogResponse with operation result
    """
    try:
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
    role_name: str = ROLE_NAME,
    connection_name: str = CONNECTION_NAME
) -> DatadogResponse:
    """
    Complete setup workflow for Datadog action connection.

    This orchestrates the two-step process:
    1. Creates an AWS action connection in Datadog
    2. Updates the IAM role trust policy with the external ID

    Args:
        api_key: Datadog API key
        app_key: Datadog application key (must have actions API access enabled)
        role_name: Name of the IAM role
        connection_name: Name for the action connection

    Returns:
        DatadogResponse with complete setup results
    """
    print("=" * 70)
    print("Datadog AWS Action Connection Setup for Stickerlandia")
    print("=" * 70)
    print(f"Role Name: {role_name}")
    print(f"Connection Name: {connection_name}")
    print("=" * 70 + "\n")

    results = {
        "steps_completed": [],
        "connection_id": None,
        "external_id": None,
        "role_name": role_name
    }

    # Get role ARN
    try:
        iam_client = boto3.client('iam')
        role_response = iam_client.get_role(RoleName=role_name)
        role_arn = role_response['Role']['Arn']
        print(f"✓ Found IAM role: {role_arn}\n")
    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Failed to find IAM role '{role_name}': {e}",
            data=results
        )

    # Step 1: Create action connection
    print("Step 1: Creating AWS action connection...")
    connection_response = create_aws_action_connection(
        api_key,
        app_key,
        connection_name,
        role_arn
    )

    if not connection_response.success:
        return DatadogResponse(
            success=False,
            status_code=connection_response.status_code,
            message=f"Step 1 failed: {connection_response.message}",
            data=results
        )

    results["connection_id"] = connection_response.data["connection_id"]
    results["external_id"] = connection_response.data["external_id"]

    if connection_response.status_code == 409:
        results["steps_completed"].append("connection_already_exists")
    else:
        results["steps_completed"].append("connection_created")

    print(f"✓ {connection_response.message}")
    print(f"  Connection ID: {results['connection_id']}")
    print(f"  External ID: {results['external_id']}\n")

    # Step 2: Update IAM role trust policy
    print("Step 2: Updating IAM role trust policy...")
    trust_policy_response = update_role_trust_policy(
        role_name,
        results["external_id"]
    )

    if not trust_policy_response.success:
        return DatadogResponse(
            success=False,
            status_code=trust_policy_response.status_code,
            message=f"Step 2 failed: {trust_policy_response.message}",
            data=results
        )

    results["steps_completed"].append("trust_policy_updated")
    print(f"✓ {trust_policy_response.message}\n")

    print("=" * 70)
    print("✓ SUCCESS: Datadog action connection setup completed!")
    print("=" * 70)
    print("\nSummary:")
    print(f"  Connection ID: {results['connection_id']}")
    print(f"  External ID: {results['external_id']}")
    print(f"  Role Name: {results['role_name']}")
    print(f"  Steps Completed: {', '.join(results['steps_completed'])}")
    print("=" * 70 + "\n")

    return DatadogResponse(
        success=True,
        status_code=200,
        message="Datadog action connection setup completed successfully",
        data=results
    )


def main():
    """Main entry point for the script."""
    # Check for required environment variables
    api_key = os.getenv("DD_API_KEY")
    app_key = os.getenv("DD_APP_KEY")

    if not api_key or not app_key:
        print("ERROR: Required environment variables not set")
        print("Please set DD_API_KEY and DD_APP_KEY environment variables")
        print("\nExample:")
        print('  export DD_API_KEY="your-api-key"')
        print('  export DD_APP_KEY="your-app-key"')
        print('  export AWS_PROFILE="gameday"')
        sys.exit(1)

    # Run setup
    response = setup_datadog_action_connection(api_key, app_key)

    if not response.success:
        print(f"\n✗ FAILED: {response.message}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
