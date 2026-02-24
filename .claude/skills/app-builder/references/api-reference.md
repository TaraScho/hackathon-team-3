# App Builder API Reference

Complete API contracts for the Datadog App Builder endpoints. All endpoints use the `https://api.datadoghq.com` base URL.

## Authentication Headers

Every request requires:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

Required app key scopes: `apps_write`, `connections_resolve`, `workflows_run` (for create/update/publish); `apps_run`, `connections_read` (for read operations).

---

## POST /api/v2/app-builder/apps — Create App

Creates a new App Builder application.

### Request Body (CreateAppRequest Schema)

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
          "properties": {
            "children": [
              {
                "type": "table",
                "name": "instanceTable",
                "properties": {
                  "data": "{{ queries.listInstances.data.instances }}",
                  "columns": [],
                  "isSearchable": true
                },
                "events": [
                  {
                    "name": "tableRowClick",
                    "type": "custom",
                    "reactions": [
                      {
                        "type": "setComponentState",
                        "target": "selectedInstance",
                        "value": "{{ ui.instanceTable.selectedRow }}"
                      }
                    ]
                  }
                ]
              }
            ]
          },
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
            "inputs": {
              "region": "us-east-1",
              "filters": []
            }
          },
          "events": [
            {
              "name": "onSuccess",
              "type": "custom",
              "reactions": []
            },
            {
              "name": "onError",
              "type": "custom",
              "reactions": []
            }
          ]
        }
      ],
      "connections": [],
      "scripts": []
    }
  }
}
```

### ComponentGrid Schema

The root component is always a `grid`. It contains child components in `properties.children`:

```json
{
  "type": "grid",
  "name": "grid0",
  "properties": {
    "children": [],
    "columns": 12,
    "isVisible": true
  },
  "events": []
}
```

### Component Schema

Each child component follows this structure:

```json
{
  "type": "table|button|textInput|select|text|...",
  "name": "uniqueComponentName",
  "properties": {
    "...type-specific properties..."
  },
  "events": [
    {
      "name": "eventName",
      "type": "custom",
      "reactions": [
        {
          "type": "reactionType",
          "...reaction-specific fields..."
        }
      ]
    }
  ]
}
```

### Query Schema

Queries come in three types:

**ActionQuery** (calls AWS/Datadog actions):
```json
{
  "name": "queryName",
  "type": "action",
  "id": "uuid",
  "properties": {
    "fqn": "com.datadoghq.aws.ec2.describe_ec2_instances",
    "connectionId": "connection-uuid",
    "inputs": { "region": "us-east-1" }
  },
  "events": []
}
```

**DataTransform** (JavaScript expression):
```json
{
  "name": "transformName",
  "type": "dataTransform",
  "id": "uuid",
  "properties": {
    "expression": "return queries.listInstances.data.instances.filter(i => i.state === 'running')"
  },
  "events": []
}
```

**StateVariable** (persistent state):
```json
{
  "name": "selectedRegion",
  "type": "stateVariable",
  "id": "uuid",
  "properties": {
    "defaultValue": "us-east-1"
  },
  "events": []
}
```

### Response (201 Created)

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

Key field: `data.id` is the app UUID used for all subsequent operations.

### Status Codes

| Code | Meaning |
|------|---------|
| 201 | App created successfully |
| 400 | Invalid app definition (malformed JSON, missing required fields) |
| 403 | Missing `apps_write` scope on the app key |
| 429 | Rate limited |

### curl

```bash
curl -X POST "https://api.datadoghq.com/api/v2/app-builder/apps" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @transformed-app.json
```

---

## GET /api/v2/app-builder/apps — List Apps

Returns a paginated list of apps with basic info (ID, name, description).

### Query Parameters

| Param | Type | Description |
|-------|------|-------------|
| `limit` | int | Apps per page (default 25) |
| `page` | int | Page number (0-indexed) |
| `filter[name]` | string | Filter by exact app name |
| `filter[query]` | string | Search by name or creator |
| `filter[deployed]` | bool | Filter by publish status |
| `filter[tags]` | string | Filter by tags |
| `sort` | string | Sort field: `name`, `-name`, `created_at`, `-created_at` |

### Response (200)

```json
{
  "data": [
    {
      "id": "12345678-abcd-efgh-ijkl-123456789012",
      "type": "appDefinitions",
      "attributes": {
        "name": "EC2 Management Console",
        "description": "View and manage EC2 instances"
      }
    }
  ],
  "meta": {
    "page": { "totalCount": 42 }
  }
}
```

### curl

```bash
curl -X GET "https://api.datadoghq.com/api/v2/app-builder/apps?limit=10&filter[name]=EC2" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## GET /api/v2/app-builder/apps/{app_id} — Get App

Returns the complete app definition including components, queries, and connections.

### Query Parameters

| Param | Type | Description |
|-------|------|-------------|
| `version` | string | `latest` (default), `deployed`, or a version number |

### Response (200)

Full app definition with all components, queries, connections, and version metadata.

### Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Invalid request |
| 403 | Missing required scope |
| 404 | App not found |
| 410 | App was deleted |

### curl

```bash
curl -X GET "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}?version=deployed" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## PATCH /api/v2/app-builder/apps/{app_id} — Update App

Creates a new version of the app. Uses the same request body format as POST create.

### Status Codes

| Code | Meaning |
|------|---------|
| 200 | App updated, new version created |
| 400 | Invalid app definition |
| 403 | Missing `apps_write` scope |
| 404 | App not found |

### curl

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @updated-app.json
```

---

## DELETE /api/v2/app-builder/apps/{app_id} — Delete App

Permanently deletes the app. If published, the deployment is also removed.

### Status Codes

| Code | Meaning |
|------|---------|
| 200 | App deleted |
| 400 | Invalid request |
| 403 | Missing `apps_write` scope |
| 404 | App not found |
| 410 | App already deleted |

### curl

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## POST /api/v2/app-builder/apps/{app_id}/deployment — Publish App

Publishes the latest version of the app, making it visible in the App Builder catalog and available for dashboard embedding. Empty request body.

### Response (201)

```json
{
  "data": {
    "id": "deployment-uuid",
    "type": "deployment",
    "attributes": {}
  }
}
```

### curl

```bash
curl -X POST "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}/deployment" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json"
```

---

## DELETE /api/v2/app-builder/apps/{app_id}/deployment — Unpublish App

Removes the live/published version. The app draft remains and can be updated and republished later.

### Status Codes

| Code | Meaning |
|------|---------|
| 200 | Deployment removed |
| 404 | App or deployment not found |

### curl

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/app-builder/apps/${APP_ID}/deployment" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## POST /api/v2/restriction_policy/app-builder-app:{app_id} — Set Restriction Policy

Sets the org-level restriction policy on an app. This controls who can view and edit the app.

### Request Body

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

### Field Notes

- `id`: Must be `app-builder-app:{app_id}` (resource type prefix required)
- `relation`: Valid values are `viewer` and `editor`
- `principals`: Array of principal strings. Format: `org:{org_id}`, `team:{team_id}`, or `user:{user_id}`

### curl

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

---

## Error Response Shape

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

Common error patterns:
- `400` with `"detail": "invalid app definition"` -- malformed components or queries
- `403` with missing scope detail -- check app key scopes
- `404` -- app ID does not exist
- `410` -- app was previously deleted
- `429` -- rate limit exceeded; back off and retry

---

## Endpoint Summary Table

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
