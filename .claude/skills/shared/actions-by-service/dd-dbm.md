# Datadog Database Monitoring Actions
Bundle: `com.datadoghq.dd.dbm` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edbm)

## com.datadoghq.dd.dbm.getDatabaseQueryDetailsSource
**Get database query details source** — Get the database query details for source enrichment.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | queryEventId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | inTransaction | boolean |  |
  | operationType | string |  |
  | instance | string |  |
  | tables | array<string> |  |
  | commands | array<string> |  |
  | querySignature | string |  |
  | statement | string |  |
  | user | string |  |
  | pid | string |  |
  | queryStart | string |  |
  | xActStart | string |  |
  | duration | string |  |
  | tags | array<string> |  |

