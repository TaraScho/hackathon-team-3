import json
import time


def lambda_handler(event, context):
    print(f"ArchiveResult invoked: {json.dumps(event)}")

    request_id = event.get("requestId", "unknown")

    # Simulate archival work (writing to S3/DynamoDB in a real system)
    time.sleep(0.2)

    print(f"Archived translation result for request {request_id}")

    return {
        "requestId": request_id,
        "archived": True,
        "archiveLocation": f"s3://parrot-translations/{request_id}.json",
    }
