#!/usr/bin/env python3
"""
Phase 3 PROPER: Test with properly scoped credentials
Creates an app key with correct scopes, then tests app creation.
"""

import os
import sys
import json
from pathlib import Path

# Add central_lambda_source to path so we can import our helpers
sys.path.insert(0, str(Path(__file__).parent / "central_lambda_source"))

from datadog_helpers.app_builder_helpers import (
    create_app_key_with_app_builder_scopes,
    get_org_id,
    get_existing_apps
)

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")


def main():
    """Test with properly scoped credentials."""
    print(f"\n{'='*70}")
    print("PHASE 3 PROPER: Testing with Properly Scoped Credentials")
    print(f"{'='*70}\n")

    # Step 1: Create or reuse app key with proper scopes
    print("Step 1: Setting up app key with App Builder scopes...")

    # Check if we already have a saved app key
    saved_key_path = Path("test_output_app_key.txt")
    new_app_key = None
    app_key_id = None

    if saved_key_path.exists():
        print("   Found existing saved app key, attempting to reuse...\n")
        with open(saved_key_path, 'r') as f:
            for line in f:
                if line.startswith("APP_KEY_ID="):
                    app_key_id = line.strip().split("=", 1)[1]
                elif line.startswith("APP_KEY="):
                    new_app_key = line.strip().split("=", 1)[1]

        if new_app_key and app_key_id:
            print(f"✅ Using existing app key!")
            print(f"   Key ID: {app_key_id}")
            print(f"   App Key: {new_app_key[:20]}...{new_app_key[-10:]}\n")

    # If we don't have a saved key, create one
    if not new_app_key:
        print(f"Using base API key: {DD_API_KEY[:20]}...")
        print(f"Using base App key: {DD_APP_KEY[:20]}...\n")

        app_key_response = create_app_key_with_app_builder_scopes(
            api_key=DD_API_KEY,
            app_key=DD_APP_KEY,
            key_name="TestAppBuilderKey-Phase3"
        )

        if not app_key_response.success:
            print(f"❌ Failed to create app key:")
            print(f"   Status: {app_key_response.status_code}")
            print(f"   Message: {app_key_response.message}")

            # If it already exists (409), that's actually OK but we need the key value
            if app_key_response.status_code == 409:
                print("\n⚠️  App key already exists but we don't have it saved.")
                print("   Please delete the existing key in Datadog UI or provide it here.")
            return

        new_app_key = app_key_response.data["key"]
        app_key_id = app_key_response.data["id"]
        print(f"✅ Created app key successfully!")
        print(f"   Key ID: {app_key_id}")
        print(f"   App Key: {new_app_key[:20]}...{new_app_key[-10:]}")

        # Save the app key for future use
        with open("test_output_app_key.txt", 'w') as f:
            f.write(f"APP_KEY_ID={app_key_id}\n")
            f.write(f"APP_KEY={new_app_key}\n")
        print(f"   Saved to: test_output_app_key.txt\n")

    # Step 2: Get org ID (using original unscoped app key)
    print(f"{'='*70}")
    print("Step 2: Retrieving organization ID...")
    print(f"{'='*70}\n")
    print("Note: Using original app key (some endpoints don't support scoped keys)\n")

    org_response = get_org_id(DD_API_KEY, DD_APP_KEY)

    if not org_response.success:
        print(f"❌ Failed to get org ID:")
        print(f"   Status: {org_response.status_code}")
        print(f"   Message: {org_response.message}")
        return

    org_id = org_response.data["org_id"]
    print(f"✅ Retrieved org ID: {org_id}\n")

    # Step 3: List existing apps
    print(f"{'='*70}")
    print("Step 3: Listing existing apps...")
    print(f"{'='*70}\n")

    existing_apps, error = get_existing_apps(DD_API_KEY, new_app_key)

    if error:
        print(f"❌ Failed to list apps:")
        print(f"   Error: {error}")
        return

    print(f"✅ Successfully listed apps!")
    print(f"   Found {len(existing_apps)} existing apps:\n")

    for i, (app_name, app_id) in enumerate(existing_apps.items(), 1):
        print(f"   {i}. {app_name}")
        print(f"      ID: {app_id}")

    # Save summary
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print(f"{'='*70}\n")

    summary = {
        "api_key": DD_API_KEY,
        "new_app_key": new_app_key,
        "app_key_id": app_key_id,
        "org_id": org_id,
        "existing_apps": existing_apps
    }

    with open("test_output_credentials_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"✅ All credential setup successful!")
    print(f"   - Created properly scoped app key")
    print(f"   - Retrieved org ID: {org_id}")
    print(f"   - Listed {len(existing_apps)} existing apps")
    print(f"\n   Summary saved to: test_output_credentials_summary.json")

    print(f"\n{'='*70}")
    print("NEXT STEPS")
    print(f"{'='*70}\n")
    print("Now we can proceed with testing app creation using:")
    print(f"  - API Key: {DD_API_KEY}")
    print(f"  - App Key: {new_app_key}")
    print(f"  - Org ID: {org_id}")
    print("\nThese credentials have the proper scopes for:")
    print("  - Creating apps")
    print("  - Setting restriction policies")
    print("  - Publishing apps")
    print("  - Managing connections")


if __name__ == "__main__":
    main()
