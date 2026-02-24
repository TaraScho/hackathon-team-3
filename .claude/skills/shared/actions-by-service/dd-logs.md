# Datadog Logs Actions
Bundle: `com.datadoghq.dd.logs` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogs)

## com.datadoghq.dd.logs.aggregateEvents
**Aggregate events** — This action aggregates events into buckets and computes metrics and timeseries.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | compute | array<object> | no | The list of metrics or timeseries to compute for the retrieved buckets. |
  | filter | object | no | The search and filter query settings. |
  | group_by | array<object> | no | The rules for the group by. |
  | options | object | no | Global query options that are used during the query. Use either timezone or time offset, but not both (fails otherwise). |
  | page | object | no | Paging settings. Page cursor is the returned paging point to use to get the next results, at most 1000 results can be paged. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | meta | object | The metadata associated with a request |
  | data | object | The query results |


## com.datadoghq.dd.logs.listLogs
**Search logs** — List endpoint returns logs that match a log search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | yes | Timeframe to retrieve the log from. |
  | index | string | no | The log index on which the request is performed. |
  | query | string | no | The search query - following the log search syntax. |
  | startAt | string | no | Hash identifier of the first log to return in the list, available in a log `id` attribute. |
  | sort | string | no | Time-ascending `asc` or time-descending `desc`results. |
  | limit | number | no | Number of logs to return in the response. Default value of 50, maximum value of 1,000. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | nextLogId | string | Hash identifier of the next log to return in the list. |
  | status | string | Status of the response. |
  | logs | array<object> | Array of logs matching the request and the `nextLogId` if sent. |


## com.datadoghq.dd.logs.listLogsV2
**Search Logs** — List endpoint returns logs that match a log search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time_range | any | no | Timestamp range for requested logs. |
  | indexes | array<string> | no | For customers with multiple indexes, the indexes to search. |
  | query | string | no | The search query - following the log search syntax. |
  | storage_tier | string | no | Specifies storage type as indexes, online-archives or flex. |
  | timeOffset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | cursor | string | no | List following results with a cursor provided in the previous query. |
  | limit | number | no | Maximum number of logs in the response. |
  | sort | string | no | Sort parameters when querying logs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of logs matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.logs.sendLogs
**Send logs** — Send logs to Datadog.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | logs | array<object> | yes | The array of logs to send. The entire payload may be up to 5MB, with a single log entry up to 1MB. |

