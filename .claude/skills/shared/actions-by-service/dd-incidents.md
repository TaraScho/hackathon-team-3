# Datadog Incidents Actions
Bundle: `com.datadoghq.dd.incidents` | 29 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eincidents)

## com.datadoghq.dd.incidents.addAttachment
**Add attachment** — Adds an attachment to a given incident.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The ID of the incident to render the template for. |
  | attachment_type | string | yes | The type of attachment to add. |
  | title | string | yes | The title of the attachment. |
  | url | string | yes | The URL of the attachment. |


## com.datadoghq.dd.incidents.addResponder
**Add responder to incident** — Add a responder to a Datadog incident.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID. |
  | user_id | ['string', 'number'] | yes | Enter a responder to add to the incident. |
  | role_id | string | no | Enter a role to give to the responder. |


## com.datadoghq.dd.incidents.addTask
**Add task to incident** — Add a task to a Datadog incident.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID. |
  | content | string | yes | The text to be appended to the timeline of the incident. |
  | user_id | string | no | Enter a user to assign the task to. |
  | date_time | string | no | Select a calendar date. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | task_id | number | The task's ID. |


## com.datadoghq.dd.incidents.createIncident
**Create incident** — Create an incident.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | customer_impacted | boolean | yes | A flag indicating whether the incident caused customer impact. |
  | fields | object | no | A condensed view of the user-defined fields for which to create initial selections. |
  | initial_cells | array<object> | no | An array of initial timeline cells to be placed at the beginning of the incident timeline. |
  | notification_handles | array<object> | no | Notification handles that will be notified of the incident at creation. |
  | title | string | yes | The title of the incident, which summarizes what happened. |
  | relationships | object | no | The relationships the incident will have with other resources once created. |
  | incident_type_uuid | string | no | A unique identifier that represents an incident type. The default incident type will be used if this property is not provided. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | incident_id | number | The incident's ID. |
  | url | string | The incident's URL. |
  | title | string | The title of the incident. |
  | state | string | The current state of the incident. |
  | severity | string | Severity level of the incident. |


## com.datadoghq.dd.incidents.createIncidentImpact
**Create incident impact** — Create an impact for an incident.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The UUID of the incident. |
  | include | array<string> | no | Specifies which related resources should be included in the response. |
  | description | string | yes | Description of the impact. |
  | end_at | string | no | Timestamp when the impact ended. |
  | fields | object | no | An object mapping impact field names to field values. |
  | start_at | string | yes | Timestamp when the impact started. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Incident impact data from a response. |
  | included | array<object> | Included related resources that the user requested. |


## com.datadoghq.dd.incidents.createIncidentPage
**Create incident page** — Create a new page for an incident.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID |
  | target | object | yes | The team or user that will receive the page. |
  | urgency | string | yes | Urgency of the page. This can impact page routing based on your organization's configuration. |
  | title | string | yes | The title of the page. |
  | description | string | no | The description of the page. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.createOrAttachServiceNowIncident
**Create or attach ServiceNow incident** — Create or attach a ServiceNow incident to this Datadog incident.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The ID of the Datadog incident. |
  | instance_name | string | yes |  |
  | record_id | string | no | If using an existing ServiceNow incident, the ID of the ServiceNow record. If this is unset, a new ServiceNow incident will be created. |
  | assignment_group | string | no |  |
  | configuration_item_mapping | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.deleteIncident
**Delete incident** — Delete an existing incident from the users organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID |


## com.datadoghq.dd.incidents.deleteIncidentImpact
**Delete incident impact** — Delete an incident impact.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The UUID of the incident. |
  | impact_id | string | yes | The UUID of the incident impact. |


## com.datadoghq.dd.incidents.generatePostmortem
**Generate postmortem** — Generates and attaches a postmortem for a given incident from a postmortem template.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The ID of the incident to generate the postmortem for. |
  | postmortem_template_id | string | yes | The ID of the postmortem template to use. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.getIncident
**Get incident** — Get the details of an incident by `incident_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID |
  | include | array<string> | no | Specifies which types of related objects should be included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Incident data from a response. |
  | included | array<object> | Included related resources that the user requested. |
  | incidentID | ['string', 'number'] | The unique ID of the incident. |
  | incident_id | ['string', 'number'] | The unique ID of the incident. |
  | url | string | The URL of the incident. |
  | title | string | The title of the incident. |
  | state | string | The current state of the incident. |
  | severity | string | Severity level of the incident. |
  | incident_commander_user | object | The incident commander. |
  | channel_link | string | Link for collaboration software. |
  | channel_id | string |  |
  | channel_name | string |  |
  | video_call_link | string | The video call link. |
  | created_at | string |  |
  | created_by_user | object | User who created the incident. |
  | incident_attributes | object | Attributes associated with this incident. |
  | modified | string | Timestamp when the incident was last modified. |
  | last_modified_by_user | object | The last user to modify the incident. |
  | resolved | string | Timestamp when the incident's state was last changed from active or stable to resolved or completed. |
  | time_to_repair | number | The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`. |
  | time_to_resolve | number |  |
  | customer_impacted | boolean | A flag indicating whether the incident caused customer impact. |
  | customer_impact_scope | ['string', 'null'] | A summary of the impact customers experienced during the incident. |
  | time_to_detect | number | The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`. |


## com.datadoghq.dd.incidents.getIncidentAutomationData
**Get incident automation data** — Get automation data for a given incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | string | yes | The ID of the incident to get automation data for. |
  | key | string | yes | The key of the automation data to get. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.getIncidentJiraIssues
**Get JIRA issues attached to a Datadog incident.** — Get the JIRA issues attached to a Datadog incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | issues | array<object> |  |


## com.datadoghq.dd.incidents.getIncidentMsTeamsChannel
**Get incident Microsoft Teams channel** — Get the Microsoft Teams channel attached to a Datadog incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ms_channel_name | ['string', 'null'] |  |
  | ms_channel_id | ['string', 'null'] |  |
  | ms_team_id | ['string', 'null'] |  |
  | ms_tenant_id | ['string', 'null'] |  |
  | redirect_url | ['string', 'null'] |  |


## com.datadoghq.dd.incidents.getIncidentSlackChannel
**Get incident Slack channel** — Get the Slack channel for a Datadog incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | channel_name | ['string', 'null'] |  |
  | channel_id | ['string', 'null'] |  |


## com.datadoghq.dd.incidents.getIncidentSource
**Get incident source** — Get the details of an incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | url | string |  |
  | title | string |  |
  | state | string |  |
  | severity | string |  |
  | customerImpacted | boolean |  |
  | customerImpactScope | string |  |
  | customerImpactDuration | number |  |
  | resolved | string |  |
  | customerImpactStart | string |  |
  | customerImpactEnd | string |  |
  | created | string |  |
  | modified | string |  |
  | detected | string |  |
  | timeToDetect | number |  |
  | timeToRepair | number |  |
  | timeToInternalResponse | number |  |
  | timeToResolve | number |  |
  | channel_id | string |  |
  | commander_user_uuid | string |  |


## com.datadoghq.dd.incidents.getIncidentSourceV2
**Get incident source** — Get the details of an incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | string | yes | The UUID of the incident. |
  | publicId | string | yes | The public ID of the incident. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | public_id | string |  |
  | data | object | Incident data from a response. |
  | included | array<object> | Included related resources that the user requested. |


## com.datadoghq.dd.incidents.getIncidentV2
**Get incident** — Get the details of an incident by `incident_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The UUID of the incident. |
  | include | array<string> | no | Specifies which types of related objects should be included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Incident data from a response. |
  | included | array<object> | Included related resources that the user requested. |


## com.datadoghq.dd.incidents.getResponders
**Get responders** — Get all responders for a Datadog incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | Enter either public ID or incident ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | responders | array<object> |  |
  | role_assignments | array<object> | All role assignments for the incident. |


## com.datadoghq.dd.incidents.getTimeline
**Get timeline** — Get timeline for a given incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | ['string', 'number'] | yes |  |
  | limit | number | no | Maximum number of timeline events to return. Default is 100. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | timeline | array<object> |  |


## com.datadoghq.dd.incidents.listIncidentImpacts
**List incident impacts** — Get all impacts for an incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The UUID of the incident. |
  | include | array<string> | no | Specifies which related resources should be included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of incident impacts. |
  | included | array<object> | Included related resources that the user requested. |


## com.datadoghq.dd.incidents.listIncidentPages
**List incident pages** — List all pages for an incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The ID of the incident. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> |  |
  | meta | object |  |
  | included | array<object> |  |


## com.datadoghq.dd.incidents.listIncidents
**List incidents** — Get all incidents for the user's organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | array<string> | no | Specifies which types of related objects should be included in the response. |
  | page_size | number | no | Size for a given page. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | included | array<object> | Included related resources that the user requested. |
  | meta | object | The metadata object containing pagination metadata. |
  | data | array<object> | An array of incidents. |


## com.datadoghq.dd.incidents.renderPostmortemTemplate
**Render postmortem template** — Renders a postmortem template for a given incident.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | string | yes | The ID of the incident to render the template for. |
  | postmortem_template_id | string | yes | The ID of the postmortem template to render. |
  | datetime_format | string | no | The datetime format to use for the template. |
  | timezone | string | no | The timezone to use for the template. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.searchIncident
**Search incidents** — Get specific incidents by given search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | yes | Specifies which incidents should be returned. The query can contain any number of incident facets joined by ANDs, along with multiple values for each of those facets joined by ORs. More information... |
  | page_size | number | no | Size for a given page. The maximum allowed value is 100. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | incidents | array<object> | All incidents |


## com.datadoghq.dd.incidents.searchIncidents
**Search incidents** — Search for incidents matching a certain query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | include | string | no | Specifies which types of related objects should be included in the response. |
  | query | string | yes | Specifies which incidents should be returned. |
  | sort | string | no | Specifies the order of returned incidents. |
  | page_size | number | no | Size for a given page. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data returned by an incident search. |
  | included | array<object> | Included related resources that the user requested. |
  | meta | object | The metadata object containing pagination metadata. |


## com.datadoghq.dd.incidents.setIncidentAutomationData
**Set incident automation data** — Set automation data for a given incident. If the key already exists, it will be updated with the new value. If the key does not exist, it will be created.
- Stability: stable
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | string | yes | The ID of the incident to set automation data for. |
  | key | string | yes | The key of the automation data to set. |
  | value | any | yes | A JSON representation of an item to be stored. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object |  |


## com.datadoghq.dd.incidents.updateIncident
**Update incident** — Update an incident.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incident_id | ['string', 'number'] | yes | The UUID of the incident. |
  | include | array<string> | no | Specifies which types of related objects should be included in the response. |
  | id | string | no | The team's ID. |
  | customer_impact_end | string | no | Timestamp when customers were no longer impacted by the incident. |
  | customer_impact_scope | string | no | A summary of the impact customers experienced during the incident. |
  | customer_impact_start | string | no | Timestamp when customers began being impacted by the incident. |
  | customer_impacted | boolean | no | A flag indicating whether the incident caused customer impact. |
  | detected | string | no | Timestamp when the incident was detected. |
  | fields | object | no | A condensed view of the user-defined fields for which to update selections. |
  | notification_handles | array<object> | no | Notification handles that will be notified of the incident during update. |
  | resolved | string | no | Timestamp when the incident's state was set to resolved. |
  | title | string | no | The title of the incident, which summarizes what happened. |
  | relationships | object | no | The incident's relationships for an update request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | incident_id | ['string', 'number'] | Enter either public ID or incident ID |
  | url | string | The incident's URL. |
  | title | string | The title of the incident. |
  | state | string | The current state of the incident. |
  | severity | string | Severity level of the incident. |
  | data | object | Incident data from a response. |
  | included | array<any> | Included related resources that the user requested. |


## com.datadoghq.dd.incidents.updateTimeline
**Update timeline** — Update timeline with given text.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | incidentId | ['string', 'number'] | yes |  |
  | content | string | yes | The text to be appended to the timeline of the incident. |

