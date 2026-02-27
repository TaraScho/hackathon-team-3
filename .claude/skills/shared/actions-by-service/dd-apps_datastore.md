# Datadog Actions Datastore Actions
Bundle: `com.datadoghq.dd.apps_datastore` | 9 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eapps_datastore)

## com.datadoghq.dd.apps_datastore.bulkDeleteDatastoreItems
**Bulk delete datastore items** — Deletes multiple items from a datastore by their keys in a single operation.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | The ID of the datastore. |
  | itemKeys | array<string> | no | List of primary keys identifying items to delete from datastore. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The `DeleteAppsDatastoreItemResponseArray` `data`. |


## com.datadoghq.dd.apps_datastore.bulkPutDatastoreItem
**Bulk put items** — Put multiple items in the datastore.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | items | array<object> | yes | An array of up to 5000 items to store in the datastore. Each item is a map with a primary key and additional attributes as key-value pairs. |
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | overwrite | boolean | no | Determines whether an existing item with the same primary key should be overwritten. If true, the item will be replaced. If false, the request fails in case of a conflict. |


## com.datadoghq.dd.apps_datastore.createDatastore
**Create datastore** — Creates a new datastore.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | description | string | no | A human-readable description about the datastore. |
  | name | string | yes | The display name for the new datastore. |
  | org_access | string | no | The organization access level for the datastore. |
  | primary_column_name | string | yes | The name of the primary key column for this datastore. |
  | primary_key_generation_strategy | string | no | Can be set to `uuid` to automatically generate primary keys when new items are added. |
  | id | string | no | Optional ID for the new datastore. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The newly created datastore's data. |


## com.datadoghq.dd.apps_datastore.deleteDatastoreItem
**Delete item** — Delete an item from the datastore.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | key | string | yes | The primary key of the item. |


## com.datadoghq.dd.apps_datastore.getDatastoreItem
**Get item** — Get an item from the datastore.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | key | string | yes | The primary key of the item. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object | The JSON representation of the item. |


## com.datadoghq.dd.apps_datastore.getItemChangeRecords
**Get datastore item change records** — Retrieves all item change records in a datastore for a given change ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | changeId | string | yes | The ID of the item change record batch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | The ID of the item change batch |
  | datastore_id | string | The ID of the datastore the changes correspond to |
  | primary_column_name | string | The primary column name of the datastore |
  | items | array<object> | The items impacted by the change associated with the change ID |
  | is_truncated | boolean | Whether items in the response were truncated to remain under the HTTP response payload size limit |


## com.datadoghq.dd.apps_datastore.listDatastoreItems
**List items** — List items in a datastore.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | query | string | no | The search query uses the [logs search syntax](https://docs.datadoghq.com/logs/explorer/search_syntax): - `attribute:value` format (defaults to primary key if attribute is omitted) - Boolean operat... |
  | sort | string | no | The sort order of the items. The `-` prefix means descending direction. The default is `primaryKey`. |
  | offset | number | no | The offset of items to start from. The default is `0`. |
  | limit | number | no | The maximum number of items in the response. Must be between 1 and 5000 (inclusive). The default is `5000`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | items | array<object> | The items in the datastore. |


## com.datadoghq.dd.apps_datastore.putDatastoreItem
**Put item** — Put an item in the datastore.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | item | object | yes | A JSON representation of an item to be stored. Only the primary key is required; additional attributes can be included as optional key-value pairs. |
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | overwrite | boolean | no | Determines whether an existing item with the same primary key should be overwritten. If true, the item will be replaced. If false, the request fails in case of a conflict. |


## com.datadoghq.dd.apps_datastore.updateDatastoreItem
**Update item** — Update an item in the datastore.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | datastoreId | string | yes | A UUID representing the datastore ID. |
  | key | string | yes | The primary key of the item. |
  | update | object | yes | A map of field paths to be updated or created, along with their new values. Field Path Rules: - Use dot notation for nested JSON fields: `jsonField.nestedField.name` - Use bracket notation for arra... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object | The JSON representation of the item. |

