# Datadog CSM Agents Actions
Bundle: `com.datadoghq.dd.csm.agents` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecsm%2Eagents)

## com.datadoghq.dd.csm.agents.listAllCSMAgents
**List all CSM Agents** — Get the list of all CSM Agents running on your hosts and containers.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page | number | no | The page index for pagination (zero-based). |
  | size | number | no | The number of items to include in a single page. |
  | query | string | no | A search query string to filter results (for example, `hostname:COMP-T2H4J27423`). |
  | order_direction | string | no | The sort direction for results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of Agents. |
  | meta | object | Metadata related to the paginated response. |


## com.datadoghq.dd.csm.agents.listAllCSMServerlessAgents
**List all CSM Serverless Agents** — Get the list of all CSM Serverless Agents running on your hosts and containers.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page | number | no | The page index for pagination (zero-based). |
  | size | number | no | The number of items to include in a single page. |
  | query | string | no | A search query string to filter results (for example, `hostname:COMP-T2H4J27423`). |
  | order_direction | string | no | The sort direction for results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of Agents. |
  | meta | object | Metadata related to the paginated response. |

