#!/usr/bin/env python3
"""
Create a test span for the summarize_incidents action.

This script creates a simple span with the action_name tag so that
evaluations can be joined to it.
"""

import os
import sys
import time
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


def create_test_span():
    """Create a test span using ddtrace."""
    try:
        from ddtrace import tracer
        from ddtrace.llmobs import LLMObs
    except ImportError:
        print("Error: ddtrace not installed")
        print("Install with: pip install ddtrace")
        return False

    # Load environment
    load_env()

    # Verify credentials
    api_key = os.getenv('DD_API_KEY') or os.getenv('DATADOG_API_KEY')
    if not api_key:
        print("Error: DD_API_KEY not set")
        return False

    # Set service name
    os.environ['DD_SERVICE'] = 'action_catalog'
    os.environ['DD_ENV'] = 'dev'

    print("Creating test span for summarize_incidents action...")

    # Enable LLM Observability
    try:
        LLMObs.enable(
            ml_app="action_catalog",
            agentless_enabled=True,
            api_key=api_key,
            site=os.getenv('DATADOG_SITE', 'datadoghq.com')
        )
        print("✓ LLMObs enabled")
    except Exception as e:
        print(f"Error enabling LLMObs: {e}")
        return False

    # Create a span
    try:
        with tracer.trace("summarize_incidents", service="action_catalog") as span:
            # Set tags
            span.set_tag("action_name", "summarize_incidents")
            span.set_tag("action_type", "llm_assisted")
            span.set_tag("ml_app", "action_catalog")

            # Simulate some work
            print("  Simulating action execution...")
            time.sleep(1)

            # Set metadata
            span.set_tag("status", "success")
            span.set_tag("duration_ms", 1000)

        print("✓ Span created successfully")
        print("  Tags: action_name=summarize_incidents, action_type=llm_assisted")

        # Give time for span to be sent
        print("  Waiting for span to be flushed...")
        time.sleep(2)

        # Force flush
        tracer.shutdown()

        print("✓ Span flushed to Datadog")
        return True

    except Exception as e:
        print(f"✗ Error creating span: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("Datadog Test Span Creator")
    print("="*50)
    print()

    success = create_test_span()

    if success:
        print("\n✅ Test span created successfully")
        print("\nNext steps:")
        print("1. Wait 1-2 minutes for span to appear in Datadog")
        print("2. Run submit_evaluation.py to submit the evaluation")
        sys.exit(0)
    else:
        print("\n❌ Failed to create test span")
        sys.exit(1)
