---
name: app-builder
description: >
  Creates and deploys Datadog App Builder applications that embed AWS service
  management UIs directly in Datadog dashboards. Use this skill when you need to:
  build an internal tool for managing EC2 instances, ECS tasks, S3 files, DynamoDB,
  SQS, Lambda, or Step Functions; create an App Builder app via the Datadog API or
  Terraform; batch-deploy multiple apps from JSON definitions; wire apps to AWS
  action connections; set org-wide restriction policies; publish apps; embed apps
  in dashboards using placeholder substitution; or transform app JSON files for API
  submission. Trigger phrases: "app builder", "internal tool", "manage EC2 in Datadog",
  "embed app in dashboard", "action_query_names_to_connection_ids", "apps_write scope",
  "appDefinitions API", "publish app", "manage ECS tasks", "explore S3".
  Do NOT use for creating the IAM trust setup (use action-connections), writing
  workflow automation specs (use workflow-automation), or creating dashboards
  without embedded apps (use dashboards).
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars
  (app key scopes: apps_run, apps_write, connections_read, connections_resolve).
metadata:
  author: hackathon-team-3
  version: 1.0.0
  tags: [app-builder, aws, internal-tools, terraform, ec2, ecs, s3]
  category: infrastructure
---

# App Builder Skill

## Overview

Datadog App Builder lets you create low-code, AWS management consoles that run inside Datadog dashboards. Apps are built from two core primitives:

- **Queries** — calls to AWS actions (via an action connection) or Datadog APIs. Each query has an `actionId` (the fully qualified name of the AWS operation), a `connectionId`, and `inputs`.
- **Components** — UI elements (tables, buttons, text inputs, dropdowns) arranged on a grid. Components reference queries for their data and trigger queries on user interactions via `events`.

Apps are defined as JSON files, transformed before API submission, and then published to make them visible.

### Dependency Diagram

```
action-connections ──► app-builder ──► dashboards
```

An action connection must exist before creating an app. The app's ID (returned after creation) is needed to embed the app in a dashboard widget.

---

## When to Use

- You want a UI inside Datadog to start/stop/reboot EC2 instances without leaving the platform
- You need to bulk-create apps for an entire AWS environment from JSON templates
- You are writing Terraform to manage apps as code alongside your infrastructure
- You need to wire an existing app to a new connection (e.g., after rotating credentials)
- You are embedding apps inside a dashboard and need to perform the placeholder substitution
- You want to understand the `transform_app_json_for_api()` transformation before submitting

---

## Prerequisites

| Requirement | Details |
|---|---|
| Action connection | Created automatically via action-connections skill if not provided; or provide an existing UUID as the `connectionId` |
| App key scopes | `apps_run`, `apps_write`, `connections_read`, `connections_resolve` |
| Org ID | Required for setting restriction policies; fetch from `GET /api/v2/current_user` |

**Note:** The action-connections skill handles IAM role creation and permission scoping. You do not need to create IAM roles manually.

---

## Available App Templates

Nine pre-built app definitions are in `examples/python/app-definitions/`:

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
      "inputs": {
        "region": "us-east-1",
        "filters": []
      }
    }
  ],
  "components": [
    {
      "type": "grid",
      "name": "instanceTable",
      "properties": {
        "data": "{{ queries.listInstances.data.instances }}"
      }
    }
  ],
  "connections": [
    {
      "connectionId": "REPLACE_WITH_CONNECTION_ID",
      "label": "AWS Connection"
    }
  ]
}
```

---

## JSON Transformation for API Submission

Before POSTing to the API, the raw app JSON must be transformed. The function `transform_app_json_for_api()` in `examples/python/app_builder_helpers.py` does the following:

1. **Replace `connectionId` placeholders** — swap `"REPLACE_WITH_CONNECTION_ID"` with the real UUID in both `queries` and `connections` arrays
2. **Remove the `handle` field** — the API rejects app definitions that include a `handle`
3. **Reconstruct the `connections` array** — deduplicate and rebuild from the queries list
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

## API Workflow: Create → Restrict → Publish

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

Required app key scopes: `apps_write`, `connections_resolve`, `workflows_run` (for create/update); `apps_run`, `connections_read` (for read).

### Step 1 — Create the app

**`POST https://api.datadoghq.com/api/v2/app-builder/apps`**

**Request body:**
```json
{
  "data": {
    "type": "appDefinitions",
    "attributes": {
      "name": "EC2 Management Console",
      "description": "View and manage EC2 instances",
      "rootInstanceName": "grid0",
      "components": [
        {
          "type": "grid",
          "name": "grid0",
          "properties": { "children": [] },
          "events": []
        }
      ],
      "queries": [
        {
          "name": "listInstances",
          "type": "action",
          "id": "unique-query-uuid",
          "properties": {
            "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
            "connectionId": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
            "inputs": { "region": "us-east-1" }
          },
          "events": []
        }
      ],
      "connections": []
    }
  }
}
```

**Response (201):**
```json
{
  "data": {
    "id": "12345678-abcd-efgh-ijkl-123456789012",
    "type": "appDefinitions",
    "attributes": {
      "name": "EC2 Management Console",
      "description": "View and manage EC2 instances"
    }
  }
}
```

Key field: `data.id` — the app UUID. Save this for restriction policy and publishing.

**Errors:** `400` (invalid app definition), `403` (missing `apps_write` scope), `429` (rate limited).

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/app-builder/apps" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @transformed-app.json
```

### Step 2 — Set org restriction policy

**`POST https://api.datadoghq.com/api/v2/restriction_policy/app-builder-app:{app_id}`**

**Request body:**
```json
{
  "data": {
    "id": "app-builder-app:12345678-abcd-efgh-ijkl-123456789012",
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {
          "relation": "editor",
          "principals": ["org:your-org-id"]
        }
      ]
    }
  }
}
```

Field notes:
- `id`: Must be `app-builder-app:{app_id}` (resource type prefix)
- `relation`: For App Builder apps, valid values are `viewer`, `editor`

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/restriction_policy/app-builder-app:${APP_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "id": "app-builder-app:'"${APP_ID}"'",
      "type": "restriction_policy",
      "attributes": {
        "bindings": [{"relation": "editor", "principals": ["org:'"${ORG_ID}"'"]}]
      }
    }
  }'
```

### Step 3 — Publish the app

**`POST https://api.datadoghq.com/api/v2/app-builder/apps/{app_id}/deployment`**

Empty request body. After this call the app is visible in the App Builder catalog and can be embedded in dashboards.

**Response (201):**
```json
{
  "data": {
    "id": "deployment-uuid",
    "type": "deployment",
    "attributes": {}
  }
}
```

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}/deployment" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json"
```

---

## Additional API Endpoints

### GET /api/v2/app-builder/apps — List apps

Paginated. Returns basic app info (ID, name, description).

**Query parameters:**
| Param | Type | Description |
|---|---|---|
| `limit` | int | Apps per page |
| `page` | int | Page number |
| `filter[name]` | string | Filter by app name |
| `filter[query]` | string | Filter by name or creator |
| `filter[deployed]` | bool | Filter by publish status |
| `filter[tags]` | string | Filter by tags |
| `sort` | string | Sort field (e.g., `name`, `-name`, `created_at`) |

```bash
curl -X GET "https://api.datadoghq.com/api/v2/app-builder/apps?limit=10&filter[name]=EC2" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### GET /api/v2/app-builder/apps/{app_id} — Get full app definition

Returns the complete app with components, queries, and connections. Optional `version` query param (`latest`, `deployed`, or version number).

```bash
curl -X GET "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}?version=deployed" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

**Status codes:** `200`, `400`, `403`, `404`, `410` (deleted).

### PATCH /api/v2/app-builder/apps/{app_id} — Update app

Creates a new version of the app. Same body format as POST create.

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @updated-app.json
```

### DELETE /api/v2/app-builder/apps/{app_id} — Delete app

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

**Status codes:** `200`, `400`, `403`, `404`, `410`.

### DELETE /api/v2/app-builder/apps/{app_id}/deployment — Unpublish app

Removes the live version. The app can still be updated and republished later.

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}/deployment" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Error response shape

All errors follow the JSON:API format:
```json
{
  "errors": [
    {
      "status": "403",
      "title": "Forbidden",
      "detail": "Missing required scope: apps_write"
    }
  ]
}
```

---

## Terraform Pattern

The `datadog_app_builder_app` resource accepts an app JSON file and a map of query names to connection IDs:

```hcl
resource "datadog_app_builder_app" "ec2_management" {
  name        = "Modify EC2 instance tags"
  description = "View and manage EC2 instances with team-based filtering and tagging"
  published   = true

  app_json = file("${path.module}/ec2-management-app_definition.json")

  # Map each query name to the connection it should use
  action_query_names_to_connection_ids = {
    for query in ["listTeams", "listInstances", "applyPRODTag", "applyDEVTag", "applyTESTTag"] :
    query => datadog_action_connection.aws_ec2_appbuilder[0].id
  }

  depends_on = [datadog_action_connection.aws_ec2_appbuilder]
}
```

The `app_json` file can use placeholder connection IDs — Terraform substitutes the real IDs via `action_query_names_to_connection_ids`.

See `examples/terraform/ec2-management-app.tf` for the full resource.

---

## Dashboard Embedding Pattern

When an app is used inside a dashboard widget, the dashboard JSON template contains a placeholder like `"APP_ID_PLACEHOLDER_EC2_MANAGEMENT"`. The `create_dashboard_with_embedded_apps()` helper in `../dashboards/examples/python/datadog_helpers.py` performs the substitution:

```python
APP_NAME_TO_KEY = {
    "ec2-management-console": "APP_ID_PLACEHOLDER_EC2_MANAGEMENT",
    "manage-ecs-tasks":       "APP_ID_PLACEHOLDER_ECS_MANAGEMENT",
    "explore-s3":             "APP_ID_PLACEHOLDER_S3_EXPLORER",
    # ...
}

# After creating each app:
app_id_map = {
    APP_NAME_TO_KEY[app_name]: app_id
    for app_name, app_id in created_apps.items()
}

# Load dashboard template and replace all placeholders
dashboard_json = load_template("techstories-dashboard-full.json")
for placeholder, real_id in app_id_map.items():
    dashboard_json = dashboard_json.replace(placeholder, real_id)
```

---

## Action Catalog Reference

When you need to look up available actions, their FQNs, required inputs, or output schemas:

1. Read the master index at `.claude/skills/shared/action-catalog-index.md` to find which service file you need
2. Read the per-service file at `.claude/skills/shared/actions-by-service/{service}.md` for full action details
3. Use the exact FQN from the reference (e.g., `com.datadoghq.aws.ec2.describe_ec2_instances`) in query `actionId` fields

Common service files for this skill:
- `aws-ec2.md` — EC2 instance management
- `aws-ecs.md` — ECS service/task management
- `aws-iam.md` — IAM user/role/policy management
- `aws-s3.md` — S3 bucket/object operations
- `aws-lambda.md` — Lambda function management
- `aws-dynamodb.md` — DynamoDB table/item operations
- `aws-sqs.md` — SQS queue operations
- `aws-stepfunctions.md` — Step Functions state machine management
- `aws-autoscaling.md` — Auto Scaling group management
- `core-workflow.md` — Loop, condition, JS transform actions

---

## Connection Setup with Least-Privilege Role

When creating an app, you can automatically provision a dedicated IAM role + connection scoped to exactly the AWS actions the app needs. This uses the shared `iam_permissions.py` utility to extract actions from the app JSON and resolve them to IAM permissions.

**Step-by-step:**
1. Extract action FQNs from the app JSON using the shared utility
2. Resolve FQNs to IAM permissions via the action catalog
3. Call `setup_datadog_action_connection(permissions=...)` from the action-connections skill to create a dedicated role + connection
4. Use the returned `connection_id` for the app

```python
import sys
sys.path.insert(0, ".claude/skills/shared")
from iam_permissions import load_action_catalog, extract_actions_from_app_json, resolve_permissions

# Step 1-2: Extract actions and resolve permissions
catalog = load_action_catalog(".claude/skills/shared/actions-by-service")
actions = extract_actions_from_app_json("path/to/app.json")
permissions = resolve_permissions(actions, catalog)

# Step 3: Create dedicated role + connection
sys.path.insert(0, ".claude/skills/action-connections/examples/python")
from setup_action_connection import setup_datadog_action_connection

response = setup_datadog_action_connection(
    api_key=os.environ["DD_API_KEY"],
    app_key=os.environ["DD_APP_KEY"],
    role_name="DatadogAction-MyApp",
    connection_name="MyApp-Connection",
    permissions=permissions,  # Scopes the role to only these permissions
)
connection_id = response.data["connection_id"]

# Step 4: Create the app using this connection
```

This gives each app its own IAM role with only the permissions it actually uses.

---

## Cross-Skill Notes

- **Delegates to action-connections**: The action-connections skill is the single IAM authority. This skill extracts the needed permissions and delegates role + connection creation. You can also provide a pre-existing `connection_id` to skip auto-provisioning.
- **Feeds into dashboards**: Each created app's ID must be collected to perform placeholder substitution in dashboard templates. The `dashboards` skill handles that embedding step.
- Connection IDs flow through two paths: Terraform uses `action_query_names_to_connection_ids`; the Python API path uses `transform_app_json_for_api()`.

---

## Level 3 References

- `examples/python/app_builder_helpers.py` — `create_app_key_with_app_builder_scopes()`, `transform_app_json_for_api()`, `create_app_builder_app()`, `set_app_restriction_policy()`, `publish_app()`, `create_all_apps_from_directory()`
- `examples/terraform/ec2-management-app.tf` — `datadog_app_builder_app` with `action_query_names_to_connection_ids` for-expression
- `examples/python/app-definitions/manage-ecs-tasks.json` — ECS app showing fqn-based action queries and multi-step event wiring
- `examples/python/app-definitions/ec2-management-console.json` — EC2 app with table component, button triggers, and filter inputs
