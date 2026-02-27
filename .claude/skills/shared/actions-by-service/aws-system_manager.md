# AWS System Manager Actions
Bundle: `com.datadoghq.aws.system_manager` | 15 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Esystem_manager)

## com.datadoghq.aws.system_manager.deleteInventory
**Delete inventory** — Delete a custom inventory type or the data associated with a custom inventory type. Deleting a custom inventory type is also referred to as deleting a custom inventory schema.
- Stability: stable
- Permissions: `ssm:DeleteInventory`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the custom inventory type for which to delete either all previously collected data, or the inventory type itself. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | typeName | string | The name of the inventory data type specified in the request. |
  | deletionId | string | Every `DeleteInventory` operation is assigned a unique ID. This option returns a unique ID. You can use this ID to query the status of a delete operation. This option is useful for ensuring that a ... |
  | deletionSummary | object | A summary of the delete operation. For more information about this summary, see [Deleting custom inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-custom.html... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.describeParameters
**Describe parameters** — Lists the parameters in your Amazon Web Services account or the parameters shared with you when you enable the Shared option. Request results are returned on a best-effort basis. If you specify MaxResults in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of MaxResults. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a NextToken. You can specify the NextToken in a subsequent call to get the next set of results.  If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, DescribeParameters retrieves whatever the original key alias was referencing.
- Stability: stable
- Permissions: `ssm:DescribeParameters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | This data type is deprecated. Instead, use ParameterFilters. |
  | parameterFilters | array<object> | no | Filters to limit the request results. |
  | maxResults | number | no | The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. |
  | nextToken | string | no | The token for the next set of items to return. (You received this token from a previous call.) |
  | shared | boolean | no | Lists parameters that are shared with you.  By default when using this option, the command returns parameters that have been shared using a standard Resource Access Manager Resource Share. In order... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Parameters | array<object> | Parameters returned by the request. |
  | NextToken | string | The token to use when requesting the next set of items. |


## com.datadoghq.aws.system_manager.getAutomationExecution
**Get automation execution** — Get detailed information about an automation execution.
- Stability: stable
- Permissions: `ssm:GetAutomationExecution`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | automationExecutionId | string | yes | The unique identifier for an existing automation execution. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | automationExecution | object | Detailed information about the current state of an automation execution. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.getCommand
**Get command** — Get commands requested by users of the Amazon Web Services account.
- Stability: stable
- Permissions: `ssm:ListCommands`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | commandId | string | no | The unique identifier for an existing command. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | command | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.getDocument
**Get document** — Get the contents of the specified Amazon Web Services Systems Manager document (SSM document).
- Stability: stable
- Permissions: `ssm:GetDocument`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | documentName | string | yes | The name of the SSM document. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | document | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.getParameter
**Get parameter** — Get information about a single parameter by specifying the parameter name.  To get information about more than one parameter, use the GetParameters operation.
- Stability: stable
- Permissions: `ssm:GetParameter`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name or Amazon Resource Name (ARN) of the parameter that you want to query. For parameters shared with you from another account, you must use the full ARN. To query by parameter label, use "Nam... |
  | withDecryption | boolean | no | Return decrypted values for secure string parameters. This flag is ignored for String and StringList parameter types. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Parameter | object | Information about a parameter. |


## com.datadoghq.aws.system_manager.listAutomationExecutions
**List automation executions** — Provide details about all active and terminated automation executions.
- Stability: stable
- Permissions: `ssm:DescribeAutomationExecutions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters to return a more specific list of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | automationExecutions | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.listCommands
**List commands** — List commands requested by users of the Amazon Web Services account.
- Stability: stable
- Permissions: `ssm:ListCommands`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | no | List commands issued against this managed node ID. |
  | filters | array<object> | no | One or more filters to return a more specific list of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | commands | array<object> | (Optional) The list of commands requested by the user. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.listDocuments
**List documents** — Return all Systems Manager (SSM) documents in the current Amazon Web Services account and region. Use a filter to limit the results.
- Stability: stable
- Permissions: `ssm:ListDocuments`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters to return a more specific list of results. |
  | maxResults | any | no | Indicates the maximum number of items to return. |
  | nextToken | any | no | Pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | documentIdentifiers | array<object> | The names of the SSM documents. |
  | nextToken | any | The token to use when requesting the next set of items. If there are no additional items to return, the string is empty. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.listInventoryData
**List inventory data** — A list of inventory items returned by the request.
- Stability: stable
- Permissions: `ssm:ListInventoryData`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes | The managed node ID for which to retrieve inventory information. |
  | typeName | string | yes | The type of inventory item for which to retrieve information. |
  | filters | array<object> | no | One or more filters to return a more specific list of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | typeName | string | The type of inventory item returned by the request. |
  | instanceId | string | The managed node ID targeted by the request to query inventory information. |
  | schemaVersion | string | The inventory schema version used by the managed node(s). |
  | captureTime | string | The time that inventory information was collected for the managed node(s). |
  | entries | array<object> | A list of inventory items on the managed node(s). |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.putInventory
**Put inventory** — Bulk update custom inventory items on one or more managed nodes. If a specified inventory item does not already exist, it is created.
- Stability: stable
- Permissions: `ssm:PutInventory`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes | A managed node ID in which to add or update inventory items. |
  | items | array<object> | yes | The inventory items to add or update on managed nodes. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.putParameter
**Put parameter** — Add a parameter to the system.
- Stability: stable
- Permissions: `ssm:PutParameter`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The fully qualified name of the parameter that you want to add to the system. The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy,... |
  | description | string | no | Information about the parameter that you want to add to the system. Optional but recommended. Don't enter personally identifiable information in this field. |
  | value | string | yes | The parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB. Parameters can't be referenced or nested in t... |
  | type | string | no | The type of parameter that you want to add to the system. SecureString isn't currently supported for CloudFormation templates. Items in a StringList must be separated by a comma (,). You can't use ... |
  | keyId | string | no | The Key Management Service (KMS) ID that you want to use to encrypt a parameter. Either the default KMS key automatically assigned to your Amazon Web Services account or a custom key. Required for ... |
  | overwrite | boolean | no | Whether or not to overwrite an existing parameter. |
  | allowedPattern | string | no | A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^\d+$ |
  | tags | any | no | Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems ... |
  | tier | string | no | The parameter tier to assign to a parameter. [Parameter Store offers a standard tier and an advanced tier for parameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutPara... |
  | policies | string | no | One or more policies to apply to a parameter. This operation takes a JSON array. [Parameter Store, a capability of Amazon Web Services Systems Manager supports the following policy types](https://d... |
  | dataType | string | no | The data type for a String parameter. Supported data types include plain text and Amazon Machine Image (AMI) IDs. [The following data type values are supported](https://docs.aws.amazon.com/systems-... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | version | number | The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter ver... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.queryInventory
**Query inventory** — Query inventory information. This includes managed node status, such as `Stopped` or `Terminated`.
- Stability: stable
- Permissions: `ssm:GetInventory`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters to return a more specific list of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | entities | array<object> | Collection of inventory entities such as a collection of managed node inventory. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.sendCommand
**Send command** — Run commands on one or more managed nodes.
- Stability: stable
- Permissions: `ssm:SendCommand`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | documentName | string | yes | The name of the SSM document to run. This can be a public document or a custom document. |
  | instanceIds | array<string> | no | The IDs of the managed nodes to run the command. Specifying managed node IDs is most useful when targeting a limited number of managed nodes. You can specify up to 50 IDs. |
  | targets | array<object> | no | An array of search criteria that targets managed nodes using a `Key,Value` combination that you specify. Specifying targets is useful to send a command to a large number of managed nodes at once. T... |
  | parameters | object | no | The required and optional parameters in the document being run. |
  | outputS3BucketName | string | no | The name of the S3 bucket to store command execution responses. |
  | outputS3KeyPrefix | string | no | The directory structure within the S3 bucket to store responses. |
  | maxConcurrency | number | no | The maximum number of targets allowed to run this task in parallel. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | command | object | The request as it was received by Systems Manager. Also provides the command ID which can be used future references to this request. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.system_manager.startAutomationExecution
**Start automation execution** — Initiate execution of an Automation runbook.
- Stability: stable
- Permissions: `ssm:StartAutomationExecution`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | documentName | string | yes | The name of the SSM document to run. This can be a public document or a custom document. |
  | parameters | object | no | The required and optional parameters in the document being run. |
  | targets | object | no | The target resource for the rate-controlled execution, and a key-value mapping to target resources. |
  | maxConcurrency | number | no | The maximum targets allowed to run this task in parallel. Can be a number, such as `10`, or a percentage, such as `10%`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | automationExecutionId | string | The unique ID of a newly scheduled automation execution. |
  | amzRequestId | string | The unique identifier for the request. |

