# Service Catalog API Reference

Complete API contracts for the Datadog Software Catalog (entity CRUD) and Teams API (team CRUD). All endpoints use the Datadog REST API v2.

---

## Authentication Headers

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

No special app key scopes are needed for catalog writes.

---

## Catalog Entity API

### POST /api/v2/catalog/entity — Upsert Entity

Creates or updates an entity definition. This is an **upsert** — `200`, `201`, and `202` all indicate success.

**Request body:** The v3 entity definition as a JSON object:

```json
{
  "apiVersion": "v3",
  "kind": "service",
  "metadata": {
    "name": "my-service",
    "owner": "my-team",
    "description": "My service description",
    "contacts": [
      { "type": "email", "name": "Support", "contact": "support@example.com" }
    ],
    "links": [
      { "name": "Repository", "type": "repo", "url": "https://github.com/org/repo" }
    ],
    "tags": ["env:production"]
  },
  "spec": {
    "lifecycle": "production",
    "tier": "High",
    "type": "web",
    "dependsOn": ["service:auth-service", "datastore:postgres-main"]
  },
  "datadog": {
    "codeLocations": [
      {
        "repositoryURL": "https://github.com/org/repo",
        "paths": ["services/my_service/**"]
      }
    ]
  }
}
```

**Response (202):**

```json
{
  "data": [
    {
      "id": "entity-uuid",
      "type": "entity",
      "attributes": {
        "apiVersion": "v3",
        "kind": "service",
        "metadata": { "name": "my-service", "owner": "my-team" }
      }
    }
  ]
}
```

**Errors:** `400` (invalid schema, missing owner team), `403` (forbidden), `429` (rate limited).

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/catalog/entity" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "apiVersion": "v3",
    "kind": "service",
    "metadata": {
      "name": "my-service",
      "owner": "my-team",
      "description": "My service"
    },
    "spec": {
      "lifecycle": "production",
      "tier": "High",
      "type": "web"
    }
  }'
```

### GET /api/v2/catalog/entity — List Entities

Returns paginated list of catalog entities with optional filtering.

**Query parameters:**

| Param | Type | Description |
|---|---|---|
| `page[offset]` | int | Offset for pagination |
| `page[limit]` | int | Max results (default 100) |
| `filter[id]` | string | Filter by entity UUID |
| `filter[ref]` | string | Filter by entity ref (e.g., `service:my-service`) |
| `filter[name]` | string | Filter by entity name |
| `filter[kind]` | string | Filter by kind (`service`, `datastore`, `queue`, `system`, `api`, `frontend`, `library`, `custom`) |
| `filter[owner]` | string | Filter by owner team handle |
| `include` | string | Include related resources |
| `includeDiscovered` | bool | Include APM/USM discovered services (default false) |

**Response (200):**

```json
{
  "data": [
    {
      "id": "entity-uuid",
      "type": "entity",
      "attributes": {
        "apiVersion": "v3",
        "kind": "service",
        "metadata": { "name": "my-service", "owner": "my-team" }
      }
    }
  ]
}
```

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/catalog/entity?filter[kind]=service&page[limit]=50" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### DELETE /api/v2/catalog/entity/{entity_id} — Delete Entity

Deletes an entity by its UUID (not the entity ref).

Returns `204 No Content` on success.

**curl:**

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/catalog/entity/${ENTITY_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## Teams API

### POST /api/v2/team — Create Team

**Request body:**

```json
{
  "data": {
    "type": "team",
    "attributes": {
      "name": "My Team",
      "handle": "my-team",
      "description": "Team description"
    },
    "relationships": {
      "users": {
        "data": []
      }
    }
  }
}
```

Field notes:
- `handle`: Required, max 195 chars, used as the entity `owner` reference
- `name`: Required, max 200 chars, display name
- `relationships.users`: Optional, add initial team members by user UUID

**Response (201):** Returns the full team object with `id`.

**Error:** `409` — team already exists (treat as success in idempotent flows).

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/team" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "team",
      "attributes": {
        "name": "My Team",
        "handle": "my-team",
        "description": "Team responsible for my-service"
      }
    }
  }'
```

### GET /api/v2/team — List Teams

**Query parameters:**

| Param | Type | Description |
|---|---|---|
| `page[number]` | int | Page number |
| `page[size]` | int | Results per page |
| `filter[keyword]` | string | Search by team name, handle, or member email |
| `filter[me]` | bool | Only teams current user belongs to |
| `sort` | string | Sort order (e.g., `name`, `-name`) |

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/team?filter[keyword]=my-team&page[size]=50" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### PATCH /api/v2/team/{team_id} — Update Team

**curl:**

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/team/${TEAM_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "team",
      "attributes": {
        "name": "Updated Team Name",
        "description": "Updated description"
      }
    }
  }'
```

### DELETE /api/v2/team/{team_id} — Delete Team

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/team/${TEAM_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Returns `204 No Content` on success.

---

## Error Response Shape

All errors follow the JSON:API format:

```json
{
  "errors": [
    {
      "status": "400",
      "title": "Bad Request",
      "detail": "owner team 'nonexistent-team' does not exist"
    }
  ]
}
```

Common error patterns:
- **400** — Invalid schema, missing required fields, or owner team does not exist
- **403** — API key or app key is invalid or lacks permissions
- **404** — Entity or team UUID not found (for DELETE/PATCH)
- **409** — Resource already exists (teams only; treat as success for idempotent flows)
- **429** — Rate limited; back off and retry with exponential backoff

---

## Endpoints Summary

| Method | Endpoint | Status Codes | Purpose |
|---|---|---|---|
| `POST` | `/api/v2/catalog/entity` | 200, 201, 202, 400, 403, 429 | Upsert entity |
| `GET` | `/api/v2/catalog/entity` | 200, 403, 429 | List entities (paginated) |
| `DELETE` | `/api/v2/catalog/entity/{id}` | 204, 400, 403, 404, 429 | Delete entity |
| `POST` | `/api/v2/team` | 201, 403, 409, 429 | Create team |
| `GET` | `/api/v2/team` | 200, 403, 429 | List teams (paginated) |
| `PATCH` | `/api/v2/team/{id}` | 200, 403, 404, 429 | Update team |
| `DELETE` | `/api/v2/team/{id}` | 204, 403, 404, 429 | Delete team |
