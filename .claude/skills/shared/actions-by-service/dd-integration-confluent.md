# Datadog Confluent Integration Actions
Bundle: `com.datadoghq.dd.integration.confluent` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Econfluent)

## com.datadoghq.dd.integration.confluent.createConfluentResource
**Create Confluent resource** — Create a Confluent resource for the account associated with the provided ID.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tags | any | no | A list of strings representing tags. |
  | account_id | string | yes | Confluent Account ID. |
  | enable_custom_metrics | boolean | no | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags. |
  | resource_type | string | yes | The resource type of the Resource. |
  | id | string | yes | The ID associated with a Confluent resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Confluent Cloud resource data. |


## com.datadoghq.dd.integration.confluent.deleteConfluentResource
**Delete Confluent resource** — Delete a Confluent resource with the provided resource id for the account associated with the provided account ID.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Confluent Account ID. |
  | resource_id | string | yes | Confluent Account Resource ID. |


## com.datadoghq.dd.integration.confluent.getConfluentResource
**Get Confluent resource** — Get a Confluent resource with the provided resource id for the account associated with the provided account ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Confluent Account ID. |
  | resource_id | string | yes | Confluent Account Resource ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Confluent Cloud resource data. |


## com.datadoghq.dd.integration.confluent.listConfluentResource
**List Confluent resource** — Get a Confluent resource for the account associated with the provided ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Confluent Account ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The JSON:API data attribute. |


## com.datadoghq.dd.integration.confluent.updateConfluentResource
**Update Confluent resource** — Update a Confluent resource with the provided resource id for the account associated with the provided account ID.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tags | any | no | A list of strings representing tags. |
  | account_id | string | yes | Confluent Account ID. |
  | resource_id | string | yes | Confluent Account Resource ID. |
  | enable_custom_metrics | boolean | no | Enable the `custom.consumer_lag_offset` metric, which contains extra metric tags. |
  | resource_type | string | yes | The resource type of the Resource. |
  | id | string | yes | The ID associated with a Confluent resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Confluent Cloud resource data. |

