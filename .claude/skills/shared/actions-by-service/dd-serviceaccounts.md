# Datadog Service Accounts Actions
Bundle: `com.datadoghq.dd.serviceaccounts` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eserviceaccounts)

## com.datadoghq.dd.serviceaccounts.createServiceAccount
**Create service account** — Create a service account for your organization.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | email | string | yes | The email of the user. |
  | name | string | no | The name of the user. |
  | service_account | boolean | yes | Whether the user is a service account. |
  | title | string | no | The title of the user. |
  | relationships | object | no | Relationships of the user object. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | User object returned by the API. |
  | included | array<object> | Array of objects related to the user. |


## com.datadoghq.dd.serviceaccounts.deleteServiceAccountApplicationKey
**Delete service account application key** — Delete an application key owned by this service account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service_account_id | string | yes | The ID of the service account. |
  | app_key_id | string | yes | The ID of the application key. |


## com.datadoghq.dd.serviceaccounts.getServiceAccountApplicationKey
**Get service account application key** — Get an application key owned by this service account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service_account_id | string | yes | The ID of the service account. |
  | app_key_id | string | yes | The ID of the application key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Partial Datadog application key. |
  | included | array<object> | Array of objects related to the application key. |


## com.datadoghq.dd.serviceaccounts.listServiceAccountApplicationKeys
**List service account application keys** — List all application keys available for this service account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | If specified, this will limit the search to application keys created within the specified timeframe. |
  | service_account_id | string | yes | The ID of the service account. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Application key attribute used to sort results. |
  | filter | string | no | Filter application keys by the specified string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of application keys. |
  | included | array<object> | Array of objects related to the application key. |
  | meta | object | Additional information related to the application key response. |


## com.datadoghq.dd.serviceaccounts.updateServiceAccountApplicationKey
**Update service account application key** — Edit an application key owned by this service account.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service_account_id | string | yes | The ID of the service account. |
  | app_key_id | string | yes | The ID of the application key. |
  | name | string | no | Name of the application key. |
  | scopes | array<string> | no | Array of scopes to grant the application key. |
  | id | string | yes | ID of the application key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Partial Datadog application key. |
  | included | array<object> | Array of objects related to the application key. |

