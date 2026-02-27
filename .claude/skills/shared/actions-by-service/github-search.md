# GitHub Search Actions
Bundle: `com.datadoghq.github.search` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Esearch)

## com.datadoghq.github.search.code
**Search code** — Searches for query terms inside of a file.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | q | string | yes | The query contains one or more search keywords and qualifiers. |
  | sort | string | no | **This field is closing down.** Sorts the results of your query. |
  | order | string | no | **This field is closing down.** Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). |
  | per_page | number | no | The number of results per page |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Search code |


## com.datadoghq.github.search.commits
**Search commits** — Find commits via various criteria on the default branch (usually `main`).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | q | string | yes | The query contains one or more search keywords and qualifiers. |
  | sort | string | no | Sorts the results of your query by `author-date` or `committer-date`. |
  | order | string | no | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for Search commits |


## com.datadoghq.github.search.issuesAndPullRequests
**Search issues and pull requests** — > [!WARNING] > **Notice:** Search for issues and pull requests will be overridden by advanced search on September 4, 2025.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | q | string | yes | The query contains one or more search keywords and qualifiers. |
  | sort | string | no | Sorts the results of your query by the number of `comments`, `reactions`, `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`, `reactions-heart`, `reactions-tada`, or `inte... |
  | order | string | no | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). |
  | per_page | number | no | The number of results per page (max 100). |
  | page | number | no | The page number of the results to fetch. |
  | advanced_search | string | no | Set to `true` to use advanced search. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | total_count | number |  |
  | incomplete_results | boolean |  |
  | items | array<object> |  |

