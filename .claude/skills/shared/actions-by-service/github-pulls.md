# GitHub Pull Requests Actions
Bundle: `com.datadoghq.github.pulls` | 20 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Epulls)

## com.datadoghq.github.pulls.checkIfMerged
**Check if merged** — Checks if a pull request has been merged into the base branch.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |


## com.datadoghq.github.pulls.create
**Create pull request** — Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | title | string | no | The title of the new pull request. |
  | head | string | yes | The name of the branch where your changes are implemented. |
  | head_repo | string | no | The name of the repository where the changes in the pull request were made. |
  | base | string | yes | The name of the branch you want the changes pulled into. |
  | body | string | no | The contents of the pull request. |
  | maintainer_can_modify | boolean | no | Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request. |
  | draft | boolean | no | Indicates whether the pull request is a draft. |
  | issue | number | no | An issue in the repository to convert to a pull request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string |  |
  | id | number |  |
  | node_id | string |  |
  | html_url | string |  |
  | diff_url | string |  |
  | patch_url | string |  |
  | issue_url | string |  |
  | commits_url | string |  |
  | review_comments_url | string |  |
  | review_comment_url | string |  |
  | comments_url | string |  |
  | statuses_url | string |  |
  | number | number | Number uniquely identifying the pull request within its repository. |
  | state | string | State of this Pull Request. |
  | locked | boolean |  |
  | title | string | The title of the pull request. |
  | user | object | A GitHub user. |
  | body | string |  |
  | labels | array<object> |  |
  | milestone | object | A collection of related issues and pull requests. |
  | active_lock_reason | string |  |
  | created_at | string |  |
  | updated_at | string |  |
  | closed_at | string |  |
  | merged_at | string |  |
  | merge_commit_sha | string |  |
  | assignee | object | A GitHub user. |
  | assignees | array<object> |  |
  | requested_reviewers | array<object> |  |
  | requested_teams | array<object> |  |
  | head | object |  |
  | base | object |  |
  | links | object |  |
  | author_association | string | How the author is associated with the repository. |
  | auto_merge | object | The status of auto merging a pull request. |
  | draft | boolean | Indicates whether or not the pull request is a draft. |
  | merged | boolean |  |
  | mergeable | boolean |  |
  | rebaseable | boolean |  |
  | mergeable_state | string |  |
  | merged_by | object | A GitHub user. |
  | comments | number |  |
  | review_comments | number |  |
  | maintainer_can_modify | boolean | Indicates whether maintainers can modify the pull request. |
  | commits | number |  |
  | additions | number |  |
  | deletions | number |  |
  | changed_files | number |  |


## com.datadoghq.github.pulls.createReviewComment
**Create review comment** — Creates a review comment on the diff of a specified pull request.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | body | string | yes | The text of the review comment. |
  | commit_id | string | yes | The SHA of the commit needing a comment. |
  | path | string | yes | The relative path to the file that necessitates a comment. |
  | position | number | no | **This parameter is closing down. |
  | side | string | no | In a split diff view, the side of the diff that the pull request's changes appear on. |
  | line | number | no | **Required unless using `subject_type:file`**. |
  | start_line | number | no | **Required when using multi-line comments unless using `in_reply_to`**. |
  | start_side | string | no | **Required when using multi-line comments unless using `in_reply_to`**. |
  | in_reply_to | number | no | The ID of the review comment to reply to. |
  | subject_type | string | no | The level at which the comment is targeted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Create review comment |


## com.datadoghq.github.pulls.deletePendingReview
**Delete pending review** — Deletes a pull request review that has not been submitted.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | review_id | number | yes | The unique identifier of the review. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Delete pending review |


## com.datadoghq.github.pulls.deleteReviewComment
**Delete review comment** — Deletes a review comment.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | comment_id | number | yes | The unique identifier of the comment. |


## com.datadoghq.github.pulls.get
**Get** — Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get |


## com.datadoghq.github.pulls.getReview
**Get review** — Retrieves a pull request review by its ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | review_id | number | yes | The unique identifier of the review. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get review |


## com.datadoghq.github.pulls.getReviewComment
**Get review comment** — Provides details for a specified review comment.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | comment_id | number | yes | The unique identifier of the comment. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Get review comment |


## com.datadoghq.github.pulls.list
**List** — Lists pull requests in a specified repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | state | string | no | Either `open`, `closed`, or `all` to filter by state. |
  | head | string | no | Filter pulls by head user or head organization and branch name in the format of `user:ref-name` or `organization:ref-name`. |
  | base | string | no | Filter pulls by base branch name. |
  | sort | string | no | What to sort results by. |
  | direction | string | no | The direction of the sort. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List |


## com.datadoghq.github.pulls.listCommits
**List commits** — Lists a maximum of 250 commits for a pull request.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List commits |


## com.datadoghq.github.pulls.listFiles
**List files** — Lists the files in a specified pull request.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List files |


## com.datadoghq.github.pulls.listRequestedReviewers
**List requested reviewers** — Gets the users or teams whose review is requested for a pull request.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for List requested reviewers |


## com.datadoghq.github.pulls.listReviewCommentsForRepo
**List review comments for repo** — Lists review comments for all pull requests in a repository.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | sort | string | no |  |
  | direction | string | no | The direction to sort results. |
  | since | string | no | Only show results that were last updated after the given time. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List review comments for repo |


## com.datadoghq.github.pulls.listReviews
**List reviews** — Lists all reviews for a specified pull request.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data for List reviews |


## com.datadoghq.github.pulls.merge
**Merge** — Merges a pull request into the base branch.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | commit_title | string | no | Title for the automatic commit message. |
  | commit_message | string | no | Extra detail to append to automatic commit message. |
  | sha | string | no | SHA that pull request head must match to allow merge. |
  | merge_method | string | no | The merge method to use. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Merge |


## com.datadoghq.github.pulls.removeRequestedReviewers
**Remove requested reviewers** — Removes review requests from a pull request for a given set of users and/or teams.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | reviewers | array<string> | yes | An array of user `login`s that will be removed. |
  | team_reviewers | array<string> | no | An array of team `slug`s that will be removed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Remove requested reviewers |


## com.datadoghq.github.pulls.requestReviewers
**Request reviewers** — Requests reviews for a pull request from a given set of users and/or teams.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | reviewers | array<string> | no | An array of user `login`s that will be requested. |
  | team_reviewers | array<string> | no | An array of team `slug`s that will be requested. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Request reviewers |


## com.datadoghq.github.pulls.submitReview
**Submit review** — Submits a pending review for a pull request.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | review_id | number | yes | The unique identifier of the review. |
  | body | string | no | The body text of the pull request review. |
  | event | string | yes | The review action you want to perform. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Submit review |


## com.datadoghq.github.pulls.update
**Update** — Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | pull_number | number | yes | The number that identifies the pull request. |
  | title | string | no | The title of the pull request. |
  | body | string | no | The contents of the pull request. |
  | state | string | no | State of this Pull Request. |
  | base | string | no | The name of the branch you want your changes pulled into. |
  | maintainer_can_modify | boolean | no | Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Update |


## com.datadoghq.github.pulls.updateReviewComment
**Update review comment** — Edits the content of a specified review comment.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | comment_id | number | yes | The unique identifier of the comment. |
  | body | string | yes | The text of the reply to the review comment. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Update review comment |

