# Datadog Embeddable Graphs Actions
Bundle: `com.datadoghq.dd.embeddablegraphs` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eembeddablegraphs)

## com.datadoghq.dd.embeddablegraphs.enableEmbeddableGraph
**Enable embeddable graph** — Enable a specified embed.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | embed_id | string | yes | ID of the embed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | success | string | Message. |


## com.datadoghq.dd.embeddablegraphs.getEmbeddableGraph
**Get embeddable graph** — Get the HTML fragment for a previously generated embed with `embed_id`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | embed_id | string | yes | Token of the embed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dash_name | string | Name of the dashboard the graph is on (null if none). |
  | dash_url | string | URL of the dashboard the graph is on (null if none). |
  | embed_id | string | ID of the embed. |
  | graph_title | string | Title of the graph. |
  | html | string | HTML fragment for the embed (iframe). |
  | revoked | boolean | Boolean flag for whether or not the embed is revoked. |
  | shared_by | number | ID of the use who shared the embed. |


## com.datadoghq.dd.embeddablegraphs.listEmbeddableGraphs
**List embeddable graphs** — Gets a list of previously created embeddable graphs.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | embedded_graphs | array<object> | List of embeddable graphs. |


## com.datadoghq.dd.embeddablegraphs.revokeEmbeddableGraph
**Revoke embeddable graph** — Revoke a specified embed.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | embed_id | string | yes | ID of the embed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | success | string | Message. |

