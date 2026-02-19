# DriftGuard - Drift Detection Engine Design

**Date**: 2026-02-19
**Status**: Approved
**Team**: Hackathon Team 3 (Taco Fiesta)

---

## Overview

This document outlines the design for DriftGuard's core drift detection engine - a system that continuously monitors infrastructure configuration drift by comparing declared configs in git repositories against actual infrastructure state from Datadog monitoring APIs.

**Supported Config Types:**
- Terraform state and configurations
- Docker Compose files
- Kubernetes manifests (cloud-agnostic)

**Key Capabilities:**
- Git-triggered and periodic drift detection (hybrid approach)
- Multi-level remediation options (manual, one-click, automated)
- Sensitive data redaction and security
- Full Datadog observability integration

---

## Architecture Overview

DriftGuard uses an **event-driven architecture** with four main components:

### 1. Config Ingestion Service
Reads Terraform, Docker Compose, and Kubernetes manifests from git repositories and normalizes them into a common, cloud-agnostic format.

### 2. Drift Detection Engine
Compares expected configs against actual infrastructure state from Datadog APIs and identifies discrepancies.

### 3. Event Queue (Redis/RQ)
Handles async job processing for:
- Git webhook events
- Scheduled periodic checks (5-minute interval)
- Remediation actions

### 4. Web API & Dashboard
Provides:
- React/TypeScript UI with DriftGuard design system
- RESTful API for drift queries and remediation actions
- Datadog integration for alerts and incidents

### Data Flow

```
Git Webhook / 5-min Scheduler
    ↓
Event Queue (Redis)
    ↓
Worker: Drift Detection Job
    ├─→ Fetch configs from git
    ├─→ Fetch actual state from Datadog
    ├─→ Compute diffs
    ├─→ Store results in PostgreSQL
    └─→ Send alerts to Datadog & Dashboard
```

**Hybrid Trigger Model:**
- Git commits trigger immediate drift checks
- 5-minute backstop runs if no commits occur
- Ensures rapid feedback on changes while catching external drift

---

## Technology Stack

### Backend
- **Language**: Python 3.13
- **Web Framework**: FastAPI (async request handling)
- **Event Queue**: Redis with RQ (simple, reliable)
- **Database**: PostgreSQL
- **Config Parsing**:
  - Terraform: `python-hcl2` library
  - Docker Compose: `PyYAML`
  - Kubernetes: `PyYAML`
- **Git Operations**: `GitPython`
- **Datadog Integration**:
  - Official `datadog-api-client` Python library
  - Datadog MCP server for advanced queries

### Frontend
- **Framework**: React with TypeScript
- **Build Tool**: Vite
- **Design System**: DriftGuard design (IBM Plex fonts, Datadog purple theme)
- **UI Components**: Custom components aligned with Datadog internal design system

### Deployment
- **Containerization**: Docker
- **Local Development**: docker-compose
- **Production**: Kubernetes manifests

---

## Data Model

### Repositories Table
Stores git repository information for config sources.

```
- id: UUID (primary key)
- git_url: String (repository URL)
- branch: String (default: main)
- credentials_ref: String (reference to secret store)
- last_sync_timestamp: Timestamp
- created_at: Timestamp
```

### ConfigResources Table
Normalized representation of infrastructure configs.

```
- id: UUID (primary key)
- repository_id: UUID (foreign key)
- resource_type: Enum (terraform, docker, kubernetes)
- resource_identifier: String (unique name/ID)
- expected_config: JSONB (normalized config)
- source_file_path: String (path in git repo)
- tags: JSONB (metadata, labels)
- updated_at: Timestamp
```

### DriftReports Table
Records of detected configuration drift.

```
- id: UUID (primary key)
- check_timestamp: Timestamp
- repository_id: UUID (foreign key)
- config_resource_id: UUID (foreign key)
- drift_status: Enum (none, warning, critical)
- diff_details: JSONB (what changed)
- actual_state: JSONB (current state from Datadog)
- severity: Enum (info, warning, critical)
- remediation_status: Enum (none, pending, completed, failed)
- error_message: Text (nullable)
- datadog_event_id: String (nullable)
```

### RemediationHistory Table
Audit log of remediation actions.

```
- id: UUID (primary key)
- drift_report_id: UUID (foreign key)
- triggered_at: Timestamp
- triggered_by: String (user or system)
- remediation_type: Enum (manual, one_click, automated)
- action_taken: Text (description)
- outcome: Enum (success, failure, rolled_back)
- error_details: Text (nullable)
```

**Query Capabilities:**
- Drift by resource, time range, severity
- Remediation success rates and history
- Team/environment filtering via tags
- Time-series analysis for trending

---

## Drift Detection Logic

The detection engine operates in four phases:

### Phase 1: Normalization
Parse each config type into a common schema:

```json
{
  "resource_id": "string",
  "resource_type": "string",
  "properties": {
    "key": "value"
  },
  "metadata": {
    "tags": {},
    "labels": {}
  }
}
```

**Cloud-Agnostic Design**: Resources are normalized regardless of source format (Terraform HCL, Docker Compose YAML, K8s manifests), enabling universal comparison logic.

### Phase 2: State Retrieval
Query Datadog Infrastructure Monitoring APIs:
- Host states and configurations
- Container states and images
- Service definitions and metadata

**Resource Mapping**: Match Datadog resources to config resources using:
- Naming conventions
- Tags and labels
- Resource identifiers

### Phase 3: Comparison
Deep equality checks on normalized properties:

1. **Missing Resources**: Exist in config but not in Datadog
2. **Extra Resources**: In Datadog but not declared in configs
3. **Value Mismatches**: Properties differ between expected and actual

**Diff Output Format:**
```json
{
  "property_path": "spec.replicas",
  "old_value": 3,
  "new_value": 5,
  "drift_type": "value_mismatch",
  "suggested_action": "Update config to match actual state"
}
```

### Phase 4: Severity Classification

- **Critical**: Security-related drifts, missing resources, unauthorized changes
- **Warning**: Configuration mismatches, non-critical value changes
- **Info**: Extra undeclared resources, metadata-only changes

---

## Sensitive Data Handling

**Security Requirements:**
- Automatic redaction of secrets, API keys, passwords, credentials
- Pattern matching for common secret formats
- Integration with secret detection tools (detect-secrets, git-secrets)

**Datadog Log Pipeline Integration:**
- Use Datadog Sensitive Data Scanner rules
- Redact before storing in database
- Redact before displaying in UI
- Redact before sending to logs/alerts

**Supported Patterns:**
- AWS keys, GCP service accounts, Azure credentials
- Database connection strings
- API tokens and bearer tokens
- SSH keys and certificates

---

## Remediation Workflow

When drift is detected, users are presented with three action options:

### Option 1: View Details
- Side-by-side diff with syntax highlighting
- Redacted sensitive values
- Resource metadata (team, environment, last checked)
- Drift history timeline

### Option 2: Remediate Now (One-Click)
Triggers immediate fix by applying expected config:
- **Terraform**: Run `terraform apply` for specific resource
- **Docker Compose**: Run `docker compose up` with updated config
- **Kubernetes**: Run `kubectl apply` for manifests

**Requirements:**
- Appropriate credentials and permissions
- Dry-run preview before actual apply
- Rollback capability on failure

### Option 3: Enable Auto-Remediation
Set up rules for automatic fixes on future similar drifts:
- Configure auto-remediation for specific resource types or teams
- Set approval requirements for critical changes
- Define rollback procedures
- Schedule remediation windows

**Approval Workflows:**
- Automatic for low-risk changes (tags, labels)
- Single approval for medium-risk (scaling, non-prod)
- Multi-approval for high-risk (security, production)

**Audit Trail:**
All remediation actions logged to:
- RemediationHistory table
- Datadog events
- Notification channels (Slack, PagerDuty, etc.)

---

## Datadog Integration

### Monitoring APIs
- **Infrastructure List API**: Get host and container states
- **Metrics API**: Resource utilization data
- **Tags API**: Map resources to configs

### Observability
**Custom Metrics:**
- `driftguard.drift.count` (by severity, resource type)
- `driftguard.detection.duration_ms`
- `driftguard.remediation.success_rate`

**Events:**
- Drift detected (with severity and resource details)
- Remediation triggered (manual/auto)
- Remediation completed (success/failure)

**APM Tracing:**
- Detection pipeline performance
- Config parsing duration
- Datadog API call latencies

### Alerting
**Monitors:**
- Critical drift detection (immediate notification)
- Warning drift accumulation (threshold-based)
- Remediation failure rate (SLO tracking)

**Incident Integration:**
- Create Datadog Incidents for high-severity drift
- Team-based notification routing
- AI-assisted root cause analysis via MCP server

### Logging
- Emit structured logs with proper tagging
- Use Datadog log pipelines with sensitive data scanner
- Correlate drift events with:
  - Deployment events
  - Infrastructure changes
  - CI/CD pipeline runs

---

## Future Enhancements

### Policy-Based Evaluation (Post-MVP)
To be implemented after core drift detection is complete:

- **Reliability Policies**: Check for HA configurations, backup settings
- **Security Policies**: Enforce encryption, network policies, RBAC
- **Cost Optimization**: Detect over-provisioned resources, unused infrastructure
- **Tagging Policies**: Ensure required tags (owner, cost-center, environment)

**Design Principle**: Build as a pluggable system from the start - separate policy engine interface that can be added without refactoring core drift detection logic.

### Datadog App Integration
- Native Datadog dashboard widgets
- Embedded drift views in Datadog UI
- Single sign-on and RBAC integration

---

## Success Criteria

**Functional Requirements:**
- Detect drift across Terraform, Docker Compose, Kubernetes configs
- Support hybrid trigger model (git webhooks + 5-min periodic)
- Provide three-tier remediation workflow (view, one-click, auto)
- Redact sensitive data in all outputs

**Non-Functional Requirements:**
- Detection latency < 30 seconds after git commit
- Support 100+ repositories and 1000+ resources
- 99.9% uptime for detection service
- Full audit trail for all remediations

**Observability Goals:**
- Full visibility in Datadog dashboards
- Alert routing to appropriate teams
- Root cause analysis via MCP server integration

---

## Next Steps

1. **Environment Setup**: Configure development environment with Python 3.13, PostgreSQL, Redis
2. **Implementation Plan**: Create detailed task breakdown using writing-plans skill
3. **Component Development**: Build services incrementally (ingestion → detection → remediation)
4. **Datadog Integration**: Set up API clients, metrics, events, monitors
5. **Frontend Development**: Build React dashboard with DriftGuard design system
6. **Testing**: Unit tests, integration tests, end-to-end scenarios
7. **Deployment**: Containerize, create K8s manifests, deploy to staging

---

*Design approved on 2026-02-19 via voice conversation*
