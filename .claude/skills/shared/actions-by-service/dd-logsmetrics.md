# Datadog Logs Metrics Actions
Bundle: `com.datadoghq.dd.logsmetrics` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogsmetrics)

## com.datadoghq.dd.logsmetrics.createLogsMetric
**Create logs metric** — Create a metric based on your ingested logs in your organization.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | aggregation_type | string | yes | The type of aggregation to use. |
  | include_percentiles | boolean | no | Toggle to include or exclude percentile aggregations for distribution metrics. |
  | path | string | no | The path to the value the log-based metric will aggregate on (only used if the aggregation type is a "distribution"). |
  | query | string | no | The search query - following the log search syntax. |
  | group_by | array<object> | no | The rules for the group by. |
  | id | string | yes | The name of the log-based metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The log-based metric properties. |


## com.datadoghq.dd.logsmetrics.deleteLogsMetric
**Delete logs metric** — Delete a specific log-based metric from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the log-based metric. |


## com.datadoghq.dd.logsmetrics.getLogsMetric
**Get logs metric** — Get a specific log-based metric from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the log-based metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The log-based metric properties. |


## com.datadoghq.dd.logsmetrics.listLogsMetrics
**List logs metrics** — Get the list of configured log-based metrics with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of log-based metric objects. |


## com.datadoghq.dd.logsmetrics.updateLogsMetric
**Update logs metric** — Update a specific log-based metric from your organization.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the log-based metric. |
  | include_percentiles | boolean | no | Toggle to include or exclude percentile aggregations for distribution metrics. |
  | query | string | no | The search query - following the log search syntax. |
  | group_by | array<object> | no | The rules for the group by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The log-based metric properties. |

