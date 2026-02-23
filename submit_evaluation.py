#!/usr/bin/env python3
"""
Submit Datadog LLM Observability Evaluation with Verification

This script submits an evaluation for the 'summarize_incidents' action with proper verification:
1. Verifies credentials exist
2. Checks that spans exist for the action before submitting evaluation
3. Submits the evaluation with label "coherence" and value 0.88
4. Provides verification instructions for the Datadog UI

Requirements:
- DD_API_KEY or DATADOG_API_KEY environment variable
- DD_APP_KEY or DATADOG_APP_KEY environment variable
- DATADOG_SITE environment variable (optional, defaults to datadoghq.com)

Usage:
    python3 submit_evaluation.py

The script will submit an evaluation with:
- ml_app: action_catalog
- label: coherence
- metric_type: score
- score_value: 0.88
- join_on: tag-based joining with action_name=summarize_incidents
"""

import os
import sys
import requests
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

# Load environment variables from .env file
def load_env():
    """Load environment variables from .env file in the same directory."""
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value


def verify_credentials() -> Tuple[str, str, str]:
    """Verify DD_API_KEY and DD_APP_KEY are set and return them."""
    load_env()

    api_key = os.getenv('DD_API_KEY') or os.getenv('DATADOG_API_KEY')
    app_key = os.getenv('DD_APP_KEY') or os.getenv('DATADOG_APP_KEY')
    site = os.getenv('DATADOG_SITE', 'datadoghq.com')

    if not api_key:
        raise ValueError("DD_API_KEY or DATADOG_API_KEY environment variable is not set")
    if not app_key:
        raise ValueError("DD_APP_KEY or DATADOG_APP_KEY environment variable is not set")

    print("✓ Credentials verified")
    return api_key, app_key, site


def verify_span_exists(
    action_name: str,
    api_key: str,
    app_key: str,
    site: str,
    max_wait_seconds: int = 60
) -> bool:
    """
    Check if spans exist with the specified action_name tag.

    Args:
        action_name: The action name to search for
        api_key: Datadog API key
        app_key: Datadog Application key
        site: Datadog site (e.g., datadoghq.com)
        max_wait_seconds: Maximum time to wait for spans to appear

    Returns:
        True if spans found, False otherwise
    """
    print(f"\n🔍 Checking for spans with action_name:{action_name}...")

    url = f"https://api.{site}/api/v2/spans/search"
    start_time = time.time()
    attempts = 0

    while (time.time() - start_time) < max_wait_seconds:
        attempts += 1

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
                        "from": "now-15m",
                        "to": "now"
                    },
                    "page": {"limit": 1}
                },
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                spans = data.get("data", [])

                if spans and len(spans) > 0:
                    span = spans[0]
                    span_id = span.get("id", "unknown")
                    attributes = span.get("attributes", {})
                    tags = attributes.get("tags", [])

                    print(f"✓ Found span: {span_id}")
                    print(f"  Service: {attributes.get('service', 'unknown')}")
                    if tags:
                        print(f"  Sample tags: {', '.join(tags[:5])}")
                    return True
                else:
                    print(f"  Attempt {attempts}: No spans found yet...")
            elif response.status_code == 403:
                print(f"✗ Authentication error: {response.status_code}")
                print(f"  Response: {response.text}")
                return False
            else:
                print(f"  Attempt {attempts}: API returned {response.status_code}")
                if response.text:
                    print(f"  Response snippet: {response.text[:200]}")

        except requests.exceptions.RequestException as e:
            print(f"  Attempt {attempts}: Request error: {e}")

        if (time.time() - start_time) < max_wait_seconds:
            time.sleep(5)  # Wait 5 seconds before retry

    print(f"✗ No spans found after {attempts} attempts ({max_wait_seconds}s)")
    return False

def submit_evaluation(
    action_name: str,
    label: str,
    score_value: float,
    api_key: str,
    app_key: str,
    site: str
) -> Optional[dict]:
    """
    Submit an evaluation to Datadog LLM Observability.

    Args:
        action_name: The action name to join evaluations to
        label: Evaluation label (e.g., "coherence", "accuracy")
        score_value: Score value (0.0 to 1.0)
        api_key: Datadog API key
        app_key: Datadog Application key
        site: Datadog site (e.g., datadoghq.com)

    Returns:
        Response data if successful, None otherwise
    """
    print(f"\n📤 Submitting evaluation...")
    print(f"  Action: {action_name}")
    print(f"  Label: {label}")
    print(f"  Score: {score_value}")

    # API endpoint
    url = f"https://api.{site}/api/intake/llm-obs/v2/eval-metric"

    # Headers
    headers = {
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
        "Content-Type": "application/json"
    }

    # Evaluation payload
    payload = {
        "data": {
            "type": "evaluation_metric",
            "attributes": {
                "metrics": [
                    {
                        "ml_app": "action_catalog",
                        "label": label,
                        "metric_type": "score",
                        "score_value": score_value,
                        "tags": [
                            f"action:{action_name}",
                            "environment:dev",
                            "submitted_by:verification_script"
                        ],
                        "timestamp_ms": int(datetime.now().timestamp() * 1000),
                        # Tag-based joining: joins to spans with action_name tag
                        "join_on": {
                            "tag": {
                                "key": "action_name",
                                "value": action_name
                            }
                        }
                    }
                ]
            }
        }
    }

    print(f"  Endpoint: {url}")
    print(f"  Payload:\n{json.dumps(payload, indent=2)}")

    # Submit evaluation
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)

        print(f"\n  Response Status: {response.status_code}")

        if response.status_code == 202:
            print("✓ Evaluation submitted successfully (202 Accepted)")
            if response.text:
                return response.json()
            return {}
        else:
            print(f"✗ Submission failed: {response.status_code}")
            print(f"  Response: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"✗ Request error: {e}")
        return None


def print_verification_instructions(action_name: str, label: str, score_value: float):
    """Print instructions for verifying the evaluation in Datadog UI."""
    print("\n" + "="*70)
    print("📋 VERIFICATION INSTRUCTIONS")
    print("="*70)
    print("\n⏱️  Step 1: Wait 1-2 minutes for processing")
    print("\n🌐 Step 2: Navigate to Datadog LLM Observability:")
    print("   URL: https://app.datadoghq.com/llm/evaluations")
    print("   Or: APM → LLM Observability → Evaluations")
    print("\n📅 Step 3: Adjust time range to include the last 15 minutes")
    print("\n🔍 Step 4: Search for evaluations:")
    print(f"   Filter by: action_name:{action_name}")
    print(f"   Or filter by: label:{label}")
    print("\n✅ Step 5: Verify the evaluation appears with:")
    print(f"   - Action: {action_name}")
    print(f"   - Label: {label}")
    print(f"   - Value: {score_value}")
    print(f"   - Tags: action:{action_name}, environment:dev, submitted_by:verification_script")
    print("\n❌ Step 6: If evaluation doesn't appear within 5 minutes:")
    print("   a. Check spans exist:")
    print("      - Navigate to: APM → Traces")
    print(f"      - Search: @action_name:{action_name}")
    print("   b. Verify time range includes submission time")
    print("   c. Check credentials have llm_observability_write permission")
    print("   d. Review API response from submission step")
    print("\n" + "="*70)


def main():
    """Main execution flow with verification steps."""
    print("Datadog LLM Observability Evaluation Submission")
    print("="*70)

    # Configuration
    action_name = "summarize_incidents"
    label = "coherence"
    score_value = 0.88

    try:
        # Step 1: Verify credentials
        print("\n[Step 1/4] Verifying credentials...")
        api_key, app_key, site = verify_credentials()

        # Step 2: Verify spans exist
        print("\n[Step 2/4] Verifying span existence...")
        print(f"Note: Looking for spans with tag 'action_name:{action_name}'")
        print("If no spans exist, you'll need to create them first (run the action)")

        spans_exist = verify_span_exists(
            action_name=action_name,
            api_key=api_key,
            app_key=app_key,
            site=site,
            max_wait_seconds=60
        )

        if not spans_exist:
            print("\n⚠️  WARNING: No spans found!")
            print("The evaluation will be submitted, but it may not appear in Datadog")
            print("unless matching spans are created within 5 minutes.")
            print("\nNote: Continuing with submission anyway...")
            print("(Evaluations can be submitted before spans exist - they will join within 5 min window)")

        # Step 3: Submit evaluation
        print("\n[Step 3/4] Submitting evaluation...")
        result = submit_evaluation(
            action_name=action_name,
            label=label,
            score_value=score_value,
            api_key=api_key,
            app_key=app_key,
            site=site
        )

        if result is None:
            print("\n❌ Evaluation submission failed")
            return 1

        # Step 4: Print verification instructions
        print("\n[Step 4/4] Verification instructions")
        print_verification_instructions(action_name, label, score_value)

        print("\n✅ Process completed successfully")
        print("\nNext steps:")
        print("1. Wait 1-2 minutes")
        print("2. Check the Datadog UI using the instructions above")
        print("3. Document your findings")

        return 0

    except ValueError as e:
        print(f"\n❌ Configuration error: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
