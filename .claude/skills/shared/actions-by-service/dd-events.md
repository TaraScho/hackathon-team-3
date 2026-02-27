# Datadog Events Actions
Bundle: `com.datadoghq.dd.events` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eevents)

## com.datadoghq.dd.events.createEvent
**Create event** — Post events to the stream.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | title | string | yes | The event title. |
  | text | string | yes | The body of the event. |
  | date_happened | number | no | POSIX timestamp of the event. |
  | priority | string | no | The priority of the event. |
  | host | string | no | Host name to associate with the event. |
  | tags | any | no | A list of tags to apply to the event. |
  | alert_type | string | no | If an alert event is enabled, set its type. |
  | aggregation_key | string | no | An arbitrary string to use for aggregation. |
  | device_name | string | no | A device name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | event | object | Object representing an event with additional tag_value and tag_value_list properties. |
  | status | string | A response status from the Events API. |


## com.datadoghq.dd.events.getEvent
**Get event** — Query event details.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | event_id | string | yes | The ID of the event. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the event. |
  | event | object | Object representing an event with additional tag_value and tag_value_list properties. |
  | status | string | A response status from the Events API. |


## com.datadoghq.dd.events.listEvents
**List events** — Query and filter the event stream by time, priority, sources and tags. Returns up to 1000 events.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | yes | The time period range used to filter the event stream |
  | priority | string | no | Priority of your events, either `low` or `normal`. |
  | sources | string | no | A comma separated string of sources. |
  | tags | any | no | A list indicating what tags, if any, should be used to filter the list of monitors by scope. |
  | unaggregated | boolean | no | Set unaggregated to `true` to return all events within the specified [`start`,`end`] timeframe. |
  | exclude_aggregate | boolean | no | Set `exclude_aggregate` to `true` to only return unaggregated events where `is_aggregate=false` in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | events | array<object> | An array of events with additional tag_value and tag_value_list properties. |
  | status | string | A response status from the Events API. |


## com.datadoghq.dd.events.listEventsV2
**List events** — List events that match an events search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | Search query following events syntax. |
  | time_range | any | no | The time range for which to search events. |
  | sort | string | no | Order of events in results. |
  | page_cursor | ['string', 'null'] | no | List following results with a cursor provided in the previous query. |
  | page_limit | number | no | Maximum number of events in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of events matching the request. |
  | links | object | Links attributes. |
  | meta | object | The metadata associated with a request. |


## com.datadoghq.dd.events.searchEvents
**Search events** — Search for events in your Datadog account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | Events search uses the logs search syntax. Like logs search, events search permits: - AND, OR, and - operators - Wildcards - Escape characters - Searching tags and facets with key:value - Searching... |
  | time | any | no | Timeframe to retrieve the events from. |
  | limit | number | no | Number of events per page. Default 100. Max 5000. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | events | array<object> |  |

