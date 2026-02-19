# Copyright 2025 Amazon.com and its affiliates; all rights reserved.
# This file is Amazon Web Services Content and may not be duplicated or distributed without permission.

# Test script to find the correct action ID for IAM attach role policy.
# Run: source .env && python walkup-quest-2026/team_lambda_source/test_workflow_action_ids.py

import sys
sys.path.insert(0, 'walkup-quest-2026/team_lambda_source')
from create_workflows import (
    get_connection_id_by_name,
    get_attach_iam_policy_workflow_spec,
    make_request,
    DD_URL,
    DD_API_KEY,
    DD_APP_KEY
)
import json

# Possible action ID variations to try
ACTION_ID_VARIATIONS = [
    "com.datadoghq.aws.iam.attach_role_policy",
    "com.datadoghq.aws.iam.attachrolepolicy",
    "com.datadoghq.aws.iam.AttachRolePolicy",
    "com.datadoghq.aws.iam.attachRolePolicy",
    "com.datadoghq.integration.aws.iam.attach_role_policy",
    "com.datadoghq.aws.attachrolepolicy",
]

def test_action_id(connection_id, action_id):
    """
    Test if an action ID works by attempting to create a workflow with it.
    Returns True if the action ID is valid, False otherwise.
    """
    workflow_spec = get_attach_iam_policy_workflow_spec(connection_id, action_id=action_id)

    payload = {
        "data": {
            "type": "workflows",
            "attributes": {
                "name": f"Test Workflow - {action_id}",
                "description": "Temporary test workflow to validate action ID",
                "spec": workflow_spec
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": DD_API_KEY,
        "DD-APPLICATION-KEY": DD_APP_KEY,
    }

    try:
        response = make_request(
            f"{DD_URL}/v2/workflows",
            "POST",
            headers,
            payload
        )

        if response.status in (200, 201):
            # Success! Delete the test workflow
            workflow_data = json.loads(response.data.decode("utf-8"))
            workflow_id = workflow_data.get("data", {}).get("id")
            print(f"✓ ACTION ID WORKS: {action_id}")
            print(f"  Created test workflow: {workflow_id}")

            # Delete it
            delete_response = make_request(
                f"{DD_URL}/v2/workflows/{workflow_id}",
                "DELETE",
                headers
            )
            if delete_response.status in (200, 204):
                print(f"  Deleted test workflow")
            return True
        else:
            error_data = response.data.decode("utf-8")
            # Check if the error is about the action ID
            if "no action registered" in error_data:
                print(f"✗ Invalid action ID: {action_id}")
                return False
            else:
                # Different error - might be worth investigating
                print(f"? Action ID: {action_id} - Different error: {error_data[:200]}")
                return False
    except Exception as e:
        print(f"✗ Error testing {action_id}: {e}")
        return False


def main():
    print("=" * 70)
    print("Testing Action ID Variations for IAM Attach Role Policy")
    print("=" * 70)

    # Get connection ID
    print("\n1. Looking up AWS connection...")
    connection_id = get_connection_id_by_name(
        DD_API_KEY,
        DD_APP_KEY,
        "DatadogWorkflowAutomationConnection"
    )

    if not connection_id:
        print("ERROR: Could not find AWS action connection")
        return 1

    print(f"   Found connection: {connection_id}")

    # Test each action ID variation
    print("\n2. Testing action ID variations...")
    valid_action_ids = []

    for action_id in ACTION_ID_VARIATIONS:
        print(f"\nTesting: {action_id}")
        if test_action_id(connection_id, action_id):
            valid_action_ids.append(action_id)

    # Report results
    print("\n" + "=" * 70)
    print("RESULTS")
    print("=" * 70)

    if valid_action_ids:
        print(f"\n✓ Found {len(valid_action_ids)} valid action ID(s):")
        for action_id in valid_action_ids:
            print(f"  - {action_id}")
        print("\nUpdate create_workflows.py to use the correct action ID.")
        return 0
    else:
        print("\n✗ No valid action IDs found!")
        print("\nThis could mean:")
        print("  1. The action is not available in this Datadog account/org")
        print("  2. The AWS connection needs additional permissions")
        print("  3. The action ID format is different than expected")
        print("\nNext steps:")
        print("  - Check the Datadog Workflow UI and manually create a workflow")
        print("  - Export it and look at the action ID used")
        print("  - Or contact Datadog support to confirm the action exists")
        return 1


if __name__ == "__main__":
    sys.exit(main())
