# Datadog Software Catalog Actions
Bundle: `com.datadoghq.dd.softwarecatalog` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Esoftwarecatalog)

## com.datadoghq.dd.softwarecatalog.deleteCatalogEntity
**Delete a single entity definition** — Delete a single entity in Software Catalog.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | entity_id | string | yes | UUID or Entity Ref. |


## com.datadoghq.dd.softwarecatalog.listCatalogEntity
**List all entity definitions** — Get a list of entities from Software Catalog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |
  | page_limit | number | no | Maximum number of entities in the response. |
  | filter_id | string | no | Filter entities by UUID. |
  | filter_ref | string | no | Filter entities by reference. |
  | filter_name | string | no | Filter entities by name. |
  | filter_kind | string | no | Filter entities by kind. |
  | filter_owner | string | no | Filter entities by owner. |
  | filter_relation_type | string | no | Filter entities by relation type. |
  | filter_exclude_snapshot | string | no | Filter entities by excluding snapshotted entities. |
  | include | string | no | Include relationship data. |
  | includeDiscovered | boolean | no | If true, includes discovered services from APM and USM that do not have entity definitions. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of entity data. |
  | included | array<object> | List entity response included. |
  | links | object | List entity response links. |
  | meta | object | Entity metadata. |


## com.datadoghq.dd.softwarecatalog.upsertCatalogEntity
**Create or update an entity definition** — Create or update entities in Software Catalog.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | data | any | yes | The [JSON or YAML definition](https://docs.datadoghq.com/software_catalog/service_definitions/v3-0/) of the entity to be created or updated. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of entity data. |
  | included | array<object> | Upsert entity response included. |
  | meta | object | Entity metadata. |

