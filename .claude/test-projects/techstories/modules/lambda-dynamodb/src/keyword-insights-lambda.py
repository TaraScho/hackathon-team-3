import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

# Define the tech keywords to track
TECH_KEYWORDS = [
    "ai", "machine learning", "artificial intelligence", "deep learning",
    "python", "javascript", "typescript", "golang", "java", "ruby",
    "cloud", "aws", "azure", "gcp", "serverless", "microservices",
    "kubernetes", "docker", "containers", "terraform", "ansible",
    "ci/cd", "devops", "sre", "monitoring", "observability",
    "blockchain", "web3", "crypto", "security", "authentication",
    "api", "graphql", "rest api", "edge computing", "iot", "5g",
    "data science", "big data", "sql", "nosql", "postgresql", "mongodb",
    "streaming", "kafka", "event-driven", "scalability", "resilience"
]

def extract_keywords(text):
    """Extract keywords from text by simple case-insensitive matching."""
    found = []
    text_lower = text.lower()
    for keyword in TECH_KEYWORDS:
        if keyword in text_lower:
            found.append(keyword)
    return found

def lambda_handler(event, context):
    """Process SQS events containing post data and check for keywords."""
    print(f"Received event with {len(event['Records'])} records")

    for i, record in enumerate(event['Records']):
        try:
            body = json.loads(record['body'])
            title = body.get('title', '<no title>')
            content = body.get('content', '')

            print(f"[Record {i}] Title: {title}")
            print(f"[Record {i}] Content length: {len(content)} characters")

            keywords = extract_keywords(content)
            print(f"[Record {i}] Found keywords: {keywords}")

            for keyword in keywords:
                response = table.update_item(
                    Key={'keyword': keyword},
                    UpdateExpression="ADD #count :inc",
                    ExpressionAttributeNames={'#count': 'count'},
                    ExpressionAttributeValues={':inc': 1}
                )
                print(f"[Record {i}] Incremented count for keyword '{keyword}'")

        except Exception as e:
            print(f"[Record {i}] Error processing record: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps("Processed messages")
    }
