#!/usr/bin/env python3
"""
Phase 3: Test Creating Single App
Tests creating an app via POST /api/v2/app-builder/apps endpoint.
"""

import os
import requests
import json
import sys
from pathlib import Path

# Import our transformation logic from Phase 1
sys.path.insert(0, str(Path(__file__).parent))
from test_json_transform import transform_app_json

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")
BASE_URL = "https://api.datadoghq.com"

# Use a real connection ID from your account
# You'll need to replace this with an actual connection ID from your setup
TEST_CONNECTION_ID = "REPLACE_WITH_REAL_CONNECTION_ID"
TEST_CONNECTION_NAME = "TestAWSConnection-Phase3"


def create_app(api_key, app_key, app_payload):
    """
    Create an App Builder app.

    Args:
        api_key: Datadog API key
        app_key: Datadog app key with app builder permissions
        app_payload: Transformed app JSON (already wrapped in API envelope)

    Returns:
        Tuple of (success: bool, data: dict, status_code: int, error_message: str)
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    try:
        print(f"Calling POST {BASE_URL}/api/v2/app-builder/apps")
        print(f"Payload size: {len(json.dumps(app_payload))} bytes")

        response = requests.post(
            f"{BASE_URL}/api/v2/app-builder/apps",
            headers=headers,
            json=app_payload,
            timeout=30  # Longer timeout for app creation
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code in [200, 201]:
            data = response.json()
            return True, data, response.status_code, None
        elif response.status_code == 409:
            # App already exists - this is actually a "success" case for our logic
            return True, None, 409, "App already exists"
        else:
            error_msg = response.text
            try:
                error_json = response.json()
                error_msg = json.dumps(error_json, indent=2)
            except:
                pass
            return False, None, response.status_code, error_msg

    except Exception as e:
        return False, None, 0, f"Exception: {type(e).__name__}: {e}"


def main():
    """Run Phase 3 test."""
    print(f"\n{'='*70}")
    print("PHASE 3: Create Single App")
    print(f"{'='*70}\n")

    # Check if connection ID was set
    if TEST_CONNECTION_ID == "REPLACE_WITH_REAL_CONNECTION_ID":
        print("⚠️  WARNING: TEST_CONNECTION_ID not set!")
        print("   Please update TEST_CONNECTION_ID in this script with a real connection ID")
        print("   from your Datadog account.\n")

        # Try to help the user find a connection ID
        print("Attempting to list available connections...\n")
        try:
            headers = {
                "Accept": "application/json",
                "DD-API-KEY": DD_API_KEY,
                "DD-APPLICATION-KEY": DD_APP_KEY
            }
            response = requests.get(
                f"{BASE_URL}/api/v2/actions/connections",
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                connections = response.json().get('data', [])
                if connections:
                    print("Available connections:")
                    for conn in connections:
                        conn_id = conn.get('id', 'N/A')
                        conn_name = conn.get('attributes', {}).get('name', 'N/A')
                        conn_type = conn.get('attributes', {}).get('integration', {}).get('type', 'N/A')
                        print(f"  - {conn_name} ({conn_type}): {conn_id}")
                    print(f"\nUse one of these connection IDs in TEST_CONNECTION_ID variable")
                else:
                    print("No connections found in your account")
        except Exception as e:
            print(f"Could not list connections: {e}")

        return

    # Transform the app JSON
    json_file = Path(__file__).parent / "central_lambda_source" / "datadog_helpers" / "app-builder-apps" / "manage-dynamodb.json"

    if not json_file.exists():
        print(f"❌ JSON file not found: {json_file}")
        return

    print("Step 1: Transforming app JSON...")
    try:
        app_payload = transform_app_json(
            json_file_path=str(json_file),
            connection_id=TEST_CONNECTION_ID,
            connection_name=TEST_CONNECTION_NAME
        )
        print("✓ Transformation complete\n")
    except Exception as e:
        print(f"❌ Transformation failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Create the app
    print(f"{'='*70}")
    print("Step 2: Creating app via API...")
    print(f"{'='*70}\n")

    success, data, status_code, error = create_app(DD_API_KEY, DD_APP_KEY, app_payload)

    if not success:
        print(f"❌ Failed to create app:")
        print(f"   Status: {status_code}")
        print(f"   Error: {error}")
        return

    if status_code == 409:
        print(f"✓ App already exists (409) - This is expected behavior")
        print(f"  Our production code will skip this app and continue")
    else:
        print(f"✓ App created successfully!")
        print(f"  Status: {status_code}")

        if data:
            print(f"\n{'='*70}")
            print("CREATED APP DETAILS")
            print(f"{'='*70}\n")

            app_id = data.get('data', {}).get('id', 'N/A')
            app_name = data.get('data', {}).get('attributes', {}).get('name', 'N/A')

            print(f"App ID: {app_id}")
            print(f"App Name: {app_name}")

            # Save the response
            with open("test_output_created_app.json", 'w') as f:
                json.dump(data, f, indent=2)
            print(f"\nFull response saved to: test_output_created_app.json")

    print(f"\n{'='*70}")
    print("✅ PHASE 3 TEST COMPLETE - Ready for Phase 4")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
