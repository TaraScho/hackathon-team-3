---
name: software-catalog
description: >
  Creates and populates the Datadog Software Catalog (Service Catalog) with service
  entity definitions — via the v3 API schema, Python/requests, or Terraform. Use
  this skill when you need to: register services in the Datadog Software Catalog,
  define service metadata (owner, description, contacts, links, code location),
  map service dependencies with dependsOn/componentOf, register non-service entities
  (datastore, queue, system, api), create Datadog teams before registering services,
  batch-register multiple services from a data definitions list, use the v3 catalog
  entity schema (apiVersion: v3, kind: service), upsert catalog entries idempotently,
  or write Terraform for datadog_service_definition. Trigger phrases: "software catalog",
  "service catalog", "register service", "catalog entity", "service definition",
  "service metadata", "POST /api/v2/catalog/entity", "v3 schema service", "ALL_SERVICES",
  "create team datadog", "service owner team", "service contact", "code_location tag",
  "batch register services", "dependsOn", "componentOf", "datastore entity",
  "system entity", "service dependencies".
  Do NOT use for creating dashboards, monitors, App Builder apps, or workflow
  automations — this skill only handles catalog entity and team registration.
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars.
  No special app key scopes needed for catalog writes.
metadata:
  author: hackathon-team-3
  version: 1.2.0
  tags: [datadog, software-catalog, software-catalog, teams, python, terraform]
  category: observability
---

# Service Catalog Skill

## Overview

The Datadog Software Catalog gives every service a single source of truth: owner team, contacts, repo links, lifecycle state, dependency graph, and code location. Registering entities programmatically ensures consistency across orgs and makes catalog population repeatable in GameDay setups, CI/CD pipelines, and IaC provisioning runs.

Key facts:
- Endpoint: `POST /api/v2/catalog/entity` — behaves as an **upsert** (200, 201, or 202 all mean success)
- Schema: **apiVersion: v3** with kinds: `service`, `datastore`, `queue`, `system`, `api`
- Teams referenced in `metadata.owner` must exist in Datadog before the entity is registered
- **v3 code location**: use `datadog.codeLocations` (first-class field); the `code_location:<glob>` tag works but is a legacy v2.x pattern
- `spec.dependsOn` declares outbound dependencies using entity refs (`service:name`, `queue:name`, `datastore:name`)
- `extensions` is a free-form object for custom metadata; no Datadog features are affected by it
- `tier` is a **free-form string** (no enforced enum); common values are `"High"`, `"critical"`, `"1"`
- v3 integrations use **camelCase** keys: `serviceURL` (not `service-url` like v2.2)

### Official Schema Source

All schemas are at: `https://github.com/DataDog/schema/tree/main/software-catalog`

### Dependency Diagram

```
software-catalog (standalone)
       │
       ├──► dashboards (link services to SLO/monitor widgets)
       └──► app-builder (surface service catalog data in internal tools)
```

This skill has **no prerequisites** from other skills in this repo.

---

## When to Use

- Bootstrapping a new Datadog org and need services visible in the Software Catalog
- Programmatically registering services from a list (GameDay setup, onboarding scripts, CI)
- Mapping service dependencies (`dependsOn`, `componentOf`) to build a system topology
- Registering non-service entities: databases, queues, systems, APIs
- Creating Datadog teams before service entity registration
- Writing Terraform to own service catalog state as code
- Embedding catalog registration in a Lambda setup function

---

## Prerequisites

| Requirement | Details |
|---|---|
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Datadog app key — no special scopes required for catalog writes |
| Python dependencies | `requests` (no boto3 needed unless running in Lambda) |
| Teams | Must exist in Datadog before service entities reference them as `owner` |

---

## Core Workflow

The registration follows a strict two-pass orchestration:

1. **Define services** as a Python list of dicts (`ALL_SERVICES`) — see `examples/python/service_data.py`
2. **Create teams first** (idempotent — 409 = already exists = success) — see `examples/python/service_catalog_helpers.py:create_team()`
3. **Register service entities** (upsert — 200/201/202 all = success) — see `examples/python/service_catalog_helpers.py:create_service_entity()`
4. **Batch orchestration** ties it together — see `examples/python/register_all_services.py`

**Required service fields:** `name`, `description`, `owner`, `repo_url`, `contact_name`, `contact_email`
**Optional fields:** `code_location`, `additional_links`, `depends_on`, `component_of`, `extensions`

Key functions in `examples/python/service_catalog_helpers.py`:
- `build_headers()` — Construct Datadog API auth headers
- `create_team()` — Idempotent team creation (409 = already exists = success)
- `create_service_entity()` — Upsert a v3 catalog entity
- `DatadogResponse` — Wrapper dataclass for consistent return values

---

## API Reference

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

### POST /api/v2/catalog/entity — Upsert entity

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

### GET /api/v2/catalog/entity — List entities

**Query parameters:**
| Param | Type | Description |
|---|---|---|
| `page[offset]` | int | Offset for pagination |
| `page[limit]` | int | Max results (default 100) |
| `filter[id]` | string | Filter by entity UUID |
| `filter[ref]` | string | Filter by entity ref (e.g., `service:my-service`) |
| `filter[name]` | string | Filter by entity name |
| `filter[kind]` | string | Filter by kind (`service`, `datastore`, `queue`, `system`, `api`) |
| `filter[owner]` | string | Filter by owner team handle |
| `include` | string | Include related resources |
| `includeDiscovered` | bool | Include APM/USM discovered services (default false) |

**curl:**
```bash
curl -X GET "https://api.datadoghq.com/api/v2/catalog/entity?filter[kind]=service&page[limit]=50" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### DELETE /api/v2/catalog/entity/{entity_id} — Delete entity

The `entity_id` is the UUID returned in the entity list, not the entity ref.

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/catalog/entity/${ENTITY_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Returns `204 No Content` on success.

### POST /api/v2/team — Create a team

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
- `handle`: Required, max 195 chars, used as the entity owner reference
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

### GET /api/v2/team — List teams

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

### PATCH /api/v2/team/{team_id} — Update a team

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

### DELETE /api/v2/team/{team_id} — Delete a team

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/team/${TEAM_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Error response shape

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

### Endpoints summary

| Method | Endpoint | Status Codes | Purpose |
|---|---|---|---|
| `POST` | `/api/v2/catalog/entity` | 200, 201, 202, 400, 403, 429 | Upsert entity |
| `GET` | `/api/v2/catalog/entity` | 200, 403, 429 | List entities (paginated) |
| `DELETE` | `/api/v2/catalog/entity/{id}` | 204, 400, 403, 404, 429 | Delete entity |
| `POST` | `/api/v2/team` | 201, 403, 409, 429 | Create team |
| `GET` | `/api/v2/team` | 200, 403, 429 | List teams (paginated) |
| `PATCH` | `/api/v2/team/{id}` | 200, 403, 404, 429 | Update team |
| `DELETE` | `/api/v2/team/{id}` | 204, 403, 404, 429 | Delete team |

---

## v3 Entity Schema Reference

Full reference derived from official schemas at `github.com/DataDog/schema/tree/main/software-catalog/v3`.

```yaml
apiVersion: v3
kind: service          # service | datastore | queue | system | api
metadata:
  name: my-service     # required; kebab-case; used as entity ref
  displayName: My Service
  owner: my-team       # required; Datadog team handle (case-sensitive)
  description: "..."
  contacts:
    - type: email                                     # email | slack | microsoft-teams
      name: "Support inbox"
      contact: "support@example.com"
  links:
    - name: Repository
      type: repo        # runbook | doc | repo | dashboard | other
      url: "https://github.com/my-org/my-repo"
  tags:
    - "env:production"
  additionalOwners:
    - name: sre-team
      type: team

spec:
  lifecycle: production  # production | staging | experimental | deprecated | sandbox
  tier: "High"           # free-form string; no enforced enum
  type: web              # service: web | grpc | http | rest | graphql
  languages:
    - python
  dependsOn:             # outbound dependencies — entity refs
    - service:auth-service
    - datastore:postgres-main
    - queue:payment-queue
  componentOf:
    - system:techstories-platform

integrations:
  pagerduty:
    serviceURL: "https://my-org.pagerduty.com/service-directory/P123"  # camelCase in v3!
  opsgenie:
    serviceURL: "https://my-org.opsgenie.com/service/abc-123"          # camelCase in v3!
    region: US

datadog:
  codeLocations:         # v3 first-class code location (preferred over tag approach)
    - repositoryURL: "https://github.com/my-org/my-repo"
      paths:
        - "services/my_service/**"

extensions:              # free-form; no Datadog features affected
  cost-center: "eng-1234"
  compliance: "SOC2"
```

---

## Non-Service Entity Kinds

All v3 entity kinds share the same `metadata` shape. Their `spec` fields differ:

- **`datastore`** — `spec.type`: `redis`, `postgres`, `cassandra`, `mysql`; supports `dependencyOf` (reverse direction)
- **`queue`** — `spec.type`: `kafka`, `rabbitmq`, `sqs`; supports `dependencyOf`
- **`system`** — container for all related entities; uses `spec.components` list instead of `dependsOn`
- **`api`** — `spec.interface.fileRef` (URI to OpenAPI spec) or `spec.interface.definition` (inline); `spec.implementedBy` links to service(s)

Register non-service entities in the same batch loop using the same `POST /api/v2/catalog/entity` endpoint.

---

## Terraform Pattern (v2.2)

Use `datadog_service_definition` with `schema-version: "v2.2"`. Terraform uses the v2.2 YAML-style schema; `POST /api/v2/catalog/entity` uses v3 JSON — both populate the same catalog.

**v2.2 integrations use kebab-case** (`service-url`) unlike v3 (camelCase `serviceURL`).

See `examples/terraform/service-definitions.tf` for the full pattern including single-resource and `for_each` bulk examples.

### v3 vs v2.2 Key Differences

| Field | v3 JSON (API) | v2.2 YAML (Terraform) |
|---|---|---|
| PagerDuty URL key | `integrations.pagerduty.serviceURL` | `integrations.pagerduty.service-url` |
| OpsGenie URL key | `integrations.opsgenie.serviceURL` | `integrations.opsgenie.service-url` |
| Code location | `datadog.codeLocations[].paths` | `tags: ["code_location:glob"]` |
| Service grouping | `spec.componentOf` | `application` field |
| Dependency graph | `spec.dependsOn` | not available |

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `400` on `POST /api/v2/catalog/entity` | `owner` handle doesn't exist as a team | Create team first with `POST /api/v2/team` |
| `400` — "invalid entity ref" | `metadata.name` contains uppercase or spaces | Use kebab-case (`my-service`, not `My Service`) |
| `403` on catalog endpoint | `DD_APP_KEY` invalid or lacks write access | Catalog writes need no special scopes; verify the key itself is valid |
| Entity shows as unknown owner | Team handle in `owner` doesn't match exactly | Check `GET /api/v2/team`; handle is case-sensitive |
| Integration not appearing on entity | Used `service-url` (v2.2 kebab) in v3 JSON | v3 uses camelCase `serviceURL`; v2.2 uses kebab `service-url` — don't mix |
| `code_location` tag not surfacing properly | Using legacy tag approach in v3 entity | Use `datadog.codeLocations[].paths` in v3; tag approach is a v2.x fallback |
| `409` on `POST /api/v2/team` | Team already exists | Treat 409 as success; skip re-creation |
| `dependsOn` target not resolving | Referenced entity doesn't exist in catalog yet | Register all entity kinds (datastores, queues) before services that reference them |

---

## Cross-Skill Notes

- **dashboards**: Filter monitor queries and SLO widgets by service name. The `metadata.name` is the entity ref used in `service:<name>` filters.
- **app-builder**: Build internal tools to surface catalog data or let engineers update service ownership inline.
- **workflow-automation**: Service names in catalog should match the `service` tag on metrics and traces to enable monitor-triggered workflows.
- **repo-analyzer**: The repo-analyzer skill generates a service list that maps directly to the `ALL_SERVICES` pattern from this skill.

---

## Level 3 References

Bundled examples (in this skill directory):
- `examples/python/service_catalog_helpers.py` — `create_team()`, `create_service_entity()`, `DatadogResponse` dataclass, `build_headers()`
- `examples/python/service_data.py` — `ALL_SERVICES` list template, `get_unique_teams()`, `get_services_by_team()`
- `examples/python/register_all_services.py` — Batch orchestration script with Lambda integration pattern
- `examples/terraform/service-definitions.tf` — `datadog_service_definition` single and `for_each` bulk patterns

Official schema definitions (ground truth for field names, types, and enums):
- `https://github.com/DataDog/schema/tree/main/software-catalog/v3/` — v3 service, datastore, queue, system, api, entity, metadata, integrations schemas
- `https://github.com/DataDog/schema/blob/main/software-catalog/v2.2/schema.json` — v2.2 schema (used by Terraform `datadog_service_definition`)
