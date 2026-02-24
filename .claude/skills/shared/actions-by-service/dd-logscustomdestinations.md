# Datadog Logs Custom Destinations Actions
Bundle: `com.datadoghq.dd.logscustomdestinations` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogscustomdestinations)

## com.datadoghq.dd.logscustomdestinations.deleteLogsCustomDestination
**Delete logs custom destination** — Delete a specific custom destination in your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | custom_destination_id | string | yes | The ID of the custom destination. |


## com.datadoghq.dd.logscustomdestinations.getLogsCustomDestination
**Get logs custom destination** — Get a specific custom destination in your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | custom_destination_id | string | yes | The ID of the custom destination. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of a custom destination. |


## com.datadoghq.dd.logscustomdestinations.listLogsCustomDestinations
**List logs custom destinations** — Get the list of configured custom destinations in your organization with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of custom destinations. |

