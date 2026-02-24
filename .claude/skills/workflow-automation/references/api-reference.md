# Workflow Automation API Reference

All endpoints use base URL `https://api.datadoghq.com` (US1). Adjust for your Datadog site (e.g., `api.us3.datadoghq.com`, `api.datadoghq.eu`).

## Authentication Headers

Every request requires:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

**Required app key scopes:**

| Scope | Operations |
|---|---|
| `workflows_write` | Create, update, delete workflows |
| `workflows_read` | Get, list workflows and instances |
| `workflows_run` | Execute workflows, cancel instances |

---

## POST /api/v2/workflows -- Create a Workflow

Creates a new workflow definition. The workflow can optionally be published immediately.

**Request body:**

```json
{
  "data": {
    "type": "workflows",
    "attributes": {
      "name": "ECS Rollback",
      "description": "Rolls back an ECS service to a specified image tag",
      "tags": ["ecs", "rollback", "automated"],
      "published": true,
      "spec": {
        "handle": "ecs-rollback",
        "triggers": [
          {
            "startStepNames": ["Describe_task_definition"],
            "monitorTrigger": {
              "rateLimit": { "count": 1, "interval": "3600s" }
            }
          }
        ],
        "steps": [
          {
            "name": "Describe_task_definition",
            "actionId": "com.datadoghq.aws.ecs.describeTaskDefinition",
            "connectionLabel": "INTEGRATION_AWS",
            "parameters": [
              { "name": "taskDefinition", "value": "{{ Trigger.service_name }}" }
            ],
            "outboundEdges": [
              { "nextStepName": "Next_step", "branchName": "main" }
            ]
          }
        ],
        "connectionEnvs": [
          {
            "env": "default",
            "connections": [
              {
                "connectionId": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
                "label": "INTEGRATION_AWS"
              }
            ]
          }
        ],
        "inputSchema": {
          "parameters": [
            {
              "name": "service_name",
              "label": "Service Name",
              "description": "ECS service to roll back",
              "type": "STRING"
            }
          ]
        }
      }
    }
  }
}
```

**Key fields:**

- `data.type` must be `"workflows"` (plural)
- `spec.handle` is a unique human-readable identifier; causes conflict if reused
- `published: true` makes the workflow immediately active; `false` saves as draft
- `connectionEnvs[].connections[].label` must exactly match (case-sensitive) every step's `connectionLabel`

**Response (201 Created):**

```json
{
  "data": {
    "id": "workflow-uuid-here",
    "type": "workflows",
    "attributes": {
      "name": "ECS Rollback",
      "description": "Rolls back an ECS service to a specified image tag",
      "published": true,
      "createdAt": "2024-01-15T10:30:00.000Z",
      "modifiedAt": "2024-01-15T10:30:00.000Z",
      "spec": { "..." }
    }
  }
}
```

Key field: `data.id` is the workflow UUID used for all subsequent operations.

**Status codes:** `201` (created), `400` (invalid spec), `403` (missing `workflows_write`), `409` (handle conflict), `429` (rate limited).

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/workflows" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @workflow-spec.json
```

---

## GET /api/v2/workflows/{workflow_id} -- Get a Workflow

Retrieves a single workflow definition by UUID.

**Response (200):**

```json
{
  "data": {
    "id": "workflow-uuid-here",
    "type": "workflows",
    "attributes": {
      "name": "ECS Rollback",
      "description": "...",
      "published": true,
      "createdAt": "2024-01-15T10:30:00.000Z",
      "modifiedAt": "2024-01-15T10:30:00.000Z",
      "spec": { "..." }
    }
  }
}
```

**Status codes:** `200`, `400` (invalid ID format), `403`, `404` (not found), `429`.

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## PATCH /api/v2/workflows/{workflow_id} -- Update a Workflow

Updates an existing workflow. Uses the same body structure as create. You can send partial updates to `attributes` (e.g., update just the `spec` or just the `name`).

**Request body (partial update example):**

```json
{
  "data": {
    "type": "workflows",
    "attributes": {
      "published": true,
      "spec": { "...updated spec..." }
    }
  }
}
```

**Response (200):** Same shape as GET response with updated fields.

**Status codes:** `200`, `400`, `403`, `404`, `429`.

**curl:**

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @updated-workflow.json
```

---

## DELETE /api/v2/workflows/{workflow_id} -- Delete a Workflow

Permanently deletes a workflow. This cannot be undone.

**Response:** `204 No Content` on success (empty body).

**Status codes:** `204`, `400`, `403`, `404`, `429`.

**curl:**

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## POST /api/v2/workflows/{workflow_id}/instances -- Execute a Workflow

Triggers a manual execution of a workflow, passing input parameters via the `meta.payload` object.

**Request body:**

```json
{
  "meta": {
    "payload": {
      "service_name": "my-ecs-service",
      "image_tag": "v1.2.3"
    }
  }
}
```

Parameters in `meta.payload` must match the names defined in the workflow's `inputSchema.parameters`. Unrecognized parameters are silently ignored.

**Response (200):**

```json
{
  "data": {
    "id": "instance-uuid-here"
  }
}
```

Key field: `data.id` is the execution instance ID. Use this to poll status or cancel.

**Status codes:** `200`, `400` (invalid payload), `403` (missing `workflows_run`), `404`, `429`.

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"meta": {"payload": {"service_name": "my-ecs-service", "image_tag": "v1.2.3"}}}'
```

---

## GET /api/v2/workflows/{workflow_id}/instances -- List Executions

Lists execution instances for a workflow with pagination.

**Query parameters:**

| Param | Type | Default | Description |
|---|---|---|---|
| `page[size]` | int | 10 | Number of results per page (max 100) |
| `page[number]` | int | 0 | Zero-indexed page number |

**Response (200):**

```json
{
  "data": [
    {
      "id": "instance-uuid-1",
      "type": "workflowInstances",
      "attributes": {
        "status": "COMPLETED",
        "createdAt": "2024-01-15T10:30:00.000Z",
        "finishedAt": "2024-01-15T10:30:45.000Z"
      }
    }
  ],
  "meta": {
    "page": {
      "totalCount": 42
    }
  }
}
```

**Status codes:** `200`, `400`, `403`, `404`, `429`.

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances?page[size]=10&page[number]=0" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## GET /api/v2/workflows/{workflow_id}/instances/{instance_id} -- Get Execution Status

Retrieves the status and output of a specific workflow execution.

**Response (200):**

```json
{
  "data": {
    "id": "instance-uuid-here",
    "type": "workflowInstances",
    "attributes": {
      "status": "COMPLETED",
      "createdAt": "2024-01-15T10:30:00.000Z",
      "finishedAt": "2024-01-15T10:30:45.000Z",
      "outputs": { "..." }
    }
  }
}
```

Possible `status` values: `RUNNING`, `COMPLETED`, `FAILED`, `CANCELED`, `WAITING`.

**Status codes:** `200`, `400`, `403`, `404`, `429`.

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances/${INSTANCE_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## PUT /api/v2/workflows/{workflow_id}/instances/{instance_id}/cancel -- Cancel Execution

Cancels a running workflow execution. Only works on instances with status `RUNNING` or `WAITING`.

**Response:** `200` with the updated instance object (status becomes `CANCELED`).

**Status codes:** `200`, `400` (instance not cancelable), `403`, `404`, `429`.

**curl:**

```bash
curl -X PUT "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances/${INSTANCE_ID}/cancel" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## Error Response Shape

All error responses follow the JSON:API format:

```json
{
  "errors": [
    {
      "status": "403",
      "title": "Forbidden",
      "detail": "Missing required scope: workflows_write"
    }
  ]
}
```

The `errors` array can contain multiple error objects. Common error patterns:

| Status | Title | Common Cause |
|---|---|---|
| `400` | Bad Request | Invalid JSON, missing required fields, malformed spec |
| `403` | Forbidden | App key missing required scope |
| `404` | Not Found | Workflow or instance UUID does not exist |
| `409` | Conflict | Workflow handle already exists (create only) |
| `429` | Too Many Requests | Rate limit exceeded; retry after `Retry-After` header value |

---

## Idempotent Create-or-Update Pattern

The workflow API does not support listing or searching workflows by name or handle. To implement create-or-update:

1. Attempt `POST /api/v2/workflows` to create the workflow
2. If you receive a `409 Conflict` (handle already exists), the workflow exists
3. If you stored the workflow ID previously, use `PATCH /api/v2/workflows/{workflow_id}` to update
4. If you do not have the ID, you must retrieve it through other means (e.g., Terraform state, a local mapping file, or the Datadog UI)

**Python implementation pattern:**

```python
import requests

def create_or_update_workflow(api_key, app_key, spec_payload, known_id=None):
    headers = {
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
        "Content-Type": "application/json",
    }
    base_url = "https://api.datadoghq.com/api/v2/workflows"

    if known_id:
        # Update existing workflow
        resp = requests.patch(f"{base_url}/{known_id}", headers=headers, json=spec_payload)
        resp.raise_for_status()
        return resp.json()["data"]["id"]

    # Try to create
    resp = requests.post(base_url, headers=headers, json=spec_payload)
    if resp.status_code == 201:
        return resp.json()["data"]["id"]
    elif resp.status_code == 409:
        raise ValueError("Workflow handle exists but no known_id provided for update")
    else:
        resp.raise_for_status()
```

For Terraform-managed workflows, this pattern is unnecessary because Terraform tracks the ID in state automatically.
