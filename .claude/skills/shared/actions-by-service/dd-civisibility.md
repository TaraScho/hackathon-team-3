# Datadog CI Visibility Actions
Bundle: `com.datadoghq.dd.civisibility` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecivisibility)

## com.datadoghq.dd.civisibility.aggregateCIAppPipelineEvents
**Aggregate pipeline events** — Use this API endpoint to aggregate CI Visibility pipeline events into buckets of computed metrics and timeseries.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | created_at | any | no | Timestamp range for requested events. |
  | query | string | no | The search query following the CI Visibility Explorer search syntax. |
  | time_offset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | compute | array<object> | no | The list of metrics or timeseries to compute for the retrieved buckets. |
  | group_by | array<object> | no | The rules for the group-by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The query results. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.civisibility.aggregateCIAppTestEvents
**Aggregate test events** — The API endpoint to aggregate CI Visibility test events into buckets of computed metrics and timeseries.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | created_at | any | no | Timestamp range for requested events. |
  | query | string | no | The search query following the CI Visibility Explorer search syntax. |
  | time_offset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | compute | array<object> | no | The list of metrics or timeseries to compute for the retrieved buckets. |
  | group_by | array<object> | no | The rules for the group-by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The query results. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.civisibility.listCIAppPipelineEvents
**List pipeline events** — List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | created_at | any | no | Timestamp range for requested events. |
  | filter_query | string | no | Search query following log syntax. |
  | sort | string | no | Order of events in results. |
  | page_cursor | ['string', 'null'] | no | List following results with a cursor provided in the previous query. |
  | page_limit | number | no | Maximum number of events in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.civisibility.listCIAppTestEvents
**List test events** — List endpoint returns CI Visibility test events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time_range | any | no | Timestamp range for requested events. |
  | filter_query | string | no | Search query following log syntax. |
  | sort | string | no | Order of events in results. |
  | page_cursor | ['string', 'null'] | no | List following results with a cursor provided in the previous query. |
  | page_limit | number | no | Maximum number of events in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.civisibility.searchCIAppPipelineEvents
**Search pipeline events** — List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | created_at | any | no | Timestamp range for requested events. |
  | query | string | no | The search query following the CI Visibility Explorer search syntax. |
  | time_offset | number | no | The time offset (in seconds) to apply to the query. |
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


## com.datadoghq.dd.civisibility.searchCIAppTestEvents
**Search test events** — List endpoint returns CI Visibility test events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time_range | any | no | Timestamp range for requested events. |
  | query | string | no | The search query following the CI Visibility Explorer search syntax. |
  | time_offset | number | no | The time offset (in seconds) to apply to the query. |
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

