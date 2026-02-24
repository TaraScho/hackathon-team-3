# Datadog Microsoft Teams Integration Actions
Bundle: `com.datadoghq.dd.integration.msteams` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Emsteams)

## com.datadoghq.dd.integration.msteams.createTenantBasedHandle
**Create tenant based handle** — Create a tenant-based handle in the Datadog Microsoft Teams integration.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | channel_id | string | yes | Channel id. |
  | name | string | yes | Tenant-based handle name. |
  | team_id | string | yes | Team id. |
  | tenant_id | string | yes | Tenant id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Tenant-based handle data from a response. |


## com.datadoghq.dd.integration.msteams.createWorkflowsWebhookHandle
**Create Workflows webhook handle** — Create a Workflows webhook handle in the Datadog Microsoft Teams integration.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | yes | Workflows Webhook handle name. |
  | url | string | yes | Workflows Webhook URL. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Workflows Webhook handle data from a response. |


## com.datadoghq.dd.integration.msteams.deleteTenantBasedHandle
**Delete tenant based handle** — Delete a tenant-based handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your tenant-based handle id. |


## com.datadoghq.dd.integration.msteams.deleteWorkflowsWebhookHandle
**Delete Workflows webhook handle** — Delete a Workflows webhook handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your Workflows webhook handle id. |


## com.datadoghq.dd.integration.msteams.getChannelByName
**Get channel by name** — Get the tenant, team, and channel ID of a channel in the Datadog Microsoft Teams integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tenant_name | string | yes | Your tenant name. |
  | team_name | string | yes | Your team name. |
  | channel_name | string | yes | Your channel name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Channel data from a response. |


## com.datadoghq.dd.integration.msteams.getTenantBasedHandle
**Get tenant based handle** — Get the tenant, team, and channel information of a tenant-based handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your tenant-based handle id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Tenant-based handle data from a response. |


## com.datadoghq.dd.integration.msteams.getWorkflowsWebhookHandle
**Get Workflows webhook handle** — Get the name of a Workflows webhook handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your Workflows webhook handle id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Workflows Webhook handle data from a response. |


## com.datadoghq.dd.integration.msteams.listTenantBasedHandles
**List tenant based handles** — Get a list of all tenant-based handles from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tenant_id | string | no | Your tenant id. |
  | name | string | no | Your tenant-based handle name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of tenant-based handles. |


## com.datadoghq.dd.integration.msteams.listWorkflowsWebhookHandles
**List Workflows webhook handles** — Get a list of all Workflows webhook handles from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | name | string | no | Your Workflows webhook handle name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of Workflows webhook handles. |


## com.datadoghq.dd.integration.msteams.updateTenantBasedHandle
**Update tenant based handle** — Update a tenant-based handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your tenant-based handle id. |
  | channel_id | string | no | Channel id. |
  | name | string | no | Tenant-based handle name. |
  | team_id | string | no | Team id. |
  | tenant_id | string | no | Tenant id. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Tenant-based handle data from a response. |


## com.datadoghq.dd.integration.msteams.updateWorkflowsWebhookHandle
**Update Workflows webhook handle** — Update a Workflows webhook handle from the Datadog Microsoft Teams integration.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | handle_id | string | yes | Your Workflows webhook handle id. |
  | name | string | no | Workflows Webhook handle name. |
  | url | string | no | Workflows Webhook URL. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Workflows Webhook handle data from a response. |

