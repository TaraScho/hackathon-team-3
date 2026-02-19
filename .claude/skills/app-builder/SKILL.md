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
| Action connection | Must exist; provide its UUID as the `connectionId` when creating the app |
| App key scopes | `apps_run`, `apps_write`, `connections_read`, `connections_resolve` |
| Org ID | Required for setting restriction policies; fetch from `GET /api/v2/current_user` |

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

### Step 1 — Create the app

```
POST /api/v2/app-builder/apps
```

Body: the wrapped payload from `transform_app_json_for_api()`. Returns: `data.id` — the app UUID.

### Step 2 — Set org restriction policy

```
POST /api/v2/restriction_policy/app-builder-app:{app_id}
```

```python
payload = {
    "data": {
        "id": f"app-builder-app:{app_id}",
        "type": "restriction_policy",
        "attributes": {
            "bindings": [{"relation": "editor", "principals": [f"org:{org_id}"]}]
        }
    }
}
```

### Step 3 — Publish the app

```
POST /api/v2/app-builder/apps/{app_id}/deployment
```

Empty body. After this call the app is visible in the App Builder catalog and can be embedded in dashboards.

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

## Cross-Skill Notes

- **Requires action-connections**: The connection UUID must exist before app creation. Use `action-connections` skill first.
- **Feeds into dashboards**: Each created app's ID must be collected to perform placeholder substitution in dashboard templates. The `dashboards` skill handles that embedding step.
- Connection IDs flow through two paths: Terraform uses `action_query_names_to_connection_ids`; the Python API path uses `transform_app_json_for_api()`.

---

## Level 3 References

- `examples/python/app_builder_helpers.py` — `create_app_key_with_app_builder_scopes()`, `transform_app_json_for_api()`, `create_app_builder_app()`, `set_app_restriction_policy()`, `publish_app()`, `create_all_apps_from_directory()`
- `examples/terraform/ec2-management-app.tf` — `datadog_app_builder_app` with `action_query_names_to_connection_ids` for-expression
- `examples/python/app-definitions/manage-ecs-tasks.json` — ECS app showing fqn-based action queries and multi-step event wiring
- `examples/python/app-definitions/ec2-management-console.json` — EC2 app with table component, button triggers, and filter inputs
