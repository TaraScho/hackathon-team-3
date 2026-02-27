# Datadog Audit Actions
Bundle: `com.datadoghq.dd.auditlogs` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eauditlogs)

## com.datadoghq.dd.auditlogs.listAuditLogs
**List audit logs** — List endpoint returns events that match a Audit Logs search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested events. |
  | filter_query | string | no | Search query following Audit Logs syntax. |
  | sort | string | no | Order of events in results. |
  | page_cursor | ['string', 'null'] | no | List following results with a cursor provided in the previous query. |
  | page_limit | number | no | Maximum number of events in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.auditlogs.searchAuditLogs
**Search audit logs** — List endpoint returns Audit Logs events that match an Audit search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested events. If not provided, the query window will be the past 15 minutes. |
  | query | string | no | Search query following the Audit Logs search syntax. |
  | time_offset | number | no | Time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | cursor | string | no | List following results with a cursor provided in the previous query. |
  | limit | number | no | Maximum number of events in the response. |
  | sort | string | no | Sort parameters when querying events. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |

