# Datadog RUM Retention Filters Actions
Bundle: `com.datadoghq.dd.rum.retentionfilters` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Erum%2Eretentionfilters)

## com.datadoghq.dd.rum.retentionfilters.createRetentionFilter
**Create retention filter** — Create a RUM retention filter for a RUM application.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |
  | enabled | boolean | no | Whether the retention filter is enabled. |
  | event_type | string | yes | The type of RUM events to filter on. |
  | name | string | yes | The name of a RUM retention filter. |
  | query | string | no | The query string for a RUM retention filter. |
  | sample_rate | number | yes | The sample rate for a RUM retention filter, between 0 and 100. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The RUM retention filter. |


## com.datadoghq.dd.rum.retentionfilters.deleteRetentionFilter
**Delete retention filter** — Delete a RUM retention filter for a RUM application.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |
  | rf_id | string | yes | Retention filter ID. |


## com.datadoghq.dd.rum.retentionfilters.getRetentionFilter
**Get retention filter** — Get a RUM retention filter for a RUM application.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |
  | rf_id | string | yes | Retention filter ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The RUM retention filter. |


## com.datadoghq.dd.rum.retentionfilters.listRetentionFilters
**List retention filters** — Get the list of RUM retention filters for a RUM application.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of RUM retention filters. |


## com.datadoghq.dd.rum.retentionfilters.orderRetentionFilters
**Order retention filters** — Order RUM retention filters for a RUM application.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |
  | data | array<object> | yes | A list of RUM retention filter IDs along with type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of RUM retention filter IDs along with type. |


## com.datadoghq.dd.rum.retentionfilters.updateRetentionFilter
**Update retention filter** — Update a RUM retention filter for a RUM application.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_id | string | yes | RUM application ID. |
  | rf_id | string | yes | Retention filter ID. |
  | enabled | boolean | no | Whether the retention filter is enabled. |
  | event_type | string | no | The type of RUM events to filter on. |
  | name | string | no | The name of a RUM retention filter. |
  | query | string | no | The query string for a RUM retention filter. |
  | sample_rate | number | no | The sample rate for a RUM retention filter, between 0 and 100. |
  | id | string | yes | ID of retention filter in UUID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The RUM retention filter. |

