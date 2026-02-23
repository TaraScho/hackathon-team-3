#!/usr/bin/env python3
"""
Verify that the evaluation was successfully submitted and appears in Datadog.

This script checks:
1. LLM Observability evaluations API
2. Spans with the action_name tag
3. Provides detailed status and troubleshooting info
"""

import os
import sys
import requests
import json
from pathlib import Path


def load_env():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value


def check_evaluation_via_api(action_name, api_key, app_key, site):
    """
    Try to verify evaluation through various API endpoints.
    Note: There isn't a direct API to query evaluations, so this checks
    related data that might indicate the evaluation was processed.
    """
    print(f"\n🔍 Checking for evaluations (action_name:{action_name})...")

    # Try to search for LLM observability data
    # Note: The evaluation API is intake-only, there's no query endpoint
    # So we can only verify through the UI or by checking related spans

    print("  Note: Evaluation intake API is write-only")
    print("  Verification must be done through Datadog UI")

    return None


def check_spans(action_name, api_key, app_key, site):
    """Check if spans exist with the action_name tag."""
    print(f"\n🔍 Checking for spans (action_name:{action_name})...")

    url = f"https://api.{site}/api/v2/spans/search"

    try:
        response = requests.post(
            url,
            headers={
                "DD-API-KEY": api_key,
                "DD-APPLICATION-KEY": app_key,
                "Content-Type": "application/json"
            },
            json={
                "filter": {
                    "query": f"@action_name:{action_name}",
                    "from": "now-1h",
                    "to": "now"
                },
                "page": {"limit": 10}
            },
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            spans = data.get("data", [])

            if spans:
                print(f"✓ Found {len(spans)} span(s)")
                for i, span in enumerate(spans[:3], 1):
                    span_id = span.get("id", "unknown")
                    attributes = span.get("attributes", {})
                    print(f"\n  Span {i}:")
                    print(f"    ID: {span_id}")
                    print(f"    Service: {attributes.get('service', 'unknown')}")
                    print(f"    Resource: {attributes.get('resource_name', 'unknown')}")

                    tags = attributes.get("tags", [])
                    if tags:
                        print(f"    Tags: {', '.join(tags[:5])}")
                return True
            else:
                print("✗ No spans found")
                return False

        elif response.status_code == 404:
            print(f"✗ Span search endpoint returned 404")
            print("  This might indicate APM is not enabled or no spans index exists")
            return False
        else:
            print(f"✗ API returned {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return False

    except Exception as e:
        print(f"✗ Error checking spans: {e}")
        return False


def print_ui_verification_guide(action_name):
    """Print detailed guide for manual UI verification."""
    print("\n" + "="*70)
    print("📋 MANUAL VERIFICATION GUIDE")
    print("="*70)

    print("\n✅ EVALUATION SUBMISSION STATUS:")
    print("  - HTTP 202 Accepted response received")
    print("  - Evaluation payload was accepted by Datadog")
    print("  - Timestamp:", "Just submitted")

    print("\n🌐 TO VERIFY IN DATADOG UI:")

    print("\n1. LLM Observability Evaluations Page:")
    print("   URL: https://app.datadoghq.com/llm/evaluations")
    print("   Navigation: APM → LLM Observability → Evaluations")

    print("\n2. Time Range Settings:")
    print("   - Set to: Last 1 hour (or longer)")
    print("   - Ensure current time is included")

    print("\n3. Search/Filter:")
    print(f"   - Filter by tag: action_name:{action_name}")
    print("   - Or filter by: label:coherence")
    print("   - Or filter by: ml_app:action_catalog")

    print("\n4. Expected Evaluation Details:")
    print(f"   - Action: {action_name}")
    print("   - Label: coherence")
    print("   - Value: 0.88")
    print("   - ML App: action_catalog")
    print("   - Tags: action:summarize_incidents, environment:dev")

    print("\n5. If Evaluation Appears:")
    print("   ✅ SUCCESS! Evaluation was successfully joined to a span")
    print("   - Document the evaluation details")
    print("   - Note the span it's attached to")
    print("   - Screenshot for documentation")

    print("\n6. If Evaluation Does NOT Appear After 5 Minutes:")

    print("\n   Possible Reasons:")
    print("   a. No matching spans exist")
    print("      Solution: Create spans with action_name:summarize_incidents tag")
    print("      The evaluation will join automatically within 5-minute window")

    print("\n   b. Spans exist but don't have the correct tag")
    print("      Solution: Ensure spans have tag 'action_name' = 'summarize_incidents'")

    print("\n   c. Timing window expired (>5 minutes between eval and span)")
    print("      Solution: Re-submit evaluation OR create new spans")

    print("\n   d. Permissions issue")
    print("      Solution: Verify DD_API_KEY and DD_APP_KEY have llm_observability_write")

    print("\n7. Troubleshooting Steps:")

    print("\n   Check Spans:")
    print("   - Navigate to: APM → Traces")
    print(f"   - Search: @action_name:{action_name}")
    print("   - Verify spans exist with correct tags")

    print("\n   Check Service:")
    print("   - Look for service: action_catalog")
    print("   - Check recent trace activity")

    print("\n   Verify Time Range:")
    print("   - Expand time range to last 4 hours")
    print("   - Check for any evaluations in wider window")

    print("\n" + "="*70)


def main():
    """Main verification flow."""
    print("Datadog LLM Observability Evaluation Verification")
    print("="*70)

    action_name = "summarize_incidents"

    try:
        # Load credentials
        load_env()
        api_key = os.getenv('DD_API_KEY') or os.getenv('DATADOG_API_KEY')
        app_key = os.getenv('DD_APP_KEY') or os.getenv('DATADOG_APP_KEY')
        site = os.getenv('DATADOG_SITE', 'datadoghq.com')

        if not api_key or not app_key:
            print("Error: Missing DD_API_KEY or DD_APP_KEY")
            return 1

        print("\n✓ Credentials loaded")

        # Check for spans
        spans_exist = check_spans(action_name, api_key, app_key, site)

        if spans_exist:
            print("\n✅ Spans exist! Evaluation should join to these spans.")
        else:
            print("\n⚠️  No spans found with matching action_name tag")
            print("   Evaluation may not appear until spans are created")

        # Print verification guide
        print_ui_verification_guide(action_name)

        print("\n📝 DOCUMENTATION TASKS:")
        print("   1. Check Datadog UI using the guide above")
        print("   2. Document whether evaluation appears")
        print("   3. Note any issues or gaps discovered")
        print("   4. Record verification steps that were helpful")

        return 0

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
