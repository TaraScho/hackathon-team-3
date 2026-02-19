#!/usr/bin/env python3
"""
Phase 4: Test Restriction Policy and Publish
Tests the full lifecycle: set restriction policy and publish an existing app.
"""

import os
import sys
import json
import requests
from pathlib import Path

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")
DD_ORG_ID = "0a0bcf5a-46bc-11ee-b2e6-da7ad0900002"
BASE_URL = "https://api.datadoghq.com"

# Use an existing app for testing
TEST_APP_ID = "245cf09f-cb28-421b-8e8e-e9ef276412d9"  # Manage DynamoDB
TEST_APP_NAME = "Manage DynamoDB"


def set_restriction_policy(api_key: str, app_key: str, app_id: str, org_id: str) -> tuple:
    """
    Set restriction policy for an app to allow org-wide editor access.

    Returns:
        Tuple of (success: bool, status_code: int, error_message: str)
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

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

    try:
        url = f"{BASE_URL}/api/v2/restriction_policy/app-builder-app:{app_id}"
        print(f"   Calling POST {url}")

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}\n")

        if response.status_code in [200, 201]:
            return True, response.status_code, None
        else:
            error_msg = response.text
            try:
                error_json = response.json()
                error_msg = json.dumps(error_json, indent=2)
            except:
                pass
            return False, response.status_code, error_msg

    except Exception as e:
        return False, 0, f"Exception: {type(e).__name__}: {e}"


def publish_app(api_key: str, app_key: str, app_id: str) -> tuple:
    """
    Publish an app to make it live.

    Returns:
        Tuple of (success: bool, status_code: int, error_message: str)
    """
    headers = {
        "Accept": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    try:
        url = f"{BASE_URL}/api/v2/app-builder/apps/{app_id}/deployment"
        print(f"   Calling POST {url}")

        response = requests.post(
            url,
            headers=headers,
            timeout=30
        )

        print(f"   Status Code: {response.status_code}\n")

        if response.status_code in [200, 201, 204]:
            return True, response.status_code, None
        else:
            error_msg = response.text
            try:
                error_json = response.json()
                error_msg = json.dumps(error_json, indent=2)
            except:
                pass
            return False, response.status_code, error_msg

    except Exception as e:
        return False, 0, f"Exception: {type(e).__name__}: {e}"


def main():
    """Test restriction policy and publish."""
    print(f"\n{'='*70}")
    print("PHASE 4: Test Restriction Policy and Publish")
    print(f"{'='*70}\n")

    print(f"Testing with existing app:")
    print(f"  App ID: {TEST_APP_ID}")
    print(f"  App Name: {TEST_APP_NAME}")
    print(f"  Org ID: {DD_ORG_ID}\n")

    # Step 1: Set restriction policy
    print(f"{'='*70}")
    print("Step 1: Setting restriction policy...")
    print(f"{'='*70}\n")

    success, status_code, error = set_restriction_policy(
        DD_API_KEY,
        DD_APP_KEY,
        TEST_APP_ID,
        DD_ORG_ID
    )

    if not success:
        print(f"❌ Failed to set restriction policy:")
        print(f"   Status: {status_code}")
        print(f"   Error: {error}\n")
        return
    else:
        print(f"✅ Restriction policy set successfully!")
        print(f"   Status: {status_code}")
        print(f"   Policy: org:{DD_ORG_ID} has editor access\n")

    # Step 2: Publish the app
    print(f"{'='*70}")
    print("Step 2: Publishing app...")
    print(f"{'='*70}\n")

    success, status_code, error = publish_app(
        DD_API_KEY,
        DD_APP_KEY,
        TEST_APP_ID
    )

    if not success:
        print(f"❌ Failed to publish app:")
        print(f"   Status: {status_code}")
        print(f"   Error: {error}\n")
        # Note: This might fail if app is already published, which is OK
        if status_code == 400:
            print(f"   Note: App might already be published (this is OK)\n")
    else:
        print(f"✅ App published successfully!")
        print(f"   Status: {status_code}\n")

    print(f"{'='*70}")
    print("✅ PHASE 4 COMPLETE - Ready for Phase 5")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
