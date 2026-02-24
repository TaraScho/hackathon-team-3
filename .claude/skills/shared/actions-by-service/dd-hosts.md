# Datadog Hosts Actions
Bundle: `com.datadoghq.dd.hosts` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ehosts)

## com.datadoghq.dd.hosts.getHost
**Get host** — Get details of host tracked in Datadog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Name of the host to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dashboard_url | string | Url to the Datadog Dashboard for this host. |
  | network_url | string | Url to Datadog Network for this host. |
  | processes_url | string | Url to Datadog Processes for this host. |
  | containers_url | string | Url to Datadog Containers for this host. |
  | name | string | The host name. |
  | up | boolean | Displays UP when the expected metrics are received and displays `???` if no metrics are received. |
  | is_muted | boolean | If a host is muted or unmuted. |
  | mute_timeout | ['number', 'null'] | Timeout of the mute applied to your host. |
  | last_reported_time | number | Last time the host reported a metric data point. |
  | apps | array<string> | The Datadog integrations reporting metrics for the host. |
  | tags_by_source | object | List of tags for each source (AWS, Datadog Agent, Chef.). |
  | aws_name | string | AWS name of your host. |
  | metrics | object | Host Metrics collected. |
  | sources | array<string> | Source or cloud provider associated with your host. |
  | meta | object | Metadata associated with your host. |
  | host_name | string | The host name. |
  | id | ['number', 'string'] | The host ID. |
  | aliases | array<string> | Host aliases collected by Datadog. |


## com.datadoghq.dd.hosts.getHostTotals
**Get host totals** — Retrieve total number of active and up hosts in your Datadog account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | from | number | no | Number of seconds from which you want to get total number of active hosts. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | total_up | number | Number of host that are UP and reporting to Datadog. |
  | total_active | number | Total number of active host (UP and ???) reporting to Datadog. |


## com.datadoghq.dd.hosts.listHosts
**List hosts** — Search for hosts by name, alias, or tag.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter | string | no | String to filter search results. |
  | sort_field | string | no | Sort hosts by this field. |
  | sort_dir | string | no | Direction of sort. |
  | start | number | no | Host result to start search from. |
  | count | number | no | Number of hosts to return. |
  | from | number | no | Number of seconds since UNIX epoch from which you want to search your hosts. |
  | include_muted_hosts_data | boolean | no | Include information on the muted status of hosts and when the mute expires. |
  | include_hosts_metadata | boolean | no | Include additional metadata about the hosts (agent_version, machine, platform, processor, etc.). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | total_returned | number | Number of host returned. |
  | total_matching | number | Number of host matching the query. |
  | host_list | array<object> | Array of hosts. |


## com.datadoghq.dd.hosts.muteHost
**Mute host** — Mute a host.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes |  |
  | duration_seconds | number | no | Duration of the mute, relative to when the workflow runs, expressed as a number of seconds. If not provided, the mute is in effect indefinitely until you cancel it. |
  | override | boolean | no | If true and the host is already muted, replaces existing host mute settings. |
  | message | string | no | Message to associate with the muting of this host. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | action | string | Action applied to the hosts. |
  | hostname | string | The host name. |
  | message | string | Message associated with the mute. |
  | end | number | POSIX timestamp in seconds when the host is unmuted. |


## com.datadoghq.dd.hosts.unmuteHost
**Unmute host** — Unmute a host.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Name of the host to unmute. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | action | string | Action applied to the hosts. |
  | hostname | string | The host name. |
  | message | string | Message associated with the mute. |
  | end | number | POSIX timestamp in seconds when the host is unmuted. |

