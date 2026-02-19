"""Tests for drift detection engine."""

import pytest
from app.services.drift_detector import DriftDetector, DriftResult, DriftDiff


@pytest.fixture
def drift_detector():
    """Create a DriftDetector instance."""
    return DriftDetector()


def test_compare_resources_no_drift(drift_detector):
    """Test comparing resources with no drift."""
    expected = {
        "type": "aws_instance",
        "name": "web-server",
        "properties": {
            "instance_type": "t2.micro",
            "ami": "ami-12345678",
            "tags": {"Environment": "production"}
        }
    }

    actual = {
        "type": "aws_instance",
        "name": "web-server",
        "properties": {
            "instance_type": "t2.micro",
            "ami": "ami-12345678",
            "tags": {"Environment": "production"}
        }
    }

    result = drift_detector.compare_resources(expected, actual)

    assert result is not None
    assert result.has_drift is False
    assert len(result.diffs) == 0


def test_compare_resources_with_drift(drift_detector):
    """Test comparing resources with drift."""
    expected = {
        "type": "aws_instance",
        "name": "web-server",
        "properties": {
            "instance_type": "t2.micro",
            "ami": "ami-12345678"
        }
    }

    actual = {
        "type": "aws_instance",
        "name": "web-server",
        "properties": {
            "instance_type": "t2.small",
            "ami": "ami-12345678"
        }
    }

    result = drift_detector.compare_resources(expected, actual)

    assert result is not None
    assert result.has_drift is True
    assert len(result.diffs) > 0

    # Check instance_type drift
    instance_type_diff = next(
        (d for d in result.diffs if d.path == "properties.instance_type"),
        None
    )
    assert instance_type_diff is not None
    assert instance_type_diff.expected_value == "t2.micro"
    assert instance_type_diff.actual_value == "t2.small"
    assert instance_type_diff.severity in ["info", "warning", "critical"]


def test_sensitive_data_redaction(drift_detector):
    """Test that sensitive data is redacted in drift results."""
    expected = {
        "type": "aws_db_instance",
        "name": "database",
        "properties": {
            "password": "super_secret_password",
            "api_key": "sk-1234567890abcdef"
        }
    }

    actual = {
        "type": "aws_db_instance",
        "name": "database",
        "properties": {
            "password": "different_password",
            "api_key": "sk-9876543210fedcba"
        }
    }

    result = drift_detector.compare_resources(expected, actual)

    assert result.has_drift is True

    # Verify sensitive data is redacted
    for diff in result.diffs:
        assert "***REDACTED***" in str(diff.expected_value) or diff.expected_value == "***REDACTED***"
        assert "***REDACTED***" in str(diff.actual_value) or diff.actual_value == "***REDACTED***"
