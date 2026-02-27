import json
import time
import hashlib


PARROT_PREFIXES = {
    "spanish": "SQUAWK! Traduccion: ",
    "french": "SQUAWK! Traduction: ",
    "german": "SQUAWK! Ubersetzung: ",
    "italian": "SQUAWK! Traduzione: ",
    "portuguese": "SQUAWK! Traducao: ",
    "japanese": "SQUAWK! Honyaku: ",
}


def lambda_handler(event, context):
    print(f"PerformTranslation invoked: {json.dumps(event)}")

    text = event.get("text", "")
    target_language = event.get("targetLanguage", "spanish")
    request_id = event.get("requestId", "unknown")

    # Simulate translation work
    time.sleep(0.3)

    prefix = PARROT_PREFIXES.get(target_language, "SQUAWK! ")
    translated = f"{prefix}{text} (polly wants a cracker)"

    translation_hash = hashlib.md5(translated.encode()).hexdigest()[:8]

    return {
        "requestId": request_id,
        "originalText": text,
        "targetLanguage": target_language,
        "translatedText": json.dumps({
            "requestId": request_id,
            "language": target_language,
            "translation": translated,
            "hash": translation_hash,
        }),
        "charCount": len(translated),
    }
