# Datadog On-Call Actions
Bundle: `com.datadoghq.dd.oncall` | 18 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eoncall)

## com.datadoghq.dd.oncall.acknowledgeOnCallPage
**Acknowledge on-call page** — Acknowledges an On-Call Page.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_id | string | yes | The page ID. |


## com.datadoghq.dd.oncall.createOnCallEscalationPolicy
**Create on-call escalation policy** — Create an on-call escalation policy.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | name | string | yes | Specifies the name for the new escalation policy. |
  | resolve_page_on_policy_end | boolean | no | Indicates whether the page is automatically resolved when the policy ends. |
  | retries | number | no | Specifies how many times the escalation sequence is retried if there is no response. |
  | steps | array<object> | yes | A list of escalation steps, each defining assignment, escalation timeout, and targets for the new policy. |
  | relationships | object | no | Represents relationships in an escalation policy creation request, including references to teams. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type. |
  | included | array<object> | Provides any included related resources, such as steps or targets, returned with the policy. |


## com.datadoghq.dd.oncall.createOnCallPage
**Create on-call page** — Trigger a new On-Call Page.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | description | string | no | A short summary of the issue or context. |
  | tags | array<string> | no | Tags to help categorize or filter the page. |
  | target | object | yes | Information about the target to notify (such as a team or user). |
  | title | string | yes | The title of the page. |
  | urgency | string | yes | On-Call Page urgency level. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The information returned after successfully creating a page. |


## com.datadoghq.dd.oncall.createOnCallSchedule
**Create on-call schedule** — Create an on-call schedule.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | layers | array<object> | yes | The layers of On-Call coverage that define rotation intervals and restrictions. |
  | name | string | yes | A human-readable name for the new schedule. |
  | time_zone | string | yes | The time zone in which the schedule is defined. |
  | relationships | object | no | Gathers relationship objects for the schedule creation request, including the teams to associate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the primary data object for a schedule, linking attributes and relationships. |
  | included | array<object> | Any additional resources related to this schedule, such as teams and layers. |


## com.datadoghq.dd.oncall.deleteOnCallEscalationPolicy
**Delete on-call escalation policy** — Delete an On-Call escalation policy.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | yes | The ID of the escalation policy. |


## com.datadoghq.dd.oncall.deleteOnCallSchedule
**Delete on-call schedule** — Delete an On-Call schedule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | schedule_id | string | yes | The ID of the schedule. |


## com.datadoghq.dd.oncall.escalateOnCallPage
**Escalate on-call page** — Escalates an On-Call Page.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_id | string | yes | The page ID. |


## com.datadoghq.dd.oncall.getOnCallEscalationPolicy
**Get on-call escalation policy** — Get an On-Call escalation policy.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | yes | The ID of the escalation policy. |
  | include | string | no | Comma-separated list of included relationships to be returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type. |
  | included | array<object> | Provides any included related resources, such as steps or targets, returned with the policy. |


## com.datadoghq.dd.oncall.getOnCallSchedule
**Get on-call schedule** — Get an On-Call schedule.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | schedule_id | string | yes | The ID of the schedule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the primary data object for a schedule, linking attributes and relationships. |
  | included | array<object> | Any additional resources related to this schedule, such as teams and layers. |


## com.datadoghq.dd.oncall.getOnCallTeamRoutingRules
**Get on call team routing rules** — Get a team's On-Call routing rules.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | The team ID. |
  | include | string | no | Comma-separated list of included relationships to be returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type. |
  | included | array<object> | Provides related routing rules or other included resources. |


## com.datadoghq.dd.oncall.getPageSource
**Get page source** — Get a page source.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | uuid | string | yes | The UUID of the page to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The page data object. |
  | links | object | Related links for this resource. |
  | included | array<object> | Included related resources (users, teams, scheduled actions, etc.). |


## com.datadoghq.dd.oncall.getScheduleOnCallUser
**Get schedule on call user** — Retrieves the user who is on-call for the specified schedule at a given time.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | at_ts | any | no | Retrieves the on-call user at the given timestamp (ISO-8601). |
  | include | string | no | Specifies related resources to include in the response as a comma-separated list. |
  | schedule_id | string | yes | The ID of the schedule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data for an on-call shift. |
  | included | array<object> | The `Shift` `included`. |


## com.datadoghq.dd.oncall.getTeamOnCallUsers
**Get team on call users** — Get a team's on-call users at a given time.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | team_id | string | yes | The team ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Defines the main on-call responder object for a team, including relationships and metadata. |
  | included | array<object> | The `TeamOnCallResponders` `included`. |


## com.datadoghq.dd.oncall.page
**Page** — Page a specific team or user.
- Stability: beta
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | title | string | yes | Single line page title. |
  | description | string | yes | Multi line page description |
  | urgency | string | yes | Urgency of the page. This can impact page routing based on your organization's configuration. |
  | target | object | yes | The team or user that will receive the page. |
  | tags | any | no | Tags to associate with the page. This can impact page routing based on your organization's configuration. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | The ID of the page. |
  | type | string | The type of resource being returned. This is always "page". |


## com.datadoghq.dd.oncall.resolveOnCallPage
**Resolve on-call page** — Resolves an On-Call Page.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_id | string | yes | The page ID. |


## com.datadoghq.dd.oncall.setOnCallTeamRoutingRules
**Set on call team routing rules** — Set a team's On-Call routing rules.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | team_id | string | yes | The team ID. |
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | rules | array<object> | no | A list of routing rule items that define how incoming pages should be handled. |
  | id | string | no | Specifies the unique identifier for this set of team routing rules. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the top-level data object for team routing rules, containing the ID, relationships, and resource type. |
  | included | array<object> | Provides related routing rules or other included resources. |


## com.datadoghq.dd.oncall.updateOnCallEscalationPolicy
**Update on-call escalation policy** — Update an On-Call escalation policy.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | yes | The ID of the escalation policy. |
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | name | string | yes | Specifies the name of the escalation policy. |
  | resolve_page_on_policy_end | boolean | no | Indicates whether the page is automatically resolved when the policy ends. |
  | retries | number | no | Specifies how many times the escalation sequence is retried if there is no response. |
  | steps | array<object> | yes | A list of escalation steps, each defining assignment, escalation timeout, and targets. |
  | id | string | yes | Specifies the unique identifier of the escalation policy being updated. |
  | relationships | object | no | Represents relationships in an escalation policy update request, including references to teams. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type. |
  | included | array<object> | Provides any included related resources, such as steps or targets, returned with the policy. |


## com.datadoghq.dd.oncall.updateOnCallSchedule
**Update on-call schedule** — Update an on-call schedule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Comma-separated list of included relationships to be returned. |
  | schedule_id | string | yes | The ID of the schedule. |
  | layers | array<object> | yes | The updated list of layers (rotations) for this schedule. |
  | name | string | yes | A short name for the schedule. |
  | time_zone | string | yes | The time zone used when interpreting rotation times. |
  | id | string | yes | The ID of the schedule to be updated. |
  | relationships | object | no | Houses relationships for the schedule update, typically referencing teams. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Represents the primary data object for a schedule, linking attributes and relationships. |
  | included | array<object> | Any additional resources related to this schedule, such as teams and layers. |

