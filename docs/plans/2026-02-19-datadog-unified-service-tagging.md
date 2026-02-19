# Datadog Unified Service Tagging Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement Datadog unified service tagging using containerized Agent with Docker label-based autodiscovery.

**Architecture:** Add Datadog Agent as a service in docker-compose.yml, configure Docker labels on each service (backend, worker, frontend) with unified tags (service, env, version). Agent autodiscovers containers and applies tags to all telemetry.

**Tech Stack:** Docker Compose, Datadog Agent, Docker Labels

---

## Task 1: Create Git Worktree

**Purpose:** Isolate implementation work from ongoing development on taco-fiesta branch.

**Step 1: Create worktree directory**

Run:
```bash
git worktree add ../hackathon-team-3-dd-tagging taco-fiesta
```

Expected: Output showing worktree created at `../hackathon-team-3-dd-tagging`

**Step 2: Change to worktree directory**

Run:
```bash
cd ../hackathon-team-3-dd-tagging
```

Expected: Working directory is now the worktree

**Step 3: Verify branch**

Run:
```bash
git branch --show-current
```

Expected: Output shows `taco-fiesta`

---

## Task 2: Add Datadog Agent Service

**Files:**
- Modify: `docker-compose.yml:1-87`

**Step 1: Read current docker-compose.yml**

Run:
```bash
cat docker-compose.yml
```

Expected: See current services (postgres, redis, backend, worker, frontend)

**Step 2: Add Datadog Agent service**

Add the following service after the `redis` service and before the `backend` service in `docker-compose.yml`:

```yaml
  datadog-agent:
    image: datadog/agent:latest
    container_name: datadog-agent
    environment:
      DD_API_KEY: ${DATADOG_API_KEY}
      DD_SITE: ${DATADOG_SITE:-datadoghq.com}
      DD_LOGS_ENABLED: true
      DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL: true
      DD_APM_ENABLED: true
      DD_APM_NON_LOCAL_TRAFFIC: true
      DD_PROCESS_AGENT_ENABLED: true
      DD_CONTAINER_EXCLUDE: "name:datadog-agent"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /proc/:/host/proc/:ro
      - /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
    ports:
      - "8126:8126"
    healthcheck:
      test: ["CMD-SHELL", "agent health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

**Step 3: Verify docker-compose syntax**

Run:
```bash
docker-compose config
```

Expected: YAML parsed successfully with no errors

**Step 4: Commit Datadog Agent service**

Run:
```bash
git add docker-compose.yml
git commit -m "feat: add Datadog Agent service to docker-compose

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

Expected: Commit created successfully

---

## Task 3: Add Unified Tags to Backend Service

**Files:**
- Modify: `docker-compose.yml:32-54`

**Step 1: Add labels to backend service**

Add the following `labels` section to the `backend` service in `docker-compose.yml`:

```yaml
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      DATABASE_URL: postgresql://driftguard:driftguard@postgres:5432/driftguard
      REDIS_URL: redis://redis:6379/0
      DATADOG_API_KEY: ${DATADOG_API_KEY}
      DATADOG_APP_KEY: ${DATADOG_APP_KEY}
      DATADOG_SITE: ${DATADOG_SITE:-datadoghq.com}
      APP_ENV: ${APP_ENV:-development}
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
      SECRET_KEY: ${SECRET_KEY}
    ports:
      - "8000:8000"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      datadog-agent:
        condition: service_healthy
    volumes:
      - ./backend/app:/app/app
    labels:
      com.datadoghq.tags.service: "driftguard-api"
      com.datadoghq.tags.env: "${APP_ENV:-development}"
      com.datadoghq.tags.version: "0.1.0"
```

**Step 2: Verify docker-compose syntax**

Run:
```bash
docker-compose config
```

Expected: YAML parsed successfully, labels visible in backend service

**Step 3: Commit backend labels**

Run:
```bash
git add docker-compose.yml
git commit -m "feat: add unified service tags to backend service

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

Expected: Commit created successfully

---

## Task 4: Add Unified Tags to Worker Service

**Files:**
- Modify: `docker-compose.yml:55-74`

**Step 1: Add labels to worker service**

Add the following `labels` section and update `depends_on` for the `worker` service in `docker-compose.yml`:

```yaml
  worker:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: python -m app.queue.worker
    environment:
      DATABASE_URL: postgresql://driftguard:driftguard@postgres:5432/driftguard
      REDIS_URL: redis://redis:6379/0
      DATADOG_API_KEY: ${DATADOG_API_KEY}
      DATADOG_APP_KEY: ${DATADOG_APP_KEY}
      DATADOG_SITE: ${DATADOG_SITE:-datadoghq.com}
      APP_ENV: ${APP_ENV:-development}
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
      SECRET_KEY: ${SECRET_KEY}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      datadog-agent:
        condition: service_healthy
    labels:
      com.datadoghq.tags.service: "driftguard-worker"
      com.datadoghq.tags.env: "${APP_ENV:-development}"
      com.datadoghq.tags.version: "0.1.0"
```

**Step 2: Verify docker-compose syntax**

Run:
```bash
docker-compose config
```

Expected: YAML parsed successfully, labels visible in worker service

**Step 3: Commit worker labels**

Run:
```bash
git add docker-compose.yml
git commit -m "feat: add unified service tags to worker service

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

Expected: Commit created successfully

---

## Task 5: Add Unified Tags to Frontend Service

**Files:**
- Modify: `docker-compose.yml:75-83`

**Step 1: Add labels to frontend service**

Add the following `labels` section and update `depends_on` for the `frontend` service in `docker-compose.yml`:

```yaml
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - backend
      - datadog-agent
    labels:
      com.datadoghq.tags.service: "driftguard-frontend"
      com.datadoghq.tags.env: "${APP_ENV:-development}"
      com.datadoghq.tags.version: "0.1.0"
```

**Step 2: Verify docker-compose syntax**

Run:
```bash
docker-compose config
```

Expected: YAML parsed successfully, labels visible in frontend service

**Step 3: Commit frontend labels**

Run:
```bash
git add docker-compose.yml
git commit -m "feat: add unified service tags to frontend service

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

Expected: Commit created successfully

---

## Task 6: Update Environment Variables Documentation

**Files:**
- Modify: `.env.example:1-16`

**Step 1: Read current .env.example**

Run:
```bash
cat .env.example
```

Expected: See current environment variables

**Step 2: Add DD_VERSION to .env.example**

Add the following line after the `DATADOG_SITE` line in `.env.example`:

```bash
# Database
DATABASE_URL=postgresql://driftguard:driftguard@localhost:5432/driftguard

# Redis
REDIS_URL=redis://localhost:6379/0

# Datadog
DATADOG_API_KEY=your_api_key_here
DATADOG_APP_KEY=your_app_key_here
DATADOG_SITE=datadoghq.com

# Application
APP_ENV=development
LOG_LEVEL=INFO
SECRET_KEY=change_this_in_production

# Datadog Unified Service Tagging
DD_VERSION=0.1.0
```

**Step 3: Verify file contents**

Run:
```bash
cat .env.example | grep DD_VERSION
```

Expected: Output shows `DD_VERSION=0.1.0`

**Step 4: Commit .env.example update**

Run:
```bash
git add .env.example
git commit -m "docs: add DD_VERSION to environment variables example

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

Expected: Commit created successfully

---

## Task 7: Verify Configuration

**Purpose:** Validate docker-compose configuration and check for syntax errors.

**Step 1: Validate complete docker-compose.yml**

Run:
```bash
docker-compose config --quiet
```

Expected: No output (quiet mode, successful validation)

**Step 2: Check service definitions**

Run:
```bash
docker-compose config --services
```

Expected: Output lists all services including `datadog-agent`
```
postgres
redis
datadog-agent
backend
worker
frontend
```

**Step 3: Verify labels in configuration**

Run:
```bash
docker-compose config | grep -A 3 "com.datadoghq.tags"
```

Expected: Output shows labels for backend, worker, and frontend services with service, env, and version tags

**Step 4: Document verification**

Add verification results to a comment in the final commit (will be done in next task).

---

## Task 8: Final Commit and Push

**Purpose:** Create a comprehensive final commit and push all changes to remote.

**Step 1: Check git status**

Run:
```bash
git status
```

Expected: Output shows "nothing to commit, working tree clean"

**Step 2: Review commit history**

Run:
```bash
git log --oneline -6
```

Expected: See 6 commits (1 design doc + 5 implementation commits)

**Step 3: Push to taco-fiesta branch**

Run:
```bash
git push origin taco-fiesta
```

Expected: Output shows successful push to remote

**Step 4: Verify remote branch**

Run:
```bash
git branch -vv
```

Expected: Output shows taco-fiesta tracking origin/taco-fiesta with "up to date" status

---

## Task 9: Cleanup Worktree (Optional)

**Purpose:** Remove the worktree after successful push.

**Step 1: Return to main repository**

Run:
```bash
cd /Users/giovanni.peralto/Projects/hackathon-team-3
```

Expected: Working directory is back to main repository

**Step 2: List worktrees**

Run:
```bash
git worktree list
```

Expected: Output shows both main repo and dd-tagging worktree

**Step 3: Remove worktree**

Run:
```bash
git worktree remove ../hackathon-team-3-dd-tagging
```

Expected: Output confirms worktree removed

**Step 4: Verify worktree removed**

Run:
```bash
git worktree list
```

Expected: Output shows only main repository

---

## Testing & Validation

**Manual Testing Steps:**

1. **Start services:**
   ```bash
   docker-compose up -d
   ```
   Expected: All services start successfully, including datadog-agent

2. **Check Datadog Agent logs:**
   ```bash
   docker-compose logs datadog-agent | grep "successfully"
   ```
   Expected: Log entries showing successful API key validation and container discovery

3. **Verify container discovery:**
   ```bash
   docker-compose logs datadog-agent | grep "autodiscovery"
   ```
   Expected: Log entries showing backend, worker, and frontend containers discovered

4. **Check service health:**
   ```bash
   docker-compose ps
   ```
   Expected: All services show "Up (healthy)" status

5. **Verify tags in Datadog UI:**
   - Navigate to Infrastructure > Containers in Datadog
   - Filter by `service:driftguard-api`, `service:driftguard-worker`, `service:driftguard-frontend`
   - Expected: Each service appears with correct env and version tags

---

## Success Criteria

- [ ] Git worktree created successfully
- [ ] Datadog Agent service added to docker-compose.yml
- [ ] Backend service has unified tags (service, env, version)
- [ ] Worker service has unified tags (service, env, version)
- [ ] Frontend service has unified tags (service, env, version)
- [ ] .env.example updated with DD_VERSION
- [ ] All changes committed with descriptive messages
- [ ] Changes pushed to taco-fiesta branch
- [ ] docker-compose config validates without errors
- [ ] All services start successfully
- [ ] Datadog Agent discovers containers
- [ ] Tags visible in Datadog UI

---

## Rollback Plan

If issues occur:

1. **Revert commits:**
   ```bash
   git log --oneline -6  # Note commit hash before changes
   git revert <commit-hash>..HEAD
   git push origin taco-fiesta
   ```

2. **Remove Agent service:**
   - Remove `datadog-agent` service from docker-compose.yml
   - Remove labels from backend, worker, frontend services
   - Remove depends_on references to datadog-agent

3. **Restart services:**
   ```bash
   docker-compose down
   docker-compose up -d
   ```

---

## Notes

- No application code changes required
- No Dockerfile modifications needed
- Purely infrastructure/configuration changes
- Agent is non-blocking - apps work even if agent fails
- Version (0.1.0) is static for simplicity
- Can be made dynamic later via environment variable
