# Datadog Powerpacks Actions
Bundle: `com.datadoghq.dd.powerpacks` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Epowerpacks)

## com.datadoghq.dd.powerpacks.deletePowerpack
**Delete powerpack** — Delete a powerpack.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | powerpack_id | string | yes | Powerpack id. |


## com.datadoghq.dd.powerpacks.getPowerpack
**Get powerpack** — Get a powerpack.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | powerpack_id | string | yes | ID of the powerpack. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Powerpack data object. |
  | included | array<object> | Array of objects related to the users. |


## com.datadoghq.dd.powerpacks.listPowerpacks
**List powerpacks** — Get a list of all powerpacks.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_limit | number | no | Maximum number of powerpacks in the response. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of powerpack definitions. |
  | included | array<object> | Array of objects related to the users. |
  | links | object | Links attributes. |
  | meta | object | Powerpack response metadata. |

