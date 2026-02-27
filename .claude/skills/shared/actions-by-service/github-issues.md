# GitHub Issues Actions
Bundle: `com.datadoghq.github.issues` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Eissues)

## com.datadoghq.github.issues.listComments
**List comments** — You can use the REST API to list comments on issues and pull requests.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | issue_number | number | yes | The number that identifies the issue. |
  | since | string | no | Only show results that were last updated after the given time. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List comments |


## com.datadoghq.github.issues.listForRepo
**List for repo** — List issues in a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | milestone | string | no | If an `integer` is passed, it should refer to a milestone by its `number` field. |
  | state | string | no | Indicates the state of the issues to return. |
  | assignee | string | no | Can be the name of a user. |
  | creator | string | no | The user that created the issue. |
  | mentioned | string | no | A user that's mentioned in the issue. |
  | labels | string | no | A list of comma separated label names. |
  | sort | string | no | What to sort results by. |
  | direction | string | no | The direction to sort the results by. |
  | since | string | no | Only show results that were last updated after the given time. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List for repo |

