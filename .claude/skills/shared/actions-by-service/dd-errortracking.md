# Datadog Error Tracking Actions
Bundle: `com.datadoghq.dd.errortracking` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eerrortracking)

## com.datadoghq.dd.errortracking.deleteIssueAssignee
**Delete issue assignee** — Remove the assignee of an issue by `issue_id`.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | issue_id | string | yes | The identifier of the issue. |


## com.datadoghq.dd.errortracking.getIssue
**Get issue** — Retrieve the full details for a specific error tracking issue, including attributes and relationships.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | issue_id | string | yes | The identifier of the issue. |
  | include | array<string> | no | Comma-separated list of relationship objects that should be included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The issue matching the request. |
  | included | array<object> | Array of resources related to the issue. |


## com.datadoghq.dd.errortracking.searchIssues
**Search issues** — Search issues endpoint allows you to programmatically search for issues within your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | array<string> | no | Comma-separated list of relationship objects that should be included in the response. |
  | from | number | yes | Start date (inclusive) of the query in milliseconds since the Unix epoch. |
  | order_by | string | no | The attribute to sort the search results by. |
  | persona | string | no | Persona for the search. |
  | query | string | yes | Search query following the event search syntax. |
  | to | number | yes | End date (exclusive) of the query in milliseconds since the Unix epoch. |
  | track | string | no | Track of the events to query. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of results matching the search query. |
  | included | array<object> | Array of resources related to the search results. |


## com.datadoghq.dd.errortracking.updateIssueAssignee
**Update issue assignee** — Update the assignee of an issue by `issue_id`.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | issue_id | string | yes | The identifier of the issue. |
  | id | string | yes | User identifier. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The issue matching the request. |
  | included | array<object> | Array of resources related to the issue. |


## com.datadoghq.dd.errortracking.updateIssueState
**Update issue state** — Update the state of an issue by `issue_id`.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | issue_id | string | yes | The identifier of the issue. |
  | state | string | yes | State of the issue. |
  | id | string | yes | Issue identifier. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The issue matching the request. |
  | included | array<object> | Array of resources related to the issue. |

