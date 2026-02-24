# Datadog APM Retention Filters Actions
Bundle: `com.datadoghq.dd.apmretentionfilters` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eapmretentionfilters)

## com.datadoghq.dd.apmretentionfilters.deleteAPMRetentionFilter
**Delete APM retention filter** — Delete a specific retention filter from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_id | string | yes | The ID of the retention filter. |


## com.datadoghq.dd.apmretentionfilters.getAPMRetentionFilter
**Get APM retention filter** — Get an APM retention filter.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_id | string | yes | The ID of the retention filter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of the retention filter. |


## com.datadoghq.dd.apmretentionfilters.listAPMRetentionFilters
**List APM retention filters** — Get the list of APM retention filters.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of retention filters objects. |


## com.datadoghq.dd.apmretentionfilters.reorderAPMRetentionFilters
**Reorder APM retention filters** — Re-order the execution order of retention filters.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | data | array<object> | yes | A list of retention filters objects. |

