# Datadog DDSQL Actions
Bundle: `com.datadoghq.dd.ddsql` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eddsql)

## com.datadoghq.dd.ddsql.queryInventory
**Run DDSQL query** — Get deeper visibility into your infrastructure by querying your resources with natural language or with [DDSQL](https://docs.datadoghq.com/ddsql_editor/#use-sql-syntax-ddsql), a dialect of SQL with additional support for querying tags.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | yes | The SQL query to run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | rows | array<object> | The rows returned by the query. |


## com.datadoghq.dd.ddsql.tableQuery
**Query** — Get deeper visibility into your infrastructure by querying your resources with natural language or with [DDSQL](https://docs.datadoghq.com/ddsql_editor/#use-sql-syntax-ddsql), a dialect of SQL with additional support for querying tags.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | yes | The DDSQL query to run. 1h default timeframe applies. Other data is unaffected. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Contains the query response data as rows |

