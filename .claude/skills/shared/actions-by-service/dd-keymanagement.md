# Datadog Key Management Actions
Bundle: `com.datadoghq.dd.keymanagement` | 10 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ekeymanagement)

## com.datadoghq.dd.keymanagement.deleteAPIKey
**Delete API key** — Delete an API key.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | api_key_id | string | yes | The ID of the API key. |


## com.datadoghq.dd.keymanagement.deleteApplicationKey
**Delete application key** — Delete an application key.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_key_id | string | yes | The ID of the application key. |


## com.datadoghq.dd.keymanagement.deleteCurrentUserApplicationKey
**Delete current user application key** — Delete an application key owned by current user.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_key_id | string | yes | The ID of the application key. |


## com.datadoghq.dd.keymanagement.getCurrentUserApplicationKey
**Get current user application key** — Get an application key owned by current user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_key_id | string | yes | The ID of the application key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Datadog application key. |
  | included | array<object> | Array of objects related to the application key. |


## com.datadoghq.dd.keymanagement.listAPIKeys
**List API keys** — List all API keys available for your account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_created_at | any | no | Only include API keys created between the specified date range. |
  | filter_modified_at | any | no | Only include API keys modified between the specified date range. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | API key attribute used to sort results. |
  | filter | string | no | Filter API keys by the specified string. |
  | include | string | no | Comma separated list of resource paths for related resources to include in the response. |
  | filter_remote_config_read_enabled | boolean | no | Filter API keys by remote config read enabled status. |
  | filter_category | string | no | Filter API keys by category. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of API keys. |
  | included | array<object> | Array of objects related to the API key. |
  | meta | object | Additional information related to api keys response. |


## com.datadoghq.dd.keymanagement.listApplicationKeys
**List application keys** — List all application keys available for your org.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_created_at | any | no | Only include application keys created between the specified date range. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Application key attribute used to sort results. |
  | filter | string | no | Filter application keys by the specified string. |
  | include | string | no | Resource path for related resources to include in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of application keys. |
  | included | array<object> | Array of objects related to the application key. |
  | meta | object | Additional information related to the application key response. |


## com.datadoghq.dd.keymanagement.listCurrentUserApplicationKeys
**List current user application keys** — List all application keys available for current user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_created_at | any | no | Only include application keys created between the specified date range. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Application key attribute used to sort results. |
  | filter | string | no | Filter application keys by the specified string. |
  | include | string | no | Resource path for related resources to include in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of application keys. |
  | included | array<object> | Array of objects related to the application key. |
  | meta | object | Additional information related to the application key response. |


## com.datadoghq.dd.keymanagement.updateAPIKey
**Update API key** — Update an API key.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | api_key_id | string | yes | The ID of the API key. |
  | category | string | no | The APIKeyUpdateAttributes category. |
  | name | string | yes | Name of the API key. |
  | remote_config_read_enabled | boolean | no | The APIKeyUpdateAttributes remote_config_read_enabled. |
  | id | string | yes | ID of the API key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Datadog API key. |
  | included | array<object> | Array of objects related to the API key. |


## com.datadoghq.dd.keymanagement.updateApplicationKey
**Update application key** — Edit an application key.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_key_id | string | yes | The ID of the application key. |
  | name | string | no | Name of the application key. |
  | scopes | array<string> | no | Array of scopes to grant the application key. |
  | id | string | yes | ID of the application key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Datadog application key. |
  | included | array<object> | Array of objects related to the application key. |


## com.datadoghq.dd.keymanagement.updateCurrentUserApplicationKey
**Update current user application key** — Edit an application key owned by current user.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | app_key_id | string | yes | The ID of the application key. |
  | name | string | no | Name of the application key. |
  | scopes | array<string> | no | Array of scopes to grant the application key. |
  | id | string | yes | ID of the application key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Datadog application key. |
  | included | array<object> | Array of objects related to the application key. |

