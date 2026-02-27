import json
import time


SUPPORTED_LANGUAGES = ["spanish", "french", "german", "italian", "portuguese", "japanese"]


def lambda_handler(event, context):
    print(f"ValidateRequest invoked: {json.dumps(event)}")

    text = event.get("text", "")
    target_language = event.get("targetLanguage", "").lower()
    request_id = event.get("requestId", "unknown")

    if not text:
        raise Exception("ValidationError: 'text' field is required")

    if target_language not in SUPPORTED_LANGUAGES:
        raise Exception(
            f"ValidationError: unsupported language '{target_language}'. "
            f"Supported: {', '.join(SUPPORTED_LANGUAGES)}"
        )

    # Simulate validation processing
    time.sleep(0.1)

    return {
        "requestId": request_id,
        "text": text,
        "targetLanguage": target_language,
        "validated": True,
        "charCount": len(text),
    }
