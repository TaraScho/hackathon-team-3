# Datadog Snapshots Actions
Bundle: `com.datadoghq.dd.snapshots` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Esnapshots)

## com.datadoghq.dd.snapshots.getGraphSnapshot
**Get graph snapshot** — Take graph snapshots.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | yes | Timestamp range for requested snapshot. |
  | metric_query | string | no | The metric query. |
  | event_query | string | no | A query that adds event bands to the graph. |
  | graph_def | string | no | A JSON document defining the graph. |
  | title | string | no | A title for the graph. |
  | height | number | no | The height of the graph. |
  | width | number | no | The width of the graph. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | graph_def | string | A JSON document defining the graph. |
  | metric_query | string | The metric query. |
  | snapshot_url | string | URL of your [graph snapshot](https://docs.datadoghq.com/metrics/explorer/#snapshot). |

