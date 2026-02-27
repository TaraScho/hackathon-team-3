# GitHub Repositories Actions
Bundle: `com.datadoghq.github.repos` | 31 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Erepos)

## com.datadoghq.github.repos.addCollaborator
**Add collaborator** — This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | username | string | yes | The handle for the GitHub user account. |
  | permission | string | no | The permission to grant the collaborator. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Add collaborator |


## com.datadoghq.github.repos.batchCreateOrUpdateFileContents
**Batch create or update file contents** — Create or update multiple files in a repository in batch.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | message | string | yes | The commit message. |
  | branch | string | no | The branch name. |
  | files | array<object> | yes | List of files to create or update. |
  | committer | object | no | The person that committed the file. |
  | author | object | no | The author of the file. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | commits | array<object> |  |


## com.datadoghq.github.repos.batchGetContents
**Batch get contents** — Batch get GitHub file contents.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | filePaths | array<string> | yes | Paths to the files. |
  | ref | string | no | The name of the commit/branch/tag. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | contents | array<object> |  |


## com.datadoghq.github.repos.checkCollaborator
**Check collaborator** — For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | username | string | yes | The handle for the GitHub user account. |


## com.datadoghq.github.repos.compareCommits
**Compare commits** — Compares two commits against one another.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | page | number | no | The page number of the results to fetch. |
  | per_page | number | no | The number of results per page (max 100). |
  | basehead | string | yes | The base branch and head branch to compare. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Compare commits |


## com.datadoghq.github.repos.createCommitStatus
**Create commit status** — Users with push access in a repository can create commit statuses for a given SHA.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | sha | string | yes |  |
  | state | string | yes | The state of the status. |
  | target_url | string | no | The target URL to associate with this status. |
  | description | string | no | A short description of the status. |
  | context | string | no | A string label to differentiate this status from the status of other systems. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Create commit status |


## com.datadoghq.github.repos.createInOrg
**Create a repository** — Create a new repository in the specified organization.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | org | string | yes | The organization name. |
  | name | string | yes | The name of the repository. |
  | description | string | no | A short description of the repository. |
  | homepage | string | no | A URL with more information about the repository. |
  | private | boolean | no | Whether the repository is private. |
  | visibility | string | no | The visibility of the repository. |
  | has_issues | boolean | no | Either `true` to enable issues for this repository or `false` to disable them. |
  | has_projects | boolean | no | Either `true` to enable projects for this repository or `false` to disable them. |
  | has_wiki | boolean | no | Either `true` to enable the wiki for this repository or `false` to disable it. |
  | has_downloads | boolean | no | Whether downloads are enabled. |
  | is_template | boolean | no | Either `true` to make this repo available as a template repository or `false` to prevent it. |
  | team_id | number | no | The id of the team that will be granted access to this repository. |
  | auto_init | boolean | no | Pass `true` to create an initial commit with empty README. |
  | gitignore_template | string | no | Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. |
  | license_template | string | no | Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://docs.github.com/articles/licensing-a-repository/#searchi... |
  | allow_squash_merge | boolean | no | Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging. |
  | allow_merge_commit | boolean | no | Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits. |
  | allow_rebase_merge | boolean | no | Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging. |
  | allow_auto_merge | boolean | no | Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge. |
  | delete_branch_on_merge | boolean | no | Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion. |
  | use_squash_pr_title_as_default | boolean | no | Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. |
  | squash_merge_commit_title | string | no | Required when using `squash_merge_commit_message`. |
  | squash_merge_commit_message | string | no | The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. |
  | merge_commit_title | string | no | Required when using `merge_commit_message`. |
  | merge_commit_message | string | no | The default value for a merge commit message. |
  | custom_properties | object | no | The custom properties for the new repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | number |  |
  | node_id | string |  |
  | name | string |  |
  | full_name | string |  |
  | owner | object | A GitHub user. |
  | private | boolean |  |
  | html_url | string |  |
  | description | string |  |
  | fork | boolean |  |
  | url | string |  |
  | archive_url | string |  |
  | assignees_url | string |  |
  | blobs_url | string |  |
  | branches_url | string |  |
  | collaborators_url | string |  |
  | comments_url | string |  |
  | commits_url | string |  |
  | compare_url | string |  |
  | contents_url | string |  |
  | contributors_url | string |  |
  | deployments_url | string |  |
  | downloads_url | string |  |
  | events_url | string |  |
  | forks_url | string |  |
  | git_commits_url | string |  |
  | git_refs_url | string |  |
  | git_tags_url | string |  |
  | git_url | string |  |
  | issue_comment_url | string |  |
  | issue_events_url | string |  |
  | issues_url | string |  |
  | keys_url | string |  |
  | labels_url | string |  |
  | languages_url | string |  |
  | merges_url | string |  |
  | milestones_url | string |  |
  | notifications_url | string |  |
  | pulls_url | string |  |
  | releases_url | string |  |
  | ssh_url | string |  |
  | stargazers_url | string |  |
  | statuses_url | string |  |
  | subscribers_url | string |  |
  | subscription_url | string |  |
  | tags_url | string |  |
  | teams_url | string |  |
  | trees_url | string |  |
  | clone_url | string |  |
  | mirror_url | string |  |
  | hooks_url | string |  |
  | svn_url | string |  |
  | homepage | string |  |
  | language | string |  |
  | forks_count | number |  |
  | stargazers_count | number |  |
  | watchers_count | number |  |
  | size | number | The size of the repository, in kilobytes. |
  | default_branch | string |  |
  | open_issues_count | number |  |
  | is_template | boolean |  |
  | topics | array<string> |  |
  | has_issues | boolean |  |
  | has_projects | boolean |  |
  | has_wiki | boolean |  |
  | has_pages | boolean |  |
  | has_downloads | boolean |  |
  | has_discussions | boolean |  |
  | archived | boolean |  |
  | disabled | boolean | Returns whether or not this repository disabled. |
  | visibility | string | The repository visibility: public, private, or internal. |
  | pushed_at | string |  |
  | created_at | string |  |
  | updated_at | string |  |
  | permissions | object |  |
  | allow_rebase_merge | boolean |  |
  | template_repository | object | A repository on GitHub. |
  | temp_clone_token | string |  |
  | allow_squash_merge | boolean |  |
  | allow_auto_merge | boolean |  |
  | delete_branch_on_merge | boolean |  |
  | allow_merge_commit | boolean |  |
  | allow_update_branch | boolean |  |
  | use_squash_pr_title_as_default | boolean |  |
  | squash_merge_commit_title | string | The default value for a squash merge commit title:  - `PR_TITLE` - default to the pull request's title. |
  | squash_merge_commit_message | string | The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. |
  | merge_commit_title | string | The default value for a merge commit title. |
  | merge_commit_message | string | The default value for a merge commit message. |
  | allow_forking | boolean |  |
  | web_commit_signoff_required | boolean |  |
  | subscribers_count | number |  |
  | network_count | number |  |
  | license | object | License Simple. |
  | organization | object | A GitHub user. |
  | parent | object | A repository on GitHub. |
  | source | object | A repository on GitHub. |
  | forks | number |  |
  | master_branch | string |  |
  | open_issues | number |  |
  | watchers | number |  |
  | anonymous_access_enabled | boolean | Whether anonymous git access is allowed. |
  | code_of_conduct | object | Code of Conduct Simple. |
  | security_and_analysis | object |  |
  | custom_properties | object | The custom properties that were defined for the repository. |


## com.datadoghq.github.repos.createOrUpdateFileContents
**Create or update file contents** — Create a new file or replace an existing file in a repository.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | path | string | yes | path parameter. |
  | message | string | yes | The commit message. |
  | content | string | yes | The new file content, using Base64 encoding. |
  | sha | string | no | **Required if you are updating a file**. |
  | branch | string | no | The branch name. |
  | committer | object | no | The person that committed the file. |
  | author | object | no | The author of the file. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | content | object |  |
  | commit | object |  |


## com.datadoghq.github.repos.createUsingTemplate
**Create using template** — Creates a new repository using a repository template.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | template_owner | string | yes | The account owner of the template repository. |
  | template_repo | string | yes | The name of the template repository without the `.git` extension. |
  | owner | string | no | The organization or person who will own the new repository. |
  | name | string | yes | The name of the new repository. |
  | description | string | no | A short description of the new repository. |
  | include_all_branches | boolean | no | Set to `true` to include the directory structure and files from all branches in the template repository, and not just the default branch. |
  | private | boolean | no | Either `true` to create a new private repository or `false` to create a new public one. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Create using template |


## com.datadoghq.github.repos.deleteBranchProtection
**Delete branch protection** — Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | branch | string | yes | The name of the branch. |


## com.datadoghq.github.repos.deleteFile
**Delete file** — Deletes a file in a repository.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | path | string | yes | path parameter. |
  | message | string | yes | The commit message. |
  | sha | string | yes | The blob SHA of the file being deleted. |
  | branch | string | no | The branch name. |
  | committer | object | no | object containing information about the committer. |
  | author | object | no | object containing information about the author. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Delete file |


## com.datadoghq.github.repos.deleteResource
**Delete** — Deleting a repository requires admin access.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |


## com.datadoghq.github.repos.get
**Get a repository** — The `parent` and `source` objects are present when the repository is a fork.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | number |  |
  | node_id | string |  |
  | name | string |  |
  | full_name | string |  |
  | owner | object | A GitHub user. |
  | private | boolean |  |
  | html_url | string |  |
  | description | string |  |
  | fork | boolean |  |
  | url | string |  |
  | archive_url | string |  |
  | assignees_url | string |  |
  | blobs_url | string |  |
  | branches_url | string |  |
  | collaborators_url | string |  |
  | comments_url | string |  |
  | commits_url | string |  |
  | compare_url | string |  |
  | contents_url | string |  |
  | contributors_url | string |  |
  | deployments_url | string |  |
  | downloads_url | string |  |
  | events_url | string |  |
  | forks_url | string |  |
  | git_commits_url | string |  |
  | git_refs_url | string |  |
  | git_tags_url | string |  |
  | git_url | string |  |
  | issue_comment_url | string |  |
  | issue_events_url | string |  |
  | issues_url | string |  |
  | keys_url | string |  |
  | labels_url | string |  |
  | languages_url | string |  |
  | merges_url | string |  |
  | milestones_url | string |  |
  | notifications_url | string |  |
  | pulls_url | string |  |
  | releases_url | string |  |
  | ssh_url | string |  |
  | stargazers_url | string |  |
  | statuses_url | string |  |
  | subscribers_url | string |  |
  | subscription_url | string |  |
  | tags_url | string |  |
  | teams_url | string |  |
  | trees_url | string |  |
  | clone_url | string |  |
  | mirror_url | string |  |
  | hooks_url | string |  |
  | svn_url | string |  |
  | homepage | string |  |
  | language | string |  |
  | forks_count | number |  |
  | stargazers_count | number |  |
  | watchers_count | number |  |
  | size | number | The size of the repository, in kilobytes. |
  | default_branch | string |  |
  | open_issues_count | number |  |
  | is_template | boolean |  |
  | topics | array<string> |  |
  | has_issues | boolean |  |
  | has_projects | boolean |  |
  | has_wiki | boolean |  |
  | has_pages | boolean |  |
  | has_downloads | boolean |  |
  | has_discussions | boolean |  |
  | archived | boolean |  |
  | disabled | boolean | Returns whether or not this repository disabled. |
  | visibility | string | The repository visibility: public, private, or internal. |
  | pushed_at | string |  |
  | created_at | string |  |
  | updated_at | string |  |
  | permissions | object |  |
  | allow_rebase_merge | boolean |  |
  | template_repository | object | A repository on GitHub. |
  | temp_clone_token | string |  |
  | allow_squash_merge | boolean |  |
  | allow_auto_merge | boolean |  |
  | delete_branch_on_merge | boolean |  |
  | allow_merge_commit | boolean |  |
  | allow_update_branch | boolean |  |
  | use_squash_pr_title_as_default | boolean |  |
  | squash_merge_commit_title | string | The default value for a squash merge commit title:  - `PR_TITLE` - default to the pull request's title. |
  | squash_merge_commit_message | string | The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. |
  | merge_commit_title | string | The default value for a merge commit title. |
  | merge_commit_message | string | The default value for a merge commit message. |
  | allow_forking | boolean |  |
  | web_commit_signoff_required | boolean |  |
  | subscribers_count | number |  |
  | network_count | number |  |
  | license | object | License Simple. |
  | organization | object | A GitHub user. |
  | parent | object | A repository on GitHub. |
  | source | object | A repository on GitHub. |
  | forks | number |  |
  | master_branch | string |  |
  | open_issues | number |  |
  | watchers | number |  |
  | anonymous_access_enabled | boolean | Whether anonymous git access is allowed. |
  | code_of_conduct | object | Code of Conduct Simple. |
  | security_and_analysis | object |  |
  | custom_properties | object | The custom properties that were defined for the repository. |


## com.datadoghq.github.repos.getBranch
**Get a branch** — Get a branch from a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | branch | string | yes | The name of the branch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | name | string |  |
  | commit | object | Commit. |
  | links | object |  |
  | protected | boolean |  |
  | protection | object | Branch Protection. |
  | protection_url | string |  |
  | pattern | string |  |
  | required_approving_review_count | number |  |


## com.datadoghq.github.repos.getBranchProtection
**Get branch protection** — Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | branch | string | yes | The name of the branch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get branch protection |


## com.datadoghq.github.repos.getCommit
**Get commit** — Returns the contents of a single commit reference.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | page | number | no | The page number of the results to fetch. |
  | per_page | number | no | The number of results per page (max 100). |
  | ref | string | yes | The commit reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get commit |


## com.datadoghq.github.repos.getContent
**Get repository content** — Get the contents of a file or directory in a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | path | string | yes | path parameter. |
  | ref | string | no | The name of the commit/branch/tag. |


## com.datadoghq.github.repos.getReadme
**Get readme** — Gets the preferred README for a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | ref | string | no | The name of the commit/branch/tag. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get readme |


## com.datadoghq.github.repos.listBranches
**List branches** — List branches for a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | protected | boolean | no | Setting to `true` returns only branches protected by branch protections or rulesets. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List branches |


## com.datadoghq.github.repos.listCollaborators
**List collaborators** — For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | affiliation | string | no | Filter collaborators returned by their affiliation. |
  | permission | string | no | Filter collaborators by the permissions they have on the repository. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List collaborators |


## com.datadoghq.github.repos.listCommitStatusesForRef
**List commit statuses for ref** — Users with pull access in a repository can view commit statuses for a given ref.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | ref | string | yes | The commit reference. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List commit statuses for ref |


## com.datadoghq.github.repos.listCommits
**List commits** — **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | sha | string | no | SHA or branch to start listing commits from. |
  | path | string | no | Only commits containing this file path will be returned. |
  | author | string | no | GitHub username or email address to use to filter by commit author. |
  | committer | string | no | GitHub username or email address to use to filter by commit committer. |
  | since | string | no | Only show results that were last updated after the given time. |
  | until | string | no | Only commits before this date will be returned. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List commits |


## com.datadoghq.github.repos.listForOrg
**List repos for org** — List repositories for the specified organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | org | string | yes | The organization name. |
  | type | string | no | Specifies the types of repositories you want returned. |
  | sort | string | no | The property to sort the results by. |
  | direction | string | no | The order to sort by. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |


## com.datadoghq.github.repos.listForUser
**List for user** — Lists public repositories for the specified user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | username | string | yes | The handle for the GitHub user account. |
  | type | string | no | Limit results to repositories of the specified type. |
  | sort | string | no | The property to sort the results by. |
  | direction | string | no | The order to sort by. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List for user |


## com.datadoghq.github.repos.listLanguages
**List languages** — Lists languages for the specified repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for List languages |


## com.datadoghq.github.repos.listPullRequestsAssociatedWithCommit
**List pull requests associated with commit** — Lists the merged pull request that introduced the commit to the repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | commit_sha | string | yes | The SHA of the commit. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List pull requests associated with commit |


## com.datadoghq.github.repos.merge
**Merge** — Merge a branch.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | base | string | yes | The name of the base branch that the head will be merged into. |
  | head | string | yes | The head to merge. |
  | commit_message | string | no | Commit message to use for the merge commit. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Merge |


## com.datadoghq.github.repos.removeCollaborator
**Remove collaborator** — Removes a collaborator from a repository.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | username | string | yes | The handle for the GitHub user account. |


## com.datadoghq.github.repos.renameBranch
**Rename branch** — Renames a branch in a repository.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | branch | string | yes | The name of the branch. |
  | new_name | string | yes | The new name of the branch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Rename branch |


## com.datadoghq.github.repos.update
**Update** — **Note**: To edit a repository's topics, use the [Replace all repository topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) endpoint.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | name | string | no | The name of the repository. |
  | description | string | no | A short description of the repository. |
  | homepage | string | no | A URL with more information about the repository. |
  | private | boolean | no | Either `true` to make the repository private or `false` to make it public. |
  | visibility | string | no | The visibility of the repository. |
  | security_and_analysis | object | no | Specify which security and analysis features to enable or disable for the repository. |
  | has_issues | boolean | no | Either `true` to enable issues for this repository or `false` to disable them. |
  | has_projects | boolean | no | Either `true` to enable projects for this repository or `false` to disable them. |
  | has_wiki | boolean | no | Either `true` to enable the wiki for this repository or `false` to disable it. |
  | is_template | boolean | no | Either `true` to make this repo available as a template repository or `false` to prevent it. |
  | default_branch | string | no | Updates the default branch for this repository. |
  | allow_squash_merge | boolean | no | Either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging. |
  | allow_merge_commit | boolean | no | Either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits. |
  | allow_rebase_merge | boolean | no | Either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging. |
  | allow_auto_merge | boolean | no | Either `true` to allow auto-merge on pull requests, or `false` to disallow auto-merge. |
  | delete_branch_on_merge | boolean | no | Either `true` to allow automatically deleting head branches when pull requests are merged, or `false` to prevent automatic deletion. |
  | allow_update_branch | boolean | no | Either `true` to always allow a pull request head branch that is behind its base branch to be updated even if it is not required to be up to date before merging, or false otherwise. |
  | use_squash_pr_title_as_default | boolean | no | Either `true` to allow squash-merge commits to use pull request title, or `false` to use commit message. |
  | squash_merge_commit_title | string | no | Required when using `squash_merge_commit_message`. |
  | squash_merge_commit_message | string | no | The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. |
  | merge_commit_title | string | no | Required when using `merge_commit_message`. |
  | merge_commit_message | string | no | The default value for a merge commit message. |
  | archived | boolean | no | Whether to archive this repository. |
  | allow_forking | boolean | no | Either `true` to allow private forks, or `false` to prevent private forks. |
  | web_commit_signoff_required | boolean | no | Either `true` to require contributors to sign off on web-based commits, or `false` to not require contributors to sign off on web-based commits. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Update |


## com.datadoghq.github.repos.updateBranchProtection
**Update branch protection** — Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | branch | string | yes | The name of the branch. |
  | required_status_checks | object | yes | Require status checks to pass before merging. |
  | enforce_admins | boolean | yes | Enforce all configured restrictions for administrators. |
  | required_pull_request_reviews | object | yes | Require at least one approving review on a pull request, before merging. |
  | restrictions | object | yes | Restrict who can push to the protected branch. |
  | required_linear_history | boolean | no | Enforces a linear commit Git history, which prevents anyone from pushing merge commits to a branch. |
  | allow_force_pushes | boolean | no | Permits force pushes to the protected branch by anyone with write access to the repository. |
  | allow_deletions | boolean | no | Allows deletion of the protected branch by anyone with write access to the repository. |
  | block_creations | boolean | no | If set to `true`, the `restrictions` branch protection settings which limits who can push will also block pushes which create new branches, unless the push is initiated by a user, team, or app whic... |
  | required_conversation_resolution | boolean | no | Requires all conversations on code to be resolved before a pull request can be merged into a branch that matches this rule. |
  | lock_branch | boolean | no | Whether to set the branch as read-only. |
  | allow_fork_syncing | boolean | no | Whether users can pull changes from upstream when the branch is locked. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Update branch protection |

