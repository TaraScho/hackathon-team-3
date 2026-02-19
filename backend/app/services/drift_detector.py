"""Drift detection engine for comparing expected vs actual infrastructure state."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .sensitive_data import SensitiveDataRedactor


@dataclass
class DriftDiff:
    """Represents a single difference between expected and actual state."""

    path: str
    expected_value: Any
    actual_value: Any
    severity: str  # "info", "warning", "critical"
    suggestion: Optional[str] = None


@dataclass
class DriftResult:
    """Results of drift detection for a resource."""

    resource_type: str
    resource_name: str
    has_drift: bool
    diffs: List[DriftDiff] = field(default_factory=list)
    missing_properties: List[str] = field(default_factory=list)
    extra_properties: List[str] = field(default_factory=list)


class DriftDetector:
    """Detects configuration drift between expected and actual infrastructure state."""

    # Properties that indicate critical changes
    CRITICAL_PROPERTIES = {
        "ami",
        "image",
        "security_group",
        "security_groups",
        "subnet_id",
        "vpc_id",
        "engine_version",
        "availability_zone",
    }

    # Properties that indicate warnings
    WARNING_PROPERTIES = {
        "instance_type",
        "volume_size",
        "backup_retention_period",
        "monitoring_enabled",
        "publicly_accessible",
    }

    def __init__(self):
        """Initialize the drift detector."""
        self.redactor = SensitiveDataRedactor()

    def compare_resources(self, expected: Dict[str, Any], actual: Dict[str, Any]) -> DriftResult:
        """
        Compare expected configuration against actual infrastructure state.

        Args:
            expected: Expected resource configuration from Terraform
            actual: Actual resource state from Datadog

        Returns:
            DriftResult containing all detected differences
        """
        resource_type = expected.get("type", "unknown")
        resource_name = expected.get("name", "unknown")

        diffs: List[DriftDiff] = []
        missing_properties: List[str] = []
        extra_properties: List[str] = []

        # Compare properties
        expected_props = expected.get("properties", {})
        actual_props = actual.get("properties", {})

        # Detect differences in expected properties
        for key, expected_value in expected_props.items():
            if key not in actual_props:
                missing_properties.append(key)
            elif self._values_differ(expected_value, actual_props[key]):
                diff = self._create_diff(
                    path=f"properties.{key}",
                    expected=expected_value,
                    actual=actual_props[key],
                )
                diffs.append(diff)

        # Detect extra properties in actual state
        for key in actual_props:
            if key not in expected_props:
                extra_properties.append(key)

        has_drift = len(diffs) > 0 or len(missing_properties) > 0 or len(extra_properties) > 0

        return DriftResult(
            resource_type=resource_type,
            resource_name=resource_name,
            has_drift=has_drift,
            diffs=diffs,
            missing_properties=missing_properties,
            extra_properties=extra_properties,
        )

    def detect_missing_resources(
        self, expected_resources: List[Dict[str, Any]], actual_resources: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Detect resources that exist in expected config but not in actual state.

        Args:
            expected_resources: List of expected resources
            actual_resources: List of actual resources

        Returns:
            List of missing resources
        """
        actual_ids = {
            (r.get("type"), r.get("name")) for r in actual_resources
        }

        missing = []
        for resource in expected_resources:
            resource_id = (resource.get("type"), resource.get("name"))
            if resource_id not in actual_ids:
                missing.append(resource)

        return missing

    def _values_differ(self, expected: Any, actual: Any) -> bool:
        """
        Check if two values differ, handling different types appropriately.

        Args:
            expected: Expected value
            actual: Actual value

        Returns:
            True if values differ significantly
        """
        # Handle None/null cases
        if expected is None and actual is None:
            return False
        if expected is None or actual is None:
            return True

        # Handle dict comparison
        if isinstance(expected, dict) and isinstance(actual, dict):
            # Compare all keys from expected
            for key in expected:
                if key not in actual:
                    return True
                if self._values_differ(expected[key], actual[key]):
                    return True
            return False

        # Handle list comparison
        if isinstance(expected, list) and isinstance(actual, list):
            if len(expected) != len(actual):
                return True
            return any(self._values_differ(e, a) for e, a in zip(expected, actual))

        # Handle string/number comparison with type coercion
        try:
            if str(expected).lower() == str(actual).lower():
                return False
        except (AttributeError, TypeError):
            pass

        return expected != actual

    def _create_diff(self, path: str, expected: Any, actual: Any) -> DriftDiff:
        """
        Create a DriftDiff object with severity classification and suggestion.

        Args:
            path: Property path (e.g., "properties.instance_type")
            expected: Expected value
            actual: Actual value

        Returns:
            DriftDiff object
        """
        # Redact sensitive data
        expected_redacted = self._redact_value(expected, path)
        actual_redacted = self._redact_value(actual, path)

        # Classify severity
        severity = self._classify_severity(path, expected, actual)

        # Generate suggestion
        suggestion = self._generate_suggestion(path, expected, actual, severity)

        return DriftDiff(
            path=path,
            expected_value=expected_redacted,
            actual_value=actual_redacted,
            severity=severity,
            suggestion=suggestion,
        )

    def _classify_severity(self, path: str, expected: Any, actual: Any) -> str:
        """
        Classify the severity of a drift.

        Args:
            path: Property path
            expected: Expected value
            actual: Actual value

        Returns:
            Severity level: "critical", "warning", or "info"
        """
        property_name = path.split(".")[-1].lower()

        # Check for critical properties
        if any(critical in property_name for critical in self.CRITICAL_PROPERTIES):
            return "critical"

        # Check for warning properties
        if any(warning in property_name for warning in self.WARNING_PROPERTIES):
            return "warning"

        # Tags and labels are typically info-level
        if "tag" in property_name or "label" in property_name:
            return "info"

        # Default to warning for unknown properties
        return "warning"

    def _generate_suggestion(self, path: str, expected: Any, actual: Any, severity: str) -> str:
        """
        Generate an actionable suggestion for fixing the drift.

        Args:
            path: Property path
            expected: Expected value
            actual: Actual value
            severity: Severity level

        Returns:
            Suggestion text
        """
        property_name = path.split(".")[-1]

        if severity == "critical":
            return f"CRITICAL: Update {property_name} from '{actual}' to '{expected}' immediately to match expected configuration."
        elif severity == "warning":
            return f"WARNING: Consider updating {property_name} from '{actual}' to '{expected}' to align with expected configuration."
        else:
            return f"INFO: {property_name} differs from expected value. Review if update from '{actual}' to '{expected}' is needed."

    def _redact_value(self, value: Any, path: str = "") -> Any:
        """
        Redact sensitive data from a value.

        Args:
            value: Value to redact
            path: Property path to check for sensitive keys

        Returns:
            Redacted value
        """
        # Check if the property name itself suggests sensitive data
        property_name = path.split(".")[-1].lower() if path else ""
        if any(sensitive in property_name for sensitive in self.redactor.SENSITIVE_KEYS):
            return "***REDACTED***"

        if isinstance(value, dict):
            return self.redactor.redact_dict(value)
        elif isinstance(value, str):
            return self.redactor.redact_string(value)
        else:
            return value
