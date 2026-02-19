#!/usr/bin/env python3
"""
Phase 3 FOR REAL: Actually create an app with proper credentials
Now that we have properly scoped credentials, let's create an app!
"""

import os
import sys
import json
import requests
from pathlib import Path

# Add central_lambda_source to path
sys.path.insert(0, str(Path(__file__).parent / "central_lambda_source"))

from datadog_helpers.app_builder_helpers import (
    transform_app_json_for_api,
    get_existing_apps
)

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")
BASE_URL = "https://api.datadoghq.com"

# Real AWS connection from your account
AWS_CONNECTION_ID = "2a8a6d56-4c60-4772-9f1e-69bafed9f0ae"
AWS_CONNECTION_NAME = "DatadogAWSConnection-1071"


def create_app(api_key: str, app_key: str, app_payload: dict) -> tuple:
    """
    Create an App Builder app.

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
        print(f"   Calling POST {BASE_URL}/api/v2/app-builder/apps")
        print(f"   Payload size: {len(json.dumps(app_payload))} bytes")

        response = requests.post(
            f"{BASE_URL}/api/v2/app-builder/apps",
            headers=headers,
            json=app_payload,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}\n")

        if response.status_code in [200, 201]:
            data = response.json()
            return True, data, response.status_code, None
        elif response.status_code == 409:
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
    """Test creating an app for real."""
    print(f"\n{'='*70}")
    print("PHASE 3 FOR REAL: Create App with Proper Credentials")
    print(f"{'='*70}\n")

    # Step 1: Check existing apps
    print("Step 1: Checking existing apps...")
    existing_apps, error = get_existing_apps(DD_API_KEY, DD_APP_KEY)

    if error:
        print(f"❌ Failed to list apps: {error}")
        return

    print(f"✅ Found {len(existing_apps)} existing apps\n")

    # Step 2: Transform our test JSON
    print(f"{'='*70}")
    print("Step 2: Transforming app JSON...")
    print(f"{'='*70}\n")

    # Use test-minimal-app.json as our test case (so we can actually create it)
    json_file = Path(__file__).parent / "central_lambda_source" / "datadog_helpers" / "app-builder-apps" / "test-minimal-app.json"

    if not json_file.exists():
        print(f"❌ JSON file not found: {json_file}")
        return

    try:
        app_payload = transform_app_json_for_api(
            json_file_path=str(json_file),
            connection_id=AWS_CONNECTION_ID,
            connection_name=AWS_CONNECTION_NAME
        )

        app_name = app_payload["data"]["attributes"]["name"]
        print(f"✅ Transformed app: {app_name}")
        print(f"   Connection ID: {AWS_CONNECTION_ID}")
        print(f"   Connection Name: {AWS_CONNECTION_NAME}\n")

    except Exception as e:
        print(f"❌ Transformation failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Step 3: Check if app already exists
    print(f"{'='*70}")
    print("Step 3: Checking for duplicate...")
    print(f"{'='*70}\n")

    if app_name in existing_apps:
        print(f"⚠️  App '{app_name}' already exists!")
        print(f"   ID: {existing_apps[app_name]}")
        print(f"\n   This is the expected behavior - our production code will")
        print(f"   skip creating this app and move to the next one.\n")

        print(f"{'='*70}")
        print("✅ DUPLICATE DETECTION WORKS")
        print(f"{'='*70}\n")
        return

    # Step 4: Create the app
    print(f"   App does not exist, proceeding with creation...\n")

    print(f"{'='*70}")
    print("Step 4: Creating app via API...")
    print(f"{'='*70}\n")

    success, data, status_code, error = create_app(DD_API_KEY, DD_APP_KEY, app_payload)

    if not success:
        print(f"❌ Failed to create app:")
        print(f"   Status: {status_code}")
        print(f"   Error: {error}\n")
        return

    if status_code == 409:
        print(f"✅ App already exists (409)")
        print(f"   This is handled correctly in our logic\n")
    else:
        print(f"✅ App created successfully!")
        print(f"   Status: {status_code}\n")

        if data:
            app_id = data.get('data', {}).get('id', 'N/A')
            app_name_created = data.get('data', {}).get('attributes', {}).get('name', 'N/A')

            print(f"{'='*70}")
            print("CREATED APP DETAILS")
            print(f"{'='*70}\n")
            print(f"App ID: {app_id}")
            print(f"App Name: {app_name_created}")

            # Save the response
            with open("test_output_created_app_real.json", 'w') as f:
                json.dump(data, f, indent=2)
            print(f"\nFull response saved to: test_output_created_app_real.json")

            # Return the app_id for use in Phase 4
            with open("test_output_app_id.txt", 'w') as f:
                f.write(app_id)
            print(f"App ID saved to: test_output_app_id.txt")

    print(f"\n{'='*70}")
    print("✅ PHASE 3 COMPLETE - Ready for Phase 4")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
