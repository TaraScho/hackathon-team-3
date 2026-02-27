import json
import time


def lambda_handler(event, context):
    print(f"MarkComplete invoked: {json.dumps(event)}")

    request_id = event.get("requestId", "unknown")
    archive_error = event.get("archiveError")

    # Simulate completion bookkeeping
    time.sleep(0.1)

    status = "completed_with_archive_error" if archive_error else "completed"

    if archive_error:
        print(f"Request {request_id} completed with archive error: {json.dumps(archive_error)}")
    else:
        print(f"Request {request_id} completed successfully")

    return {
        "requestId": request_id,
        "status": status,
        "completedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
