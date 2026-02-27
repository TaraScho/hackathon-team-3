# Datadog RUM Actions
Bundle: `com.datadoghq.dd.rum` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Erum)

## com.datadoghq.dd.rum.aggregateRUMEvents
**Aggregate RUM events** — The API endpoint to aggregate RUM events into buckets of computed metrics and timeseries.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested events. If not provided, the query window will be the past 15 minutes. |
  | query | string | no | The search query following the RUM search syntax. |
  | time_offset | number | no | The time offset (in seconds) to apply to the query. |
  | timezone | string | no | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
  | cursor | string | no | List following results with a cursor provided in the previous query. |
  | limit | number | no | Maximum number of events in the response. |
  | compute | array<object> | no | The list of metrics or timeseries to compute for the retrieved buckets. |
  | group_by | array<object> | no | The rules for the group by. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The query results. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.rum.createRUMApplication
**Create RUM application** — Create a new RUM application in your organization.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Name of the RUM application. |
  | product_analytics_retention_state | string | no | Controls the retention policy for Product Analytics data derived from RUM events. |
  | rum_event_processing_state | string | no | Configures which RUM events are processed and stored for the application. |
  | type | string | yes | Type of the RUM application. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | RUM application. |


## com.datadoghq.dd.rum.deleteRUMApplication
**Delete RUM application** — Delete an existing RUM application in your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | RUM application ID. |


## com.datadoghq.dd.rum.deleteRumMetric
**Delete RUM metric** — Delete a specific rum-based metric from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the rum-based metric. |


## com.datadoghq.dd.rum.getRUMApplication
**Get RUM application** — Get a RUM application.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | created_at | number | Timestamp in ms of the creation date. |
  | created_by_handle | string | The handle of the creator user. |
  | client_token | string |  |
  | hash | string | Hash of the RUM application. |
  | is_active | boolean | Indicates if the RUM application is active. |
  | name | string |  |
  | org_id | number |  |
  | type | string | Type of the RUM application. Supported values are browser, ios, android, react-native, and flutter. |
  | updated_at | number | Timestamp in ms of the last update date. |
  | updated_by_handle | string | Handle of the updator user. |


## com.datadoghq.dd.rum.getRumMetric
**Get RUM metric** — Get a specific rum-based metric from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_id | string | yes | The name of the rum-based metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The rum-based metric properties. |


## com.datadoghq.dd.rum.listRUMApplications
**List RUM applications** — List all of the RUM applications.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | applications | array<object> |  |


## com.datadoghq.dd.rum.listRUMEvents
**List RUM events** — List endpoint returns events that match a RUM search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | no | The time period range for requested events |
  | filter_query | string | no | Search query following RUM syntax. |
  | sort | string | no | Order of events in results. |
  | sortDirection | string | no | Order of events in results. |
  | page_limit | number | no | Maximum number of events in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | meta | object | The metadata associated with a request. |
  | links | object | Links attributes. |


## com.datadoghq.dd.rum.listRumMetrics
**List RUM metrics** — Get the list of configured rum-based metrics with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of rum-based metric objects. |


## com.datadoghq.dd.rum.searchRUMEvents
**Search RUM events** — List endpoint returns RUM events that match a RUM search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | options | object | no | Global query options that are used during the query. |
  | filter | object | no | The search and filter query settings. |
  | sort | string | no | Sort parameters when querying events. |
  | sortDirection | string | no | Sort parameters when querying events. |
  | page | object | no | Paging attributes for listing events. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of events matching the request. |
  | meta | object | The metadata associated with a request. |
  | links | object | Links attributes. |


## com.datadoghq.dd.rum.updateRUMApplication
**Update RUM application** — Update a RUM application.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes |  |
  | name | string | no | The new name of the RUM application. |
  | type | string | no | The new type of the RUM application. Supported values are browser, ios, android, react-native, and flutter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | created_at | number | Timestamp in ms of the creation date. |
  | created_by_handle | string | The handle of the creator user. |
  | client_token | string |  |
  | hash | string | Hash of the RUM application. |
  | is_active | boolean | Indicates if the RUM application is active. |
  | name | string |  |
  | org_id | number |  |
  | type | string | Type of the RUM application. Supported values are browser, ios, android, react-native, and flutter. |
  | updated_at | number | Timestamp in ms of the last update date. |
  | updated_by_handle | string | Handle of the updator user. |

