#!/usr/bin/env python3
"""
Datadog App Builder Setup Helpers

Provides functions to programmatically create and manage Datadog App Builder apps.
Designed to work with the Quest Development Kit pattern.
"""

import os
import json
import time
import re
import requests
from typing import Dict, List, Optional, Tuple
from pathlib import Path

# Import shared helpers
from datadog_helpers.datadog_helpers import (
    DatadogResponse,
    build_headers,
    BASE_URL,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES
)


# Mapping from app names to normalized keys for dashboard templates
APP_NAME_TO_KEY = {
    "TechStories Service Overview": "aws_quick_review",
    "EC2 Management Console": "ec2_manager",
    "Lambda Function Manager": "lambda_manager",
    "Manage ECS Tasks": "ecs_manager",
    "Manage DynamoDB": "dynamodb_manager",
    "Manage SQS Queues": "sqs_manager",
    "Manage Step Functions": "step_functions_manager",
    "Explore S3 Files": "s3_explorer"
}


def create_app_key_with_app_builder_scopes(
    api_key: str,
    app_key: str,
    key_name: str = "AppBuilderKey",
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create a new Datadog application key with App Builder & Workflow Automation scopes.

    This is a specialized version focusing on app builder needs.
    Scopes include apps_write, apps_run, connections_read, connections_write, etc.

    Args:
        api_key: Datadog API key
        app_key: Existing Datadog application key (with permission to create keys)
        key_name: Name for the new application key
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with the new app key in data["key"]
    """
    headers = build_headers(api_key, app_key)

    # App Builder & Workflow Automation scopes
    scopes = [
        "actions_interface_run",
        "apps_datastore_manage",
        "apps_datastore_read",
        "apps_datastore_write",
        "apps_run",
        "apps_write",
        "connection_groups_read",
        "connection_groups_write",
        "connections_read",
        "connections_resolve",
        "connections_write",
        "on_prem_runner_read",
        "on_prem_runner_use",
        "on_prem_runner_write",
        "workflows_read",
        "workflows_run",
        "workflows_write"
    ]

    payload = {
        "data": {
            "type": "application_keys",
            "attributes": {
                "name": key_name,
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
                    message=f"Created app key with app builder scopes: {key_name}",
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


def get_org_id(api_key: str, app_key: str) -> DatadogResponse:
    """
    Get the organization ID for the current Datadog account.

    Uses the /api/v2/current_user endpoint to retrieve org information.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key

    Returns:
        DatadogResponse with org_id in data["org_id"]
    """
    headers = build_headers(api_key, app_key)

    try:
        response = requests.get(
            f"{BASE_URL}/api/v2/current_user",
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 200:
            response_data = response.json()
            # The org ID is in data.relationships.org.data.id
            org_id = (response_data.get("data", {})
                     .get("relationships", {})
                     .get("org", {})
                     .get("data", {})
                     .get("id", ""))

            if org_id:
                return DatadogResponse(
                    success=True,
                    status_code=200,
                    message=f"Retrieved org ID: {org_id}",
                    data={"org_id": org_id}
                )
            else:
                return DatadogResponse(
                    success=False,
                    status_code=200,
                    message="Could not find org ID in response",
                    data={"full_response": response_data}
                )
        else:
            error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"
            return DatadogResponse(
                success=False,
                status_code=response.status_code,
                message=f"Failed to get org ID: {error_msg}"
            )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error getting org ID: {e}"
        )


def remove_fields_recursive(obj, fields_to_remove: set):
    """
    Recursively remove specified fields from nested JSON structure.

    Args:
        obj: Dict, list, or primitive value
        fields_to_remove: Set of field names to remove

    Returns:
        Cleaned object with specified fields removed
    """
    if isinstance(obj, dict):
        return {
            k: remove_fields_recursive(v, fields_to_remove)
            for k, v in obj.items()
            if k not in fields_to_remove
        }
    elif isinstance(obj, list):
        return [remove_fields_recursive(item, fields_to_remove) for item in obj]
    return obj


def transform_app_json_for_api(
    json_file_path: str,
    connection_id: str,
    connection_name: str
) -> Dict:
    """
    Transform app JSON file for API submission.

    Steps:
    1. Load JSON from file
    2. Replace all connectionId values with provided connection_id
    3. Remove 'handle' and 'id' fields (per API requirements)
    4. Reconstruct connections array with new connection info
    5. Wrap in API envelope structure

    Args:
        json_file_path: Path to app JSON file
        connection_id: Connection ID to use for all AWS actions
        connection_name: Connection name

    Returns:
        Transformed JSON ready for API submission
    """
    # Load the JSON file
    with open(json_file_path, 'r') as f:
        app_data = json.load(f)

    # Step 1: Replace all connectionId values
    # Convert to string, do regex replacement, convert back
    json_str = json.dumps(app_data)
    json_str = re.sub(
        r'"connectionId":\s*"[^"]*"',
        f'"connectionId": "{connection_id}"',
        json_str
    )
    app_data = json.loads(json_str)

    # Step 2: Remove 'handle' field only (if it exists)
    # Note: 'id' fields for queries/components are required by the API
    # Only top-level 'handle' field (from GET response) needs to be removed
    fields_to_remove = {'handle'}
    app_data_cleaned = remove_fields_recursive(app_data, fields_to_remove)

    # Step 3: Reconstruct connections array AFTER cleanup
    app_data_cleaned['connections'] = [{
        "id": connection_id,
        "name": connection_name
    }]

    # Step 4: Wrap in API envelope
    api_payload = {
        "data": {
            "type": "appDefinitions",
            "attributes": app_data_cleaned
        }
    }

    return api_payload


def get_existing_apps(
    api_key: str,
    app_key: str
) -> Tuple[Dict[str, str], Optional[str]]:
    """
    Fetch existing App Builder apps from Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key

    Returns:
        Tuple of (dict mapping app name to app ID, error message if any)
    """
    headers = build_headers(api_key, app_key)

    try:
        response = requests.get(
            f"{BASE_URL}/api/v2/app-builder/apps",
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 200:
            data = response.json()
            apps = data.get("data", [])
            app_map = {
                app.get("attributes", {}).get("name"): app.get("id")
                for app in apps
                if app.get("attributes", {}).get("name")
            }
            return app_map, None
        else:
            return {}, f"Could not fetch existing apps (status {response.status_code})"

    except Exception as e:
        return {}, f"Error fetching existing apps: {e}"


def create_app_builder_app(
    api_key: str,
    app_key: str,
    app_payload: Dict,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create an App Builder app.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key with app builder permissions
        app_payload: Transformed app JSON (already wrapped in API envelope)
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with app_id in data["app_id"]
    """
    headers = build_headers(api_key, app_key)

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/app-builder/apps",
                headers=headers,
                json=app_payload,
                timeout=30  # Longer timeout for app creation
            )

            if response.status_code in [200, 201]:
                response_data = response.json()
                app_id = response_data.get("data", {}).get("id", "")
                app_name = response_data.get("data", {}).get("attributes", {}).get("name", "")

                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"Created app: {app_name}",
                    data={
                        "app_id": app_id,
                        "app_name": app_name,
                        "full_response": response_data
                    }
                )
            elif response.status_code == 409:
                # App already exists
                return DatadogResponse(
                    success=True,
                    status_code=409,
                    message="App already exists"
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to create app: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error creating app: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to create app after {max_retries} retries"
    )


def set_app_restriction_policy(
    api_key: str,
    app_key: str,
    app_id: str,
    org_id: str,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Set restriction policy for an app to allow org-wide editor access.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        app_id: App Builder app ID
        org_id: Datadog organization ID
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)

    payload = {
        "data": {
            "id": f"app-builder-app:{app_id}",
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
                f"{BASE_URL}/api/v2/restriction_policy/app-builder-app:{app_id}",
                headers=headers,
                json=payload,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code in [200, 201]:
                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"Set restriction policy for app {app_id}"
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


def publish_app(
    api_key: str,
    app_key: str,
    app_id: str,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Publish an app to make it live.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        app_id: App Builder app ID
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/app-builder/apps/{app_id}/deployment",
                headers=headers,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code in [200, 201, 204]:
                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"Published app {app_id}"
                )
            elif response.status_code == 409:
                # App already published - this is OK
                return DatadogResponse(
                    success=True,
                    status_code=409,
                    message=f"App {app_id} already published"
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to publish app: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error publishing app: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to publish app after {max_retries} retries"
    )


def create_all_apps_from_directory(
    api_key: str,
    app_key: str,
    connection_id: str,
    connection_name: str,
    org_id: str,
    apps_dir: Optional[str] = None
) -> Dict:
    """
    Create all App Builder apps from JSON files in a directory.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key (with app builder permissions)
        connection_id: AWS connection ID to use for all apps
        connection_name: AWS connection name
        org_id: Datadog organization ID (for restriction policies)
        apps_dir: Directory containing app JSON files (defaults to app-builder-apps/)

    Returns:
        Dict with summary: {
            "created": [...],
            "skipped": [...],
            "failed": [...],
            "app_ids": {"app_name": "app_id", ...}  # All app IDs (created + skipped)
        }
    """
    if apps_dir is None:
        # Default to app-builder-apps subdirectory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        apps_dir = os.path.join(current_dir, "app-builder-apps")

    summary = {
        "created": [],
        "skipped": [],
        "failed": [],
        "app_ids": {}  # Map of app_name -> app_id for all apps
    }

    # Get existing apps first
    existing_apps, error = get_existing_apps(api_key, app_key)
    if error:
        print(f"Warning: Could not fetch existing apps: {error}")
        existing_apps = {}

    # Find all JSON files
    json_files = []
    for file in os.listdir(apps_dir):
        if file.endswith('.json') and not file.startswith('.'):
            json_files.append(os.path.join(apps_dir, file))

    print(f"Found {len(json_files)} JSON files in {apps_dir}")

    # Process each file
    for json_file in json_files:
        try:
            # Transform the app JSON
            app_payload = transform_app_json_for_api(
                json_file_path=json_file,
                connection_id=connection_id,
                connection_name=connection_name
            )

            app_name = app_payload["data"]["attributes"]["name"]
            print(f"\nProcessing: {app_name}")

            # Check if app already exists
            if app_name in existing_apps:
                app_id = existing_apps[app_name]
                print(f"  ⏭️  App already exists (ID: {app_id})")

                # Still set restriction policy for existing app
                policy_response = set_app_restriction_policy(api_key, app_key, app_id, org_id)
                if policy_response.success:
                    print(f"  ✅ Updated restriction policy")
                else:
                    print(f"  ⚠️  Warning: Could not update restriction policy: {policy_response.message}")

                # Publish the existing app (in case it wasn't published before)
                publish_response = publish_app(api_key, app_key, app_id)
                if publish_response.success:
                    print(f"  ✅ Published app")
                else:
                    print(f"  ⚠️  Warning: Could not publish app: {publish_response.message}")

                # Normalize app name to key for dashboard templates
                normalized_key = APP_NAME_TO_KEY.get(app_name, app_name.lower().replace(" ", "_"))

                summary["skipped"].append({
                    "name": app_name,
                    "file": os.path.basename(json_file),
                    "app_id": app_id
                })
                summary["app_ids"][normalized_key] = app_id
                continue

            # Create the app
            create_response = create_app_builder_app(api_key, app_key, app_payload)

            if not create_response.success:
                print(f"  ❌ Failed to create: {create_response.message}")
                summary["failed"].append({
                    "name": app_name,
                    "file": os.path.basename(json_file),
                    "error": create_response.message
                })
                continue

            if create_response.status_code == 409:
                print(f"  ⏭️  App already exists (409)")
                # Try to get the app_id from existing_apps lookup
                app_id = existing_apps.get(app_name)

                if app_id:
                    # Set restriction policy and publish for 409 response
                    policy_response = set_app_restriction_policy(api_key, app_key, app_id, org_id)
                    if policy_response.success:
                        print(f"  ✅ Updated restriction policy")
                    else:
                        print(f"  ⚠️  Warning: Could not update restriction policy: {policy_response.message}")

                    publish_response = publish_app(api_key, app_key, app_id)
                    if publish_response.success:
                        print(f"  ✅ Published app")
                    else:
                        print(f"  ⚠️  Warning: Could not publish app: {publish_response.message}")

                    normalized_key = APP_NAME_TO_KEY.get(app_name, app_name.lower().replace(" ", "_"))
                    summary["skipped"].append({
                        "name": app_name,
                        "file": os.path.basename(json_file),
                        "app_id": app_id
                    })
                    summary["app_ids"][normalized_key] = app_id
                else:
                    print(f"  ⚠️  Could not find app_id for existing app")
                    summary["skipped"].append({
                        "name": app_name,
                        "file": os.path.basename(json_file)
                    })
                continue

            app_id = create_response.data["app_id"]
            print(f"  ✅ Created app (ID: {app_id})")

            # Set restriction policy
            policy_response = set_app_restriction_policy(api_key, app_key, app_id, org_id)
            if policy_response.success:
                print(f"  ✅ Set restriction policy")
            else:
                print(f"  ⚠️  Warning: Could not set restriction policy: {policy_response.message}")

            # Publish the app
            publish_response = publish_app(api_key, app_key, app_id)
            if publish_response.success:
                print(f"  ✅ Published app")
            else:
                print(f"  ⚠️  Warning: Could not publish app: {publish_response.message}")

            # Normalize app name to key for dashboard templates
            normalized_key = APP_NAME_TO_KEY.get(app_name, app_name.lower().replace(" ", "_"))

            summary["created"].append({
                "name": app_name,
                "file": os.path.basename(json_file),
                "app_id": app_id
            })
            summary["app_ids"][normalized_key] = app_id

        except Exception as e:
            print(f"  ❌ Error processing {os.path.basename(json_file)}: {e}")
            summary["failed"].append({
                "file": os.path.basename(json_file),
                "error": str(e)
            })

    return summary
