# Datadog Spans Metrics Actions
Bundle: `com.datadoghq.dd.spansmetrics` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Espansmetrics)

## com.datadoghq.dd.spansmetrics.createSpansMetric
**Create spans metric** — Create a metric based on your ingested spans in your organization.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | aggregation_type | string | yes | The type of aggregation to use. |
  | include_percentiles | boolean | no | Toggle to include or exclude percentile aggregations for distribution metrics. |
  | path | string | no | The path to the value the span-based metric will aggregate on (only used if the aggregation type is a "distribution"). |
  | query | string | no | The search query - following the span search syntax. |
  | group_by | array<object> | no | The rules for the group by. |
  | id | string | yes | The name of the span-based metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The span-based metric properties. |


## com.datadoghq.dd.spansmetrics.deleteSpansMetric
**Delete spans metric** — Delete a specific span-based metric from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the span-based metric. |


## com.datadoghq.dd.spansmetrics.getSpansMetric
**Get spans metric** — Get a specific span-based metric from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the span-based metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The span-based metric properties. |


## com.datadoghq.dd.spansmetrics.listSpansMetrics
**List spans metrics** — Get the list of configured span-based metrics with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of span-based metric objects. |


## com.datadoghq.dd.spansmetrics.updateSpansMetric
**Update spans metric** — Update a specific span-based metric from your organization.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the span-based metric. |
  | include_percentiles | boolean | no | Toggle to include or exclude percentile aggregations for distribution metrics. |
  | query | string | no | The search query - following the span search syntax. |
  | group_by | array<object> | no | The rules for the group by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The span-based metric properties. |

