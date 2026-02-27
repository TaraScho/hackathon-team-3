# Datadog Spans Actions
Bundle: `com.datadoghq.dd.spans` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Espans)

## com.datadoghq.dd.spans.aggregateSpans
**Aggregate spans** — Aggregate spans into buckets and compute metrics and timeseries.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested spans. If not provided, the query window will be the past 15 minutes. |
  | query | string | no | The search query - following the span search syntax. |
  | timeOffset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | compute | array<object> | no | The list of metrics or timeseries to compute for the retrieved buckets. |
  | group_by | array<object> | no | The rules for the group by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list of matching buckets, one item per bucket. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.spans.getSpansList
**Get spans list** — Get the spans list that match a span search query. This action temporarly requires a Datadog external account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | Search query following spans syntax in this [documentation](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/). |
  | time_range | any | no | Minimum timestamp for requested spans. |
  | order | string | no | Order of spans in results. |
  | page_cursor | ['string', 'null'] | no | Cursor for pagination. You can use the page_after output value. |
  | page_limit | number | no | Maximum number of spans to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | spans | array<object> |  |
  | page_after | string |  |


## com.datadoghq.dd.spans.listSpans
**Search spans** — Return spans that match a span search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested spans. |
  | query | string | no | The search query - following the span search syntax. |
  | timeOffset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | cursor | string | no | List following results with a cursor provided in the previous query. |
  | limit | number | no | Maximum number of spans in the response. |
  | sort | string | no | Sort parameters when querying spans. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of spans matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |

