# Github Orgs Actions
Bundle: `com.datadoghq.github.orgs` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Eorgs)

## com.datadoghq.github.orgs.getMembershipForUser
**Get membership for user** — In order to get a user's membership with an organization, the authenticated user must be an organization member.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | org | string | yes | The organization name. |
  | username | string | yes | The handle for the GitHub user account. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get membership for user |

