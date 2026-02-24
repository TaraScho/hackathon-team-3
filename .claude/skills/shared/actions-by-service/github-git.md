# GitHub Git Actions
Bundle: `com.datadoghq.github.git` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Egit)

## com.datadoghq.github.git.createRef
**Create a reference** — Create a reference for your repository.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | ref | string | yes | The name of the fully qualified reference (ie: `refs/heads/master`). |
  | sha | string | yes | The SHA1 value for this reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ref | string |  |
  | node_id | string |  |
  | url | string |  |
  | object | object |  |


## com.datadoghq.github.git.getFolderTree
**Get folder tree.** — Return a single tree for the folder using the SHA1 value or ref name for that tree.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | tree_sha | string | yes | The SHA1 value or ref (branch or tag) name of the tree. |
  | folder_path | string | yes | The path to the folder to get the tree for. |
  | recursive | string | no | Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in :tree_sha. For example, setting recursive to any of the following will enable returning objec... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | sha | string |  |
  | url | string |  |
  | truncated | boolean |  |
  | tree | array<object> | Objects specifying a tree structure. |


## com.datadoghq.github.git.getTree
**Get a tree** — Return a single tree using the SHA1 value or ref name for that tree.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | owner | string | yes | The account owner of the repository. |
  | repo | string | yes | The name of the repository without the `.git` extension. |
  | tree_sha | string | yes | The SHA1 value or ref (branch or tag) name of the tree. |
  | recursive | string | no | Setting this parameter to any value returns the objects or subtrees referenced by the tree specified in :tree_sha. For example, setting recursive to any of the following will enable returning objec... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | sha | string |  |
  | url | string |  |
  | truncated | boolean |  |
  | tree | array<object> | Objects specifying a tree structure. |

