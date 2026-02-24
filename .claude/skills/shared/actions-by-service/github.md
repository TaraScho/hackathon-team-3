# GitHub Actions
Bundle: `com.datadoghq.github` | 18 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub)

## com.datadoghq.github.addLabelsToPR
**Add labels to pull request** — Add labels to an existing pull request.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | prNumber | number | yes |  |
  | labels | array<string> | yes | The names of the labels to add to the pull request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | labels | array<object> |  |


## com.datadoghq.github.addOrUpdateTeamMembership
**Add or update team member** — Add or update team membership for a GitHub user.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | organization | string | yes | The name of the GitHub organization. |
  | teamName | string | yes | The slug of the GitHub team name. This is typically the team name with hyphens instead of spaces. To see a list of team names and slugs, go to https://github.com/orgs/<YOUR_ORG>/teams. |
  | username | string | yes | The username of the team member to add or update. |
  | role | string | yes | The new role (member or maintainer) on the team for the specified GitHub user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string |  |
  | role | string |  |
  | state | string |  |


## com.datadoghq.github.checkPRStatus
**Get pull request status** — Get a pull request's status.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | prNumber | number | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | merged | boolean | Set to true if the pull request has been merged |
  | state | string | Whether this PR is open or closed |
  | mergeable | boolean | Whether this PR is mergeable or not |
  | mergeableState | string | Detailed status information about a pull request merge. |
  | author | object | Additional information about the author of the PR. |


## com.datadoghq.github.configChange
**Edit configuration files** — Perform modifications on configuration files, such as `yaml` or `ini`, and creates a pull request.
- Stability: stable
- Access: update, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The github repository, formatted as `{owner}/{repo}`, in which to perform the changes. Note: the format organization/repo.git is not supported. |
  | operations | array<object> | yes | The collection of operations to perform. |
  | targetBranch | string | no | The base branch of pull request. If not specified, we use the default branch (ex. main). If a new branch is created, it is created off of this branch. |
  | headBranch | string | no | Branch to create and put this commit on. If the branch already exists, changes will be force pushed. Defaults to "datadog-workflow-{{ InstanceId }}" |
  | createPr | boolean | no | If true, a pull request will be open with your changes. Defaults to true. |
  | prTitle | string | no | The title of the pull request to create. |
  | prDescription | string | no | The description for the pull request to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |
  | author | string |  |
  | title | string |  |


## com.datadoghq.github.createBranch
**Create branch** — Create a new branch.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | baseBranch | string | no | The base branch of pull request. If not specified, the default branch is used (ex. main). |
  | branchToCreate | string | no | The name of the branch to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | branch | string |  |
  | url | string |  |
  | sha | string |  |


## com.datadoghq.github.createComment
**Create comment** — Create a comment on a pull request.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | prNumber | number | yes |  |
  | body | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | commentId | number |  |
  | commentUrl | string |  |


## com.datadoghq.github.createIssue
**Create issue** — Create an issue.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | title | string | yes | The title of the issue. |
  | body | string | no | The contents of the issue. |
  | labels | array<string> | no | Labels to associate with this issue. |
  | assignees | array<string> | no | Github usernames for users to assign to this issue. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | issueNumber | number |  |
  | url | string |  |
  | state | string |  |


## com.datadoghq.github.createOrUpdateFile
**Create or update file** — Create or update a file in the specified GitHub repository.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The github repository, formatted as `{owner}/{repo}`, in which to perform the changes. Note: the format organization/repo.git is not supported. |
  | baseBranch | string | no | The base branch of pull request. If not specified, we use the default branch (ex. main). If a new branch is created, it is created off of this branch. |
  | branchWithChanges | string | no | Branch to create and put this commit on. If the branch already exists, changes will be force pushed. Defaults to `datadog-workflow-{{ InstanceId }}` |
  | path | string | yes | The path to the file to be created or updated. |
  | content | string | yes | The new contents of the file. |
  | createPr | boolean | no | If true, a pull request will be open with your changes. Defaults to true. |
  | prTitle | string | no | The title of the pull request to create. |
  | prDescription | string | no | The description for the pull request to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |
  | author | string |  |
  | title | string |  |


## com.datadoghq.github.createPullRequest
**Create pull request** — Create a pull request.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | baseBranch | string | no | The base branch of pull request. If not specified, we use the default branch (ex. main). |
  | branchWithChanges | string | no | The name of the branch where your changes are implemented. |
  | prTitle | string | no | The title of the pull request to create. |
  | prDescription | string | no | The description of the pull request. |
  | labels | array<string> | no | The names of the labels to add to the pull request. |
  | draft | boolean | no | Indicates whether the pull request is a draft. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |
  | author | string |  |
  | title | string |  |


## com.datadoghq.github.deleteFile
**Delete file** — Delete a file in the specified GitHub repository.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The github repository, formatted as `{owner}/{repo}`, in which to perform the changes. Note: the format organization/repo.git is not supported. |
  | baseBranch | string | no | The base branch of pull request. If not specified, we use the default branch (ex. main). If a new branch is created, it is created off of this branch. |
  | branchWithChanges | string | no | Branch to create and put this commit on. If the branch already exists, changes will be force pushed. Defaults to `datadog-workflow-{{ InstanceId }}` |
  | path | string | yes | The path to the file to be deleted. |
  | createPr | boolean | no | If true, a pull request will be open with your changes. Defaults to true. |
  | prTitle | string | no | The title of the pull request to create. |
  | prDescription | string | no | The description for the pull request to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any |  |
  | author | string |  |
  | title | string |  |


## com.datadoghq.github.getTeamMembership
**Get team membership** — Get team membership information for a GitHub user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | organization | string | yes | The name of the GitHub organization. |
  | teamName | string | yes | The slug of the GitHub team name. This is typically the team name with hyphens instead of spaces. To see a list of team names and slugs, go to https://github.com/orgs/<YOUR_ORG>/teams. |
  | username | string | yes | The username of the team member. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string |  |
  | role | string |  |
  | state | string |  |


## com.datadoghq.github.getUser
**Get user** — Get additional information about a user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | username | string | yes | The unique name of the user to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | user | object | Additional information about the supplied user. |


## com.datadoghq.github.listCommits
**List commits** — List commits in a repo.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | path | string | no | If specified, only commits containing this file path will be returned. |
  | timePeriod | any | no | Specify a time range for the commits. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | commits | array<object> |  |


## com.datadoghq.github.listPullRequests
**List pull requests** — List pull requests. Returns 30 pull requests max.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |
  | sourceBranch | string | no | Filter pull requests by source branch. Note that the source branch must have the same owner as the target repository. |
  | state | string | no | Filter pull requests by state. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | pullRequests | array<object> |  |


## com.datadoghq.github.listReleases
**List releases** — List releases in a repo.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | repository | string | yes | The target repository, with the format `{owner}/{repo}`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | releases | array<object> | List of releases |


## com.datadoghq.github.listTeamMembers
**List team members** — List members of given team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | organization | string | yes | The name of the GitHub organization. |
  | teamName | string | yes | The slug of the GitHub team name. This is typically the team name with hyphens instead of spaces. To see a list of team names and slugs, go to https://github.com/orgs/<YOUR_ORG>/teams. |
  | role | string | no | Optionally filter members by role in the team. Defaults to `all`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | members | array<object> | List of team members |


## com.datadoghq.github.removeTeamMembership
**Remove team member** — Remove team membership for a GitHub user.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | organization | string | yes | The name of the GitHub organization. |
  | teamName | string | yes | The slug of the GitHub team name. |
  | username | string | yes | The username of the team member to remove. |


## com.datadoghq.github.searchRepositories
**Search repositories** — Search for public GitHub repositories.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | yes | The query to search repositories. See GitHub docs for [search query syntax](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories). |
  | sort | string | no | Sorts the results of your query by number of stars, forks, help-wanted-issues, or how recently the items were updated. If not specified, best match will be returned. |
  | order | string | no | Determines whether the first search result returned is the highest number of matches (desc) or lowest number of matches (asc). This parameter is ignored unless you provide sort. Default: desc. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | repositories | array<object> |  |

