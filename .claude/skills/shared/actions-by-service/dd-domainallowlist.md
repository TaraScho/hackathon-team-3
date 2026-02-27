# Datadog Domain Allowlist Actions
Bundle: `com.datadoghq.dd.domainallowlist` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edomainallowlist)

## com.datadoghq.dd.domainallowlist.getDomainAllowlist
**Get domain allowlist** — Get the domain allowlist for an organization.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The email domain allowlist response for an org. |


## com.datadoghq.dd.domainallowlist.patchDomainAllowlist
**Update domain allowlist** — Update the domain allowlist for an organization.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | domains | array<string> | yes | The list of domains in the email domain allowlist. |
  | enabled | boolean | no | Whether the email domain allowlist is enabled for the org. |
  | id | string | no | The unique identifier of the org. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The email domain allowlist response for an org. |

