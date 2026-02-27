import json
import time

from datadog_lambda.metric import lambda_metric


def lambda_handler(event, context):
    records = event.get("Records", [])
    print(f"WebhookDelivery invoked with {len(records)} records")

    succeeded = 0
    failed = 0

    for record in records:
        try:
            body = json.loads(record.get("body", "{}"))
            request_id = body.get("requestId", "unknown")
            language = body.get("language", "unknown")

            print(f"Delivering translation {request_id} ({language})")

            # Simulate webhook delivery
            time.sleep(0.15)

            print(f"Successfully delivered translation {request_id}")
            succeeded += 1

        except Exception as e:
            print(f"Failed to deliver record: {e}")
            failed += 1

    lambda_metric("parrot.webhook.delivered", succeeded, tags=[f"env:monitoring-aws-lab"])
    if failed:
        lambda_metric("parrot.webhook.failed", failed, tags=[f"env:monitoring-aws-lab"])

    return {
        "batchItemFailures": [],
        "delivered": succeeded,
        "failed": failed,
    }
