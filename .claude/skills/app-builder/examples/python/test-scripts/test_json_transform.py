#!/usr/bin/env python3
"""
Phase 1: Test JSON Transformation for App Builder
Tests connection ID replacement and JSON structure wrapping without making API calls.
"""

import json
import re
from pathlib import Path

def remove_fields(obj, fields_to_remove):
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
            k: remove_fields(v, fields_to_remove)
            for k, v in obj.items()
            if k not in fields_to_remove
        }
    elif isinstance(obj, list):
        return [remove_fields(item, fields_to_remove) for item in obj]
    return obj


def transform_app_json(json_file_path, connection_id, connection_name):
    """
    Transform app JSON for API submission.

    Steps:
    1. Load JSON from file
    2. Replace all connectionId values
    3. Reconstruct connections array
    4. Remove 'handle' and 'id' fields
    5. Wrap in API envelope structure

    Args:
        json_file_path: Path to app JSON file
        connection_id: New connection ID to use
        connection_name: Connection name

    Returns:
        Transformed JSON ready for API submission
    """
    print(f"\n{'='*70}")
    print(f"Transforming: {json_file_path}")
    print(f"Connection ID: {connection_id}")
    print(f"Connection Name: {connection_name}")
    print(f"{'='*70}\n")

    # Load the JSON file
    with open(json_file_path, 'r') as f:
        app_data = json.load(f)

    print(f"✓ Loaded JSON successfully")
    print(f"  Original app name: {app_data.get('name', 'UNKNOWN')}")

    # Step 1: Replace all connectionId values
    # Convert to string, do regex replacement, convert back
    json_str = json.dumps(app_data, indent=2)

    # Count how many connectionIds we're replacing
    original_count = len(re.findall(r'"connectionId":\s*"[^"]*"', json_str))
    print(f"\n✓ Found {original_count} connectionId occurrences to replace")

    # Do the replacement
    json_str = re.sub(
        r'"connectionId":\s*"[^"]*"',
        f'"connectionId": "{connection_id}"',
        json_str
    )

    app_data = json.loads(json_str)

    # Verify replacement worked
    new_json_str = json.dumps(app_data)
    new_count = len(re.findall(rf'"connectionId":\s*"{re.escape(connection_id)}"', new_json_str))
    print(f"✓ Replaced with new connection ID ({new_count} occurrences)")

    # Step 2: Remove 'handle' and 'id' fields BEFORE reconstructing connections
    # This way we remove all the component/query IDs but then add back connection id
    fields_to_remove = {'handle', 'id'}
    print(f"\n✓ Removing fields: {fields_to_remove}")
    app_data_cleaned = remove_fields(app_data, fields_to_remove)

    # Step 3: Reconstruct connections array AFTER cleanup
    original_connections = app_data.get('connections', [])
    print(f"✓ Original connections array had {len(original_connections)} entries")

    app_data_cleaned['connections'] = [{
        "id": connection_id,
        "name": connection_name
    }]
    print(f"✓ Reconstructed connections array with new connection")

    # Count how many fields we removed
    original_str = json.dumps(app_data)
    cleaned_str = json.dumps(app_data_cleaned)
    handle_count = original_str.count('"handle":')
    id_count = original_str.count('"id":')
    print(f"  Removed {handle_count} 'handle' fields")
    print(f"  Removed {id_count} 'id' fields")

    # Step 4: Wrap in API envelope structure
    api_payload = {
        "data": {
            "type": "appDefinitions",
            "attributes": app_data_cleaned
        }
    }

    print(f"\n✓ Wrapped in API envelope structure")

    return api_payload


def main():
    """Run the transformation test."""

    # Test configuration
    test_connection_id = "test-conn-12345678-1234-1234-1234-123456789abc"
    test_connection_name = "TestAWSConnection"

    # Path to test JSON file
    json_file = Path(__file__).parent / "central_lambda_source" / "datadog_helpers" / "app-builder-apps" / "manage-dynamodb.json"

    if not json_file.exists():
        print(f"❌ Error: JSON file not found at {json_file}")
        return

    # Transform the JSON
    try:
        transformed = transform_app_json(
            json_file_path=str(json_file),
            connection_id=test_connection_id,
            connection_name=test_connection_name
        )

        print(f"\n{'='*70}")
        print("TRANSFORMATION COMPLETE")
        print(f"{'='*70}\n")

        # Print a preview of the transformed JSON
        print("Preview of transformed structure:")
        print(json.dumps(transformed, indent=2)[:1000] + "\n... (truncated)")

        # Verify key aspects
        print(f"\n{'='*70}")
        print("VERIFICATION CHECKS")
        print(f"{'='*70}\n")

        print(f"✓ Has 'data' wrapper: {('data' in transformed)}")
        print(f"✓ Has 'type' field: {('type' in transformed.get('data', {}))}")
        print(f"✓ Type is 'appDefinitions': {(transformed.get('data', {}).get('type') == 'appDefinitions')}")
        print(f"✓ Has 'attributes': {('attributes' in transformed.get('data', {}))}")

        attrs = transformed.get('data', {}).get('attributes', {})
        print(f"✓ App name preserved: {attrs.get('name', 'MISSING')}")
        print(f"✓ Connections array updated: {len(attrs.get('connections', []))} connection(s)")

        if attrs.get('connections'):
            conn = attrs['connections'][0]
            print(f"  - Connection ID: {conn.get('id', 'MISSING')}")
            print(f"  - Connection Name: {conn.get('name', 'MISSING')}")

        # Check if any connectionId still has old value (shouldn't happen)
        json_str = json.dumps(transformed)
        non_test_conn_ids = re.findall(r'"connectionId":\s*"([^"]*)"', json_str)
        non_test_conn_ids = [cid for cid in non_test_conn_ids if cid != test_connection_id]

        if non_test_conn_ids:
            print(f"\n⚠️  WARNING: Found connectionIds that weren't replaced:")
            for cid in set(non_test_conn_ids):
                print(f"    - {cid}")
        else:
            print(f"\n✓ All connectionIds successfully replaced with test connection ID")

        print(f"\n{'='*70}")
        print("✅ PHASE 1 TEST COMPLETE - Ready for Phase 2")
        print(f"{'='*70}\n")

        # Save transformed JSON for inspection
        output_file = Path(__file__).parent / "test_output_transformed_app.json"
        with open(output_file, 'w') as f:
            json.dump(transformed, f, indent=2)
        print(f"Full transformed JSON saved to: {output_file}")

    except Exception as e:
        print(f"\n❌ ERROR during transformation:")
        print(f"   {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
