# Datadog Teams Actions
Bundle: `com.datadoghq.dd.teams` | 18 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eteams)

## com.datadoghq.dd.teams.addUser
**Add user** — Add a user to a team.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team | string | yes | The name of the team. |
  | userId | string | yes | The ID of the user. |
  | isAdmin | boolean | no | Specifies if the new user is an admin. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | user | object |  |


## com.datadoghq.dd.teams.createTeam
**Create team** — Create a new team.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | avatar | string | no | Unicode representation of the avatar for the team, limited to a single grapheme. |
  | banner | number | no | Banner selection for the team. |
  | description | string | no | Free-form markdown description/content for the team's homepage. |
  | handle | string | yes | The team's identifier. |
  | hidden_modules | array<string> | no | Collection of hidden modules for the team. |
  | name | string | yes | The name of the team. |
  | visible_modules | array<string> | no | Collection of visible modules for the team. |
  | relationships | object | no | Relationships formed with the team on creation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A team. |


## com.datadoghq.dd.teams.createTeamLink
**Create team link** — Add a new link to a team.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | ID of the team the link is associated with. |
  | label | string | yes | The link's label. |
  | position | number | no | The link's position, used to sort links for the team. |
  | url | string | yes | The URL for the link. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Team link. |


## com.datadoghq.dd.teams.deleteTeam
**Delete team** — Remove a team using the team's `id`.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |


## com.datadoghq.dd.teams.deleteTeamLink
**Delete team link** — Remove a link from a team.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | link_id | string | yes | None. |


## com.datadoghq.dd.teams.deleteTeamMembership
**Delete team membership** — Remove a user from a team.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | user_id | string | yes | None. |


## com.datadoghq.dd.teams.getTeam
**Get team** — Get a specific team given a team ID or team name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team | string | no | The name, or parts of the name, of the team to filter for. You must specify either the team name or the team ID, but not both. |
  | teamId | string | no | The ID of the team. You must specify either the team name or the team ID, but not both. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | members | array<object> | The members of the team. |
  | created_at | string | Creation date of the team. |
  | description | string | Free-form markdown description/content for the team's homepage. |
  | handle | string | The team's identifier. |
  | link_count | number | The number of links belonging to the team. |
  | modified_at | string | Modification date of the team. |
  | name | string | The name of the team. |
  | summary | string | A brief summary of the team, derived from the `description`. |
  | user_count | number | The number of users belonging to the team. |


## com.datadoghq.dd.teams.getTeamLink
**Get team link** — Get a single link for a team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | link_id | string | yes | None. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Team link. |


## com.datadoghq.dd.teams.getTeamLinks
**Get team links** — Get all links for a given team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Team links response data. |


## com.datadoghq.dd.teams.getTeamMemberships
**Get team memberships** — Get a paginated list of members for a team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Specifies the order of returned team memberships. |
  | filter_keyword | string | no | Search query, can be user email or name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Team memberships response data. |
  | included | array<object> | Resources related to the team memberships. |
  | links | object | Teams response links. |
  | meta | object | Teams response metadata. |


## com.datadoghq.dd.teams.getTeamPermissionSettings
**Get team permission settings** — Get all permission settings for a given team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Team permission settings response data. |


## com.datadoghq.dd.teams.getUserMemberships
**Get user memberships** — Get a list of memberships for a user.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | user_uuid | string | yes | None. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Team memberships response data. |
  | included | array<object> | Resources related to the team memberships. |
  | links | object | Teams response links. |
  | meta | object | Teams response metadata. |


## com.datadoghq.dd.teams.listTeams
**List teams** — Get all teams.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_number | number | no | Specific page number to return. |
  | page_size | number | no | Size for a given page. |
  | sort | string | no | Specifies the order of the returned teams. |
  | include | array<string> | no | Included related resources optionally requested. |
  | filter_keyword | string | no | Search query. |
  | fields_team | array<string> | no | List of fields that need to be fetched. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Teams response data. |
  | meta | object | Teams response metadata. |
  | links | object | Teams response links. |
  | included | array<object> | Resources related to the team. |


## com.datadoghq.dd.teams.removeUser
**Remove user** — Remove a user from a team.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team | string | yes | The name of the team. |
  | userId | string | yes | The ID of the user. |


## com.datadoghq.dd.teams.updateTeam
**Update team** — Update a team using the team's `id`.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | avatar | string | no | Unicode representation of the avatar for the team, limited to a single grapheme. |
  | banner | number | no | Banner selection for the team. |
  | description | string | no | Free-form markdown description/content for the team's homepage. |
  | handle | string | yes | The team's identifier. |
  | hidden_modules | array<string> | no | Collection of hidden modules for the team. |
  | name | string | yes | The name of the team. |
  | visible_modules | array<string> | no | Collection of visible modules for the team. |
  | relationships | object | no | Team update relationships. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A team. |


## com.datadoghq.dd.teams.updateTeamLink
**Update team link** — Update a team link.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | ID of the team the link is associated with. |
  | link_id | string | yes | None. |
  | label | string | yes | The link's label. |
  | position | number | no | The link's position, used to sort links for the team. |
  | url | string | yes | The URL for the link. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Team link. |


## com.datadoghq.dd.teams.updateTeamMembership
**Update team membership** — Update a user's membership attributes on a team.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | user_id | string | yes | None. |
  | provisioned_by | string | no | The mechanism responsible for provisioning the team relationship. |
  | provisioned_by_id | string | no | UUID of the User or Service Account who provisioned this team membership, or null if provisioned via SAML mapping. |
  | role | string | no | The user's role within the team. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A user's relationship with a team. |
  | included | array<object> | Resources related to the team memberships. |


## com.datadoghq.dd.teams.updateTeamPermissionSetting
**Update team permission setting** — Update a team permission setting for a given team.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | None. |
  | action | string | yes | None. |
  | value | string | no | What type of user is allowed to perform the specified action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Team permission setting. |

