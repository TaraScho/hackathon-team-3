"""Sensitive data redaction for security."""

import re
from typing import Any, Dict, Pattern


class SensitiveDataRedactor:
    """Redacts sensitive information from configuration data."""

    # Patterns for detecting sensitive data
    PATTERNS: Dict[str, Pattern] = {
        "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
        "aws_secret_key": re.compile(r"[A-Za-z0-9/+=]{40}"),
        "api_key": re.compile(r"api[_-]?key['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9_\-]+)", re.IGNORECASE),
        "password": re.compile(r"password['\"]?\s*[:=]\s*['\"]?([^\s'\"]+)", re.IGNORECASE),
        "token": re.compile(r"token['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9_\-\.]+)", re.IGNORECASE),
        "private_key": re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA )?PRIVATE KEY-----"),
    }

    # Keys that commonly contain sensitive data
    SENSITIVE_KEYS = {
        "password",
        "secret",
        "token",
        "api_key",
        "apikey",
        "access_key",
        "secret_key",
        "private_key",
        "credential",
        "auth",
    }

    def redact_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recursively redact sensitive data from a dictionary.

        Args:
            data: Dictionary potentially containing sensitive data

        Returns:
            Dictionary with sensitive data redacted
        """
        redacted = {}

        for key, value in data.items():
            # Check if key name suggests sensitive data
            if any(sensitive in key.lower() for sensitive in self.SENSITIVE_KEYS):
                redacted[key] = "***REDACTED***"
            elif isinstance(value, dict):
                redacted[key] = self.redact_dict(value)
            elif isinstance(value, list):
                redacted[key] = [
                    self.redact_dict(item) if isinstance(item, dict) else self.redact_string(str(item))
                    for item in value
                ]
            elif isinstance(value, str):
                redacted[key] = self.redact_string(value)
            else:
                redacted[key] = value

        return redacted

    def redact_string(self, text: str) -> str:
        """
        Redact sensitive patterns from a string.

        Args:
            text: String potentially containing sensitive data

        Returns:
            String with sensitive patterns redacted
        """
        redacted = text

        for pattern_name, pattern in self.PATTERNS.items():
            redacted = pattern.sub("***REDACTED***", redacted)

        return redacted
