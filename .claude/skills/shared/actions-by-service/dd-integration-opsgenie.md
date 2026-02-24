# Datadog Opsgenie Integration Actions
Bundle: `com.datadoghq.dd.integration.opsgenie` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Eopsgenie)

## com.datadoghq.dd.integration.opsgenie.deleteOpsgenieService
**Delete Opsgenie service** — Delete a single service object in the Datadog Opsgenie integration.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | integration_service_id | string | yes | The UUID of the service. |


## com.datadoghq.dd.integration.opsgenie.getOpsgenieService
**Get Opsgenie service** — Get a single service from the Datadog Opsgenie integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | integration_service_id | string | yes | The UUID of the service. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Opsgenie service data from a response. |


## com.datadoghq.dd.integration.opsgenie.listOpsgenieServices
**List Opsgenie services** — Get a list of all services from the Datadog Opsgenie integration.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of Opsgenie services. |

