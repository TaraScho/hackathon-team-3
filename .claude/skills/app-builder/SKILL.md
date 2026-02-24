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
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars
  (app key scopes: apps_run, apps_write, connections_read, connections_resolve).
metadata:
  author: hackathon-team-3
  version: 1.1.0
  tags: [app-builder, aws, internal-tools, terraform, ec2, ecs, s3]
  category: infrastructure
---

# App Builder Skill

## Overview

Datadog App Builder lets you create low-code AWS management consoles that run inside Datadog dashboards. Apps are built from two core primitives:

- **Queries** -- calls to AWS actions (via an action connection) or Datadog APIs. Each query has an `actionId` (the FQN of the AWS operation), a `connectionId`, and `inputs`.
- **Components** -- UI elements (tables, buttons, text inputs, dropdowns) arranged on a grid. Components reference queries for data and trigger queries on user interactions via `events`.

Apps are defined as JSON files, transformed before API submission, then published to make them visible.

### Dependency Diagram

```
action-connections --> app-builder --> dashboards
```

An action connection must exist before creating an app. The app's ID (returned after creation) is needed to embed the app in a dashboard widget.

---

## When to Use

- You want a UI inside Datadog to start/stop/reboot EC2 instances without leaving the platform
- You need to bulk-create apps for an entire AWS environment from JSON templates
- You are writing Terraform to manage apps as code alongside your infrastructure
- You need to wire an existing app to a new connection (e.g., after rotating credentials)
- You are embedding apps inside a dashboard and need to perform placeholder substitution
- You want to understand the `transform_app_json_for_api()` transformation before submitting

---

## Prerequisites

| Requirement | Details |
|---|---|
| Action connection | Created via action-connections skill; or provide an existing UUID as the `connectionId` |
| App key scopes | `apps_run`, `apps_write`, `connections_read`, `connections_resolve` |
| Org ID | Required for restriction policies; fetch from `GET /api/v2/current_user` |

---

## Available App Templates

Nine pre-built app definitions in `examples/python/app-definitions/`:

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

---

## App JSON Structure

Each app definition has three top-level arrays:

```json
{
  "queries": [
    {
      "name": "listInstances",
      "actionId": "com.datadoghq.aws.ec2.describe_ec2_instances",
      "connectionId": "REPLACE_WITH_CONNECTION_ID",
      "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
      "inputs": { "region": "us-east-1", "filters": [] }
    }
  ],
  "components": [
    {
      "type": "grid",
      "name": "instanceTable",
      "properties": { "data": "{{ queries.listInstances.data.instances }}" },
      "events": []
    }
  ],
  "connections": [
    { "connectionId": "REPLACE_WITH_CONNECTION_ID", "label": "AWS Connection" }
  ]
}
```

---

## JSON Transformation for API Submission

Before POSTing to the API, raw app JSON must be transformed. The function `transform_app_json_for_api()` in `examples/python/app_builder_helpers.py` does the following:

1. **Replace `connectionId` placeholders** -- swap `"REPLACE_WITH_CONNECTION_ID"` with the real UUID in both `queries` and `connections` arrays
2. **Remove the `handle` field** -- the API rejects app definitions that include a `handle`
3. **Reconstruct the `connections` array** -- deduplicate and rebuild from the queries list
4. **Wrap in API envelope**:

```python
payload = {
    "data": {
        "type": "appDefinitions",
        "attributes": {
            "name": app_name,
            "description": app_description,
            "rootInstanceName": "grid0",
            "components": transformed_components,
            "queries": transformed_queries,
            "connections": reconstructed_connections,
            "scripts": []
        }
    }
}
```

---

## API Workflow: Create, Restrict, Publish

All endpoints require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### Step 1 -- Create the app

**`POST /api/v2/app-builder/apps`** with the transformed app JSON payload.

Returns `201` with `data.id` (the app UUID). Save this for steps 2 and 3.

```bash
curl -X POST "https://api.datadoghq.com/api/v2/app-builder/apps" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @transformed-app.json
```

### Step 2 -- Set org restriction policy

**`POST /api/v2/restriction_policy/app-builder-app:{app_id}`**

The `id` field must be `app-builder-app:{app_id}`. Valid `relation` values: `viewer`, `editor`.

### Step 3 -- Publish the app

**`POST /api/v2/app-builder/apps/{app_id}/deployment`** with empty body. After this the app is visible in the catalog and embeddable in dashboards.

See `references/api-reference.md` for full curl examples for all 3 steps.

### Endpoint Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v2/app-builder/apps` | Create new app |
| GET | `/api/v2/app-builder/apps` | List apps (paginated) |
| GET | `/api/v2/app-builder/apps/{id}` | Get full app definition |
| PATCH | `/api/v2/app-builder/apps/{id}` | Update app (new version) |
| DELETE | `/api/v2/app-builder/apps/{id}` | Delete app |
| POST | `/api/v2/app-builder/apps/{id}/deployment` | Publish app |
| DELETE | `/api/v2/app-builder/apps/{id}/deployment` | Unpublish app |
| POST | `/api/v2/restriction_policy/app-builder-app:{id}` | Set restriction policy |

---

## Terraform Pattern

The `datadog_app_builder_app` resource accepts an app JSON file and a map of query names to connection IDs:

```hcl
resource "datadog_app_builder_app" "ec2_management" {
  name        = "Modify EC2 instance tags"
  description = "View and manage EC2 instances with team-based filtering and tagging"
  published   = true

  app_json = file("${path.module}/ec2-management-app_definition.json")

  action_query_names_to_connection_ids = {
    for query in ["listTeams", "listInstances", "applyPRODTag", "applyDEVTag", "applyTESTTag"] :
    query => datadog_action_connection.aws_ec2_appbuilder[0].id
  }

  depends_on = [datadog_action_connection.aws_ec2_appbuilder]
}
```

The `app_json` file can use placeholder connection IDs -- Terraform substitutes the real IDs via `action_query_names_to_connection_ids`. See `examples/terraform/ec2-management-app.tf` for the full resource.

---

## Dashboard Embedding Pattern

When an app is used inside a dashboard widget, the dashboard JSON template contains a placeholder like `"APP_ID_PLACEHOLDER_EC2_MANAGEMENT"`. After creating the app, substitute the real ID:

```python
APP_NAME_TO_KEY = {
    "ec2-management-console": "APP_ID_PLACEHOLDER_EC2_MANAGEMENT",
    "manage-ecs-tasks":       "APP_ID_PLACEHOLDER_ECS_MANAGEMENT",
    "explore-s3":             "APP_ID_PLACEHOLDER_S3_EXPLORER",
}

app_id_map = {
    APP_NAME_TO_KEY[app_name]: app_id
    for app_name, app_id in created_apps.items()
}

dashboard_json = load_template("techstories-dashboard-full.json")
for placeholder, real_id in app_id_map.items():
    dashboard_json = dashboard_json.replace(placeholder, real_id)
```

Embedded apps sync with dashboard template variables via `global?.dashboard?.templateVariables` and with the time frame via `global?.dashboard?.timeframe`. See `references/embedded-apps.md` for full details.

---

## Connection Setup with Least-Privilege Role

This skill delegates IAM role + connection creation to the action-connections skill.
Extract action FQNs → resolve IAM permissions via `iam_permissions.py` → call
`setup_datadog_action_connection(permissions=...)`. See the action-connections
skill for the full 6-step flow and code examples.

---

## Action Catalog Reference

When looking up available actions, FQNs, required inputs, or output schemas:

1. Read the master index at `.claude/skills/shared/action-catalog-index.md`
2. Read the per-service file at `.claude/skills/shared/actions-by-service/{service}.md`
3. Use the exact FQN in query `actionId` fields

Common service files: `aws-ec2.md`, `aws-ecs.md`, `aws-iam.md`, `aws-s3.md`, `aws-lambda.md`, `aws-dynamodb.md`, `aws-sqs.md`, `aws-stepfunctions.md`, `aws-autoscaling.md`, `core-workflow.md`.

---

## Cross-Skill Notes

- **Delegates to action-connections**: The action-connections skill is the single IAM authority. This skill extracts the needed permissions and delegates role + connection creation. You can also provide a pre-existing `connection_id` to skip auto-provisioning.
- **Feeds into dashboards**: Each created app's ID must be collected to perform placeholder substitution in dashboard templates. The `dashboards` skill handles that embedding step.
- Connection IDs flow through two paths: Terraform uses `action_query_names_to_connection_ids`; the Python API path uses `transform_app_json_for_api()`.

---

## Additional Resources

| Reference | Contents |
|---|---|
| `references/api-reference.md` | Full API contracts: request/response schemas, all 8 endpoints with curl examples, status codes, error shapes |
| `references/components-and-events.md` | All 22 component types, 10 event types, 8 reaction types, component state accessors |
| `references/queries-and-expressions.md` | Three query types, 9-step execution order, advanced options (debounce, polling, mocks), JS expression syntax |
| `references/embedded-apps.md` | Template variable sync, time frame sync, input parameters, dashboard widget config, catalog self-service actions, notebook embedding |

---

## Level 3 References

- `examples/python/app_builder_helpers.py` -- `transform_app_json_for_api()`, `create_app_builder_app()`, `set_app_restriction_policy()`, `publish_app()`, `create_all_apps_from_directory()`
- `examples/terraform/ec2-management-app.tf` -- `datadog_app_builder_app` with `action_query_names_to_connection_ids` for-expression
- `examples/python/app-definitions/manage-ecs-tasks.json` -- ECS app showing fqn-based action queries and multi-step event wiring
- `examples/python/app-definitions/ec2-management-console.json` -- EC2 app with table component, button triggers, and filter inputs
