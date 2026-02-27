---
name: dashboard-designer
description: >
  Reasons about which dashboard widgets, apps, and workflows are most relevant
  for a project's infrastructure, then produces a dashboard-design.json spec.
  Trigger phrases: "design dashboard", "dashboard design", "what should go on the dashboard",
  "dashboard layout", "select dashboard widgets".
metadata:
  author: hackathon-team-3
  tags: [dashboards, design, planning, observability]
  category: observability
---

# Dashboard Designer Skill

## Overview

Decides **what** belongs on a project's composite dashboard — which widget groups from example dashboards are relevant, which can be omitted, and where Phase 2 apps and workflows should be placed. Produces a `dashboard-design.json` spec consumed by `dashboard-creator`.

---

## Inputs

| Source | File | Key Fields |
|---|---|---|
| Phase 1 | `{RUN_DIR}/repo-analysis.json` | `aws_services`, `app_candidates`, `workflow_candidates` |
| Phase 2 | `{RUN_DIR}/onboarding-uuids.json` | `app_ids`, `workflow_ids` |
| Phase 2 | Software catalog output | Team handles for `$team` template variable |

---

## Workflow

### 1. Identify services and priority

Read `repo-analysis.json`. For each AWS service:
- Note resource count, complexity, and operational criticality
- Rank: services with more resources or higher blast radius get deeper widget coverage

### 2. Select widgets from example dashboards

For each identified service, read its example dashboard from `../dashboard-creator/examples/json/`:

| Service | Example file |
|---|---|
| EC2 | `aws-ec2-overview.json` |
| ECS | `amazon-ecs.json` |
| Lambda | `aws-lambda.json` |
| S3 | `amazon-s3.json` |
| DynamoDB | `amazon-dynamodb.json` |
| API Gateway | `amazon-api-gateway.json` |
| Step Functions | `aws-step-functions.json` |
| EventBridge | `amazon-eventbridge.json` |

For each example dashboard:
- Identify the widget groups (sections of related widgets)
- **Select** groups that match the project's actual usage patterns
- **Omit** groups that don't apply (e.g., replication metrics when no replication is configured) — record brief rationale for each omission

### 3. Place apps and workflows

For each app UUID in `app_ids` and workflow UUID in `workflow_ids`:
- Identify which service group it belongs to
- Place app widgets after the metrics in that group (`position: "after_metrics"`)
- Place workflow trigger widgets after the app (`position: "after_app"`)
- If no matching service group exists, create a standalone group

### 4. Write design spec

Write `{RUN_DIR}/dashboard-design.json` following the output format below.

---

## Design Principles

- **Group by service** — operators think in services, not resource types
- **Critical path gets depth** — high-traffic services get more widget groups; low-priority services get overview only
- **Apps near related metrics** — place management UIs adjacent to the metrics they act on
- **Document omissions** — every skipped widget group gets a one-line rationale
- **Template variables always** — include `env`, `service`, `team` on every dashboard

---

## Output Format: `dashboard-design.json`

```json
{
  "dashboard_title": "{project} Operations Dashboard",
  "layout_type": "ordered",
  "template_variables": ["env", "service", "team"],
  "groups": [
    {
      "title": "ECS Services",
      "rationale": "Core compute — 6 Fargate services, high operational priority",
      "source_example": "amazon-ecs.json",
      "selected_widget_groups": ["overview", "task_status", "resource_utilization"],
      "omitted_widget_groups": [
        {"name": "container_status", "reason": "Redundant with task status for Fargate-only"}
      ],
      "embedded_apps": [
        {"app_id_placeholder": "__APP_ID_ECS__", "label": "ECS Task Manager", "position": "after_metrics"}
      ],
      "embedded_workflows": [
        {"workflow_id_placeholder": "__WORKFLOW_ID_ECS_ROLLBACK__", "label": "ECS Rollback", "position": "after_app"}
      ]
    }
  ]
}
```

Each group captures: what's included, what's excluded and why, and where apps/workflows sit relative to metrics.

---

## Cross-Skill Notes

- **Reads from** `dashboard-creator/examples/json/` for widget group selection
- **Produces** `dashboard-design.json` consumed by `dashboard-creator`
- **Standalone use**: Can generate a design spec without Phase 2 outputs — omit `embedded_apps` and `embedded_workflows` arrays
