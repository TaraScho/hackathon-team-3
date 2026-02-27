# Datadog Dashboard List Actions
Bundle: `com.datadoghq.dd.dashboard_list` | 7 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edashboard_list)

## com.datadoghq.dd.dashboard_list.createDashboardListItems
**Create dashboard list items** — Add dashboards to an existing dashboard list.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_list_id | ['number', 'string'] | yes | ID of the dashboard list to add items to. |
  | dashboards | array<object> | no | List of dashboards to add the dashboard list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | added_dashboards_to_list | array<object> | List of dashboards added to the dashboard list. |


## com.datadoghq.dd.dashboard_list.deleteDashboardList
**Delete dashboard list** — Delete a dashboard list.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | list_id | number | yes | ID of the dashboard list to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleted_dashboard_list_id | number | ID of the deleted dashboard list. |


## com.datadoghq.dd.dashboard_list.deleteDashboardListItems
**Delete dashboard list items** — Delete dashboards from an existing dashboard list.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_list_id | ['number', 'string'] | yes | ID of the dashboard list to delete items from. |
  | dashboards | array<object> | no | List of dashboards to delete from the dashboard list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleted_dashboards_from_list | array<object> | List of dashboards deleted from the dashboard list. |


## com.datadoghq.dd.dashboard_list.getDashboardList
**Get dashboard list** — Fetch an existing dashboard list's definition.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | list_id | number | yes | ID of the dashboard list to fetch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | author | object | Object describing the creator of the shared element. |
  | created | string | Date of creation of the dashboard list. |
  | dashboard_count | number | The number of dashboards in the list. |
  | id | number | The ID of the dashboard list. |
  | is_favorite | boolean | Whether or not the list is in the favorites. |
  | modified | string | Date of last edition of the dashboard list. |
  | name | string | The name of the dashboard list. |
  | type | string | The type of dashboard list. |


## com.datadoghq.dd.dashboard_list.getDashboardListItems
**Get dashboard list items** — Fetch the dashboard list’s dashboard definitions.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_list_id | ['number', 'string'] | yes | ID of the dashboard list to get items from. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | total | number | Number of dashboards in the dashboard list. |
  | dashboards | array<object> | List of dashboards in the dashboard list. |


## com.datadoghq.dd.dashboard_list.listDashboardLists
**List dashboard lists** — Fetch all of your existing dashboard list definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dashboard_lists | array<object> | List of all your dashboard lists. |


## com.datadoghq.dd.dashboard_list.updateDashboardListItems
**Update dashboard list items** — Update dashboards of an existing dashboard list.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dashboard_list_id | ['number', 'string'] | yes | ID of the dashboard list to update items from. |
  | dashboards | array<object> | no | List of dashboards to update the dashboard list to. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dashboards | array<object> | List of dashboards in the dashboard list. |

