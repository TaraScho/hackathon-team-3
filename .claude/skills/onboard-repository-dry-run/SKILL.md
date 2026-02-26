---
name: onboard-repository-dry-run
description: >
  Dry-run mode for the onboard-repository skill. Produces a conceptual markdown
  report of what Datadog resources would be created — no API calls, no file
  generation. Use when asked to "test skills", "run skill tests",
  "dry-run onboarding", or "dry-run onboard-repository".
metadata:
  author: hackathon-team-3
  tags: [testing, dry-run, onboard-repository-dry-run, validation]
  category: testing
---

# Onboard Repository Dry Run Skill

## Overview

The dry-run skill produces a **conceptual report** of what Datadog resources would be created by the `onboard-repository` skill — no API calls are made, no files are generated, no resources are created. The report works identically for Terraform and non-Terraform repos because it reports on Datadog resources, not the customer's IaC format.

The report answers:
- What Datadog resources would be created (apps, workflows, dashboards, catalog entries, action connections)
- What parameters would be needed (connection IDs, app IDs, team names, etc.)
- What dependencies exist between resources
- What order they'd be created in

See `../onboard-repository/SKILL.md` for the orchestration model this skill previews.

---

## When to Use

- You want to preview what onboarding would produce before committing
- You need to validate that repo-analyzer's recommendations make sense
- You want to estimate the scope of a full onboarding run

---

## Core Workflow

### Step 1 — Run repo-analyzer

Follow the `repo-analyzer` skill workflow to produce `repo-analysis.json`. This step is identical to a real onboarding run.

### Step 2 — Select test subset

From `repo-analysis.json`, pick a representative subset:

**Apps (pick 2):**
1. Prefer Tier 1 candidates first (ECS or EC2)
2. Then Tier 2 ranked by service criticality
3. Break ties alphabetically

**Workflows (pick 2):**
1. Prefer high-criticality infrastructure patterns (`iam_broad_permissions`, `open_security_groups`)
2. Then deployment patterns (`ecs_deployment`)
3. Break ties alphabetically

### Step 3 — Generate conceptual report

Produce a structured markdown report (output directly, do not write to file):

```
========================================
DRY RUN REPORT — {repo_path}
Generated: {date}
========================================

## Phase 1: Repo Analysis

AWS services: {list}
Infrastructure patterns: {list}
App candidates: {count} | Workflow candidates: {count}
Preferred output format: {terraform | shell}

## Phase 2: Selected Resources (subset of {total_count})

### Action Connections ({count})

| # | Name | Type | IAM Permissions |
|---|---|---|---|
| 1 | DatadogAction-App-{short_label} | AWS | {permission list} |
| 2 | DatadogAction-App-{short_label} | AWS | {permission list} |
| 3 | DatadogAction-WF-{short_label} | AWS | {permission list} |
| 4 | DatadogAction-WF-{short_label} | AWS | {permission list} |

### App Builder Apps ({count})

| # | Name | Template | Connection |
|---|---|---|---|
| 1 | {short_label} Manager | {template}.json | DatadogAction-App-{short_label} |
| 2 | {short_label} Manager | {template}.json | DatadogAction-App-{short_label} |

### Workflow Automations ({count})

| # | Name | Type | Trigger | Connection |
|---|---|---|---|---|
| 1 | {short_label} Remediation | {type} | {trigger} | DatadogAction-WF-{short_label} |
| 2 | {short_label} Remediation | {type} | {trigger} | DatadogAction-WF-{short_label} |

### Software Catalog

| # | Entity | Kind | Owner |
|---|---|---|---|
| ... | ... | service | {team} |

### Dashboards

| # | Name | Type | Dependencies |
|---|---|---|---|
| 1 | {project} Operations Dashboard | Composite | All app UUIDs + workflow UUIDs |
| 2 | SRE Golden Signals | Standalone | None |

## Phase 3: Dependency Graph

```
Phase 1: repo-analyzer
  └─► Phase 2 (parallel):
      ├─ software-catalog (teams → entities)
      ├─ connection-1 → app-1 ──┐
      ├─ connection-2 → app-2 ──┤
      ├─ connection-3 → wf-1  ──┤
      ├─ connection-4 → wf-2  ──┘
  └─► Phase 3: composite dashboard (waits for all UUIDs)
```

## Summary

Total resources: {count}
- Action connections: {n}
- App Builder apps: {n}
- Workflows: {n}
- Catalog entities: {n}
- Dashboards: {n}

NO RESOURCES WERE CREATED. Run `onboard-repository` to execute.
========================================
```

---

## Resource Naming Convention

| Resource Type | Pattern |
|---|---|
| IAM Role | `DatadogAction-{Type}-{short_label}` |
| Connection | `Conn-{Type}-{short_label}` |
| App | `{short_label} Manager` |
| Workflow | `{short_label} Remediation` |
| Dashboard | `{project_name} Operations Dashboard` |

Where `{Type}` = `App` or `WF`.

---

## Cross-Skill Notes

- **Loads `onboard-repository`**: This skill previews the orchestration model from `onboard-repository`.
- **Identical Phase 1**: Repo analysis runs normally — only Phases 2-3 are conceptual.
- **No file output**: The report is displayed directly, not written to files.
- **1:1 connection model**: Each app/workflow gets its own connection in the report.
