# Datadog Reference Tables Actions
Bundle: `com.datadoghq.dd.reference_tables` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ereference_tables)

## com.datadoghq.dd.reference_tables.bulkHasKey
**Bulk has key** — Check to see if up to 250 primary keys exist in a given table. If at least one primary key has a matching row, an output is returned. Throws an error if no table with a matching table name is found.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |
  | primaryKeys | array<['string', 'number']> | yes | A set of the primary keys you are trying to look up. |


## com.datadoghq.dd.reference_tables.bulkLookup
**Bulk lookup** — Look up the rows associated with up to 250 primary keys by equality only. If at least one primary key has a matching row, an output will still be returned. Throws an error if:
- No table with a matching table name is found.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |
  | primaryKeys | array<['string', 'number']> | yes | A set of primary keys of the values you are trying to look up. |


## com.datadoghq.dd.reference_tables.getTable
**Get table** — Return up to the 99 first rows from the reference table. An error is thrown if:
- There is no table with matching table name.
- An incorrect column is given.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |
  | columns | array<string> | no | A list of all columns to be outputted. The default is to include every column. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | primaryKey | string |  |
  | rows | array<object> |  |
  | url | string |  |


## com.datadoghq.dd.reference_tables.hasKey
**Has key** — Check to see if a single primary key exists in a given table. Throws an error if no table with a matching table name is found.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |
  | primaryKey | ['string', 'number'] | yes | The value of the primary key you are trying to look up. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hasKey | boolean |  |


## com.datadoghq.dd.reference_tables.lookup
**Lookup** — Look up the row associated with the given primary key by equality only. Throws an error if:
- No table with a matching table name is found.
- No primary key with a matching entry is found.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |
  | primaryKey | ['string', 'number'] | yes | A primary key of the value for lookup. |


## com.datadoghq.dd.reference_tables.tableExists
**Table exists** — Check if a reference table exists, returns true or false.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tableName | string | yes | The name of the table for the lookup. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tableExists | boolean |  |

