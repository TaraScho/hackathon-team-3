---
name: app-builder
description: >
  Creates and deploys Datadog App Builder apps — low-code AWS management UIs
  embedded in dashboards. Handles Create → Restrict → Publish flow, JSON
  transformation, and connection wiring for EC2, ECS, S3, DynamoDB, SQS,
  Lambda, Auto Scaling, and Step Functions templates.
  Trigger phrases: "app builder", "internal tool", "manage EC2 in Datadog",
  "embed app in dashboard", "appDefinitions API", "publish app", "manage ECS tasks".
  Do NOT use for IAM trust setup (use action-connections), workflow specs
  (use workflow-automation), or dashboards without apps (use dashboards).
metadata:
  author: hackathon-team-3
  tags: [app-builder, aws, internal-tools, ec2, ecs, s3]
  category: infrastructure
---

# App Builder Skill

## Overview

Datadog App Builder creates low-code AWS management consoles that run inside Datadog dashboards. Apps are built from two core primitives:

- **Queries** — calls to AWS actions (via an action connection) or Datadog APIs. Each query has an `actionId` (FQN), a `connectionId`, and `inputs`.
- **Components** — UI elements (tables, buttons, text inputs, dropdowns) on a grid. Components reference queries for data and trigger queries via `events`.

Apps are defined as JSON files, transformed before API submission, then published.

### Dependency Diagram

```
(action-connections → app-builder) × N apps → [N app UUIDs] → dashboards (composite)
```

Each app gets its own dedicated action connection (1:1 — never shared).

---

## Doc Fetch URLs

Before executing, fetch current API and product documentation:

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/app-builder.md` |
| Components reference | `https://docs.datadoghq.com/actions/app_builder/components.md` |
| Queries reference | `https://docs.datadoghq.com/actions/app_builder/queries.md` |
| Events reference | `https://docs.datadoghq.com/actions/app_builder/events.md` |
| Expressions reference | `https://docs.datadoghq.com/actions/app_builder/expressions.md` |
| Terraform provider | TF MCP → `datadog_app_builder_app` |

---

## Output Format Selection

Read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` |
| `shell` | Claude executes `jq` + `curl` commands directly via Bash tool |

---

## When to Use

- You want a UI inside Datadog to manage AWS resources without leaving the platform
- You need to bulk-create apps from JSON templates
- You are embedding apps inside a dashboard
- You need to wire an app to a new or rotated connection

---

## Prerequisites

| Requirement | Details |
|---|---|
| Action connection | Created via action-connections skill; UUID provided as `connectionId` |
| App key scopes | `apps_run`, `apps_write`, `connections_read`, `connections_resolve` |
| Org ID | Required for restriction policies; fetch from `GET /api/v2/current_user` |

---

## Available App Templates

Nine pre-built app definitions in `examples/app-definitions/`:

| File | AWS Service | Key Operations |
|---|---|---|
| `ec2-management-console.json` | EC2 | describe, start, stop, reboot instances |
| `manage-ecs-tasks.json` | ECS | list tasks, stop tasks, describe services |
| `explore-s3.json` | S3 | list buckets, list objects, get/delete objects |
| `manage-dynamodb.json` | DynamoDB | list tables, scan, get/put/delete items |
| `manage-sqs.json` | SQS | list queues, send/receive/delete messages |
| `lambda-function-manager.json` | Lambda | list functions, invoke, get configuration |
| `manage-autoscaling.json` | Auto Scaling | describe groups, set desired capacity |
| `manage-step-functions.json` | Step Functions | list state machines, start/stop executions |
| `aws-quick-review.json` | Multi-service | Read-only overview across EC2, RDS, S3 |

All templates use `__CONNECTION_ID__` as the placeholder for connection UUIDs.

---

## Core Workflow: Create, Restrict, Publish

All API calls require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### Step 1 — Transform the app JSON

Before POSTing, transform the raw template JSON:

1. **Replace `__CONNECTION_ID__`** with the real UUID in both `queries` and `connections` arrays
2. **Remove the `handle` field** if present — the API rejects definitions that include `handle`
3. **Reconstruct `connections` array** — deduplicate from queries
4. **Wrap in API envelope**:

```json
{
  "data": {
    "type": "appDefinitions",
    "attributes": {
      "name": "App Name",
      "description": "App description",
      "rootInstanceName": "grid0",
      "components": [...],
      "queries": [...],
      "connections": [...],
      "scripts": []
    }
  }
}
```

Use `jq` to perform the transformation:
```
jq '{data: {type: "appDefinitions", attributes: {name: "App Name", description: "...", rootInstanceName: "grid0", components: .components, queries: (.queries | map(.connectionId = "REAL-UUID")), connections: (.connections | map(.connectionId = "REAL-UUID")), scripts: []}}}' template.json
```

### Step 2 — Create the app

`POST /api/v2/app-builder/apps` with the transformed payload. Returns `201` with `data.id` (app UUID).

### Step 3 — Set org restriction policy

`POST /api/v2/restriction_policy/app-builder-app:{app_id}` with `editor` binding for org principal.

### Step 4 — Publish the app

`POST /api/v2/app-builder/apps/{app_id}/deployment` with empty body. After this the app is visible and embeddable.

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **Must remove `handle`** | API rejects app definitions containing a `handle` field — always strip it before submission |
| **`appDefinitions` type** | The envelope `data.type` must be exactly `"appDefinitions"` (camelCase, plural) |
| **FQN case-sensitivity** | Action FQNs in `actionId` must match exact case; wrong case gives generic 400 "invalid app definition" |
| **Component state access** | Use `ui.{componentName}.value` for component state, `queries.{queryName}.data` for query results — mixing causes silent failures |
| **Table selected row** | `selectedRow` (singular) returns object; `selectedRows` (plural) returns array — using wrong one causes runtime errors |
| **FileUpload** | Returns `ui.{name}.files` (array) not `ui.{name}.value` |
| **runOnPageLoad** | Default is `false`; set `true` only for read-only list queries, never for mutating queries |
| **Polling minimum** | Minimum polling interval is 5000ms (5 seconds); lower values rejected silently |
| **Modal placement** | Modals are opened via `openModal` reaction, not placed directly in grid children |
| **DataTransform re-execution** | Automatically triggers whenever ANY referenced `queries.*` or `ui.*` changes — can cause cascading updates |
| **Embedded app context** | `global.dashboard` is undefined when app runs standalone; always use optional chaining: `global?.dashboard?.templateVariables?.{varName}?.[0]` |
| **Expression globals** | `_` (Lodash), `moment` (Moment.js), `JSON`, `Math`, `Array`, `Object`, `console` are all available in expressions |

---

## Dashboard Embedding

When an app is used inside a dashboard widget, the dashboard JSON contains a placeholder like `__APP_ID_EC2_MANAGEMENT__`. After creating the app, substitute the real UUID using `jq` or string replacement before creating the dashboard.

Embedded apps sync with dashboard template variables via `global?.dashboard?.templateVariables` and with the time frame via `global?.dashboard?.timeframe`.

---

## Action Catalog Reference

When looking up available actions, FQNs, required inputs, or output schemas:

1. Read the master index at `.claude/skills/shared/action-catalog-index.md`
2. Read the per-service file at `.claude/skills/shared/actions-by-service/{service}.md`
3. Use the exact FQN in query `actionId` fields

---

## Cross-Skill Notes

- **Delegates to action-connections**: Connection creation is handled by the action-connections skill. Provide a pre-existing `connection_id` or let orchestration create one.
- **Feeds into dashboards**: Each created app UUID must be collected for placeholder substitution in dashboard templates.
- **Terraform path**: Uses `action_query_names_to_connection_ids` map to wire connections. `app_json = file(...)` accepts the template JSON directly.

---

## JSON Examples

Nine app definition templates in `examples/app-definitions/`. Each contains `queries`, `components`, and `connections` arrays with `__CONNECTION_ID__` placeholders. See "Available App Templates" table above for the mapping.
