"""
Drift report API endpoints.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import DriftReport, ConfigResource, DriftStatus, Severity
from app.database import get_db

router = APIRouter()


class DriftReportResponse(BaseModel):
    """Schema for drift report response."""
    id: str
    repository_id: str
    scan_time: datetime
    drift_detected: bool
    total_resources: int
    drifted_resources: int
    severity_critical: int
    severity_high: int
    severity_medium: int
    severity_low: int
    details: dict

    class Config:
        from_attributes = True


@router.get("", response_model=List[DriftReportResponse])
async def list_drift_reports(
    repository_id: Optional[str] = Query(None, description="Filter by repository ID"),
    drift_detected: Optional[bool] = Query(None, description="Filter by drift status"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of reports to return"),
    db: Session = Depends(get_db)
):
    """
    List drift reports with optional filtering.

    Note: This aggregates individual drift reports by repository and scan time.
    """
    # Start with base query - use outerjoin to handle empty tables
    query = db.query(DriftReport).outerjoin(ConfigResource)

    # Apply filters
    if repository_id is not None:
        try:
            repo_uuid = UUID(repository_id)
            query = query.filter(ConfigResource.repository_id == repo_uuid)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid repository ID format")

    if drift_detected is not None:
        if drift_detected:
            query = query.filter(DriftReport.status == DriftStatus.DRIFTED)
        else:
            query = query.filter(DriftReport.status == DriftStatus.NO_DRIFT)

    # Order by most recent first and apply limit
    reports = query.order_by(DriftReport.detected_at.desc()).limit(limit).all()

    # Aggregate reports by repository and scan time
    aggregated_reports = []
    seen_scans = set()

    for report in reports:
        config_resource = report.config_resource
        scan_key = (str(config_resource.repository_id), report.detected_at.replace(second=0, microsecond=0))

        if scan_key in seen_scans:
            continue
        seen_scans.add(scan_key)

        # Get all reports for this repository at approximately the same time
        scan_reports = [
            r for r in reports
            if str(r.config_resource.repository_id) == scan_key[0] and
            abs((r.detected_at - report.detected_at).total_seconds()) < 60
        ]

        # Calculate aggregated metrics
        total_resources = len(scan_reports)
        drifted_resources = sum(1 for r in scan_reports if r.status == DriftStatus.DRIFTED)
        severity_critical = sum(1 for r in scan_reports if r.severity == Severity.CRITICAL)
        severity_high = sum(1 for r in scan_reports if r.severity == Severity.HIGH)
        severity_medium = sum(1 for r in scan_reports if r.severity == Severity.MEDIUM)
        severity_low = sum(1 for r in scan_reports if r.severity == Severity.LOW)

        aggregated_reports.append({
            "id": str(report.id),
            "repository_id": str(config_resource.repository_id),
            "scan_time": report.detected_at,
            "drift_detected": drifted_resources > 0,
            "total_resources": total_resources,
            "drifted_resources": drifted_resources,
            "severity_critical": severity_critical,
            "severity_high": severity_high,
            "severity_medium": severity_medium,
            "severity_low": severity_low,
            "details": report.drift_details or {}
        })

    return aggregated_reports[:limit]


@router.get("/{report_id}", response_model=DriftReportResponse)
async def get_drift_report(report_id: str, db: Session = Depends(get_db)):
    """
    Get a specific drift report by ID.
    """
    try:
        report_uuid = UUID(report_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid report ID format")

    report = db.query(DriftReport).filter(DriftReport.id == report_uuid).first()
    if not report:
        raise HTTPException(status_code=404, detail="Drift report not found")

    config_resource = report.config_resource

    # Get all reports for this repository at approximately the same time
    scan_reports = db.query(DriftReport).join(ConfigResource).filter(
        ConfigResource.repository_id == config_resource.repository_id,
        func.abs(
            func.extract('epoch', DriftReport.detected_at) -
            func.extract('epoch', report.detected_at)
        ) < 60
    ).all()

    # Calculate aggregated metrics
    total_resources = len(scan_reports)
    drifted_resources = sum(1 for r in scan_reports if r.status == DriftStatus.DRIFTED)
    severity_critical = sum(1 for r in scan_reports if r.severity == Severity.CRITICAL)
    severity_high = sum(1 for r in scan_reports if r.severity == Severity.HIGH)
    severity_medium = sum(1 for r in scan_reports if r.severity == Severity.MEDIUM)
    severity_low = sum(1 for r in scan_reports if r.severity == Severity.LOW)

    return {
        "id": str(report.id),
        "repository_id": str(config_resource.repository_id),
        "scan_time": report.detected_at,
        "drift_detected": drifted_resources > 0,
        "total_resources": total_resources,
        "drifted_resources": drifted_resources,
        "severity_critical": severity_critical,
        "severity_high": severity_high,
        "severity_medium": severity_medium,
        "severity_low": severity_low,
        "details": report.drift_details or {}
    }
