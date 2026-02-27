# Datadog Logs Indexes Actions
Bundle: `com.datadoghq.dd.logsindexes` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogsindexes)

## com.datadoghq.dd.logsindexes.createLogsIndex
**Create logs index** — Creates a new index.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | reset_time | string | no | String in `HH:00` format representing the time of day the daily limit should be reset. |
  | reset_utc_offset | string | no | String in `(-\|+)HH:00` format representing the UTC offset to apply to the given reset time. |
  | query | string | yes | The filter query. |
  | daily_limit | number | no | The number of log events you can send in this index per day before you are rate-limited. |
  | daily_limit_warning_threshold_percentage | number | no | A percentage threshold of the daily quota at which a Datadog warning event is generated. |
  | exclusion_filters | array<object> | yes | An array of exclusion objects. |
  | is_rate_limited | boolean | no | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. |
  | name | string | yes | The name of the index. |
  | num_flex_logs_retention_days | number | no | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. |
  | num_retention_days | number | no | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | daily_limit | number | The number of log events you can send in this index per day before you are rate-limited. |
  | daily_limit_reset | object | Object containing options to override the default daily limit reset time. |
  | daily_limit_warning_threshold_percentage | number | A percentage threshold of the daily quota at which a Datadog warning event is generated. |
  | exclusion_filters | array<object> | An array of exclusion objects. |
  | filter | object | Filter for logs. |
  | is_rate_limited | boolean | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. |
  | name | string | The name of the index. |
  | num_flex_logs_retention_days | number | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. |
  | num_retention_days | number | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. |


## com.datadoghq.dd.logsindexes.getLogsIndex
**Get logs index** — Get one log index from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Name of the log index. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | daily_limit | number | The number of log events you can send in this index per day before you are rate-limited. |
  | daily_limit_reset | object | Object containing options to override the default daily limit reset time. |
  | daily_limit_warning_threshold_percentage | number | A percentage threshold of the daily quota at which a Datadog warning event is generated. |
  | exclusion_filters | array<object> | An array of exclusion objects. |
  | filter | object | Filter for logs. |
  | is_rate_limited | boolean | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. |
  | name | string | The name of the index. |
  | num_flex_logs_retention_days | number | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. |
  | num_retention_days | number | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. |


## com.datadoghq.dd.logsindexes.getLogsIndexOrder
**Get logs index order** — Get the current order of your log indexes.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | index_names | array<string> | Array of strings identifying by their name(s) the index(es) of your organization. |


## com.datadoghq.dd.logsindexes.listLogIndexes
**List log indexes** — The Index object describes the configuration of a log index.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | indexes | array<object> | Array of Log index configurations. |


## com.datadoghq.dd.logsindexes.updateLogsIndex
**Update logs index** — Update an index as identified by its name.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Name of the log index. |
  | reset_time | string | no | String in `HH:00` format representing the time of day the daily limit should be reset. |
  | reset_utc_offset | string | no | String in `(-\|+)HH:00` format representing the UTC offset to apply to the given reset time. |
  | query | string | yes | The filter query. |
  | daily_limit | number | no | The number of log events you can send in this index per day before you are rate-limited. |
  | daily_limit_warning_threshold_percentage | number | no | A percentage threshold of the daily quota at which a Datadog warning event is generated. |
  | disable_daily_limit | boolean | no | If true, sets the `daily_limit` value to null and the index is not limited on a daily basis (any specified `daily_limit` value in the request is ignored). |
  | exclusion_filters | array<object> | yes | An array of exclusion objects. |
  | num_flex_logs_retention_days | number | no | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. |
  | num_retention_days | number | no | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | daily_limit | number | The number of log events you can send in this index per day before you are rate-limited. |
  | daily_limit_reset | object | Object containing options to override the default daily limit reset time. |
  | daily_limit_warning_threshold_percentage | number | A percentage threshold of the daily quota at which a Datadog warning event is generated. |
  | exclusion_filters | array<object> | An array of exclusion objects. |
  | filter | object | Filter for logs. |
  | is_rate_limited | boolean | A boolean stating if the index is rate limited, meaning more logs than the daily limit have been sent. |
  | name | string | The name of the index. |
  | num_flex_logs_retention_days | number | The total number of days logs are stored in Standard and Flex Tier before being deleted from the index. |
  | num_retention_days | number | The number of days logs are stored in Standard Tier before aging into the Flex Tier or being deleted from the index. |


## com.datadoghq.dd.logsindexes.updateLogsIndexOrder
**Update logs index order** — This endpoint updates the index order of your organization.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | index_names | array<string> | yes | Array of strings identifying by their name(s) the index(es) of your organization. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | index_names | array<string> | Array of strings identifying by their name(s) the index(es) of your organization. |

