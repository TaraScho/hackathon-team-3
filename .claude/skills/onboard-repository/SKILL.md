---
name: onboard-repository
description: >
  End-to-end Datadog onboarding orchestrator. Runs repo-analyzer, then fans out
  to app-builder, workflow-automation, software-catalog, and dashboards in the
  correct dependency order.
  Trigger phrases: "onboard this repo", "onboard repository", "set up Datadog for this repo",
  "run Datadog onboarding", "full Datadog setup".
  Do NOT use for individual skill tasks — invoke the individual skills directly.
metadata:
  author: hackathon-team-3
  tags: [orchestration, onboarding, repo-analyzer, app-builder, workflow-automation, dashboards, software-catalog]
  category: orchestration
---

# Onboard Repository Skill

## Overview

The `onboard-repository` skill is the authoritative playbook for end-to-end Datadog onboarding. It coordinates all product skills in the correct dependency order — from repo analysis through composite dashboard creation.

## Orchestration Model

```
user provides repo path
     |
     v
[Phase 1] repo-analyzer → datadog-recommendations.md + repo-analysis.json
     |
     v  [Phase 2 — parallel fan-out]
  software-catalog (teams + services)
  for each app_candidate:
    action-connections → app-builder         → app UUID ──┐
  for each workflow_candidate:                             │
    action-connections → workflow-automation → wf UUID  ──┤
     |                                                     │
     v  [Phase 3 — after all UUIDs collected] ◄────────────┘
  dashboards (composite — embeds app UUIDs + workflow UUIDs)
```

**Key rules:**
- Each `app_candidate` and `workflow_candidate` gets its **own dedicated** action connection (1:1 model — never shared)
- Phase 2 branches are independent and run in parallel
- Phase 3 waits for all UUIDs from Phase 2

---

## Phase 1: Repo Analysis

Follow the `repo-analyzer` skill workflow against the provided repo path. **Wait for completion before starting Phase 2.**

The skill produces:
1. `{repo_path}/datadog-recommendations.md` — human-readable report
2. `{repo_path}/repo-analysis.json` — machine-parseable output
3. `.claude/context/repo-analysis.json` — agent handoff copy

**Verify before continuing:**
- `app_candidates` array is non-empty
- `workflow_candidates` array is non-empty
- `preferred_output_format` is present (`terraform` | `shell`)

---

## Phase 2: Parallel Fan-Out

Three independent branches run concurrently.

### Branch A: Software Catalog

Follow the `software-catalog` skill workflow to register teams and service entities discovered from the repo.

1. Extract team names and service names from IaC tags and directory layout
2. Create teams first (idempotent — 409 = already exists)
3. Register bare service entities pointing to the teams

**Output:** Team handles + catalog entity names

### Branch B: App Builder (one per `app_candidate`)

For **each** `app_candidate` in `repo-analysis.json`:

1. Follow the `action-connections` skill workflow to create a scoped IAM role and connection for this app.
   - Include `short_label` in the connection name
   - Collect: connection UUID

2. Follow the `app-builder` skill workflow with the connection UUID.
   - Use `template` from `app_candidate.template`
   - Collect: app UUID

**Output per branch:** One app UUID. Collect all for Phase 3.

### Branch C: Workflow Automation (one per `workflow_candidate`)

For **each** `workflow_candidate` in `repo-analysis.json`:

1. Follow the `action-connections` skill workflow to create a scoped connection for this workflow.
   - Include `short_label` in the connection name
   - Collect: connection UUID

2. Follow the `workflow-automation` skill workflow with the connection UUID.
   - Use `type` and `trigger` from the candidate
   - Collect: workflow UUID

**Output per branch:** One workflow UUID. Collect all for Phase 3.

---

## Phase 2→3 Handoff Contract

After all Phase 2 branches complete, write the collected UUIDs to `.claude/context/onboarding-uuids.json`:

```json
{
  "app_ids": {
    "EcsTasks": "uuid-from-app-builder",
    "S3": "uuid-from-app-builder"
  },
  "workflow_ids": {
    "IamDisableUser": "uuid-from-workflow-automation",
    "EcsRollback": "uuid-from-workflow-automation"
  }
}
```

Keys are `short_label` values from `repo-analysis.json`. Values are the UUIDs returned by the create APIs.

---

## Phase 3: Composite Dashboard

**Wait for all app UUIDs and workflow UUIDs before starting.**

Follow the `dashboards` skill workflow to create the composite dashboard using the additive builder pattern.

Pass the collected maps:
- `project_name` — derived from the repo directory basename
- `app_ids` — `{short_label: app_uuid}` map from Branch B
- `workflow_ids` — `{short_label: workflow_uuid}` map from Branch C

The builder additively constructs widgets for each successfully created resource. Missing resources (failed branches) are simply omitted.

---

## Data Handoff Contracts

| Phase | Produces | Consumed By |
|---|---|---|
| Phase 1 | `repo-analysis.json` (`app_candidates`, `workflow_candidates`, `preferred_output_format`) | Phase 2 |
| Phase 2 Branch A | Team handles, entity names | Human reference |
| Phase 2 Branch B (×N) | App UUID per app | Phase 3 via `onboarding-uuids.json` |
| Phase 2 Branch C (×M) | Workflow UUID per workflow | Phase 3 via `onboarding-uuids.json` |
| Phase 3 | Composite dashboard URL | Final output |

---

## Dependency Summary

```
Phase 1 (repo-analyzer)
  └─ must complete before Phase 2 starts

Phase 2 — all branches independent:
  ├─ Branch A: software-catalog
  ├─ Branch B: (action-connections → app-builder) × N apps
  ├─ Branch C: (action-connections → workflow-automation) × M workflows

Phase 3 (composite dashboard)
  └─ waits for all Branch B app UUIDs + Branch C workflow UUIDs
  └─ reads from .claude/context/onboarding-uuids.json
```

---

## Cross-Skill References

| Skill | Role in Onboarding | Key Output |
|---|---|---|
| `repo-analyzer` | Phase 1 — plan generation | `repo-analysis.json`, `preferred_output_format` |
| `software-catalog` | Phase 2 Branch A — registration | Team handles, entity names |
| `action-connections` | Phase 2 — prerequisite per app/workflow | Connection UUID |
| `app-builder` | Phase 2 Branch B — app deployment | App UUID |
| `workflow-automation` | Phase 2 Branch C — workflow creation | Workflow UUID |
| `dashboards` | Phase 3 — composite dashboard | Dashboard URL |
