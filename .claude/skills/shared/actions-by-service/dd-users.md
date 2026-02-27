# Datadog Users Actions
Bundle: `com.datadoghq.dd.users` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eusers)

## com.datadoghq.dd.users.disableUser
**Disable user** — Disable a user.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | user_id | string | yes | The ID of the user. |


## com.datadoghq.dd.users.enrichUser
**List users (enrich)** — Return a list of users.
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


## com.datadoghq.dd.users.getUser
**Get user details** — Get a user by `user_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | user_id | string | yes | The ID of the user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | ID of the user. |
  | attributes | object | Attributes of the user. |
  | relationships | object | Relationships to the user. |
  | url | string | URL of the user. |


## com.datadoghq.dd.users.listUsers
**Search users** — Search users in the organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter | string | no | Filter all users by the given string. You can filter by name, or email address. If no filter is provided, all users are returned. |
  | page_size | number | no | The number of users to return. |
  | page_number | number | no | Specific page number to return. |
  | status | string | no | Status of the user. |
  | sort | string | no | User attribute to order results by. |
  | sort_dir | string | no | Direction of sort. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | users | array<object> | The list of users. |

