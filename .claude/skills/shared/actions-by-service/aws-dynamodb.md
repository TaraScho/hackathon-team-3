# AWS DynamoDB Actions
Bundle: `com.datadoghq.aws.dynamodb` | 10 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Edynamodb)

## com.datadoghq.aws.dynamodb.delete_item
**Delete item** — Delete a single item in a table by primary key.
- Stability: stable
- Permissions: `dynamodb:DeleteItem`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table from which to delete the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |
  | key | object | yes | A map of attribute names to `AttributeValue` objects, representing the primary key of the item. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.describeContinuousBackups
**Describe continuous backups** — Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED.  After continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime.   LatestRestorableDateTime is typically 5 minutes before the current time. You can restore your table to any point in time during the last 35 days.  You can call DescribeContinuousBackups at a maximum rate of 10 times per second.
- Stability: stable
- Permissions: `dynamodb:DescribeContinuousBackups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | Name of the table for which the customer wants to check the continuous backups and point in time recovery settings. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ContinuousBackupsDescription | object | Represents the continuous backups and point in time recovery settings on the table. |


## com.datadoghq.aws.dynamodb.describe_table
**Describe DynamoDB table** — Return information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.
- Stability: stable
- Permissions: `dynamodb:DescribeTable`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | table | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.getAWSDynamoDBGlobalTable
**Describe global table** — Get details about a global table.
- Stability: stable
- Permissions: `dynamodb:Describe*`, `application-autoscaling:Describe*`, `cloudwatch:PutMetricData`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | globalTable | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.get_item
**Get item** — Return a set of attributes for the item with the given primary key.
- Stability: stable
- Permissions: `dynamodb:GetItem`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table containing the requested item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |
  | key | object | yes | A map of attribute names to `AttributeValue` objects, representing the primary key of the item. |
  | attributes | string | no | A string that identifies one or more attributes to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, all attributes are ret... |
  | consistentRead | boolean | no |  |
  | allowMissingValues | boolean | no | When this is enabled, values not found in the database will be considered undefined. When disabled, missing values are treated as errors. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.listAWSDynamoDBGlobalTable
**List global tables** — List global tables.
- Stability: stable
- Permissions: `dynamodb:ListTables`, `cloudwatch:PutMetricData`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | globalTables | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.put_item
**Put item** — Create a new item, or replace an old item with a new item.
- Stability: stable
- Permissions: `dynamodb:PutItem`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table to contain the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |
  | item | object | yes | A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object | The attribute values as they appeared before the PutItem operation, but only if ReturnValues is specified as ALL_OLD in the request. Each element consists of an attribute name and an attribute value. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.scanItems
**Scan items** — Return one or more items and item attributes by accessing every item in a table. To have DynamoDB return fewer items, you can provide a `filterExpression` input.
- Stability: stable
- Permissions: `dynamodb:Scan`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table containing the requested items or if you provide IndexName, the name of the table to which that index belongs. You can also provide the Amazon Resource Name (ARN) of the table... |
  | filterExpression | string | no | A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned. R... |
  | expressionAttributeNames | object | no | One or more substitution tokens for attribute names in an expression. Use the # character in an expression to dereference an attribute name. |
  | expressionAttributeValues | object | no | One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. |
  | attributes | string | no | A string that identifies one or more attributes to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, all attributes are ret... |
  | limit | number | no | The maximum number of items to evaluate (not necessarily the number of matching items). |
  | consistentRead | boolean | no | A Boolean value that determines the read consistency model during the scan. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | Items | array<object> | An array of item attributes that match the scan criteria. Each element in this array consists of an attribute name and the value for that attribute. |
  | Count | number | The number of items in the response. If you set ScanFilter in the request, then Count is the number of items returned after the filter was applied, and ScannedCount is the number of matching items ... |
  | ScannedCount | number | The number of items evaluated, before any ScanFilter is applied. A high ScannedCount value with few, or no, Count results indicates an inefficient Scan operation. For more information, see Count an... |
  | LastEvaluatedKey | object | The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request. If LastEvaluatedKey ... |
  | ConsumedCapacity | object | The capacity units consumed by the Scan operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operatio... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.dynamodb.updateContinuousBackups
**Update continuous backups** — UpdateContinuousBackups enables or disables point in time recovery for the specified table. A successful UpdateContinuousBackups call returns the current ContinuousBackupsDescription. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED.  Once continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime.   LatestRestorableDateTime is typically 5 minutes before the current time. You can restore your table to any point in time during the last 35 days.
- Stability: stable
- Permissions: `dynamodb:UpdateContinuousBackups`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |
  | pointInTimeRecoverySpecification | object | yes | Represents the settings used to enable point in time recovery. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ContinuousBackupsDescription | object | Represents the continuous backups and point in time recovery settings on the table. |


## com.datadoghq.aws.dynamodb.update_item
**Update item** — Edit an existing item's attributes, or add a new item to the table if it does not already exist.
- Stability: stable
- Permissions: `dynamodb:UpdateItem`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | tableName | string | yes | The name of the table containing the item to update. You can also provide the Amazon Resource Name (ARN) of the table in this parameter. |
  | key | object | yes | A map of attribute names to `AttributeValue` objects, representing the primary key of the item. |
  | updateExpression | string | yes | An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them. See [AWS documentation](https://docs.aws.amazon.com/amazondynamodb/late... |
  | updateValues | object | yes | One or more values that can be substituted in an expression. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | item | object |  |
  | amzRequestId | string | The unique identifier for the request. |

