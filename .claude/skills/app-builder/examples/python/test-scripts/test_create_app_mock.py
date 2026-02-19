#!/usr/bin/env python3
"""
Phase 3 Alternative: Test app creation with mock connection ID
This will likely fail due to invalid connection, but will show us the API error handling.
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

# Use a fake connection ID to test the endpoint
TEST_CONNECTION_ID = "00000000-0000-0000-0000-000000000000"
TEST_CONNECTION_NAME = "MockConnection"


def main():
    """Test app creation with mock connection."""
    print(f"\n{'='*70}")
    print("PHASE 3 ALTERNATIVE: Test App Creation Endpoint")
    print("Using mock connection ID to test API behavior")
    print(f"{'='*70}\n")

    # Create a minimal test app payload directly (skip file loading)
    minimal_app = {
        "data": {
            "type": "appDefinitions",
            "attributes": {
                "name": "Test App - Phase 3",
                "description": "Minimal test app for API validation",
                "queries": [],
                "components": [{
                    "name": "testComponent",
                    "type": "text",
                    "properties": {
                        "text": "Hello from test app"
                    }
                }],
                "connections": [{
                    "id": TEST_CONNECTION_ID,
                    "name": TEST_CONNECTION_NAME
                }],
                "rootInstanceName": "testComponent",
                "tags": ["test"],
                "favorite": False,
                "selfService": False
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": DD_API_KEY,
        "DD-APPLICATION-KEY": DD_APP_KEY
    }

    print("Attempting to create minimal test app...")
    print(f"App name: {minimal_app['data']['attributes']['name']}")
    print(f"Connection ID: {TEST_CONNECTION_ID}\n")

    try:
        response = requests.post(
            f"{BASE_URL}/api/v2/app-builder/apps",
            headers=headers,
            json=minimal_app,
            timeout=30
        )

        print(f"Status Code: {response.status_code}\n")

        if response.status_code in [200, 201]:
            print("✅ SUCCESS! App created (unexpected with mock connection)")
            data = response.json()
            print(json.dumps(data, indent=2))
        elif response.status_code == 403:
            print("❌ PERMISSION DENIED (403)")
            print("   The app key lacks permissions for app creation")
            print("   This confirms we need `apps_write` scope")
            try:
                error = response.json()
                print(f"\n   Error details: {json.dumps(error, indent=2)}")
            except:
                print(f"\n   Raw response: {response.text}")
        elif response.status_code == 400:
            print("⚠️  BAD REQUEST (400)")
            print("   This could mean:")
            print("   - Invalid connection ID")
            print("   - Missing required fields")
            print("   - Invalid app structure")
            try:
                error = response.json()
                print(f"\n   Error details: {json.dumps(error, indent=2)}")
            except:
                print(f"\n   Raw response: {response.text}")
        else:
            print(f"❌ UNEXPECTED STATUS: {response.status_code}")
            try:
                error = response.json()
                print(f"   Error: {json.dumps(error, indent=2)}")
            except:
                print(f"   Raw response: {response.text}")

    except Exception as e:
        print(f"❌ EXCEPTION: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

    print(f"\n{'='*70}")
    print("FINDINGS")
    print(f"{'='*70}\n")
    print("To properly test app creation, we need:")
    print("1. An app key with `apps_write` and `connections_read` scopes")
    print("2. A valid AWS action connection ID")
    print("\nThe `create_app_key_with_actions_scope()` function in")
    print("`setup_action_connection.py` already handles #1")
    print("\nFor now, we'll proceed with building the production code")
    print("based on the API documentation and existing bash script patterns.")


if __name__ == "__main__":
    main()
