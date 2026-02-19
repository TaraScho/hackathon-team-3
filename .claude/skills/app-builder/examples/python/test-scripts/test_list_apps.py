#!/usr/bin/env python3
"""
Phase 2: Test List Existing Apps API
Tests calling the GET /api/v2/app-builder/apps endpoint to understand response structure.
"""

import os
import requests
import json

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")
BASE_URL = "https://api.datadoghq.com"


def list_apps(api_key, app_key):
    """
    List all App Builder apps in the organization.

    Returns:
        Tuple of (success: bool, data: dict, error_message: str)
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    try:
        print(f"Calling GET {BASE_URL}/api/v2/app-builder/apps")
        response = requests.get(
            f"{BASE_URL}/api/v2/app-builder/apps",
            headers=headers,
            timeout=10
        )

        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}\n")

        if response.status_code == 200:
            data = response.json()
            return True, data, None
        else:
            error_msg = response.text
            try:
                error_json = response.json()
                error_msg = json.dumps(error_json, indent=2)
            except:
                pass
            return False, None, f"Status {response.status_code}: {error_msg}"

    except Exception as e:
        return False, None, f"Exception: {type(e).__name__}: {e}"


def main():
    """Run Phase 2 test."""
    print(f"\n{'='*70}")
    print("PHASE 2: List Existing Apps")
    print(f"{'='*70}\n")

    success, data, error = list_apps(DD_API_KEY, DD_APP_KEY)

    if not success:
        print(f"❌ Failed to list apps:")
        print(f"   {error}")
        return

    print(f"✓ Successfully retrieved apps list\n")

    # Analyze response structure
    print(f"{'='*70}")
    print("RESPONSE STRUCTURE ANALYSIS")
    print(f"{'='*70}\n")

    print(f"Top-level keys: {list(data.keys())}")

    if 'data' in data:
        apps = data['data']
        print(f"Number of apps: {len(apps)}")
        print(f"Apps data type: {type(apps)}\n")

        if len(apps) > 0:
            print(f"{'='*70}")
            print("SAMPLE APP STRUCTURE (First App)")
            print(f"{'='*70}\n")

            first_app = apps[0]
            print(f"App keys: {list(first_app.keys())}")
            print(f"\nApp type: {first_app.get('type', 'N/A')}")
            print(f"App ID: {first_app.get('id', 'N/A')}")

            if 'attributes' in first_app:
                attrs = first_app['attributes']
                print(f"\nAttributes keys: {list(attrs.keys())}")
                print(f"App Name: {attrs.get('name', 'N/A')}")
                print(f"App Description: {attrs.get('description', 'N/A')}")
                print(f"App Tags: {attrs.get('tags', [])}")

            print(f"\n{'='*70}")
            print("ALL APPS SUMMARY")
            print(f"{'='*70}\n")

            for i, app in enumerate(apps, 1):
                app_id = app.get('id', 'NO_ID')
                app_name = app.get('attributes', {}).get('name', 'NO_NAME')
                app_desc = app.get('attributes', {}).get('description', 'NO_DESC')
                print(f"{i}. {app_name}")
                print(f"   ID: {app_id}")
                print(f"   Description: {app_desc}")
                print()

            # Create name-to-ID mapping like we'll need for checking duplicates
            print(f"{'='*70}")
            print("NAME TO ID MAPPING")
            print(f"{'='*70}\n")

            name_map = {}
            for app in apps:
                app_name = app.get('attributes', {}).get('name')
                app_id = app.get('id')
                if app_name:
                    name_map[app_name] = app_id
                    print(f"{app_name}: {app_id}")

            print(f"\n✓ Generated name-to-ID mapping with {len(name_map)} entries")

        else:
            print("No apps found in the organization")

    else:
        print("⚠️  Response does not have 'data' key")
        print(f"Full response: {json.dumps(data, indent=2)}")

    print(f"\n{'='*70}")
    print("✅ PHASE 2 TEST COMPLETE - Ready for Phase 3")
    print(f"{'='*70}\n")

    # Save full response for inspection
    with open("test_output_list_apps.json", 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Full response saved to: test_output_list_apps.json")


if __name__ == "__main__":
    main()
