---
name: software-catalog
description: >
  Registers entities in the Datadog Software Catalog via v3 API.
  Supports all 8 entity kinds (service, system, datastore, queue,
  api, frontend, library, custom), team creation, dependency mapping,
  and batch upsert. Teams-first, then entities orchestration.
  Trigger phrases: "software catalog", "service catalog", "register service",
  "catalog entity", "v3 schema", "create team datadog",
  "dependsOn", "componentOf", "batch register services".
  Do NOT use for dashboards, monitors, App Builder apps, or workflow
  automations — this skill only handles catalog entity and team registration.
metadata:
  author: hackathon-team-3
  tags: [datadog, software-catalog, teams]
  category: observability
---

# Software Catalog Skill

## Overview

The Datadog Software Catalog gives every service a single source of truth: owner team, contacts, repo links, lifecycle state, dependency graph, and code location.

Key facts:
- Endpoint: `POST /api/v2/catalog/entity` — behaves as **upsert** (200, 201, 202 all mean success)
- Schema: **apiVersion: v3** with kinds: `service`, `datastore`, `queue`, `system`, `api`, `frontend`, `library`, `custom`
- Teams referenced in `metadata.owner` must exist before entity registration

### Dependency Diagram

```
software-catalog (standalone)
       |
       +---> dashboards (link services to SLO/monitor widgets)
       +---> app-builder (surface catalog data in internal tools)
```

No prerequisites from other skills.

---

## Doc Fetch URLs

Before executing, fetch current API and product documentation:

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/software-catalog.md` |
| Entity model | `https://docs.datadoghq.com/software_catalog/entity_model.md` |
| Setup guide | `https://docs.datadoghq.com/software_catalog/set_up.md` |
| Terraform provider | TF MCP → `datadog_software_catalog` |
| Official schemas | `https://github.com/DataDog/schema/tree/main/software-catalog` |

---

## Output Format Selection

Read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` (uses v2.2 schema with kebab-case) |
| `shell` | Claude executes `curl` commands directly via Bash tool (uses v3 JSON with camelCase) |

**Note:** Terraform uses v2.2 schema (`service-url`); shell/API uses v3 (`serviceURL`). Both populate the same catalog.

---

## When to Use

- Bootstrapping a new Datadog org with service catalog entries
- Programmatically registering services in CI/Lambda/GameDay setup
- Mapping service dependencies (`dependsOn`, `componentOf`)
- Registering non-service entities: databases, queues, systems, APIs, frontends, libraries
- Creating Datadog teams before entity registration

---

## Prerequisites

| Requirement | Details |
|---|---|
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Datadog app key — no special scopes required for catalog writes |
| Teams | Must exist in Datadog before entities reference them as `owner` |

---

## Core Workflow: Teams First, Then Entities

All API calls require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### Step 1 — Create teams

`POST /api/v2/team` for each unique team handle. This is idempotent: 409 = already exists = success.

### Step 2 — Register entities

`POST /api/v2/catalog/entity` with v3 JSON body for each entity. This is an upsert: 200, 201, 202 all mean success.

v3 entity structure:
```json
{
  "apiVersion": "v3",
  "kind": "service",
  "metadata": {
    "name": "my-service",
    "owner": "backend-team",
    "description": "Service description",
    "contacts": [{"name": "Support", "type": "email", "contact": "team@example.com"}],
    "links": [{"name": "Repo", "type": "repo", "url": "https://github.com/org/repo"}],
    "tags": ["env:production"]
  },
  "spec": {
    "lifecycle": "production",
    "tier": "High",
    "dependsOn": ["datastore:postgres-main", "queue:email-queue"],
    "componentOf": ["system:platform"]
  },
  "integrations": {
    "pagerduty": {"serviceURL": "https://..."}
  },
  "datadog": {
    "codeLocations": [{"repositoryURL": "https://github.com/org/repo", "paths": ["services/my-service/**"]}]
  },
  "extensions": {"cost-center": "eng-1234"}
}
```

---

## Entity Kinds

| Kind | Description | Key Spec Fields |
|---|---|---|
| `service` | Backend service or microservice | `type`, `lifecycle`, `tier`, `languages`, `dependsOn`, `componentOf` |
| `system` | Container grouping entities | `components` list |
| `datastore` | Database or data store | `type` (postgres, redis, etc.), `dependencyOf` |
| `queue` | Message queue or event stream | `type` (kafka, sqs, etc.), `dependencyOf` |
| `api` | API definition | `type` (openapi, grpc), `interface`, `implementedBy` |
| `frontend` | Web or mobile application | `type` (web-app, mobile-app), `languages`, `dependsOn` |
| `library` | Shared library, SDK, package | `type` (library, sdk), `languages`, `dependencyOf` |
| `custom` | Any entity not covered above | Free-form `spec` fields |

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **camelCase in v3** | v3 integrations use `serviceURL` (camelCase); v2.2 uses `service-url` (kebab-case) — mixing causes validation errors |
| **Team handle case-sensitivity** | Handles are case-sensitive; wrong case causes "owner team does not exist" error |
| **Entity names must be kebab-case** | Lowercase, hyphens only, no spaces or uppercase |
| **Entity ref format** | `kind:name` (e.g., `service:my-service`, `datastore:postgres-main`) |
| **Relationship resolution is async** | References to non-existent entities don't error immediately — show as "unresolved" in UI |
| **Bidirectional relationships** | Datadog infers reverse direction automatically — `dependsOn` creates implicit `dependencyOf` |
| **Delete uses UUID, not ref** | `DELETE /api/v2/catalog/entity/{entity_id}` uses UUID from response, NOT entity ref |
| **Code locations** | v3 uses `datadog.codeLocations[]` (first-class field); the `code_location:<glob>` tag is legacy v2.x |
| **additionalOwners** | Enables multi-ownership: `metadata.additionalOwners[].type` can be `team` or `operator` |
| **Discovered vs user-defined** | Upserting a full v3 entity with same name as APM-discovered service enriches and converts it |
| **Namespace** | Optional, defaults to `"default"` — enables multi-tenant catalog in same org |

---

## Cross-Skill Notes

- **dashboards**: Filter monitor queries by `service:<name>`. The `metadata.name` is the entity ref.
- **workflow-automation**: Service names should match the `service` tag on metrics/traces for monitor-triggered workflows.
- **repo-analyzer**: Generates service list mapping to this skill's entity registration.

---

## JSON Examples

`examples/services.yaml` — sample service definitions (3 services with teams, dependencies, contacts) for reference when building entity payloads. Convert to v3 JSON for API submission.
