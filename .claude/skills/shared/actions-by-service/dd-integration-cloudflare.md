# Datadog Cloudflare Integration Actions
Bundle: `com.datadoghq.dd.integration.cloudflare` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Ecloudflare)

## com.datadoghq.dd.integration.cloudflare.deleteCloudflareAccount
**Delete Cloudflare account** — Delete a Cloudflare account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | None. |


## com.datadoghq.dd.integration.cloudflare.getCloudflareAccount
**Get Cloudflare account** — Get a Cloudflare account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | None. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data object of a Cloudflare account. |


## com.datadoghq.dd.integration.cloudflare.listCloudflareAccounts
**List Cloudflare accounts** — List Cloudflare accounts.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The JSON:API data schema. |

