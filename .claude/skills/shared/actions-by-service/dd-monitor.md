# Datadog Monitor Actions
Bundle: `com.datadoghq.dd.monitor` | 17 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Emonitor)

## com.datadoghq.dd.monitor.checkCanDeleteMonitor
**Check can delete monitor** — Check if the given monitors can be deleted.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitorId | ['number', 'string'] | yes | The ID of the monitor to check. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | canDelete | boolean |  |


## com.datadoghq.dd.monitor.cloneMonitor
**Clone monitor** — Clone the specified monitor.
- Stability: stable
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitorId | number | yes | The ID of the monitor to be cloned. |
  | name | string | no | Replaced the cloned monitor name with the provided name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |


## com.datadoghq.dd.monitor.createMonitor
**Create monitor** — Create a monitor using the specified options.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | The monitor name. |
  | monitorType | any | yes | The [type](https://docs.datadoghq.com/api/latest/monitors/#monitor-types) of the monitor. |
  | message | string | yes | A message to include with notifications for this monitor. You can build a notification section in the monitor product using autocomplete and copy and paste it into this field. |
  | priority | number | no | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | tags | any | no | Tags associated to your monitor. |
  | escalation_message | string | no | We recommend using the [is_renotify](https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify), block in the original message instead. A message to include with a re-notification. Supports... |
  | include_tags | boolean | no | A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title. |
  | notify_audit | boolean | no | A Boolean indicating whether tagged users is notified on changes to this monitor. |
  | renotify_interval | number | no | The number of minutes after the last notification before a monitor re-notifies on the current status. |
  | renotify_occurrences | number | no | The number of times re-notification messages should be sent on the current status at the provided re-notification interval. |
  | renotify_statuses | array<string> | no | The types of monitor statuses for which re-notification messages are sent. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |


## com.datadoghq.dd.monitor.deleteMonitor
**Delete monitor** — Delete the specified monitor.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The ID of the monitor. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleted_monitor_id | ['number', 'string'] | ID of the deleted monitor. |


## com.datadoghq.dd.monitor.deleteMonitorConfigPolicy
**Delete monitor config policy** — Delete a monitor configuration policy.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | yes | ID of the monitor configuration policy. |


## com.datadoghq.dd.monitor.getMonitor
**Get monitor** — Get details about the specified monitor from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The ID of the monitor. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |


## com.datadoghq.dd.monitor.getMonitorConfigPolicy
**Get monitor config policy** — Get a monitor configuration policy by `policy_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | yes | ID of the monitor configuration policy. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A monitor configuration policy data. |


## com.datadoghq.dd.monitor.getMonitorGroupByName
**Get monitor group by name** — Get the monitor group by name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['string', 'number'] | yes | The ID of the monitor. |
  | group_name | string | yes | The name of the monitor group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | name | string | The name of the monitor. |
  | last_triggered_ts | number | Latest timestamp the monitor group triggered. |
  | last_notified_ts | number | Latest timestamp of the notification sent for this monitor group. |
  | status | string | The different states your monitor can be in. |
  | last_resolved_ts | number | Latest timestamp the monitor group was resolved. |
  | last_nodata_ts | number | Latest timestamp the monitor was in NO_DATA state. |


## com.datadoghq.dd.monitor.getMonitorSource
**Get monitor source** — Get details about the specified monitor from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The ID of the monitor. |
  | event_id | string | yes | The ID of the event. |
  | monitor_attributes | object | no | Used to overwrite information grabbed by source enrichment. |


## com.datadoghq.dd.monitor.listMonitorConfigPolicies
**List monitor config policies** — Get all monitor configuration policies.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of monitor configuration policies. |


## com.datadoghq.dd.monitor.listMonitors
**List monitors** — List monitors from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | no | A string to filter monitors by name. |
  | tags | any | no | A list indicating what tags, if any, should be used to filter the list of monitors by scope. |
  | monitor_tags | any | no | A list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. |
  | with_downtimes | boolean | no | If this argument is set to true, then the returned data includes all current active downtimes for each monitor. |
  | limit | number | no | The number of monitors to return. Defaults to 100. |


## com.datadoghq.dd.monitor.listMonitorsV2
**List monitors** — List monitors from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | no | A string to filter monitors by name. |
  | tags | any | no | A list indicating what tags, if any, should be used to filter the list of monitors by scope. |
  | monitor_tags | any | no | A list indicating what service and/or custom tags, if any, should be used to filter the list of monitors. |
  | with_downtimes | boolean | no | If this argument is set to true, then the returned data includes all current active downtimes for each monitor. |
  | limit | number | no | The number of monitors to return. Defaults to 100. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | monitors | array<object> |  |


## com.datadoghq.dd.monitor.muteMonitor
**Mute monitor** — Mute the specified monitor.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitorId | ['number', 'string'] | yes | The ID of the monitor to be muted. |
  | scope | string | no | The scope to apply the mute to. For example, if your alert is grouped by `{host}`, you might mute `host:app1`. |
  | duration | string | no | Duration of the mute, relative to when the workflow runs, in ISO-8601 duration format. - `P1W`: Mute for one week. - `P1DT6H30M`: Mute for one day, six hours and 30 minutes. - `PT10S`: Mute for ten... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |


## com.datadoghq.dd.monitor.resolveMonitor
**Resolve monitor** — Mark the monitor as resolved for all groups. The monitor state will become 'OK'.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | ['number', 'string'] | yes | The ID of the monitor. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |


## com.datadoghq.dd.monitor.searchMonitorGroups
**Search monitor groups** — Search and filter your monitor groups details.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | A query to search for monitors. |
  | page | number | no | Page to start paginating from. |
  | per_page | number | no | Number of monitors to return per page. |
  | sort | string | no | String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | counts | object | The counts of monitor groups per different criteria. |
  | groups | array<object> | The list of found monitor groups. |
  | metadata | object | Metadata about the response. |


## com.datadoghq.dd.monitor.searchMonitors
**Search monitors** — Search and filter your monitors details.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | A query to search for monitors. |
  | page | number | no | Page to start paginating from. |
  | per_page | number | no | Number of monitors to return per page. |
  | sort | string | no | String for sort order, composed of field and sort order separate by a comma, for example `name,asc`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | counts | object | The counts of monitors per different criteria. |
  | metadata | object | Metadata about the response. |
  | monitors | array<object> | The list of found monitors. |


## com.datadoghq.dd.monitor.unmuteMonitor
**Unmute monitor** — Unmute the specified monitor.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitorId | ['number', 'string'] | yes | The ID of the monitor to be muted. |
  | scope | string | no | The scope to apply the mute to. For example, if your alert is grouped by `{host}`, you might mute `host:app1`. |
  | all_scopes | boolean | no | Clear muting across all scopes. Default is `false`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the monitor. |
  | creator | object |  |
  | id | ['number', 'string'] | ID of this monitor. |
  | message | string | A message to include with notifications for this monitor. |
  | name | string | The monitor name. |
  | tags | array<string> | Tags associated to your monitor. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | options | object | List of options associated with your monitor. |
  | overall_state | string | The different states your monitor can be in. |
  | query | string | The monitor query. |
  | evaluated_query | string | The query evaluated by the monitor |
  | type | string | The type of the monitor. |
  | priority | ['number', 'null'] | Integer from 1 (high) to 5 (low) indicating alert severity. |
  | multi | boolean | Whether or not the monitor is broken down on different groups. |
  | created | string | Timestamp of the monitor creation. |
  | deleted | ['string', 'null'] | Whether or not the monitor is deleted. |
  | modified | string | Last timestamp when the monitor was edited. |
  | state | object | Wrapper object with the different monitor states. |
  | restricted_roles | any | A list of role identifiers that can be pulled from the Roles API. |
  | overall_state_modified | ['string', 'null'] | Timestamp of last time the state of the monitor changed. |
  | created_at | ['number', 'null'] | Unix timestamp of monitor creation. |
  | org_id | ['number', 'null'] |  |

