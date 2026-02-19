# Datadog Unified Service Tagging Design

**Date**: 2026-02-19
**Author**: Claude Code
**Status**: Approved

## Overview

Implement Datadog's unified service tagging for the DriftGuard application by adding a Datadog Agent container and configuring Docker labels for automatic service discovery and tagging. This enables comprehensive observability with consistent tagging across all telemetry (metrics, logs, traces).

## Goals

1. Add Datadog Agent as a containerized service
2. Implement unified service tags (service, env, version) via Docker labels
3. Enable automatic container discovery and telemetry collection
4. Maintain clean separation using git worktree for isolated development
5. Commit and push changes to taco-fiesta branch

## Architecture

### High-Level Design

The Datadog Agent runs as a sidecar container in docker-compose, discovering application containers via the Docker socket. Each service has Docker labels defining unified tags, which the agent automatically applies to all collected telemetry.

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Compose Network                  │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Backend    │  │    Worker    │  │   Frontend   │     │
│  │              │  │              │  │              │     │
│  │ Labels:      │  │ Labels:      │  │ Labels:      │     │
│  │ service=api  │  │ service=wrkr │  │ service=fe   │     │
│  │ env=dev      │  │ env=dev      │  │ env=dev      │     │
│  │ version=0.1  │  │ version=0.1  │  │ version=0.1  │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
│         │                 │                 │              │
│         │    logs/metrics/events            │              │
│         └────────────┬────────────────┬─────┘              │
│                      ▼                │                     │
│              ┌───────────────┐        │                     │
│              │ Datadog Agent │◄───────┘                     │
│              │               │                              │
│              │ Autodiscovery │                              │
│              │ Tag Injection │                              │
│              └───────┬───────┘                              │
│                      │                                      │
└──────────────────────┼──────────────────────────────────────┘
                       │
                       ▼
              Datadog Platform
```

### Unified Service Tags

**Tag Structure:**
- `service`: Identifies the service (driftguard-api, driftguard-worker, driftguard-frontend)
- `env`: Environment name (development, staging, production)
- `version`: Application version (0.1.0)

**Tag Assignment:**

| Service  | service               | env         | version |
|----------|-----------------------|-------------|---------|
| Backend  | driftguard-api        | development | 0.1.0   |
| Worker   | driftguard-worker     | development | 0.1.0   |
| Frontend | driftguard-frontend   | development | 0.1.0   |

## Components

### 1. Datadog Agent Service

**Container Configuration:**
- Image: `datadog/agent:latest`
- Requires: `DD_API_KEY` environment variable
- Mounts: Docker socket at `/var/run/docker.sock` (read-only)

**Enabled Features:**
- Container autodiscovery
- Log collection (stdout/stderr)
- APM receiver (optional for future ddtrace integration)
- Process monitoring
- Docker metrics

**Environment Variables:**
- `DD_API_KEY`: Datadog API key from .env
- `DD_SITE`: Datadog site (datadoghq.com)
- `DD_LOGS_ENABLED`: Enable log collection (true)
- `DD_APM_ENABLED`: Enable APM receiver (true)
- `DD_PROCESS_AGENT_ENABLED`: Enable process monitoring (true)
- `DD_CONTAINER_EXCLUDE`: Exclude patterns for containers (none)

### 2. Docker Labels per Service

Each application service gets three standard Datadog labels:

```yaml
labels:
  com.datadoghq.tags.service: "<service-name>"
  com.datadoghq.tags.env: "${APP_ENV:-development}"
  com.datadoghq.tags.version: "0.1.0"
```

**Service-Specific Labels:**
- Backend: `service:driftguard-api`
- Worker: `service:driftguard-worker`
- Frontend: `service:driftguard-frontend`

### 3. Environment Variables

**New Variables in .env.example:**
```bash
# Datadog Agent
DD_VERSION=0.1.0
```

**Existing Variables (reused):**
- `DATADOG_API_KEY` - For both API client and agent
- `DATADOG_APP_KEY` - For API client only
- `DATADOG_SITE` - Site configuration
- `APP_ENV` - Maps to env tag

### 4. Version Management

**Static Version (v0.1.0):**
- Hardcoded in docker-compose labels for simplicity
- Matches FastAPI app version and package.json version
- Can be made dynamic via environment variable later

**Version Source of Truth:**
- Backend/Worker: FastAPI app version in main.py (0.1.0)
- Frontend: package.json version (0.1.0)

## Data Flow

### Telemetry Collection

1. **Application services start** with Docker labels defining unified tags
2. **Datadog Agent discovers** containers via Docker socket API
3. **Agent extracts labels** and applies tags to telemetry
4. **Agent collects**:
   - Container metrics (CPU, memory, network, disk I/O)
   - Application logs (stdout/stderr streams)
   - Custom metrics/events via DatadogClient API
   - Process information
5. **Agent forwards** all telemetry to Datadog with unified tags attached

### Integration with Existing DatadogClient

The existing `backend/app/services/datadog_client.py` benefits automatically:
- Events sent via `send_event()` correlate with container metrics
- Metrics from `send_metric()` gain container context
- Cross-service correlation enabled in Datadog UI
- No code changes required

### Log Collection

**Automatic Log Capture:**
- All container stdout/stderr automatically collected
- Logs tagged with service/env/version
- Sources: Python app logs, uvicorn access logs, nginx logs

**Log Attributes:**
- `service`: From Docker label
- `env`: From Docker label
- `version`: From Docker label
- `container_id`: Auto-added by agent
- `container_name`: Auto-added by agent
- `image_name`: Auto-added by agent

## Error Handling

### Agent Failure Scenarios

**Missing API Key:**
- Agent fails to start (fail-fast behavior)
- Docker Compose shows agent container in error state
- Applications continue running normally

**Agent Crash:**
- Applications unaffected (non-blocking design)
- Telemetry not collected until agent restarts
- Existing DatadogClient API calls still work directly

**Network Issues:**
- Agent retries with exponential backoff
- Local buffering of telemetry (agent internal)
- Applications continue operating normally

### Graceful Degradation

- Agent is optional for application functionality
- Can disable agent service without breaking app
- Direct API calls from DatadogClient continue working
- No changes to application startup or runtime behavior

## Security

### Docker Socket Access

**Requirement:**
- Agent needs read access to Docker socket for container discovery
- Mounted as read-only: `/var/run/docker.sock:/var/run/docker.sock:ro`

**Risk Mitigation:**
- Read-only mount prevents agent from controlling containers
- Agent container runs with minimal privileges
- No write access to Docker API

### API Key Protection

**Storage:**
- `DD_API_KEY` stored in .env file (gitignored)
- Never committed to version control
- .env.example shows placeholder only

**Access:**
- Only agent and backend/worker need API key
- Frontend doesn't have access to API keys
- Environment variables not exposed to browser

### Network Isolation

**Container Communication:**
- Agent accesses Docker socket only
- Application containers isolated from each other
- No direct container-to-container access to agent

**Minimal Permissions:**
- Agent runs with least privilege required
- No host network mode
- No privileged container flag

## Implementation Approach

### Git Worktree Isolation

**Why Worktree:**
- Avoids interference with ongoing work on taco-fiesta branch
- Clean separation of changes
- Easy to review and merge independently

**Process:**
1. Create worktree in separate directory
2. Make all changes in isolated workspace
3. Commit changes with descriptive message
4. Push to taco-fiesta branch
5. Optionally merge or keep separate

### Files to Modify

1. **docker-compose.yml** - Add agent service, add labels to existing services
2. **.env.example** - Add DD_VERSION variable
3. **CLAUDE.md** - Update implementation status (optional)

### No Code Changes Required

- No modifications to backend/worker Python code
- No modifications to frontend TypeScript/React code
- No changes to Dockerfiles
- Purely infrastructure/configuration changes

## Testing & Validation

### Verification Steps

1. **Agent startup**: Verify agent container starts successfully
2. **Container discovery**: Check agent logs for discovered containers
3. **Tag application**: Verify tags appear in Datadog UI
4. **Metric collection**: Confirm container metrics flowing to Datadog
5. **Log collection**: Verify application logs appear with tags
6. **Correlation**: Test service map shows all services with proper tags

### Success Criteria

- [ ] Datadog Agent container runs healthy
- [ ] All three services discovered by agent
- [ ] Unified tags visible in Datadog infrastructure list
- [ ] Logs tagged with service/env/version
- [ ] Container metrics flowing to Datadog
- [ ] Service map shows driftguard-api, driftguard-worker, driftguard-frontend

## Future Enhancements

**Post-Implementation Improvements:**

1. **APM Instrumentation**: Add ddtrace library for automatic tracing
2. **Dynamic Versioning**: Read version from git tag or CI/CD
3. **Custom Checks**: Add Datadog agent checks for app health
4. **Log Parsing**: Configure log pipelines in Datadog for structured logs
5. **Dashboards**: Create service-specific dashboards using unified tags
6. **Monitors**: Set up alerts using service/env/version tags

## References

- [Datadog Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)
- [Datadog Agent Docker](https://docs.datadoghq.com/agent/docker/)
- [Datadog Docker Labels](https://docs.datadoghq.com/agent/docker/tag/)
- [Datadog Container Monitoring](https://docs.datadoghq.com/containers/docker/)

## Summary

This design implements Datadog unified service tagging using a containerized agent with Docker label-based autodiscovery. The approach requires no application code changes, provides comprehensive observability, and maintains clean isolation via git worktree. The implementation is simple, secure, and follows Datadog best practices for container monitoring.
