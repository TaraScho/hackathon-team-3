# Datadog Roles Actions
Bundle: `com.datadoghq.dd.roles` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eroles)

## com.datadoghq.dd.roles.addPermissionToRole
**Add permission to role** — Add a permission to a role.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | relationshipToPermission | object | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> |  |


## com.datadoghq.dd.roles.addUserToRole
**Add user to role** — Add a user to a role.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | relationshipToUser | object | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | included | array<object> |  |
  | data | array<object> |  |
  | meta | object |  |


## com.datadoghq.dd.roles.cloneRole
**Clone role** — Clone an existing role.
- Stability: stable
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | name | string | yes | Name of the new role that is cloned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Role object returned by the API. |


## com.datadoghq.dd.roles.deleteRole
**Delete role** — Delete a role.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |


## com.datadoghq.dd.roles.getRole
**Get role** — Get a role in the organization specified by the role’s `role_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the role. |
  | data | object | Role object returned by the API. |


## com.datadoghq.dd.roles.listPermissions
**List permissions** — Returns a list of all permissions, including name, description, and ID.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> |  |


## com.datadoghq.dd.roles.listRolePermissions
**List role permissions** — Return a list of all permissions for a single role.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> |  |


## com.datadoghq.dd.roles.listRoleUsers
**List role users** — Get all users of a role.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | User attribute to order results by. |
  | filter | string | no | Filter all users by the given string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | included | array<object> |  |
  | data | array<object> |  |
  | meta | object |  |


## com.datadoghq.dd.roles.listRoles
**List roles** — Return all roles, including their names and IDs.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Sort roles depending on the given field. |
  | filter | string | no | Filter all roles by the given string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of returned roles. |
  | meta | object |  |


## com.datadoghq.dd.roles.removePermissionFromRole
**Remove permission from role** — Remove a permission from a role.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | relationshipToPermission | object | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> |  |


## com.datadoghq.dd.roles.removeUserFromRole
**Remove user from role** — Remove a user from a role.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | role_id | string | yes | The ID of the role. |
  | relationshipToUser | object | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | included | array<object> |  |
  | data | array<object> |  |
  | meta | object |  |

