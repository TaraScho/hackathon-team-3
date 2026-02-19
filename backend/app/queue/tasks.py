"""Redis queue tasks for async drift detection."""

import logging
import shutil
from pathlib import Path
from typing import Optional
from uuid import UUID
from datetime import datetime, timezone

from redis import Redis
from rq import Queue

from app.config import settings
from app.database import SessionLocal
from app.models import Repository, ConfigResource, DriftReport, DriftStatus, Severity, ResourceType
from app.services.git_ingestion import GitIngestionService
from app.services.datadog_client import DatadogClient
from app.services.drift_detector import DriftDetector

# Setup logging
logger = logging.getLogger(__name__)

# Redis connection
redis_conn = Redis.from_url(settings.REDIS_URL)
queue = Queue("drift_detection", connection=redis_conn)


def enqueue_drift_detection(repository_id: UUID) -> str:
    """
    Enqueue a drift detection job for a repository.

    Args:
        repository_id: UUID of the repository to scan

    Returns:
        Job ID for tracking
    """
    job = queue.enqueue(
        run_drift_detection_job,
        repository_id,
        job_timeout="30m",  # 30 minute timeout
    )
    logger.info(f"Enqueued drift detection job {job.id} for repository {repository_id}")
    return job.id


def run_drift_detection_job(repository_id: UUID) -> dict:
    """
    Main drift detection job that orchestrates the entire pipeline.

    Pipeline:
    1. Fetch repository from database
    2. Clone and ingest configs with GitIngestionService
    3. Store configs in ConfigResource table
    4. Fetch actual state from Datadog
    5. Run drift detection
    6. Store drift reports
    7. Send Datadog events and metrics
    8. Clean up workspace

    Args:
        repository_id: UUID of the repository to scan

    Returns:
        dict with job results
    """
    db = SessionLocal()
    workspace_path: Optional[Path] = None

    try:
        logger.info(f"Starting drift detection job for repository {repository_id}")

        # Step 1: Fetch repository from database
        repository = db.query(Repository).filter(Repository.id == repository_id).first()
        if not repository:
            raise ValueError(f"Repository {repository_id} not found")

        logger.info(f"Processing repository: {repository.git_url}")

        # Step 2: Clone and ingest configs with GitIngestionService
        git_service = GitIngestionService()
        ingestion_result = git_service.ingest_repository(
            repo_url=repository.git_url,
            branch=repository.branch
        )

        workspace_path = ingestion_result['repo_path']
        config_files = ingestion_result['config_files']
        resources = ingestion_result['resources']

        logger.info(f"Found {len(config_files)} config files, parsed {len(resources)} resources")

        # Step 3: Store configs in ConfigResource table
        config_resources = []
        for resource in resources:
            config_resource = ConfigResource(
                repository_id=repository.id,
                resource_type=ResourceType.TERRAFORM,  # For now, only Terraform
                file_path=str(resource.file_path),
                resource_name=resource.name,
                expected_config={
                    "type": resource.type,
                    "name": resource.name,
                    "properties": resource.properties,
                    "tags": resource.tags,
                }
            )
            db.add(config_resource)
            config_resources.append(config_resource)

        db.commit()
        logger.info(f"Stored {len(config_resources)} config resources in database")

        # Step 4: Fetch actual state from Datadog
        datadog_client = DatadogClient()
        actual_hosts = datadog_client.get_infrastructure_list()
        logger.info(f"Fetched {len(actual_hosts)} hosts from Datadog")

        # Step 5: Run drift detection
        drift_detector = DriftDetector()
        drift_reports = []
        drift_count = 0

        for config_resource in config_resources:
            # Find matching actual resource by name/tags
            actual_resource = _find_matching_resource(
                config_resource.expected_config,
                actual_hosts
            )

            if actual_resource:
                # Compare expected vs actual
                drift_result = drift_detector.compare_resources(
                    expected=config_resource.expected_config,
                    actual=actual_resource
                )

                # Store actual config
                config_resource.actual_config = actual_resource
                config_resource.last_checked_timestamp = datetime.now(timezone.utc)

                # Create drift report
                if drift_result.has_drift:
                    drift_count += 1
                    status = DriftStatus.DRIFTED
                    severity = _determine_severity(drift_result)
                else:
                    status = DriftStatus.NO_DRIFT
                    severity = Severity.LOW

                drift_report = DriftReport(
                    config_resource_id=config_resource.id,
                    status=status,
                    severity=severity,
                    drift_details={
                        "diffs": [
                            {
                                "path": diff.path,
                                "expected_value": diff.expected_value,
                                "actual_value": diff.actual_value,
                                "severity": diff.severity,
                                "suggestion": diff.suggestion,
                            }
                            for diff in drift_result.diffs
                        ],
                        "missing_properties": drift_result.missing_properties,
                        "extra_properties": drift_result.extra_properties,
                    }
                )
            else:
                # Resource not found in actual state
                drift_count += 1
                drift_report = DriftReport(
                    config_resource_id=config_resource.id,
                    status=DriftStatus.ERROR,
                    severity=Severity.CRITICAL,
                    error_message="Resource not found in actual infrastructure"
                )

            db.add(drift_report)
            drift_reports.append(drift_report)

        # Step 6: Commit drift reports to database
        db.commit()
        logger.info(f"Created {len(drift_reports)} drift reports, {drift_count} with drift")

        # Step 7: Send Datadog events and metrics
        try:
            # Send event
            event_title = f"Drift Detection Completed: {repository.git_url}"
            event_text = f"""
Drift detection scan completed for repository {repository.git_url}.

Results:
- Total resources scanned: {len(config_resources)}
- Resources with drift: {drift_count}
- No drift: {len(config_resources) - drift_count}
            """.strip()

            datadog_client.send_event(
                title=event_title,
                text=event_text,
                tags=[
                    f"repository:{repository.git_url}",
                    f"branch:{repository.branch}",
                    "service:driftguard",
                ],
                alert_type="info" if drift_count == 0 else "warning"
            )

            # Send metrics
            datadog_client.send_metric(
                metric_name="driftguard.resources.scanned",
                value=len(config_resources),
                tags=[
                    f"repository:{repository.git_url}",
                    f"branch:{repository.branch}",
                ]
            )

            datadog_client.send_metric(
                metric_name="driftguard.resources.drift",
                value=drift_count,
                tags=[
                    f"repository:{repository.git_url}",
                    f"branch:{repository.branch}",
                ]
            )

            logger.info("Sent events and metrics to Datadog")

        except Exception as e:
            logger.error(f"Failed to send Datadog events/metrics: {e}")

        # Update repository last sync timestamp
        repository.last_sync_timestamp = datetime.now(timezone.utc)
        db.commit()

        # Step 8: Clean up workspace
        if workspace_path:
            try:
                shutil.rmtree(workspace_path)
                logger.info("Cleaned up workspace")
            except Exception as e:
                logger.warning(f"Failed to clean up workspace: {e}")

        result = {
            "status": "success",
            "repository_id": str(repository_id),
            "resources_scanned": len(config_resources),
            "drift_detected": drift_count,
            "reports_created": len(drift_reports),
        }

        logger.info(f"Drift detection job completed successfully: {result}")
        return result

    except Exception as e:
        logger.error(f"Drift detection job failed: {e}", exc_info=True)

        # Clean up workspace on error
        if workspace_path and workspace_path.exists():
            try:
                shutil.rmtree(workspace_path)
            except Exception as cleanup_error:
                logger.warning(f"Failed to clean up workspace after error: {cleanup_error}")

        raise

    finally:
        db.close()


def _find_matching_resource(expected_config: dict, actual_hosts: list) -> Optional[dict]:
    """
    Find a matching actual resource for an expected config.

    Args:
        expected_config: Expected resource configuration
        actual_hosts: List of actual hosts from Datadog

    Returns:
        Matching actual resource or None
    """
    expected_name = expected_config.get("name", "")
    expected_tags = expected_config.get("tags", {})

    for host in actual_hosts:
        # Match by name
        if host.get("name") == expected_name or host.get("host_name") == expected_name:
            return {
                "type": "host",
                "name": host.get("name"),
                "properties": {
                    "up": host.get("up"),
                    "tags": host.get("tags", []),
                    "meta": host.get("meta", {}),
                }
            }

        # Match by tags
        host_tags = host.get("tags", [])
        if expected_tags and any(f"{k}:{v}" in host_tags for k, v in expected_tags.items()):
            return {
                "type": "host",
                "name": host.get("name"),
                "properties": {
                    "up": host.get("up"),
                    "tags": host_tags,
                    "meta": host.get("meta", {}),
                }
            }

    return None


def _determine_severity(drift_result) -> Severity:
    """
    Determine overall severity based on drift result.

    Args:
        drift_result: DriftResult object

    Returns:
        Severity enum value
    """
    # Check if any diffs are critical
    for diff in drift_result.diffs:
        if diff.severity == "critical":
            return Severity.CRITICAL

    # Check if any diffs are warning
    for diff in drift_result.diffs:
        if diff.severity == "warning":
            return Severity.HIGH

    # If missing properties, consider medium
    if drift_result.missing_properties:
        return Severity.MEDIUM

    # Otherwise, low severity
    return Severity.LOW
