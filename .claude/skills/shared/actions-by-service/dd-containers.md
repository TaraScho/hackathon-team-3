# Datadog Containers Actions
Bundle: `com.datadoghq.dd.containers` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Econtainers)

## com.datadoghq.dd.containers.listContainerImages
**List container images** — Get all Container Images for your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_tags | any | no | Filter by tags. |
  | group_by | string | no | Comma-separated list of tags to group Container Images by. |
  | sort | string | no | Attribute to sort Container Images by. |
  | page_size | number | no | Maximum number of results returned. |
  | page_cursor | ['string', 'null'] | no | String to query the next page of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of Container Image objects. |
  | links | object | Pagination links. |
  | meta | object | Response metadata object. |


## com.datadoghq.dd.containers.listContainers
**List containers** — Get all containers for your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_tags | any | no | Filter by tags. |
  | group_by | string | no | Comma-separated list of tags to group containers by. |
  | sort | string | no | Attribute to sort containers by. |
  | page_size | number | no | Maximum number of results returned. |
  | page_cursor | ['string', 'null'] | no | String to query the next page of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of Container objects. |
  | links | object | Pagination links. |
  | meta | object | Response metadata object. |

