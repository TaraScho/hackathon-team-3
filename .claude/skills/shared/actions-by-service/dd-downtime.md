# Datadog Downtime Actions
Bundle: `com.datadoghq.dd.downtime` | 13 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edowntime)

## com.datadoghq.dd.downtime.cancelDowntime
**Cancel Downtime** — Cancel a downtime.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | downtime_id | ['number', 'string'] | yes | ID of the downtime to cancel. |


## com.datadoghq.dd.downtime.cancelDowntimeV2
**Cancel Downtime** — Cancel a downtime.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | downtime_id | ['number', 'string'] | yes | ID of the downtime to cancel. |


## com.datadoghq.dd.downtime.cancelDowntimesByScope
**Cancel downtimes by scope** — Delete all downtimes that match the scope of `X`.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scope | string | yes | The scope(s) to which the downtime applies and must be in `key:value` format. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | cancelled_ids | array<number> | ID of downtimes that were canceled. |


## com.datadoghq.dd.downtime.getDowntime
**Get Downtime** — Get downtime detail by `downtime_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | downtime_id | ['number', 'string'] | yes | ID of the downtime to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the downtime. |
  | active | boolean | If a scheduled downtime currently exists. |
  | canceled | number | If a scheduled downtime is canceled. |
  | creator_id | number | User ID of the downtime creator. |
  | disabled | boolean | If a downtime has been disabled. |
  | downtime_type | number | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts. |
  | end | number | POSIX timestamp to end the downtime. |
  | id | ['number', 'string'] | The downtime ID. |
  | message | string | A message to include with notifications for this downtime. |
  | monitor_id | ['number', 'string'] | A single monitor to which the downtime applies. |
  | monitor_tags | array<string> | A comma-separated list of monitor tags. |
  | parent_id | ['number', 'string'] | ID of the parent Downtime. |
  | recurrence | object | An object defining the recurrence of the downtime. |
  | scope | array<string> | The scope(s) to which the downtime applies. |
  | start | number | POSIX timestamp to start the downtime. |
  | timezone | string | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | updater_id | number | ID of the last user that updated the downtime. |
  | active_child | object | The downtime object definition of the active child for the original parent recurring downtime. |


## com.datadoghq.dd.downtime.getDowntimeV2
**Get Downtime** — Get downtime detail by `downtime_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | downtime_id | string | yes | ID of the downtime to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | The ID of the downtime. |
  | created_by | any | The user who created the downtime. |
  | url | string | The URL of the downtime. |
  | canceled | string | Time that the downtime was canceled. |
  | created | string | Creation time of the downtime. |
  | display_timezone | string | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | message | string | A message to include with notifications for this downtime. |
  | modified | string | Time that the downtime was last modified. |
  | monitor_identifier | any | Monitor identifier for the downtime. |
  | mute_first_recovery_notification | boolean | If the first recovery notification during a downtime should be muted. |
  | notify_end_states | array<string> | States that will trigger a monitor notification when the `notify_end_types` action occurs. |
  | notify_end_types | array<string> | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state. |
  | schedule | any | The schedule that defines when the monitor starts, stops, and recurs. |
  | scope | string | The scope to which the downtime applies. |
  | status | string | The current status of the downtime. |


## com.datadoghq.dd.downtime.listDowntimes
**List downtimes** — Get all scheduled downtimes.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | current_only | boolean | no | Only return downtimes that are active when the request is made. |


## com.datadoghq.dd.downtime.listDowntimesV2
**List downtimes** — Get all scheduled downtimes.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | current_only | boolean | no | Only return downtimes that are active when the request is made. |
  | page_limit | number | no | Maximum number of downtimes in the response. Default is 100. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | downtimes | array<object> |  |


## com.datadoghq.dd.downtime.listMonitorDowntimes
**List monitor downtimes** — Get all active downtimes for the specified monitor.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The id of the monitor. |


## com.datadoghq.dd.downtime.listMonitorDowntimesV2
**List monitor downtimes** — Get all active downtimes for the specified monitor.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The id of the monitor. |
  | page_limit | number | no | Maximum number of downtimes in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | downtimeMatches | array<object> |  |


## com.datadoghq.dd.downtime.scheduleDowntime
**Schedule Downtime** — Schedule a downtime.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scope | array<string> | yes | The scope(s) to which the downtime applies. |
  | duration_seconds | number | no | How long to schedule the downtime for. Select length of time from drop down or input custom length of time in seconds. If not provided, the downtime is in effect indefinitely until you cancel it. |
  | message | string | no | A message to include with notifications for this downtime. |
  | monitor_id | ['number', 'string'] | no | A single monitor to which the downtime applies. |
  | monitor_tags | any | no | A comma-separated list of monitor tags. |
  | mute_first_recovery_notification | boolean | no | If the first recovery notification during a downtime should be muted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | active | boolean | If a scheduled downtime currently exists. |
  | active_child | object | The downtime object definition of the active child for the original parent recurring downtime. |
  | canceled | number | If a scheduled downtime is canceled. |
  | creator_id | number | User ID of the downtime creator. |
  | disabled | boolean | If a downtime has been disabled. |
  | downtime_type | number | `0` for a downtime applied on `*` or all, `1` when the downtime is only scoped to hosts, or `2` when the downtime is scoped to anything but hosts. |
  | end | number | POSIX timestamp to end the downtime. |
  | id | ['number', 'string'] | The downtime ID. |
  | message | string | A message to include with notifications for this downtime. |
  | monitor_id | ['number', 'string'] | A single monitor to which the downtime applies. |
  | monitor_tags | array<string> | A comma-separated list of monitor tags. |
  | mute_first_recovery_notification | boolean | If the first recovery notification during a downtime should be muted. |
  | parent_id | ['number', 'string'] | ID of the parent Downtime. |
  | recurrence | object | An object defining the recurrence of the downtime. |
  | scope | array<string> | The scope(s) to which the downtime applies. |
  | start | number | POSIX timestamp to start the downtime. |
  | timezone | string | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | updater_id | number | ID of the last user that updated the downtime. |


## com.datadoghq.dd.downtime.scheduleDowntimeV2
**Schedule Downtime** — Schedule a downtime.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scope | string | yes | The scope to which the downtime applies. |
  | monitor_identifier | any | yes | Monitor identifier for the downtime. |
  | schedule | any | no | Schedule for the downtime. |
  | display_timezone | string | no | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | message | string | no | A message to include with notifications for this downtime. |
  | mute_first_recovery_notification | boolean | no | If the first recovery notification during a downtime should be muted. |
  | notify_end_states | array<string> | no | States that will trigger a monitor notification when the `notify_end_types` action occurs. |
  | notify_end_types | array<string> | no | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | The ID of the downtime. |
  | created_by | any | The user who created the downtime. |
  | url | string | The URL of the downtime. |
  | canceled | string | Time that the downtime was canceled. |
  | created | string | Creation time of the downtime. |
  | display_timezone | string | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | message | string | A message to include with notifications for this downtime. |
  | modified | string | Time that the downtime was last modified. |
  | monitor_identifier | any | Monitor identifier for the downtime. |
  | mute_first_recovery_notification | boolean | If the first recovery notification during a downtime should be muted. |
  | notify_end_states | array<string> | States that will trigger a monitor notification when the `notify_end_types` action occurs. |
  | notify_end_types | array<string> | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state. |
  | schedule | any | The schedule that defines when the monitor starts, stops, and recurs. |
  | scope | string | The scope to which the downtime applies. |
  | status | string | The current status of the downtime. |


## com.datadoghq.dd.downtime.searchDowntimes
**Search downtimes** — Search all scheduled downtimes matching the provided filters. The search is limited to 1000 downtimes.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scopes | array<string> | no | A list of scope values the downtimes should have. Logical operator like `OR` or `AND` are not supported in the values. Instead of `service:(a OR b)`, add two values `service:a` and `service:b` and ... |
  | monitor_tags | any | no | A list of monitor tags that the filtered downtimes should have. You can also use `-` to exclude monitor tags. For example, `-env:staging` will return downtimes without the monitor tag `env:staging`. |
  | joinOperator | string | no | The logical operator to use when combining multiple search criteria from the Scopes and Monitor Tags arrays. Defaults to `OR`. |
  | current_only | boolean | no | Only return downtimes that are active when the request is made. |
  | recurring | boolean | no | Filter downtimes that are recurring. |
  | automuted | boolean | no | Filter downtimes that are automuted. |
  | page_limit | number | no | Maximum number of downtimes in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | downtimes | array<object> | The list of downtimes that match the search criteria. |


## com.datadoghq.dd.downtime.updateDowntime
**Update downtime** — Update a downtime by `downtime_id`.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | downtime_id | string | yes | ID of the downtime to update. |
  | display_timezone | string | no | The timezone in which to display the downtime's start and end times in Datadog applications. |
  | message | string | no | A message to include with notifications for this downtime. |
  | monitor_identifier | any | no | Monitor identifier for the downtime. |
  | mute_first_recovery_notification | boolean | no | If the first recovery notification during a downtime should be muted. |
  | notify_end_states | array<string> | no | States that will trigger a monitor notification when the `notify_end_types` action occurs. |
  | notify_end_types | array<string> | no | Actions that will trigger a monitor notification if the downtime is in the `notify_end_types` state. |
  | schedule | any | no | Schedule for the downtime. |
  | scope | string | no | The scope to which the downtime applies. |
  | id | string | yes | ID of this downtime. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Downtime data. |
  | included | array<object> | Array of objects related to the downtime that the user requested. |

