import json
import os
import random
import uuid
import time

import boto3


sfn = boto3.client("stepfunctions")
STATE_MACHINE_ARN = os.environ["STATE_MACHINE_ARN"]

SAMPLE_TEXTS = [
    "Hello, how are you today?",
    "The quick brown fox jumps over the lazy dog.",
    "Polly wants a cracker and some sunflower seeds.",
    "Cloud computing is transforming the way we build software.",
    "Observability helps teams understand complex distributed systems.",
    "The parrot repeated everything the pirate said.",
    "Monitoring your infrastructure is critical for reliability.",
    "Step Functions orchestrate complex workflows with ease.",
    "Data streams monitoring tracks message flow across queues.",
    "Serverless architectures reduce operational overhead significantly.",
]

LANGUAGES = ["spanish", "french", "german", "italian", "portuguese", "japanese"]


def lambda_handler(event, context):
    request_id = str(uuid.uuid4())
    text = random.choice(SAMPLE_TEXTS)
    language = random.choice(LANGUAGES)

    payload = {
        "requestId": request_id,
        "text": text,
        "targetLanguage": language,
        "source": "traffic-generator",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    print(f"Starting execution: {request_id} ({language})")

    response = sfn.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        name=f"traffic-{request_id}",
        input=json.dumps(payload),
    )

    print(f"Started execution: {response['executionArn']}")

    return {
        "requestId": request_id,
        "executionArn": response["executionArn"],
    }
