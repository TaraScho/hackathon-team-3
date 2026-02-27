# AWS DMS Actions
Bundle: `com.datadoghq.aws.dms` | 9 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Edms)

## com.datadoghq.aws.dms.createMigrationProject
**Create migration project** — Creates the migration project using the specified parameters. You can run this action only after you create an instance profile and data providers using CreateInstanceProfile and CreateDataProvider.
- Stability: stable
- Permissions: `dms:CreateMigrationProject`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | migrationProjectName | string | no | A user-friendly name for the migration project. |
  | sourceDataProviderDescriptors | array<object> | yes | Information about the source data provider, including the name, ARN, and Secrets Manager parameters. |
  | targetDataProviderDescriptors | array<object> | yes | Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters. |
  | instanceProfileIdentifier | string | yes | The identifier of the associated instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consec... |
  | transformationRules | string | no | The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object n... |
  | description | string | no | A user-friendly description of the migration project. |
  | tags | any | no | One or more tags to be assigned to the migration project. |
  | schemaConversionApplicationAttributes | object | no | The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MigrationProject | object | The migration project that was created. |


## com.datadoghq.aws.dms.createReplicationTask
**Create replication task** — Creates a replication task using the specified parameters.
- Stability: stable
- Permissions: `dms:CreateReplicationTask`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationTaskIdentifier | string | yes | An identifier for the replication task. Constraints:   Must contain 1-255 alphanumeric characters or hyphens.   First character must be a letter.   Cannot end with a hyphen or contain two consecuti... |
  | sourceEndpointArn | string | yes | An Amazon Resource Name (ARN) that uniquely identifies the source endpoint. |
  | targetEndpointArn | string | yes | An Amazon Resource Name (ARN) that uniquely identifies the target endpoint. |
  | replicationInstanceArn | string | yes | The Amazon Resource Name (ARN) of a replication instance. |
  | migrationType | string | yes | The migration type. Valid values: full-load \| cdc \| full-load-and-cdc |
  | tableMappings | string | yes | The table mappings for the task, in JSON format. For more information, see Using Table Mapping to Specify Task Settings in the Database Migration Service User Guide. |
  | replicationTaskSettings | string | no | Overall settings for the task, in JSON format. For more information, see Specifying Task Settings for Database Migration Service Tasks in the Database Migration Service User Guide. |
  | cdcStartTime | string | no | Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in ... |
  | cdcStartPosition | string | no | Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results... |
  | cdcStopPosition | string | no | Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”... |
  | tags | any | no | One or more tags to be assigned to the replication task. |
  | taskData | string | no | Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the Database... |
  | resourceIdentifier | string | no | A friendly name for the resource identifier at the end of the EndpointArn response parameter that is returned in the created Endpoint object. The value for this parameter can have up to 31 characte... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationTask | object | The replication task that was created. |


## com.datadoghq.aws.dms.deleteMigrationProject
**Delete migration project** — Deletes the specified migration project.  The migration project must be closed before you can delete it.
- Stability: stable
- Permissions: `dms:DeleteMigrationProject`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | migrationProjectIdentifier | string | yes | The name or Amazon Resource Name (ARN) of the migration project to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MigrationProject | object | The migration project that was deleted. |


## com.datadoghq.aws.dms.describeMigrationProjects
**Describe migration projects** — Returns a paginated list of migration projects for your account in the current region.
- Stability: stable
- Permissions: `dms:DescribeMigrationProjects`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | Filters applied to the migration projects described in the form of key-value pairs. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, DMS includes a pagination token in the response so that you can retrieve the rem... |
  | marker | string | no | Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the val... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the val... |
  | MigrationProjects | array<object> | A description of migration projects. |


## com.datadoghq.aws.dms.describeReplicationTasks
**Describe replication tasks** — Returns information about replication tasks for your account in the current region.
- Stability: stable
- Permissions: `dms:DescribeReplicationTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | Filters applied to replication tasks. Valid filter names: replication-task-arn \| replication-task-id \| migration-type \| endpoint-arn \| replication-instance-arn |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that the remai... |
  | marker | string | no | An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. |
  | withoutSettings | boolean | no | An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose true; otherwise, choose false (the defa... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. |
  | ReplicationTasks | array<object> | A description of the replication tasks. |


## com.datadoghq.aws.dms.modifyMigrationProject
**Modify migration project** — Modifies the specified migration project using the provided parameters.  The migration project must be closed before you can modify it.
- Stability: stable
- Permissions: `dms:ModifyMigrationProject`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | migrationProjectIdentifier | string | yes | The identifier of the migration project. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyph... |
  | migrationProjectName | string | no | A user-friendly name for the migration project. |
  | sourceDataProviderDescriptors | array<object> | no | Information about the source data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters. |
  | targetDataProviderDescriptors | array<object> | no | Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters. |
  | instanceProfileIdentifier | string | no | The name or Amazon Resource Name (ARN) for the instance profile. |
  | transformationRules | string | no | The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object n... |
  | description | string | no | A user-friendly description of the migration project. |
  | schemaConversionApplicationAttributes | object | no | The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MigrationProject | object | The migration project that was modified. |


## com.datadoghq.aws.dms.modifyReplicationTask
**Modify replication task** — Modifies the specified replication task. You can&#x27;t modify the task endpoints. The task must be stopped before you can modify it.  For more information about DMS tasks, see Working with Migration Tasks in the Database Migration Service User Guide.
- Stability: stable
- Permissions: `dms:ModifyReplicationTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationTaskArn | string | yes | The Amazon Resource Name (ARN) of the replication task. |
  | replicationTaskIdentifier | string | no | The replication task identifier. Constraints:   Must contain 1-255 alphanumeric characters or hyphens.   First character must be a letter.   Cannot end with a hyphen or contain two consecutive hyph... |
  | migrationType | string | no | The migration type. Valid values: full-load \| cdc \| full-load-and-cdc |
  | tableMappings | string | no | When using the CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with file://. For example, --table-mappings file://mappingfile.json. When working w... |
  | replicationTaskSettings | string | no | JSON file that contains settings for the task, such as task metadata settings. |
  | cdcStartTime | string | no | Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in ... |
  | cdcStartPosition | string | no | Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results... |
  | cdcStopPosition | string | no | Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”... |
  | taskData | string | no | Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see Specifying Supplemental Data for Task Settings in the Database... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationTask | object | The replication task that was modified. |


## com.datadoghq.aws.dms.startReplicationTask
**Start replication task** — Starts the replication task. For more information about DMS tasks, see Working with Migration Tasks  in the Database Migration Service User Guide.
- Stability: stable
- Permissions: `dms:StartReplicationTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationTaskArn | string | yes | The Amazon Resource Name (ARN) of the replication task to be started. |
  | startReplicationTaskType | string | yes | The type of replication task to start. |
  | cdcStartTime | string | no | Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in ... |
  | cdcStartPosition | string | no | Indicates when you want a change data capture (CDC) operation to start. |
  | cdcStopPosition | string | no | Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationTask | object | The replication task started. |


## com.datadoghq.aws.dms.stopReplicationTask
**Stop replication task** — Stops the replication task.
- Stability: stable
- Permissions: `dms:StopReplicationTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationTaskArn | string | yes | The Amazon Resource Name(ARN) of the replication task to be stopped. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationTask | object | The replication task stopped. |

