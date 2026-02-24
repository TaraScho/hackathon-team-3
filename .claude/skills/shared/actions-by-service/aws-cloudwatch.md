# AWS CloudWatch Actions
Bundle: `com.datadoghq.aws.cloudwatch` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecloudwatch)

## com.datadoghq.aws.cloudwatch.getMetricData
**Get metric data** — Retrieve CloudWatch metric values. This operation can also include a CloudWatch Metrics Insights query and one or more metric math functions.
- Stability: stable
- Permissions: `cloudwatch:GetMetricData`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | metricDataQueries | array<object> | yes | The metric queries to be returned. A single GetMetricData call can include as many as 500 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, a Metrics Ins... |
  | startTime | string | yes | The time stamp indicating the earliest data to be returned. The value specified is inclusive; results include data points with the specified time stamp. |
  | endTime | string | yes | The time stamp indicating the latest data to be returned. The value specified is exclusive; results include data points up to the specified time stamp. |
  | nextToken | string | no | Include this value, if it was returned by the previous GetMetricData operation, to get the next set of data points. |
  | scanBy | string | no | The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest dat... |
  | maxDatapoints | number | no | The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used. |
  | labelOptions | object | no | This structure includes the Timezone parameter, which you can use to specify your time zone so that the labels of returned data display the correct time for your time zone. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MetricDataResults | array<object> | The metrics that are returned, including the metric name, namespace, and dimensions. |
  | NextToken | string | A token that marks the next batch of returned results. |
  | Messages | array<object> | Contains a message about this GetMetricData operation, if the operation results in such a message. An example of a message that might be returned is Maximum number of allowed metrics exceeded. If t... |

