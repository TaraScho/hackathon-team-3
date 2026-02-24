# Advanced Features

Advanced configuration, import/sync integrations, auto-discovery, entity relationships, custom entity types, and migration guidance for the Datadog Software Catalog.

---

## GitHub Team Sync

Datadog can automatically sync team definitions from GitHub Organizations to Datadog Teams.

### Setup

1. Install the Datadog GitHub App integration for your GitHub Organization.
2. In Datadog, navigate to **Organization Settings > Teams > Team Provisioning**.
3. Enable **GitHub Teams Sync** and select the GitHub Organization.
4. Map GitHub teams to Datadog teams. The sync runs every hour.

### Behavior

- New GitHub teams are created in Datadog automatically.
- Team membership is mirrored: adding/removing a user in GitHub updates Datadog.
- The Datadog team `handle` is derived from the GitHub team slug (lowercase, hyphenated).
- Manual edits to synced teams in Datadog are overwritten on the next sync cycle.
- Disabling the sync preserves existing Datadog teams but stops further updates.

### Catalog Impact

- Synced team handles can be used directly in entity `metadata.owner` fields.
- If a GitHub team is deleted, the corresponding Datadog team is removed, which may orphan catalog entities that reference it as `owner`.

---

## Backstage Import

Datadog can import entity definitions from a Backstage catalog.

### How It Works

1. Backstage uses `catalog-info.yaml` files with `apiVersion: backstage.io/v1alpha1`.
2. Datadog provides a **Backstage import endpoint** that accepts Backstage-format YAML and translates it to v3 internally.
3. Use `POST /api/v2/catalog/entity` with the raw Backstage YAML as the body (Content-Type: `application/yaml`).

### Key Mapping

| Backstage Field | Datadog v3 Equivalent |
|---|---|
| `metadata.name` | `metadata.name` |
| `metadata.description` | `metadata.description` |
| `spec.owner` | `metadata.owner` |
| `spec.type` | `spec.type` |
| `spec.lifecycle` | `spec.lifecycle` |
| `spec.system` | `spec.componentOf` |
| `spec.dependsOn` | `spec.dependsOn` |
| `metadata.annotations["pagerduty.com/service-id"]` | `integrations.pagerduty.serviceURL` |

### Limitations

- Backstage `Component`, `API`, and `System` kinds are supported. Other Backstage kinds (Resource, Domain, Group) are mapped on a best-effort basis.
- Custom Backstage annotations do not automatically transfer to Datadog `extensions`.
- Team references must still resolve to existing Datadog teams.

---

## ServiceNow Import

Datadog integrates with ServiceNow CMDB to import service definitions.

### Setup

1. Configure the Datadog-ServiceNow integration tile with your ServiceNow instance URL and credentials.
2. Enable **CMDB Sync** in the integration settings.
3. Map ServiceNow CI types to Datadog entity kinds.

### Behavior

- ServiceNow Configuration Items (CIs) of type `cmdb_ci_service` are synced to Datadog as `service` entities.
- The sync runs on a configurable schedule (default: every 6 hours).
- CI relationships in ServiceNow (e.g., "depends on", "used by") are translated to `dependsOn`/`dependencyOf` in Datadog.
- Ownership is mapped from the ServiceNow `assignment_group` to a Datadog team handle.
- Entities imported from ServiceNow are tagged with `source:servicenow` and `cmdb_ci_id:<id>`.

---

## APM/USM Auto-Discovery

Datadog APM (Application Performance Monitoring) and USM (Universal Service Monitoring) can automatically discover services and register them in the catalog.

### How It Works

- APM agents report services based on instrumented traces. Each unique `service` tag value becomes a discovered entity.
- USM detects services at the network level (eBPF-based) without code changes. It identifies services by their network endpoints.
- Discovered services appear in the catalog with `source: auto-discovery` and limited metadata.

### Enrichment Workflow

1. Discovered services start as "unregistered" in the catalog with minimal metadata (name, discovered tags).
2. Use the `GET /api/v2/catalog/entity?includeDiscovered=true` query parameter to list discovered-but-unregistered services.
3. Enrich by POSTing a full v3 entity definition with the same `metadata.name`. The upsert overwrites the auto-discovered stub.
4. Once enriched, the entity shows `source: user-defined` and retains the APM/USM telemetry linkage.

### Best Practice

Run a periodic script that lists discovered entities, compares against your `ALL_SERVICES` manifest, and registers any missing entities with full metadata. This ensures new services deployed via APM/USM are automatically enriched.

---

## Entity Relationships

v3 supports several relationship types to model service topology:

### Relationship Fields

| Field | Used In | Direction | Meaning |
|---|---|---|---|
| `spec.dependsOn` | service, frontend, custom | Outbound | "This entity depends on..." |
| `spec.dependencyOf` | datastore, queue, library | Inbound | "These entities depend on me" |
| `spec.componentOf` | service, frontend, datastore, queue | Upward | "I belong to this system" |
| `spec.components` | system | Downward | "These entities belong to me" |
| `spec.implementedBy` | api | Link | "This API is implemented by these services" |

### Entity Ref Format

All relationship fields use entity refs in the format `kind:name`:
- `service:order-service`
- `datastore:postgres-main`
- `queue:payment-events`
- `system:commerce-platform`
- `api:orders-api`
- `frontend:storefront-web`
- `library:auth-sdk`

### Relationship Resolution

- Relationships are resolved asynchronously. A `dependsOn` reference to a non-existent entity will not cause an error, but the relationship will show as "unresolved" in the UI.
- Register all entity kinds (datastores, queues, systems) before or alongside services to ensure complete relationship graphs.
- Bidirectional relationships (e.g., service A `dependsOn` datastore B, and datastore B lists `dependencyOf` service A) are not required but improve the topology view. Datadog infers the reverse direction automatically.

---

## Custom Entity Types via API

The `custom` kind enables registering any entity type not covered by the 7 built-in kinds (service, system, datastore, queue, api, frontend, library).

### Use Cases

- ML models with framework, version, and training metadata
- Infrastructure components (load balancers, CDN configs)
- Business capabilities or product areas
- Data pipelines or ETL jobs

### Registration

Custom entities use the same `POST /api/v2/catalog/entity` endpoint. The `kind` field is set to `custom`, and any fields under `spec` are free-form.

```yaml
apiVersion: v3
kind: custom
metadata:
  name: fraud-model-v2
  owner: ml-team
spec:
  type: ml-model          # Arbitrary type string for your custom kind
  framework: pytorch
  version: "2.1.0"
```

### Querying

Filter custom entities: `GET /api/v2/catalog/entity?filter[kind]=custom`.

Custom entities participate in the same relationship graph as built-in entities. They can use `dependsOn`, `componentOf`, and other relationship fields.

---

## v2.2 to v3 Migration

### Key Differences

| Aspect | v2.2 (YAML / Terraform) | v3 (JSON / API) |
|---|---|---|
| Schema version | `schema-version: "v2.2"` | `apiVersion: "v3"` |
| Entity kinds | service only | service, system, datastore, queue, api, frontend, library, custom |
| PagerDuty key | `integrations.pagerduty.service-url` | `integrations.pagerduty.serviceURL` |
| OpsGenie key | `integrations.opsgenie.service-url` | `integrations.opsgenie.serviceURL` |
| Code location | `tags: ["code_location:glob"]` | `datadog.codeLocations[].paths` |
| Service grouping | `application` field | `spec.componentOf` |
| Dependencies | Not available | `spec.dependsOn` / `spec.dependencyOf` |
| Additional owners | Not available | `metadata.additionalOwners` |
| Namespace | Not available | `metadata.namespace` |
| Inheritance | Not available | `metadata.inheritFrom` |

### Migration Steps

1. **Export existing v2.2 entities**: Use `GET /api/v2/catalog/entity?filter[kind]=service` to list all current entities.
2. **Transform schema**: Map v2.2 fields to v3 equivalents (see table above). Pay special attention to kebab-case to camelCase changes in integrations.
3. **Add new v3 features**: Enrich with `dependsOn`, `componentOf`, `additionalOwners`, `datadog.codeLocations`, and `namespace` as needed.
4. **Register non-service entities**: v3 supports datastores, queues, systems, and APIs. Register these to build a complete topology.
5. **Upsert via API**: POST each v3 entity to `POST /api/v2/catalog/entity`. The upsert overwrites existing v2.2 definitions.
6. **Verify**: List entities and confirm the schema shows `apiVersion: v3`.

### Compatibility

- v2.2 and v3 entities coexist in the same catalog. You do not need to migrate all entities at once.
- Terraform `datadog_service_definition` continues to use v2.2 schema. You can manage some entities via Terraform (v2.2) and others via API (v3).
- The catalog UI displays both schema versions identically.

---

## Version Compatibility Table

| Feature | v2.1 | v2.2 | v3 |
|---|---|---|---|
| Service entities | Yes | Yes | Yes |
| System entities | No | No | Yes |
| Datastore entities | No | No | Yes |
| Queue entities | No | No | Yes |
| API entities | No | No | Yes |
| Frontend entities | No | No | Yes |
| Library entities | No | No | Yes |
| Custom entities | No | No | Yes |
| `dependsOn` relationships | No | No | Yes |
| `componentOf` grouping | No | No | Yes |
| `additionalOwners` | No | No | Yes |
| `metadata.namespace` | No | No | Yes |
| `metadata.inheritFrom` | No | No | Yes |
| `datadog.codeLocations` | No | No | Yes |
| `datadog.performanceData` | No | No | Yes |
| PagerDuty/OpsGenie integration | Yes | Yes | Yes |
| Terraform support | Limited | Yes (`datadog_service_definition`) | API only |
| Backstage import | No | No | Yes |
| `application` grouping | No | Yes | Replaced by `componentOf` |
| `code_location` tag | Yes | Yes | Deprecated (use `datadog.codeLocations`) |
