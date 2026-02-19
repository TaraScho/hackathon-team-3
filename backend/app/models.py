import enum
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, JSON, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
import uuid


# Enums
class ResourceType(enum.Enum):
    """Types of configuration resources that can be monitored."""
    TERRAFORM = "terraform"
    KUBERNETES = "kubernetes"
    CLOUDFORMATION = "cloudformation"
    DOCKER_COMPOSE = "docker_compose"
    ANSIBLE = "ansible"
    HELM = "helm"


class DriftStatus(enum.Enum):
    """Status of drift detection."""
    NO_DRIFT = "no_drift"
    DRIFTED = "drifted"
    ERROR = "error"
    PENDING = "pending"


class Severity(enum.Enum):
    """Severity level of detected drift."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RemediationStatus(enum.Enum):
    """Status of remediation action."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RemediationType(enum.Enum):
    """Type of remediation action."""
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    SUGGESTED = "suggested"


class RemediationOutcome(enum.Enum):
    """Outcome of remediation action."""
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILURE = "failure"
    ROLLBACK = "rollback"


# Models
class Repository(Base):
    """Repository containing infrastructure configuration."""
    __tablename__ = "repositories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    git_url = Column(String(512), nullable=False, unique=True)
    branch = Column(String(128), nullable=False, default="main")
    credentials_ref = Column(String(256), nullable=True)
    last_sync_timestamp = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    config_resources = relationship("ConfigResource", back_populates="repository", cascade="all, delete-orphan")


class ConfigResource(Base):
    """Individual configuration resource (e.g., a Terraform file, K8s manifest)."""
    __tablename__ = "config_resources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"), nullable=False)
    resource_type = Column(Enum(ResourceType), nullable=False)
    file_path = Column(String(512), nullable=False)
    resource_name = Column(String(256), nullable=False)
    expected_config = Column(JSON, nullable=False)
    actual_config = Column(JSON, nullable=True)
    last_checked_timestamp = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    repository = relationship("Repository", back_populates="config_resources")
    drift_reports = relationship("DriftReport", back_populates="config_resource", cascade="all, delete-orphan")


class DriftReport(Base):
    """Report of detected configuration drift."""
    __tablename__ = "drift_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    config_resource_id = Column(UUID(as_uuid=True), ForeignKey("config_resources.id"), nullable=False)
    status = Column(Enum(DriftStatus), nullable=False, default=DriftStatus.PENDING)
    severity = Column(Enum(Severity), nullable=False, default=Severity.LOW)
    drift_details = Column(JSON, nullable=True)
    detected_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    config_resource = relationship("ConfigResource", back_populates="drift_reports")
    remediation_history = relationship("RemediationHistory", back_populates="drift_report", cascade="all, delete-orphan")


class RemediationHistory(Base):
    """History of remediation actions taken for drift."""
    __tablename__ = "remediation_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    drift_report_id = Column(UUID(as_uuid=True), ForeignKey("drift_reports.id"), nullable=False)
    remediation_type = Column(Enum(RemediationType), nullable=False)
    remediation_status = Column(Enum(RemediationStatus), nullable=False, default=RemediationStatus.PENDING)
    remediation_outcome = Column(Enum(RemediationOutcome), nullable=True)
    action_taken = Column(Text, nullable=False)
    executed_by = Column(String(256), nullable=True)
    executed_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime(timezone=True), nullable=True)
    error_message = Column(Text, nullable=True)
    rollback_details = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    drift_report = relationship("DriftReport", back_populates="remediation_history")
