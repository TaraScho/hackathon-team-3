# AWS RDS Actions
Bundle: `com.datadoghq.aws.rds` | 21 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Erds)

## com.datadoghq.aws.rds.applyPendingMaintenanceAction
**Apply pending maintenance action** — Applies a pending maintenance action to a resource (for example, to a DB instance).
- Stability: stable
- Permissions: `rds:ApplyPendingMaintenanceAction`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceIdentifier | string | yes | The RDS Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see  Constructing an RDS Amazon Resource Name (ARN). |
  | applyAction | string | yes | The pending maintenance action to apply to this resource. Valid Values: system-update, db-upgrade, hardware-maintenance, ca-certificate-rotation |
  | optInType | string | yes | A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type immediate can't be undone. Valid Values:    immediate - Apply the maintenance action immedi... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ResourcePendingMaintenanceActions | object |  |


## com.datadoghq.aws.rds.createRdsDbInstance
**Create DB instance** — Create a new DB instance.
- Stability: stable
- Permissions: `rds:CreateDBInstance`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | engine | string | yes | The database engine to use for this DB instance. Not every database engine is available in every AWS Region. |
  | dbInstanceClass | string | yes | The compute and memory capacity of the DB instance. Not all DB instance classes are available in all AWS Regions, or for all database engines. |
  | dbInstanceIdentifier | string | yes | The identifier for this DB instance. This parameter is stored as a lowercase string. Constraints:   Must contain from 1 to 63 letters, numbers, or hyphens.   First character must be a letter.   Can... |
  | dbClusterIdentifier | string | no | The identifier of the DB cluster to add this instance to. |
  | masterUsername | string | no | The name for the master user. Not applicable for Aurora DB instances; master username is managed by the cluster. Constraints: It can contain 1–16 alphanumeric characters and underscores. Its first ... |
  | allocatedStorage | number | no | The amount of storage in gibibytes (GiB) to allocate for the DB instance. Not applicable for Aurora DB instances. |
  | licenseModel | string | no | The license model information for this DB instance.  License models for RDS for Db2 require additional configuration. The Bring Your Own License (BYOL) model requires a custom parameter group. The ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.createRdsDbInstanceReadReplica
**Create DB instance read replica** — Create a new DB instance that acts as a read replica for an existing source DB instance. All read replica DB instances are created with backups disabled. All other attributes (including DB security groups and DB parameter groups) are inherited from the source DB instance or cluster.
- Stability: stable
- Permissions: `rds:CreateDBInstanceReadReplica`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbInstanceIdentifier | string | yes | Identifier of the read replica. |
  | sourceDBInstanceIdentifier | string | no | Identifier of the DB Instance to be replicated. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.deleteRdsDbInstance
**Delete DB instance** — Delete a previously provisioned DB instance.
- Stability: stable
- Permissions: `rds:DeleteDBInstance`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbInstanceIdentifier | string | yes | The DB instance identifier for the DB instance to be deleted. This parameter isn't case-sensitive. Constraints:   Must match the name of an existing DB instance. |
  | finalSnapshot | any | yes | Whether to create a final snapshot of the DB or not. |
  | deleteAutomatedBackups | boolean | yes | Whether all automated backups for that instance are deleted or not. Manual DB snapshots of the DB instance will not be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.describeDBCluster
**Describe DB cluster** — Describe existing Amazon Aurora DB cluster or Multi-AZ DB cluster.
- Stability: stable
- Permissions: `rds:DescribeDBClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbClusterIdentifier | string | yes | User-supplied, case-insensitive, DB cluster identifier or the Amazon Resource Name (ARN) of the DB cluster. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbCluster | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.describeDBEngineVersions
**Describe DB engine versions** — Describes the properties of specific versions of DB engines.
- Stability: stable
- Permissions: `rds:DescribeDBEngineVersions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | engine | string | no | The database engine to return version details for. Valid Values:    aurora-mysql     aurora-postgresql     custom-oracle-ee     custom-oracle-ee-cdb     custom-oracle-se2     custom-oracle-se2-cdb ... |
  | engineVersion | string | no | A specific database engine version to return details for. Example: 5.1.49 |
  | dBParameterGroupFamily | string | no | The name of a specific DB parameter group family to return details for. Constraints:   If supplied, must match an existing DB parameter group family. |
  | filters | array<object> | no | A filter that specifies one or more DB engine versions to describe. Supported filters:    db-parameter-group-family - Accepts parameter groups family names. The results list only includes informati... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more than the MaxRecords value is available, a pagination token called a marker is included in the response so you can retrieve the rema... |
  | marker | string | no | An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. |
  | defaultOnly | boolean | no | Specifies whether to return only the default version of the specified engine or the engine and major version combination. |
  | listSupportedCharacterSets | boolean | no | Specifies whether to list the supported character sets for each engine version. If this parameter is enabled and the requested engine supports the CharacterSetName parameter for CreateDBInstance, t... |
  | listSupportedTimezones | boolean | no | Specifies whether to list the supported time zones for each engine version. If this parameter is enabled and the requested engine supports the TimeZone parameter for CreateDBInstance, the response ... |
  | includeAll | boolean | no | Specifies whether to also list the engine versions that aren't available. The default is to list only available engine versions. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords. |
  | DBEngineVersions | array<object> | A list of DBEngineVersion elements. |


## com.datadoghq.aws.rds.describePendingMaintenanceActions
**Describe pending maintenance actions** — Returns a list of resources (for example, DB instances) that have at least one pending maintenance action.
- Stability: stable
- Permissions: `rds:DescribePendingMaintenanceActions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceIdentifier | string | no | The ARN of a resource to return pending maintenance actions for. |
  | filters | array<object> | no | A filter that specifies one or more resources to return pending maintenance actions for. Supported filters:    db-cluster-id - Accepts DB cluster identifiers and DB cluster Amazon Resource Names (A... |
  | marker | string | no | An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number o... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so that you can r... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | PendingMaintenanceActions | array<object> | A list of the pending maintenance actions for the resource. |
  | Marker | string | An optional pagination token provided by a previous DescribePendingMaintenanceActions request. If this parameter is specified, the response includes only records beyond the marker, up to a number o... |


## com.datadoghq.aws.rds.describe_db_instance
**Describe DB instance** — Describe a DB instance.
- Stability: stable
- Permissions: `rds:DescribeDBInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dbInstanceIdentifier | string | no |  |
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.listDBClusters
**List DB clusters** — List existing Amazon Aurora DB clusters and Multi-AZ DB clusters.
- Stability: stable
- Permissions: `rds:DescribeDBClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no | Maximum number of records to include in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbClusters | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.list_db_instances
**List DB instances** — List DB instances with optional filters.
- Stability: stable
- Permissions: `rds:DescribeDBInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | A filter that specifies one or more DB instances to describe. Supported filters: db-cluster-id, db-instance-id, dbi-resource-id, domain, engine. |
  | maxRecords | number | no |  |
  | marker | any | no | Pagination parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstances | array<object> | A list of DBInstance objects. |
  | marker | any | An optional pagination token provided by a previous DescribeDBInstances request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by M... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.modifyDBInstance
**Modify DB instance** — Modifies settings for a DB instance. You can change one or more database configuration parameters by specifying these parameters and the new values in the request.
- Stability: stable
- Permissions: `rds:ModifyDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dBInstanceIdentifier | string | yes | Database instance identifier |
  | allocatedStorage | number | no | The new amount of storage in gibibytes (GiB) to allocate for the DB instance. For RDS for Db2, MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL, the value supplied must be at least 10... |
  | dBInstanceClass | string | no | The new compute and memory capacity of the DB instance, for example db.m4.large. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the f... |
  | dBSubnetGroupName | string | no | The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. If your DB instance isn't in a VPC, you can also use this parameter to move your... |
  | dBSecurityGroups | array<string> | no | A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible. This setting doesn't a... |
  | vpcSecurityGroupIds | array<string> | no | A list of Amazon EC2 VPC security groups to associate with this DB instance. This change is asynchronously applied as soon as possible. This setting doesn't apply to the following DB instances:   A... |
  | applyImmediately | boolean | no | Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the PreferredMaintenanceWindow setting for the DB ins... |
  | masterUserPassword | string | no | The new password for the master user. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. Between the time of the request and the compl... |
  | dBParameterGroupName | string | no | The name of the DB parameter group to apply to the DB instance. Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter c... |
  | backupRetentionPeriod | number | no | The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.  Enabling and disabling backups ... |
  | preferredBackupWindow | string | no | The daily time range during which automated backups are created if automated backups are enabled, as determined by the BackupRetentionPeriod parameter. Changing this parameter doesn't result in an ... |
  | preferredMaintenanceWindow | string | no | The weekly time range during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the cha... |
  | multiAZ | boolean | no | Specifies whether the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage. The change is applied during the next maintenance window unless the ApplyImmediately... |
  | engineVersion | string | no | The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the ApplyImmediately parame... |
  | allowMajorVersionUpgrade | boolean | no | Specifies whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. This setting doesn't apply to... |
  | autoMinorVersionUpgrade | boolean | no | Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window. An outage occurs when all the following conditions are met:   The automatic upgr... |
  | licenseModel | string | no | The license model for the DB instance. This setting doesn't apply to Amazon Aurora or RDS Custom DB instances. Valid Values:   RDS for Db2 - bring-your-own-license    RDS for MariaDB - general-publ... |
  | iops | number | no | The new Provisioned IOPS (I/O operations per second) value for the RDS instance. Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unles... |
  | optionGroupName | string | no | The option group to associate the DB instance with. Changing this parameter doesn't result in an outage, with one exception. If the parameter change results in an option group that enables OEM, it ... |
  | newDBInstanceIdentifier | string | no | The new identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot occurs immediately if you enable ApplyImmediately, or will occur d... |
  | storageType | string | no | The storage type to associate with the DB instance. If you specify io1, io2, or gp3 you must also include a value for the Iops parameter. If you choose to migrate your DB instance from using standa... |
  | tdeCredentialArn | string | no | The ARN from the key store with which to associate the instance for TDE encryption. This setting doesn't apply to RDS Custom DB instances. |
  | tdeCredentialPassword | string | no | The password for the given ARN from the key store in order to access the device. This setting doesn't apply to RDS Custom DB instances. |
  | cACertificateIdentifier | string | no | The CA certificate identifier to use for the DB instance's server certificate. This setting doesn't apply to RDS Custom DB instances. For more information, see Using SSL/TLS to encrypt a connection... |
  | domain | string | no | The Active Directory directory ID to move the DB instance to. Specify none to remove the instance from its current domain. You must create the domain before this operation. Currently, you can creat... |
  | domainFqdn | string | no | The fully qualified domain name (FQDN) of an Active Directory domain. Constraints:   Can't be longer than 64 characters.   Example: mymanagedADtest.mymanagedAD.mydomain |
  | domainOu | string | no | The Active Directory organizational unit for your DB instance to join. Constraints:   Must be in the distinguished name format.   Can't be longer than 64 characters.   Example: OU=mymanagedADtestOU... |
  | domainAuthSecretArn | string | no | The ARN for the Secrets Manager secret with the credentials for the user joining the domain. Example: arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456 |
  | domainDnsIps | array<string> | no | The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers. Constraints:   Two IP addresses must be provided. If there isn't a secondary domain controller, use the ... |
  | copyTagsToSnapshot | boolean | no | Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags aren't copied. This setting doesn't apply to Amazon Aurora DB instances. Copying tags to sn... |
  | monitoringInterval | number | no | The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify 0. If MonitoringRoleArn is... |
  | dBPortNumber | number | no | The port number on which the database accepts connections. The value of the DBPortNumber parameter must not match any of the port values specified for options in the option group for the DB instanc... |
  | publiclyAccessible | boolean | no | Specifies whether the DB instance is publicly accessible. When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name ... |
  | monitoringRoleArn | string | no | The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, arn:aws:iam:123456789012:role/emaccess. For information on creating a monitorin... |
  | domainIAMRoleName | string | no | The name of the IAM role to use when making API calls to the Directory Service. This setting doesn't apply to RDS Custom DB instances. |
  | disableDomain | boolean | no | Specifies whether to remove the DB instance from the Active Directory domain. |
  | promotionTier | number | no | The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see  Fault Tolerance for an Aurora DB Cl... |
  | enableIAMDatabaseAuthentication | boolean | no | Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled. This setting doesn't apply to Amazo... |
  | enablePerformanceInsights | boolean | no | Specifies whether to enable Performance Insights for the DB instance. For more information, see Using Amazon Performance Insights in the Amazon RDS User Guide. This setting doesn't apply to RDS Cus... |
  | performanceInsightsKMSKeyId | string | no | The Amazon Web Services KMS key identifier for encryption of Performance Insights data. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. ... |
  | performanceInsightsRetentionPeriod | number | no | The number of days to retain Performance Insights data. This setting doesn't apply to RDS Custom DB instances. Valid Values:    7     month * 31, where month is a number of months from 1-23. Exampl... |
  | cloudwatchLogsExportConfiguration | object | no | The log types to be enabled for export to CloudWatch Logs for a specific DB instance. A change to the CloudwatchLogsExportConfiguration parameter is always applied to the DB instance immediately. T... |
  | processorFeatures | array<object> | no | The number of CPU cores and the number of threads per core for the DB instance class of the DB instance. This setting doesn't apply to RDS Custom DB instances. |
  | useDefaultProcessorFeatures | boolean | no | Specifies whether the DB instance class of the DB instance uses its default processor features. This setting doesn't apply to RDS Custom DB instances. |
  | deletionProtection | boolean | no | Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more informa... |
  | maxAllocatedStorage | number | no | The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance. For more information about this setting, including limitations that apply to it, see  ... |
  | certificateRotationRestart | boolean | no | Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate. By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not up... |
  | replicaMode | string | no | A value that sets the open mode of a replica database to either mounted or read-only.  Currently, this parameter is only supported for Oracle DB instances.  Mounted DB replicas are included in Orac... |
  | enableCustomerOwnedIp | boolean | no | Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance. A CoIP provides local or external connectivity to resources in your Outpost subnets through your o... |
  | awsBackupRecoveryPointArn | string | no | The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup. This setting doesn't apply to RDS Custom DB instances. |
  | automationMode | string | no | The automation mode of the RDS Custom DB instance. If full, the DB instance automates monitoring and instance recovery. If all paused, the instance pauses automation for the duration set by ResumeF... |
  | resumeFullAutomationModeMinutes | number | no | The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation. Default: 60  Constraints:   Must be at least 60.   Must be no more than 1,440. |
  | networkType | string | no | The network type of the DB instance. The network type is determined by the DBSubnetGroup specified for the DB instance. A DBSubnetGroup can support only the IPv4 protocol or the IPv4 and the IPv6 p... |
  | storageThroughput | number | no | The storage throughput value for the DB instance. This setting applies only to the gp3 storage type. This setting doesn't apply to Amazon Aurora or RDS Custom DB instances. |
  | manageMasterUserPassword | boolean | no | Specifies whether to manage the master user password with Amazon Web Services Secrets Manager. If the DB instance doesn't manage the master user password with Amazon Web Services Secrets Manager, y... |
  | rotateMasterUserPassword | boolean | no | Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password. This setting is valid only if the master user password is managed by RDS in Amazo... |
  | masterUserSecretKmsKeyId | string | no | The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager. This setting is valid only if both of the followin... |
  | engine | string | no | The target Oracle DB engine when you convert a non-CDB to a CDB. This intermediate step is necessary to upgrade an Oracle Database 19c non-CDB to an Oracle Database 21c CDB. Note the following requ... |
  | dedicatedLogVolume | boolean | no | Indicates whether the DB instance has a dedicated log volume (DLV) enabled. |
  | multiTenant | boolean | no | Specifies whether the to convert your DB instance from the single-tenant conﬁguration to the multi-tenant conﬁguration. This parameter is supported only for RDS for Oracle CDB instances. During the... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DBInstance | object |  |


## com.datadoghq.aws.rds.rebootDBCluster
**Reboot DB cluster** — Reboots a DB cluster. After the reboot, the DB cluster is available, but the primary DB instance is taken offline. This action results in a momentary outage for the DB cluster during which the primary DB cluster status is set to rebooting.
- Stability: stable
- Permissions: `rds:RebootDBCluster`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dBClusterIdentifier | string | yes | Database cluster identifier |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DBCluster | object |  |


## com.datadoghq.aws.rds.rebootDBInstance
**Reboot DB instance** — Reboots a previously provisioned DB instance. This action results in a momentary outage for the instance, during which the instance status is set to rebooting.
- Stability: stable
- Permissions: `rds:RebootDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dBInstanceIdentifier | string | yes | Database instance identifier |
  | forceFailover | boolean | no | Specifies whether the reboot is conducted through a Multi-AZ failover. Constraint: You can't enable force failover if the instance isn't configured for Multi-AZ. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DBInstance | object |  |


## com.datadoghq.aws.rds.rebootDBShardGroup
**Reboot DB shard group** — You might need to reboot your DB shard group, usually for maintenance reasons. For example, if you make certain modifications, reboot the DB shard group for the changes to take effect. This operation applies only to Aurora Limitless Database DBb shard groups.
- Stability: stable
- Permissions: `rds:RebootDBShardGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dBShardGroupIdentifier | string | yes | The name of the DB shard group to reboot. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DBShardGroupResourceId | string | The Amazon Web Services Region-unique, immutable identifier for the DB shard group. |
  | DBShardGroupIdentifier | string | The name of the DB shard group. |
  | DBClusterIdentifier | string | The name of the primary DB cluster for the DB shard group. |
  | MaxACU | number | The maximum capacity of the DB shard group in Aurora capacity units (ACUs). |
  | MinACU | number | The minimum capacity of the DB shard group in Aurora capacity units (ACUs). |
  | ComputeRedundancy | number | Specifies whether to create standby instances for the DB shard group. Valid values are the following:   0 - Creates a single, primary DB instance for each physical shard. This is the default value,... |
  | Status | string | The status of the DB shard group. |
  | PubliclyAccessible | boolean | Indicates whether the DB shard group is publicly accessible. When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the... |
  | Endpoint | string | The connection endpoint for the DB shard group. |


## com.datadoghq.aws.rds.set_autoscale_params
**Set min and max autoscale capacity** — Set Min and Max capacity in the scaling configuration of an Aurora Serverless DB cluster.
- Stability: stable
- Permissions: `rds:ModifyDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbClusterIdentifier | string | yes | The DB cluster identifier for the cluster being modified. This parameter isn't case-sensitive. Valid for Cluster Type: Aurora DB clusters and Multi-AZ DB clusters Constraints:   Must match the iden... |
  | minCapacity | number | no | The minimum capacity for an Aurora DB cluster in `serverless` DB engine mode. For Aurora MySQL, valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. For Aurora PostgreS... |
  | maxCapacity | number | no | The maximum capacity for an Aurora DB cluster in `serverless` DB engine mode. For Aurora MySQL, valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. For Aurora PostgreS... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbCluster | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.startDBCluster
**Start DB cluster** — Start an Amazon Aurora DB cluster that was stopped.
- Stability: stable
- Permissions: `rds:StartDBCluster`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbClusterIdentifier | string | yes | The DB cluster identifier of the Amazon Aurora DB cluster to be started. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbCluster | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.start_rds_db_instance
**Start DB instance** — Start an Amazon RDS DB instance that was stopped using the Amazon Web Services console, the stop-db-instance CLI command, or the StopDBInstance action.
- Stability: stable
- Permissions: `rds:StartDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dbInstanceIdentifier | string | yes | The user-supplied instance identifier. |
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.stopDBCluster
**Stop DB cluster** — Stop an Amazon Aurora DB cluster. When you stop a DB cluster, Aurora retains the DB cluster's metadata, including its endpoints and DB parameter groups.
- Stability: stable
- Permissions: `rds:StopDBCluster`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dbClusterIdentifier | string | yes | The DB cluster identifier of the Amazon Aurora DB cluster to be stopped. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbCluster | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.stop_rds_db_instance
**Stop DB instance** — Stop an Amazon RDS DB instance.
- Stability: stable
- Permissions: `rds:StopDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dbInstanceIdentifier | string | yes | The user-supplied instance identifier. |
  | region | string | yes |  |
  | dbSnapshotIdentifier | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.update_allocated_storage
**Update allocated storage** — The new amount of storage in gibibytes (GiB) to allocate for the DB instance.
- Stability: stable
- Permissions: `rds:ModifyDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dbInstanceIdentifier | string | yes | The identifier of DB instance to modify. This value is stored as a lowercase string. Constraints:   Must match the identifier of an existing DB instance. |
  | region | string | yes |  |
  | allocatedStorage | number | no | The new storage amount in GiB for the RDS instance. Must be at least 10% greater than current value for MariaDB, MySQL, Oracle, and PostgreSQL and will be rounded up if not to be at least 10% if a ... |
  | iops | number | no |  |
  | applyImmediately | boolean | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.rds.update_security_groups
**Update instance security groups** — A list of DB security groups or VPC security groups to authorize on this DB instance.
- Stability: stable
- Permissions: `rds:ModifyDBInstance`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | dbInstanceIdentifier | string | yes | The identifier of DB instance to modify. This value is stored as a lowercase string. Constraints:   Must match the identifier of an existing DB instance. |
  | region | string | yes |  |
  | dbSecurityGroups | array<string> | no |  |
  | vpcSecurityGroups | array<string> | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | dbInstanceIdentifier | string |  |
  | amzRequestId | string | The unique identifier for the request. |

