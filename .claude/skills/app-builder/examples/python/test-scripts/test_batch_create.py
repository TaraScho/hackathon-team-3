#!/usr/bin/env python3
"""
Phase 6: Test Batch App Creation
Tests creating all apps from directory using the complete workflow.
"""

import os
import sys
import json
from pathlib import Path

# Add central_lambda_source to path
sys.path.insert(0, str(Path(__file__).parent / "central_lambda_source"))

from datadog_helpers.app_builder_helpers import create_all_apps_from_directory

# Credentials from environment variables
DD_API_KEY = os.environ.get("DD_API_KEY", "")
DD_APP_KEY = os.environ.get("DD_APP_KEY", "")
DD_ORG_ID = "0a0bcf5a-46bc-11ee-b2e6-da7ad0900002"

# Real AWS connection
AWS_CONNECTION_ID = "2a8a6d56-4c60-4772-9f1e-69bafed9f0ae"
AWS_CONNECTION_NAME = "DatadogAWSConnection-1071"


def main():
    """Test batch app creation."""
    print(f"\n{'='*70}")
    print("PHASE 6: Batch App Creation from Directory")
    print(f"{'='*70}\n")

    print("Configuration:")
    print(f"  API Key: {DD_API_KEY[:20]}...")
    print(f"  App Key: {DD_APP_KEY[:20]}...")
    print(f"  Org ID: {DD_ORG_ID}")
    print(f"  Connection ID: {AWS_CONNECTION_ID}")
    print(f"  Connection Name: {AWS_CONNECTION_NAME}\n")

    print(f"{'='*70}")
    print("Creating apps from directory...")
    print(f"{'='*70}\n")

    summary = create_all_apps_from_directory(
        api_key=DD_API_KEY,
        app_key=DD_APP_KEY,
        connection_id=AWS_CONNECTION_ID,
        connection_name=AWS_CONNECTION_NAME,
        org_id=DD_ORG_ID
    )

    print(f"\n{'='*70}")
    print("BATCH CREATION SUMMARY")
    print(f"{'='*70}\n")

    print(f"✅ Created: {len(summary['created'])} apps")
    for app in summary['created']:
        print(f"   - {app['name']} (ID: {app['app_id']})")

    print(f"\n⏭️  Skipped: {len(summary['skipped'])} apps (already exist)")
    for app in summary['skipped']:
        print(f"   - {app['name']}")

    print(f"\n❌ Failed: {len(summary['failed'])} apps")
    for app in summary['failed']:
        app_name = app.get('name', app.get('file', 'Unknown'))
        print(f"   - {app_name}: {app['error']}")

    # Save summary
    with open("test_output_batch_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull summary saved to: test_output_batch_summary.json")

    print(f"\n{'='*70}")
    print("✅ PHASE 6 COMPLETE - All Testing Done!")
    print(f"{'='*70}\n")

    print("Next steps:")
    print("  1. Review the app_builder_helpers.py implementation")
    print("  2. Integrate with task_zero._configure_datadog_trial_account()")
    print("  3. Test in full Quest environment")


if __name__ == "__main__":
    main()
