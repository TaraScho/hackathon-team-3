# Datadog Fastly Integration Actions
Bundle: `com.datadoghq.dd.integration.fastly` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Efastly)

## com.datadoghq.dd.integration.fastly.createFastlyService
**Create Fastly service** — Create a Fastly service for an account.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tags | any | no | A list of tags for the Fastly service. |
  | account_id | string | yes | Fastly Account id. |
  | id | string | yes | The ID of the Fastly service. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data object for Fastly service requests. |


## com.datadoghq.dd.integration.fastly.deleteFastlyAccount
**Delete Fastly account** — Delete a Fastly account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Fastly Account id. |


## com.datadoghq.dd.integration.fastly.deleteFastlyService
**Delete Fastly service** — Delete a Fastly service for an account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Fastly Account id. |
  | service_id | string | yes | Fastly Service ID. |


## com.datadoghq.dd.integration.fastly.getFastlyAccount
**Get Fastly account** — Get a Fastly account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Fastly Account id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data object of a Fastly account. |


## com.datadoghq.dd.integration.fastly.getFastlyService
**Get Fastly service** — Get a Fastly service for an account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Fastly Account id. |
  | service_id | string | yes | Fastly Service ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data object for Fastly service requests. |


## com.datadoghq.dd.integration.fastly.listFastlyAccounts
**List Fastly accounts** — List Fastly accounts.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The JSON:API data schema. |


## com.datadoghq.dd.integration.fastly.listFastlyServices
**List Fastly services** — List Fastly services for an account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Fastly Account id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The JSON:API data schema. |


## com.datadoghq.dd.integration.fastly.updateFastlyService
**Update Fastly service** — Update a Fastly service for an account.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tags | any | no | A list of tags for the Fastly service. |
  | account_id | string | yes | Fastly Account id. |
  | service_id | string | yes | Fastly Service ID. |
  | id | string | yes | The ID of the Fastly service. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data object for Fastly service requests. |

