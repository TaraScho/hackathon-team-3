# Github Teams Actions
Bundle: `com.datadoghq.github.teams` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Eteams)

## com.datadoghq.github.teams.getByName
**Get by name** — Gets a team using the team's `slug`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | org | string | yes | The organization name. |
  | team_slug | string | yes | The slug of the team name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get by name |

