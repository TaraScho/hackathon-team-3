# Datadog Case Management Actions
Bundle: `com.datadoghq.dd.casem` | 17 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecasem)

## com.datadoghq.dd.casem.addComment
**Add comment** — Add a comment to a case in Datadog.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | The case key. |
  | comment | string | yes | Comment to post on this case. |


## com.datadoghq.dd.casem.archiveCase
**Archive case** — Archive case.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | Case's UUID or key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A case. |


## com.datadoghq.dd.casem.assignCase
**Assign case** — Assign case to a user.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | Case's UUID or key. |
  | assignee_id | string | yes | Assignee's UUID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A case. |


## com.datadoghq.dd.casem.createCase
**Create case** — Create a new case in Datadog.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | The Project this case relates to. |
  | type_id | string | no |  |
  | assignee_id | string | no | The ID of the user assigned to this case. |
  | services | array<string> | no | The services this case relates to. |
  | teams | array<string> | no | The teams this case relates to. |
  | envs | array<string> | no | The environments this case relates to. |
  | datacenters | array<string> | no | The datacenters this case relates to. |
  | description | string | no |  |
  | priority | string | no |  |
  | status_name | string | no |  |
  | status | string | no |  |
  | title | string | yes |  |
  | type | string | no |  |
  | attachment_links | array<string> | no | List of attachments linked to the case - can be security signals, monitors or error tracking issues. |
  | with_notebook | boolean | no | Whether to create a notebook with the case. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | key | string | This case's key |
  | id | string | This case's ID. |
  | project_id | string | The Project this case relates to. |
  | assignee_id | string | This case's assigned User ID. |
  | services | array<string> | List of services this case relates to. |
  | teams | array<string> | List of teams this case relates to. |
  | envs | array<string> | List of environments this case relates to. |
  | datacenters | array<string> | List of datacenters this case relates to. |
  | attributes | object | List of attributes this case relates to. |
  | custom_attributes | object | List of custom attributes this case relates to. |
  | description | string |  |
  | priority | string |  |
  | status | string |  |
  | status_name | string |  |
  | status_group | string |  |
  | title | string |  |
  | type | string |  |
  | attachments | array<object> |  |
  | investigation_notebook_id | string | The investigation notebook ID linked to this case. |
  | url | string | The case URL. |
  | archivedAt | string | Timestamp of when the case was archived. |
  | closedAt | string | Timestamp of when the case was closed. |
  | createdAt | string | Timestamp of when the case was created. |


## com.datadoghq.dd.casem.createProject
**Create project** — Create a project.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | key | string | yes | Project's key. |
  | name | string | yes | name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A Project. |


## com.datadoghq.dd.casem.deleteProject
**Delete project** — Remove a project using the project's `id`.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | Project UUID. |


## com.datadoghq.dd.casem.enrichCase
**List cases (enrich)** — Return a list of cases.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | search | string | no | Returns the list of items matching the search criteria. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | options | array<object> | List of results to display in the dropdown. |
  | placeholder | string | Placeholder text to display when the dropdown has no selection |
  | icon | object | Icon to display in the dropdown. |


## com.datadoghq.dd.casem.enrichProject
**List projects (enrich)** — Return a list of projects.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | search | string | no | Returns the list of items matching the search criteria. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | options | array<object> | List of results to display in the dropdown. |
  | placeholder | string | Placeholder text to display when the dropdown has no selection |
  | icon | object | Icon to display in the dropdown. |


## com.datadoghq.dd.casem.enrichProjectWithJira
**List projects with Jira integration (enrich)** — Return a list of projects with Jira integration configured.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | search | string | no | Returns the list of items matching the search criteria. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | options | array<object> | List of results to display in the dropdown. |
  | placeholder | string | Placeholder text to display when the dropdown has no selection |
  | icon | object | Icon to display in the dropdown. |


## com.datadoghq.dd.casem.getCase
**Get case** — Get a case in Datadog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | key | string | yes | The case key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | key | string | This case's key |
  | id | string | This case's ID. |
  | project_id | string | The Project this case relates to. |
  | assignee_id | string | This case's assigned User ID. |
  | services | array<string> | List of services this case relates to. |
  | teams | array<string> | List of teams this case relates to. |
  | envs | array<string> | List of environments this case relates to. |
  | datacenters | array<string> | List of datacenters this case relates to. |
  | attributes | object | List of attributes this case relates to. |
  | custom_attributes | object | List of custom attributes this case relates to. |
  | description | string |  |
  | priority | string |  |
  | status | string |  |
  | status_name | string |  |
  | status_group | string |  |
  | title | string |  |
  | type | string |  |
  | attachments | array<object> |  |
  | investigation_notebook_id | string | The investigation notebook ID linked to this case. |
  | url | string | The case URL. |
  | archivedAt | string | Timestamp of when the case was archived. |
  | closedAt | string | Timestamp of when the case was closed. |
  | createdAt | string | Timestamp of when the case was created. |


## com.datadoghq.dd.casem.getProject
**Get project** — Get the details of a project by `project_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | Project UUID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A Project. |


## com.datadoghq.dd.casem.getProjects
**Get projects** — Get all projects.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Projects response data. |


## com.datadoghq.dd.casem.searchCases
**Search cases** — Search cases.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort_field | string | no | Specify which field to sort. |
  | filter | string | no | Search query. |
  | sort_asc | boolean | no | Specify if order is ascending or not. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Cases response data. |
  | meta | object | Cases response metadata. |


## com.datadoghq.dd.casem.unarchiveCase
**Unarchive case** — Unarchive case.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | Case's UUID or key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A case. |


## com.datadoghq.dd.casem.unassignCase
**Unassign case** — Unassign case.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | Case's UUID or key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A case. |


## com.datadoghq.dd.casem.updatePriority
**Update priority** — Update case priority.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | Case's UUID or key. |
  | priority | string | yes | Case priority. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A case. |


## com.datadoghq.dd.casem.updateStatus
**Update status** — Update the status of a case in Datadog.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | The case key. |
  | status_name | string | no |  |
  | status | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | key | string | This case's key |
  | id | string | This case's ID. |
  | project_id | string | The Project this case relates to. |
  | assignee_id | string | This case's assigned User ID. |
  | services | array<string> | List of services this case relates to. |
  | teams | array<string> | List of teams this case relates to. |
  | envs | array<string> | List of environments this case relates to. |
  | datacenters | array<string> | List of datacenters this case relates to. |
  | attributes | object | List of attributes this case relates to. |
  | custom_attributes | object | List of custom attributes this case relates to. |
  | description | string |  |
  | priority | string |  |
  | status | string |  |
  | status_name | string |  |
  | status_group | string |  |
  | title | string |  |
  | type | string |  |
  | attachments | array<object> |  |
  | investigation_notebook_id | string | The investigation notebook ID linked to this case. |
  | url | string | The case URL. |
  | archivedAt | string | Timestamp of when the case was archived. |
  | closedAt | string | Timestamp of when the case was closed. |
  | createdAt | string | Timestamp of when the case was created. |

