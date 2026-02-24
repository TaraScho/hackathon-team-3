---
name: software-catalog
description: >
  Registers entities in the Datadog Software Catalog via v3 API, Python, or
  Terraform. Supports all 8 entity kinds (service, system, datastore, queue,
  api, frontend, library, custom), team creation, dependency mapping, and
  batch upsert. Teams-first, then entities orchestration.
  Trigger phrases: "software catalog", "service catalog", "register service",
  "catalog entity", "v3 schema", "ALL_SERVICES", "create team datadog",
  "dependsOn", "componentOf", "batch register services".
  Do NOT use for dashboards, monitors, App Builder apps, or workflow
  automations — this skill only handles catalog entity and team registration.
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars.
  No special app key scopes needed for catalog writes.
metadata:
  author: hackathon-team-3
  version: 2.0.0
  tags: [datadog, software-catalog, teams, python, terraform]
  category: observability
---

# Service Catalog Skill

## Overview

The Datadog Software Catalog gives every service a single source of truth: owner team, contacts, repo links, lifecycle state, dependency graph, and code location. Registering entities programmatically ensures consistency across orgs and makes catalog population repeatable in GameDay setups, CI/CD pipelines, and IaC provisioning runs.

Key facts:
- Endpoint: `POST /api/v2/catalog/entity` — behaves as an **upsert** (200, 201, or 202 all mean success)
- Schema: **apiVersion: v3** with kinds: `service`, `datastore`, `queue`, `system`, `api`, `frontend`, `library`, `custom`
- Teams referenced in `metadata.owner` must exist in Datadog before the entity is registered
- **v3 code location**: use `datadog.codeLocations` (first-class field); the `code_location:<glob>` tag works but is a legacy v2.x pattern
- `spec.dependsOn` declares outbound dependencies using entity refs (`service:name`, `queue:name`, `datastore:name`)
- `extensions` is a free-form object for custom metadata; no Datadog features are affected by it
- `tier` is a **free-form string** (no enforced enum); common values are `"High"`, `"critical"`, `"1"`
- v3 integrations use **camelCase** keys: `serviceURL` (not `service-url` like v2.2)
- `metadata.additionalOwners` enables multi-ownership: declare secondary teams with `type` (team/operator) and optional `managed` flag

### Official Schema Source

All schemas are at: `https://github.com/DataDog/schema/tree/main/software-catalog`

### Dependency Diagram

```
software-catalog (standalone)
       |
       +---> dashboards (link services to SLO/monitor widgets)
       +---> app-builder (surface service catalog data in internal tools)
```

This skill has **no prerequisites** from other skills in this repo.

---

## When to Use

- Bootstrapping a new Datadog org and need services visible in the Software Catalog
- Programmatically registering services from a list (GameDay setup, onboarding scripts, CI)
- Mapping service dependencies (`dependsOn`, `componentOf`) to build a system topology
- Registering non-service entities: databases, queues, systems, APIs, frontends, libraries, or custom types
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

## Required and Optional Fields Quick Reference

| Field | Required | Notes |
|---|---|---|
| `metadata.name` | Yes | Kebab-case, unique within kind+namespace |
| `metadata.owner` | Yes | Must be an existing Datadog team handle |
| `metadata.description` | No | Recommended for catalog discoverability |
| `metadata.contacts` | No | Email, Slack, or Microsoft Teams channels |
| `metadata.links` | No | Repo, runbook, doc, dashboard, or other URLs |
| `metadata.tags` | No | Datadog tags (e.g., `env:production`) |
| `metadata.namespace` | No | Multi-tenant namespace (default: "default") |
| `metadata.inheritFrom` | No | Inherit fields from another entity ref |
| `metadata.additionalOwners` | No | Secondary ownership (type: team/operator) |
| `spec.lifecycle` | No | production, staging, experimental, deprecated, sandbox |
| `spec.tier` | No | Free-form string |
| `spec.type` | No | Kind-dependent (e.g., web, grpc, postgres, kafka) |
| `spec.dependsOn` | No | Outbound dependency entity refs |
| `spec.componentOf` | No | Parent system entity refs |
| `integrations` | No | PagerDuty / OpsGenie with camelCase keys |
| `datadog.codeLocations` | No | Source code links (repositoryURL + glob paths) |
| `extensions` | No | Free-form custom metadata |

---

## Entity Kinds Quick List

| Kind | Description | Key Spec Fields |
|---|---|---|
| `service` | Backend service or microservice | `type`, `lifecycle`, `tier`, `languages`, `dependsOn`, `componentOf` |
| `system` | Container grouping related entities | `components` list |
| `datastore` | Database or data store | `type` (postgres, redis, etc.), `dependencyOf` |
| `queue` | Message queue or event stream | `type` (kafka, sqs, etc.), `dependencyOf` |
| `api` | API definition | `type` (openapi, grpc), `interface`, `implementedBy` |
| `frontend` | Web or mobile application | `type` (web-app, mobile-app), `languages`, `dependsOn` |
| `library` | Shared library, SDK, or package | `type` (library, sdk), `languages`, `dependencyOf` |
| `custom` | Any entity not covered above | Free-form `spec` fields |

All kinds share the same `metadata` structure. Register all kinds via the same `POST /api/v2/catalog/entity` endpoint.

---

## Multi-Ownership Pattern

v3 supports declaring additional owners beyond the primary `metadata.owner`:

```yaml
metadata:
  owner: commerce-team          # Primary owner (required)
  additionalOwners:
    - name: sre-team
      type: operator            # team | operator
      managed: true             # Optional: indicates managed responsibility, not ownership
    - name: platform-team
      type: team
```

This is useful for services jointly owned by multiple teams or where an SRE team provides operational support without primary ownership.

---

## v3 vs v2.2 Key Differences

| Field | v3 JSON (API) | v2.2 YAML (Terraform) |
|---|---|---|
| PagerDuty URL key | `integrations.pagerduty.serviceURL` | `integrations.pagerduty.service-url` |
| OpsGenie URL key | `integrations.opsgenie.serviceURL` | `integrations.opsgenie.service-url` |
| Code location | `datadog.codeLocations[].paths` | `tags: ["code_location:glob"]` |
| Service grouping | `spec.componentOf` | `application` field |
| Dependency graph | `spec.dependsOn` | not available |
| Entity kinds | 8 kinds (service, system, datastore, queue, api, frontend, library, custom) | service only |
| Additional owners | `metadata.additionalOwners` | not available |

---

## Terraform Pattern (v2.2)

Use `datadog_service_definition` with `schema-version: "v2.2"`. Terraform uses the v2.2 YAML-style schema; `POST /api/v2/catalog/entity` uses v3 JSON — both populate the same catalog.

**v2.2 integrations use kebab-case** (`service-url`) unlike v3 (camelCase `serviceURL`).

See `examples/terraform/service-definitions.tf` for the full pattern including single-resource and `for_each` bulk examples.

---

## Endpoint Summary

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/v2/catalog/entity` | Upsert entity (200/201/202 = success) |
| `GET` | `/api/v2/catalog/entity` | List entities (paginated, filterable) |
| `DELETE` | `/api/v2/catalog/entity/{id}` | Delete entity by UUID |
| `POST` | `/api/v2/team` | Create team (409 = already exists) |
| `GET` | `/api/v2/team` | List teams (paginated, filterable) |
| `PATCH` | `/api/v2/team/{id}` | Update team |
| `DELETE` | `/api/v2/team/{id}` | Delete team |

For full API contracts, request/response schemas, query parameters, curl examples, and error handling, see `references/api-reference.md`.

---

## Cross-Skill Notes

- **dashboards**: Filter monitor queries and SLO widgets by service name. The `metadata.name` is the entity ref used in `service:<name>` filters.
- **app-builder**: Build internal tools to surface catalog data or let engineers update service ownership inline.
- **workflow-automation**: Service names in catalog should match the `service` tag on metrics and traces to enable monitor-triggered workflows.
- **repo-analyzer**: The repo-analyzer skill generates a service list that maps directly to the `ALL_SERVICES` pattern from this skill.

---

## Additional Resources

Detailed reference documentation is available in the `references/` directory:

- **`references/api-reference.md`** — Full API contracts for all catalog and team endpoints. Includes request/response schemas, query parameters, curl examples, status codes, and error response shapes.
- **`references/v3-schema.md`** — Complete v3 entity schema for all 8 kinds. Full metadata structure including namespace, inheritFrom, additionalOwners. Spec fields per kind. Integrations, datadog block, extensions. Full YAML examples for every entity kind.
- **`references/advanced-features.md`** — GitHub team sync, Backstage/ServiceNow import, APM/USM auto-discovery, entity relationships, custom entity types, v2.2-to-v3 migration guide, and version compatibility table.

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
