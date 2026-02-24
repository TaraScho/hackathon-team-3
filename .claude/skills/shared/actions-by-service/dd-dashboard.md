# Datadog Dashboard Actions
Bundle: `com.datadoghq.dd.dashboard` | 12 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edashboard)

## com.datadoghq.dd.dashboard.cloneDashboard
**Clone dashboard** — Clone the specified dashboard.
- Stability: stable
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboardId | string | yes | The ID of the dashboard to be cloned. |
  | title | string | no | Replace the cloned dashboard title. |
  | description | string | no | Replace the cloned dashboard description with the provided string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string | ID of the dashboard. |
  | title | string | Title of the dashboard. |
  | description | string | Description of the dashboard. |
  | restricted_roles | array<string> | A list of role identifiers. |
  | url | string | The URL of the dashboard. |
  | created_at | string | Creation date of the dashboard. |
  | modified_at | string | Modification date of the dashboard. |
  | author_handle | string | Identifier of the dashboard author. |
  | author_name | string | Name of the dashboard author. |
  | layout_type | string | Layout type of the dashboard. |
  | reflow_type | string | Reflow type for a **new dashboard layout** dashboard. |
  | notify_list | array<string> | List of handles of users to notify when changes are made to this dashboard. |
  | tags | array<string> | List of tags for this dashboard. |
  | template_variables | array<object> | List of template variables for this dashboard. |
  | template_variable_presets | array<object> | Array of template variables saved views. |
  | widgets | array<object> | List of widgets to display on the dashboard. |
  | is_read_only | boolean | Whether this dashboard is read-only. |


## com.datadoghq.dd.dashboard.deleteDashboard
**Delete dashboard** — Delete a dashboard using the specified ID.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleted_dashboard_id | string | ID of the deleted dashboard. |


## com.datadoghq.dd.dashboard.deleteDashboards
**Delete dashboards** — Delete dashboards using the specified IDs.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | data | array<object> | yes | List of dashboard bulk action request data objects. |


## com.datadoghq.dd.dashboard.deletePublicDashboard
**Delete public dashboard** — Revoke the public URL for a dashboard associated with the specified token. This will make the dashboard private.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | token | string | yes | The token of the shared dashboard. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleted_public_dashboard_token | string | Token associated with the shared dashboard that was revoked. |


## com.datadoghq.dd.dashboard.getDashboard
**Get dashboard details** — Get a dashboard with widgets using the specified ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_id | string | yes | If you’re dynamically passing in a Dashboard using a variable, then ensure that you pass in a Dashboard ID value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string | The URL of the dashboard. |
  | id | string | ID of the dashboard. |
  | title | string | Title of the dashboard. |
  | description | string | Description of the dashboard. |
  | restricted_roles | array<string> | A list of role identifiers. |
  | created_at | string | Creation date of the dashboard. |
  | modified_at | string | Modification date of the dashboard. |
  | author_handle | string | Identifier of the dashboard author. |
  | author_name | string | Name of the dashboard author. |
  | layout_type | string | Layout type of the dashboard. |
  | reflow_type | string | Reflow type for a **new dashboard layout** dashboard. |
  | notify_list | array<string> | List of handles of users to notify when changes are made to this dashboard. |
  | tags | array<string> | List of tags for this dashboard. |
  | template_variables | array<object> | List of template variables for this dashboard. |
  | template_variable_presets | array<object> | Array of template variables saved views. |
  | widgets | array<object> | List of widgets to display on the dashboard. |
  | is_read_only | boolean | Whether this dashboard is read-only. |


## com.datadoghq.dd.dashboard.getDashboardWithoutWidgets
**Get dashboard** — Get a dashboard using the specified ID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_id | string | yes | If you’re dynamically passing in a Dashboard using a variable, then ensure that you pass in a Dashboard ID value. |
  | templateVariables | object | no | Provided template variables will be used to create the Dashboard link this action outputs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | numberOfWidgets | number |  |
  | tag_value | object |  |
  | tag_value_list | object |  |
  | id | string | ID of the dashboard. |
  | title | string | Title of the dashboard. |
  | description | string | Description of the dashboard. |
  | restricted_roles | array<string> | A list of role identifiers. |
  | url | string | The URL of the dashboard. |
  | created_at | string | Creation date of the dashboard. |
  | modified_at | string | Modification date of the dashboard. |
  | author_handle | string | Identifier of the dashboard author. |
  | author_name | string | Name of the dashboard author. |
  | layout_type | string | Layout type of the dashboard. |
  | reflow_type | string | Reflow type for a **new dashboard layout** dashboard. |
  | notify_list | array<string> | List of handles of users to notify when changes are made to this dashboard. |
  | tags | array<string> | List of tags for this dashboard. |
  | template_variables | array<object> | List of template variables for this dashboard. |
  | template_variable_presets | array<object> | Array of template variables saved views. |
  | is_read_only | boolean | Whether this dashboard is read-only. |


## com.datadoghq.dd.dashboard.getPublicDashboard
**Get public dashboard** — Fetch an existing shared dashboard's sharing metadata associated with the specified token.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | token | string | yes | The token of the shared dashboard. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | author | object | Identifier of the dashboard author. |
  | created_at | string | Date the dashboard was shared. |
  | dashboard_id | string | ID of the dashboard. |
  | dashboard_type | string | he type of the associated private dashboard. |
  | gloabal_time | object | Object containing the live span selection for the dashboard. |
  | global_time_selectable_enabled | boolean | Whether to allow viewers to select a different global time setting for the shared dashboard. |
  | public_url | string | URL of the shared dashboard. |
  | selectable_template_vars | object | List of objects representing template variables on the shared dashboard which can have selectable values. |
  | share_list | array<string> | List of email addresses that can receive an invitation to access to the shared dashboard. |
  | share_type | string | Type of sharing access (either open to anyone who has the public URL or invite-only). |
  | token | string | A unique token assigned to the shared dashboard. |


## com.datadoghq.dd.dashboard.getPublicDashboardInvitations
**Get public dashboard invitations** — Describe the invitations that exist for the given shared dashboard (paginated).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | token | string | yes | Token of the shared dashboard for which to fetch invitations. |
  | page_size | number | no | The number of records to return in a single request. |
  | page_number | number | no | The page to access (base 0). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any | An object or list of objects containing the information for an invitation to a shared dashboard. |
  | meta | object | Pagination metadata returned by the API. |


## com.datadoghq.dd.dashboard.getSharedDashboard
**Get shared dashboard** — Fetch an existing shared dashboard’s sharing metadata associated with the specified token.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | shared_dashboard_token | string | yes | Unique token assigned to the shared dashboard. Generated when a dashboard is shared. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | author | object | Identifier of the dashboard author. |
  | created_at | string | Date the dashboard was shared. |
  | dashboard_id | string | ID of the dashboard. |
  | dashboard_type | string | he type of the associated private dashboard. |
  | gloabal_time | object | Object containing the live span selection for the dashboard. |
  | global_time_selectable_enabled | boolean | Whether to allow viewers to select a different global time setting for the shared dashboard. |
  | public_url | string | URL of the shared dashboard. |
  | selectable_template_vars | object | List of objects representing template variables on the shared dashboard which can have selectable values. |
  | share_list | array<string> | List of email addresses that can receive an invitation to access to the shared dashboard. |
  | share_type | string | Type of sharing access (either open to anyone who has the public URL or invite-only). |
  | token | string | A unique token assigned to the shared dashboard. |


## com.datadoghq.dd.dashboard.listDashboards
**List dashboards** — Get all dashboards.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dashboards | array<object> | List of dashboard definitions. |


## com.datadoghq.dd.dashboard.restoreDashboard
**Restore dashboard** — Restore dashboard with the specified ID.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboardId | string | yes |  |


## com.datadoghq.dd.dashboard.sendPublicDashboardInvitation
**Send public dashboard invitation** — Send emails to specified email addresses containing links to access a given authenticated shared dashboard.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | token | string | yes | The token of the shared dashboard. |
  | page | object | no | Object containing the total count of invitations across all pages. |
  | data | any | yes | An object or list of objects containing the information for an invitation to a shared dashboard. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any | An object or list of objects containing the information for an invitation to a shared dashboard. |
  | meta | object | Pagination metadata returned by the API. |

