# AWS ElastiCache Actions
Bundle: `com.datadoghq.aws.elasticache` | 66 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eelasticache)

## com.datadoghq.aws.elasticache.addTagsToResource
**Add tags to resource** — Add metadata tags (key-value pairs) to a specified ElastiCache resource.
- Stability: stable
- Permissions: `elasticache:AddTagsToResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceName | string | yes | The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:0123456789:... |
  | tags | any | yes | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TagList | array<object> | A list of tags as key-value pairs. |


## com.datadoghq.aws.elasticache.authorizeCacheSecurityGroupIngress
**Authorize cache security group ingress** — Allows network ingress to a cache security group.
- Stability: stable
- Permissions: `elasticache:AuthorizeCacheSecurityGroupIngress`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSecurityGroupName | string | yes | The cache security group that allows network ingress. |
  | eC2SecurityGroupName | string | yes | The Amazon EC2 security group to be authorized for ingress to the cache security group. |
  | eC2SecurityGroupOwnerId | string | yes | The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheSecurityGroup | object |  |


## com.datadoghq.aws.elasticache.batchApplyUpdateAction
**Batch apply update action** — Applies the service update to a batch of cache clusters.
- Stability: stable
- Permissions: `elasticache:BatchApplyUpdateAction`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupIds | array<string> | no | The replication group IDs |
  | cacheClusterIds | array<string> | no | The cache cluster IDs |
  | serviceUpdateName | string | yes | The unique ID of the service update |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProcessedUpdateActions | array<object> | Update actions that have been processed successfully |
  | UnprocessedUpdateActions | array<object> | Update actions that haven't been processed successfully |


## com.datadoghq.aws.elasticache.batchStopUpdateAction
**Batch stop update action** — Stops the service update for a batch of cache clusters.
- Stability: stable
- Permissions: `elasticache:BatchStopUpdateAction`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupIds | array<string> | no | The replication group IDs |
  | cacheClusterIds | array<string> | no | The cache cluster IDs |
  | serviceUpdateName | string | yes | The unique ID of the service update |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProcessedUpdateActions | array<object> | Update actions that have been processed successfully |
  | UnprocessedUpdateActions | array<object> | Update actions that haven't been processed successfully |


## com.datadoghq.aws.elasticache.completeMigration
**Complete migration** — Complete the migration of data.
- Stability: stable
- Permissions: `elasticache:CompleteMigration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The ID of the replication group to which data is being migrated. |
  | force | boolean | no | Forces the migration to stop without ensuring that data is in sync. It is recommended to use this option only to abort the migration and not recommended when application wants to continue migration... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.copyServerlessCacheSnapshot
**Copy serverless cache snapshot** — Creates a copy of an existing serverless cache’s snapshot. Available for Redis OSS and Serverless Memcached only.
- Stability: stable
- Permissions: `elasticache:CopyServerlessCacheSnapshot`
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceServerlessCacheSnapshotName | string | yes | The identifier of the existing serverless cache’s snapshot to be copied. Available for Redis OSS and Serverless Memcached only. |
  | targetServerlessCacheSnapshotName | string | yes | The identifier for the snapshot to be created. Available for Redis OSS and Serverless Memcached only. |
  | kmsKeyId | string | no | The identifier of the KMS key used to encrypt the target snapshot. Available for Redis OSS and Serverless Memcached only. |
  | tags | any | no | A list of tags to be added to the target snapshot resource. A tag is a key-value pair. Available for Redis OSS and Serverless Memcached only. Default: NULL |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCacheSnapshot | object | The response for the attempt to copy the serverless cache snapshot. Available for Redis OSS and Serverless Memcached only. |


## com.datadoghq.aws.elasticache.copySnapshot
**Copy snapshot** — Makes a copy of an existing snapshot. This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:CopySnapshot`
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceSnapshotName | string | yes | The name of an existing snapshot from which to make a copy. |
  | targetSnapshotName | string | yes | A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting. |
  | targetBucket | string | no | The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access. When using this parameter to export a snapshot, be sure Amazon Ela... |
  | kmsKeyId | string | no | The ID of the KMS key used to encrypt the target snapshot. |
  | tags | any | no | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Snapshot | object |  |


## com.datadoghq.aws.elasticache.createCacheCluster
**Create cache cluster** — Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached or Redis OSS. This operation is not supported for Redis OSS (cluster mode enabled) clusters.
- Stability: stable
- Permissions: `elasticache:CreateCacheCluster`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | yes | The node group (shard) identifier. This parameter is stored as a lowercase string.  Constraints:    A name must contain from 1 to 50 alphanumeric characters or hyphens.   The first character must b... |
  | replicationGroupId | string | no | The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluste... |
  | aZMode | string | no | Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region. This parameter is only support... |
  | preferredAvailabilityZone | string | no | The EC2 Availability Zone in which the cluster is created. All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availa... |
  | preferredAvailabilityZones | array<string> | no | A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important. This option is only supported on Memcached.  If you are creating your cluster... |
  | numCacheNodes | number | no | The initial number of cache nodes that the cluster has. For clusters running Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40. If you need more t... |
  | cacheNodeType | string | no | The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory a... |
  | engine | string | no | The name of the cache engine to be used for this cluster. Valid values for this parameter are: memcached \| redis |
  | engineVersion | string | no | The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.  Important: You can upgrade to a newe... |
  | cacheParameterGroupName | string | no | The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which h... |
  | cacheSubnetGroupName | string | no | The name of the subnet group to be used for the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).  If you're going to launch your clu... |
  | cacheSecurityGroupNames | array<string> | no | A list of security group names to associate with this cluster. Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). |
  | securityGroupIds | array<string> | no | One or more VPC security groups associated with the cluster. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC). |
  | tags | any | no | A list of tags to be added to this resource. |
  | snapshotArns | array<string> | no | A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis OSS RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node grou... |
  | snapshotName | string | no | The name of a Redis OSS snapshot from which to restore data into the new node group (shard). The snapshot status changes to restoring while the new node group (shard) is being created.  This parame... |
  | preferredMaintenanceWindow | string | no | Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance windo... |
  | port | number | no | The port number on which each of the cache nodes accepts connections. |
  | notificationTopicArn | string | no | The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.  The Amazon SNS topic owner must be the same as the cluster owner. |
  | autoMinorVersionUpgrade | boolean | no | If you are running Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous ve... |
  | snapshotRetentionLimit | number | no | The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot taken today is retained for 5 days before ... |
  | snapshotWindow | string | no | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: 05:00-09:00  If you do not specify this parameter, ElastiCache automatical... |
  | outpostMode | string | no | Specifies whether the nodes in the cluster are created in a single outpost or across multiple outposts. |
  | preferredOutpostArn | string | no | The outpost ARN in which the cache cluster is created. |
  | preferredOutpostArns | array<string> | no | The outpost ARNs in which the cache cluster is created. |
  | logDeliveryConfigurations | array<object> | no | Specifies the destination, format and type of the logs. |
  | transitEncryptionEnabled | boolean | no | A flag that enables in-transit encryption when set to true. |
  | networkType | string | no | Must be either ipv4 \| ipv6 \| dual_stack. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the Nitro system. |
  | ipDiscovery | string | no | The network type you choose when modifying a cluster, either ipv4 \| ipv6. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all instance... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheCluster | object |  |


## com.datadoghq.aws.elasticache.createCacheParameterGroup
**Create cache parameter group** — Creates a new Amazon ElastiCache cache parameter group.
- Stability: stable
- Permissions: `elasticache:CreateCacheParameterGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | yes | A user-specified name for the cache parameter group. |
  | cacheParameterGroupFamily | string | yes | The name of the cache parameter group family that the cache parameter group can be used with. Valid values are: memcached1.4 \| memcached1.5 \| memcached1.6 \| redis2.6 \| redis2.8 \| redis3.2 \| redis4.... |
  | description | string | yes | A user-specified description for the cache parameter group. |
  | tags | any | no | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheParameterGroup | object |  |


## com.datadoghq.aws.elasticache.createCacheSecurityGroup
**Create cache security group** — Creates a new cache security group. Use a cache security group to control access to one or more clusters. Cache security groups are only used when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cluster inside of a VPC, use a cache subnet group instead. For more information, see CreateCacheSubnetGroup.
- Stability: stable
- Permissions: `elasticache:CreateCacheSecurityGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSecurityGroupName | string | yes | A name for the cache security group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word "Default". Example: mysecurit... |
  | description | string | yes | A description for the cache security group. |
  | tags | any | no | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheSecurityGroup | object |  |


## com.datadoghq.aws.elasticache.createCacheSubnetGroup
**Create cache subnet group** — Creates a new cache subnet group. Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
- Stability: stable
- Permissions: `elasticache:CreateCacheSubnetGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSubnetGroupName | string | yes | A name for the cache subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 alphanumeric characters or hyphens. Example: mysubnetgroup |
  | cacheSubnetGroupDescription | string | yes | A description for the cache subnet group. |
  | subnetIds | array<string> | yes | A list of VPC subnet IDs for the cache subnet group. |
  | tags | any | no | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheSubnetGroup | object |  |


## com.datadoghq.aws.elasticache.createGlobalReplicationGroup
**Create global replication group** — Creates cross-region read replica clusters for ElastiCache (Redis OSS) to enable low-latency reads and disaster recovery across regions.
- Stability: stable
- Permissions: `elasticache:CreateGlobalReplicationGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupIdSuffix | string | yes | The suffix name of a Global datastore. Amazon ElastiCache automatically applies a prefix to the Global datastore ID when it is created. Each Amazon Region has its own prefix. For instance, a Global... |
  | globalReplicationGroupDescription | string | no | Provides details of the Global datastore |
  | primaryReplicationGroupId | string | yes | The name of the primary cluster that accepts writes and will replicate updates to the secondary cluster. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.createReplicationGroup
**Create replication group** — Creates a Redis OSS (cluster mode disabled) or a Redis OSS (cluster mode enabled) replication group. This action can be used to create a standalone regional replication group or a secondary replication group associated with a Global datastore.
- Stability: stable
- Permissions: `elasticache:CreateReplicationGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The replication group identifier. This parameter is stored as a lowercase string. Constraints:   A name must contain from 1 to 40 alphanumeric characters or hyphens.   The first character must be a... |
  | replicationGroupDescription | string | yes | A user-created description for the replication group. |
  | globalReplicationGroupId | string | no | The name of the Global datastore |
  | primaryClusterId | string | no | The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of available. This parameter is not required if NumCacheCluste... |
  | automaticFailoverEnabled | boolean | no | Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.  AutomaticFailoverEnabled must be enabled for Redis OSS (cluster mode enabled) r... |
  | multiAZEnabled | boolean | no | A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see Minimizing Downtime: Multi-AZ. |
  | numCacheClusters | number | no | The number of clusters this replication group initially has. This parameter is not used if there is more than one node group (shard). You should use ReplicasPerNodeGroup instead. If AutomaticFailov... |
  | preferredCacheClusterAZs | array<string> | no | A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary clu... |
  | numNodeGroups | number | no | An optional parameter that specifies the number of node groups (shards) for this Redis OSS (cluster mode enabled) replication group. For Redis OSS (cluster mode disabled) either omit this parameter... |
  | replicasPerNodeGroup | number | no | An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5. |
  | nodeGroupConfiguration | array<object> | no | A list of node group (shard) configuration options. Each node group (shard) configuration has the following members: PrimaryAvailabilityZone, ReplicaAvailabilityZones, ReplicaCount, and Slots. If y... |
  | cacheNodeType | string | no | The compute and memory capacity of the nodes in the node group (shard). The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory a... |
  | engine | string | no | The name of the cache engine to be used for the clusters in this replication group. The value must be set to Redis. |
  | engineVersion | string | no | The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.  Important:... |
  | cacheParameterGroupName | string | no | The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used. If you are running Redis O... |
  | cacheSubnetGroupName | string | no | The name of the cache subnet group to be used for the replication group.  If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a clus... |
  | cacheSecurityGroupNames | array<string> | no | A list of cache security group names to associate with this replication group. |
  | securityGroupIds | array<string> | no | One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC). |
  | tags | any | no | A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValu... |
  | snapshotArns | array<string> | no | A list of Amazon Resource Names (ARN) that uniquely identify the Redis OSS RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 o... |
  | snapshotName | string | no | The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to restoring while the new replication group is being created. |
  | preferredMaintenanceWindow | string | no | Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance windo... |
  | port | number | no | The port number on which each member of the replication group accepts connections. |
  | notificationTopicArn | string | no | The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.  The Amazon SNS topic owner must be the same as the cluster owner. |
  | autoMinorVersionUpgrade | boolean | no | If you are running Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous ve... |
  | snapshotRetentionLimit | number | no | The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 day... |
  | snapshotWindow | string | no | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard). Example: 05:00-09:00  If you do not specify this parameter, ElastiCache automatical... |
  | transitEncryptionEnabled | boolean | no | A flag that enables in-transit encryption when set to true. This parameter is valid only if the Engine parameter is redis, the EngineVersion parameter is 3.2.6, 4.x or later, and the cluster is bei... |
  | atRestEncryptionEnabled | boolean | no | A flag that enables encryption at rest when set to true. You cannot modify the value of AtRestEncryptionEnabled after the replication group is created. To enable encryption at rest on a replication... |
  | kmsKeyId | string | no | The ID of the KMS key used to encrypt the disk in the cluster. |
  | userGroupIds | array<string> | no | The user group to associate with the replication group. |
  | logDeliveryConfigurations | array<object> | no | Specifies the destination, format and type of the logs. |
  | dataTieringEnabled | boolean | no | Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see Data tiering. |
  | networkType | string | no | Must be either ipv4 \| ipv6 \| dual_stack. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all instances built on the Nitro system. |
  | ipDiscovery | string | no | The network type you choose when creating a replication group, either ipv4 \| ipv6. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all... |
  | transitEncryptionMode | string | no | A setting that allows you to migrate your clients to use in-transit encryption, with no downtime. When setting TransitEncryptionEnabled to true, you can set your TransitEncryptionMode to preferred ... |
  | clusterMode | string | no | Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Redis OSS clients to connect using both cluster ... |
  | serverlessCacheSnapshotName | string | no | The name of the snapshot used to create a replication group. Available for Redis OSS only. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.createServerlessCache
**Create serverless cache** — Creates a serverless cache.
- Stability: stable
- Permissions: `elasticache:CreateServerlessCache`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheName | string | yes | User-provided identifier for the serverless cache. This parameter is stored as a lowercase string. |
  | description | string | no | User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters. |
  | engine | string | yes | The name of the cache engine to be used for creating the serverless cache. |
  | majorEngineVersion | string | no | The version of the cache engine that will be used to create the serverless cache. |
  | cacheUsageLimits | object | no | Sets the cache usage limits for storage and ElastiCache Processing Units for the cache. |
  | kmsKeyId | string | no | ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used. |
  | securityGroupIds | array<string> | no | A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other informat... |
  | snapshotArnsToRestore | array<string> | no | The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Redis OSS and Serverless Memcached only. |
  | tags | any | no | The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL. |
  | userGroupId | string | no | The identifier of the UserGroup to be associated with the serverless cache. Available for Redis OSS only. Default is NULL. |
  | subnetIds | array<string> | no | A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC. |
  | snapshotRetentionLimit | number | no | The number of snapshots that will be retained for the serverless cache that is being created. As new snapshots beyond this limit are added, the oldest snapshots will be deleted on a rolling basis. ... |
  | dailySnapshotTime | string | no | The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCache | object | The response for the attempt to create the serverless cache. |


## com.datadoghq.aws.elasticache.createServerlessCacheSnapshot
**Create serverless cache snapshot** — This API creates a copy of an entire ServerlessCache at a specific moment in time. Available for Redis OSS and Serverless Memcached only.
- Stability: stable
- Permissions: `elasticache:CreateServerlessCacheSnapshot`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheSnapshotName | string | yes | The name for the snapshot being created. Must be unique for the customer account. Available for Redis OSS and Serverless Memcached only. Must be between 1 and 255 characters. |
  | serverlessCacheName | string | yes | The name of an existing serverless cache. The snapshot is created from this cache. Available for Redis OSS and Serverless Memcached only. |
  | kmsKeyId | string | no | The ID of the KMS key used to encrypt the snapshot. Available for Redis OSS and Serverless Memcached only. Default: NULL |
  | tags | any | no | A list of tags to be added to the snapshot resource. A tag is a key-value pair. Available for Redis OSS and Serverless Memcached only. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCacheSnapshot | object | The state of a serverless cache snapshot at a specific point in time, to the millisecond. Available for Redis OSS and Serverless Memcached only. |


## com.datadoghq.aws.elasticache.createSnapshot
**Create snapshot** — Creates a copy of an entire cluster or replication group at a specific moment in time.  This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:CreateSnapshot`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | no | The identifier of an existing replication group. The snapshot is created from this replication group. |
  | cacheClusterId | string | no | The identifier of an existing cluster. The snapshot is created from this cluster. |
  | snapshotName | string | yes | A name for the snapshot being created. |
  | kmsKeyId | string | no | The ID of the KMS key used to encrypt the snapshot. |
  | tags | any | no | A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Snapshot | object |  |


## com.datadoghq.aws.elasticache.decreaseNodeGroupsInGlobalReplicationGroup
**Decrease node groups in global replication group** — Decreases the number of node groups in a Global datastore.
- Stability: stable
- Permissions: `elasticache:DecreaseNodeGroupsInGlobalReplicationGroup`
- Access: update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | nodeGroupCount | number | yes | The number of node groups (shards) that results from the modification of the shard configuration |
  | globalNodeGroupsToRemove | array<string> | no | If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRemove is a list of NodeG... |
  | globalNodeGroupsToRetain | array<string> | no | If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRetain is a list of NodeG... |
  | applyImmediately | boolean | yes | Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.decreaseReplicaCount
**Decrease replica count** — Dynamically decreases the number of replicas in a Redis OSS (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis OSS (cluster mode enabled) replication group. This operation is performed with no cluster down time.
- Stability: stable
- Permissions: `elasticache:DecreaseReplicaCount`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The id of the replication group from which you want to remove replica nodes. |
  | newReplicaCount | number | no | The number of read replica nodes you want at the completion of this operation. For Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group... |
  | replicaConfiguration | array<object> | no | A list of ConfigureShard objects that can be used to configure each shard in a Redis OSS (cluster mode enabled) replication group. The ConfigureShard has three members: NewReplicaCount, NodeGroupId... |
  | replicasToRemove | array<string> | no | A list of the node ids to remove from the replication group or node group (shard). |
  | applyImmediately | boolean | yes | If True, the number of replica nodes is decreased immediately. ApplyImmediately=False is not currently supported. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.deleteCacheCluster
**Delete cache cluster** — Deletes a previously provisioned cluster. DeleteCacheCluster deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation. Check documentation for unsupported clusters.
- Stability: stable
- Permissions: `elasticache:DeleteCacheCluster`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | yes | The cluster identifier for the cluster to be deleted. This parameter is not case sensitive. |
  | finalSnapshotIdentifier | string | no | The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheCluster | object |  |


## com.datadoghq.aws.elasticache.deleteCacheParameterGroup
**Delete cache parameter group** — Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters. You cannot delete the default cache parameter groups in your account.
- Stability: stable
- Permissions: `elasticache:DeleteCacheParameterGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | yes | The name of the cache parameter group to delete.  The specified cache security group must not be associated with any clusters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticache.deleteCacheSecurityGroup
**Delete cache security group** — Deletes a cache security group.  You cannot delete a cache security group if it is associated with any clusters.
- Stability: stable
- Permissions: `elasticache:DeleteCacheSecurityGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSecurityGroupName | string | yes | The name of the cache security group to delete.  You cannot delete the default security group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticache.deleteCacheSubnetGroup
**Delete cache subnet group** — Deletes a cache subnet group.  You cannot delete a default cache subnet group or one that is associated with any clusters.
- Stability: stable
- Permissions: `elasticache:DeleteCacheSubnetGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSubnetGroupName | string | yes | The name of the cache subnet group to delete. Constraints: Must contain no more than 255 alphanumeric characters or hyphens. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticache.deleteGlobalReplicationGroup
**Delete global replication group** — Deleting a Global datastore is a two-step process:    First, you must DisassociateGlobalReplicationGroup to remove the secondary clusters in the Global datastore.   Once the Global datastore contains only the primary cluster, you can use the DeleteGlobalReplicationGroup API to delete the Global datastore while retainining the primary cluster using RetainPrimaryReplicationGroup&#x3D;true.   Since the Global Datastore has only a primary cluster, you can delete the Global Datastore while retaining the primary by setting RetainPrimaryReplicationGroup&#x3D;true. The primary cluster is never deleted when deleting a Global Datastore. It can only be deleted when it no longer is associated with any Global Datastore. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.
- Stability: stable
- Permissions: `elasticache:DeleteGlobalReplicationGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | retainPrimaryReplicationGroup | boolean | yes | The primary replication group is retained as a standalone replication group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.deleteReplicationGroup
**Delete replication group** — Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting RetainPrimaryCluster&#x3D;true. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.     CreateSnapshot permission is required to create a final snapshot. Without this permission, the API call will fail with an Access Denied exception.   This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:DeleteReplicationGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The identifier for the cluster to be deleted. This parameter is not case sensitive. |
  | retainPrimaryCluster | boolean | no | If set to true, all of the read replicas are deleted, but the primary node is retained. |
  | finalSnapshotIdentifier | string | no | The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the fresh... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.deleteServerlessCache
**Delete serverless cache** — Deletes a specified existing serverless cache.   CreateServerlessCacheSnapshot permission is required to create a final snapshot. Without this permission, the API call will fail with an Access Denied exception.
- Stability: stable
- Permissions: `elasticache:DeleteServerlessCache`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheName | string | yes | The identifier of the serverless cache to be deleted. |
  | finalSnapshotName | string | no | Name of the final snapshot to be taken before the serverless cache is deleted. Available for Redis OSS and Serverless Memcached only. Default: NULL, i.e. a final snapshot is not taken. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCache | object | Provides the details of the specified serverless cache that is about to be deleted. |


## com.datadoghq.aws.elasticache.deleteServerlessCacheSnapshot
**Delete serverless cache snapshot** — Deletes an existing serverless cache snapshot. Available for Redis OSS and Serverless Memcached only.
- Stability: stable
- Permissions: `elasticache:DeleteServerlessCacheSnapshot`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheSnapshotName | string | yes | Idenfitier of the snapshot to be deleted. Available for Redis OSS and Serverless Memcached only. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCacheSnapshot | object | The snapshot to be deleted. Available for Redis OSS and Serverless Memcached only. |


## com.datadoghq.aws.elasticache.deleteSnapshot
**Delete snapshot** — Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.  This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:DeleteSnapshot`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | snapshotName | string | yes | The name of the snapshot to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Snapshot | object |  |


## com.datadoghq.aws.elasticache.describeCacheClusters
**Describe cache clusters** — Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied.
- Stability: stable
- Permissions: `elasticache:DescribeCacheClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | no | The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | showCacheNodeInfo | boolean | no | An optional flag that can be included in the DescribeCacheCluster request to retrieve information about the individual cache nodes. |
  | showCacheClustersNotInReplicationGroups | boolean | no | An optional flag that can be included in the DescribeCacheCluster request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and si... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | CacheClusters | array<object> | A list of clusters. Each item in the list contains detailed information about one cluster. |


## com.datadoghq.aws.elasticache.describeCacheEngineVersions
**Describe cache engine versions** — Returns a list of the available cache engines and their versions.
- Stability: stable
- Permissions: `elasticache:DescribeCacheEngineVersions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | engine | string | no | The cache engine to return. Valid values: memcached \| redis |
  | engineVersion | string | no | The cache engine version to return. Example: 1.4.14 |
  | cacheParameterGroupFamily | string | no | The name of a specific cache parameter group family to return details for. Valid values are: memcached1.4 \| memcached1.5 \| memcached1.6 \| redis2.6 \| redis2.8 \| redis3.2 \| redis4.0 \| redis5.0 \| redi... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | defaultOnly | boolean | no | If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | CacheEngineVersions | array<object> | A list of cache engine version details. Each element in the list contains detailed information about one cache engine version. |


## com.datadoghq.aws.elasticache.describeCacheParameterGroups
**Describe cache parameter groups** — Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.
- Stability: stable
- Permissions: `elasticache:DescribeCacheParameterGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | no | The name of a specific cache parameter group to return details for. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | CacheParameterGroups | array<object> | A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group. |


## com.datadoghq.aws.elasticache.describeCacheParameters
**Describe cache parameters** — Returns the detailed parameter list for a particular cache parameter group.
- Stability: stable
- Permissions: `elasticache:DescribeCacheParameters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | yes | The name of a specific cache parameter group to return details for. |
  | source | string | no | The parameter types to return. Valid values: user \| system \| engine-default |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | Parameters | array<object> | A list of Parameter instances. |
  | CacheNodeTypeSpecificParameters | array<object> | A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter. |


## com.datadoghq.aws.elasticache.describeCacheSecurityGroups
**Describe cache security groups** — Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group. This applicable only when you have ElastiCache in Classic setup.
- Stability: stable
- Permissions: `elasticache:DescribeCacheSecurityGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSecurityGroupName | string | no | The name of the cache security group to return details for. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | CacheSecurityGroups | array<object> | A list of cache security groups. Each element in the list contains detailed information about one group. |


## com.datadoghq.aws.elasticache.describeCacheSubnetGroups
**Describe cache subnet groups** — Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group. This is applicable only when you have ElastiCache in VPC setup. All ElastiCache clusters now launch in VPC by default.
- Stability: stable
- Permissions: `elasticache:DescribeCacheSubnetGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSubnetGroupName | string | no | The name of the cache subnet group to return details for. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | CacheSubnetGroups | array<object> | A list of cache subnet groups. Each element in the list contains detailed information about one group. |


## com.datadoghq.aws.elasticache.describeEngineDefaultParameters
**Describe engine default parameters** — Returns the default engine and system parameter information for the specified cache engine.
- Stability: stable
- Permissions: `elasticache:DescribeEngineDefaultParameters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupFamily | string | yes | The name of the cache parameter group family. Valid values are: memcached1.4 \| memcached1.5 \| memcached1.6 \| redis2.6 \| redis2.8 \| redis3.2 \| redis4.0 \| redis5.0 \| redis6.x \| redis6.2 \| redis7 |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | EngineDefaults | object |  |


## com.datadoghq.aws.elasticache.describeEvents
**Describe events** — Returns events related to clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cluster, cache security group, or cache parameter group by providing the name as a parameter. By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days&#x27; worth of events if necessary.
- Stability: stable
- Permissions: `elasticache:DescribeEvents`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceIdentifier | string | no | The identifier of the event source for which events are returned. If not specified, all sources are included in the response. |
  | sourceType | string | no | The event source to retrieve events for. If no value is specified, all events are returned. |
  | startTime | string | no | The beginning of the time interval to retrieve events for, specified in ISO 8601 format.  Example: 2017-03-30T07:03:49.555Z |
  | endTime | string | no | The end of the time interval for which to retrieve events, specified in ISO 8601 format.  Example: 2017-03-30T07:03:49.555Z |
  | duration | number | no | The number of minutes worth of events to retrieve. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | Events | array<object> | A list of events. Each element in the list contains detailed information about one event. |


## com.datadoghq.aws.elasticache.describeGlobalReplicationGroups
**Describe global replication groups** — Returns information about a particular global replication group. If no identifier is specified, returns information about all Global datastores.
- Stability: stable
- Permissions: `elasticache:DescribeGlobalReplicationGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | no | The name of the Global datastore |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | showMemberInfo | boolean | no | Returns the list of members that comprise the Global datastore. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | GlobalReplicationGroups | array<object> | Indicates the slot configuration and global identifier for each slice group. |


## com.datadoghq.aws.elasticache.describeReplicationGroups
**Describe replication groups** — Returns information about a particular replication group. If no identifier is specified, DescribeReplicationGroups returns information about all replication groups.  This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:DescribeReplicationGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | no | The identifier for the replication group to be described. This parameter is not case sensitive. If you do not specify this parameter, information about all replication groups is returned. |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | ReplicationGroups | array<object> | A list of replication groups. Each item in the list contains detailed information about one replication group. |


## com.datadoghq.aws.elasticache.describeReservedCacheNodes
**Describe reserved cache nodes** — Returns information about reserved cache nodes for this account, or about a specified reserved cache node.
- Stability: stable
- Permissions: `elasticache:DescribeReservedCacheNodes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | reservedCacheNodeId | string | no | The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID. |
  | reservedCacheNodesOfferingId | string | no | The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier. |
  | cacheNodeType | string | no | The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type. The following node types are supported by ElastiCache. Generally speakin... |
  | duration | string | no | The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration. Valid Values: 1 \| 3 \| 31536000 \| 94608000 |
  | productDescription | string | no | The product description filter value. Use this parameter to show only those reservations matching the specified product description. |
  | offeringType | string | no | The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid values: "Light Utilization"\|"Medium Utilization"\|"Heavy Utilizati... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | ReservedCacheNodes | array<object> | A list of reserved cache nodes. Each element in the list contains detailed information about one node. |


## com.datadoghq.aws.elasticache.describeReservedCacheNodesOfferings
**Describe reserved cache nodes offerings** — Lists available reserved cache node offerings.
- Stability: stable
- Permissions: `elasticache:DescribeReservedCacheNodesOfferings`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | reservedCacheNodesOfferingId | string | no | The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier. Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706 |
  | cacheNodeType | string | no | The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type. The following node types are supported by ElastiCache. Generally sp... |
  | duration | string | no | Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration. Valid Values: 1 \| 3 \| 31536000 \| 94608000 |
  | productDescription | string | no | The product description filter value. Use this parameter to show only the available offerings matching the specified product description. |
  | offeringType | string | no | The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type. Valid Values: "Light Utilization"\|"Medium Utilization"\|"Heavy Utilizati... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | Provides an identifier to allow retrieval of paginated results. |
  | ReservedCacheNodesOfferings | array<object> | A list of reserved cache node offerings. Each element in the list contains detailed information about one offering. |


## com.datadoghq.aws.elasticache.describeServerlessCacheSnapshots
**Describe serverless cache snapshots** — Returns information about serverless cache snapshots. Available for Redis OSS and Serverless Memcached only.
- Stability: stable
- Permissions: `elasticache:DescribeServerlessCacheSnapshots`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheName | string | no | The identifier of serverless cache. If this parameter is specified, only snapshots associated with that specific serverless cache are described. Available for Redis OSS and Serverless Memcached only. |
  | serverlessCacheSnapshotName | string | no | The identifier of the serverless cache’s snapshot. If this parameter is specified, only this snapshot is described. Available for Redis OSS and Serverless Memcached only. |
  | snapshotType | string | no | The type of snapshot that is being described. Available for Redis OSS and Serverless Memcached only. |
  | nextToken | string | no | An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to th... |
  | maxResults | number | no | The maximum number of records to include in the response. If more records exist than the specified max-results value, a market is included in the response so that remaining results can be retrieved... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | NextToken | string | An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to th... |
  | ServerlessCacheSnapshots | array<object> | The serverless caches snapshots associated with a given description request. Available for Redis OSS and Serverless Memcached only. |


## com.datadoghq.aws.elasticache.describeServerlessCaches
**Describe serverless caches** — Returns information about a specific serverless cache.
- Stability: stable
- Permissions: `elasticache:DescribeServerlessCaches`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheName | string | no | The identifier for the serverless cache. If this parameter is specified, only information about that specific serverless cache is returned. Default: NULL |
  | maxResults | number | no | The maximum number of records in the response. If more records exist than the specified max-records value, the next token is included in the response so that remaining results can be retrieved. The... |
  | nextToken | string | no | An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to th... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | NextToken | string | An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to th... |
  | ServerlessCaches | array<object> | The serverless caches associated with a given description request. |


## com.datadoghq.aws.elasticache.describeServiceUpdates
**Describe service updates** — Returns details of the service updates.
- Stability: stable
- Permissions: `elasticache:DescribeServiceUpdates`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceUpdateName | string | no | The unique ID of the service update |
  | serviceUpdateStatus | array<string> | no | The status of the service update |
  | maxRecords | number | no | The maximum number of records to include in the response |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | ServiceUpdates | array<object> | A list of service updates |


## com.datadoghq.aws.elasticache.describeSnapshots
**Describe snapshots** — Returns information about cluster or replication group snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.  This operation is valid for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:DescribeSnapshots`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | no | A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described. |
  | cacheClusterId | string | no | A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described. |
  | snapshotName | string | no | A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described. |
  | snapshotSource | string | no | If set to system, the output shows snapshots that were automatically created by ElastiCache. If set to user the output shows snapshots that were manually created. If omitted, the output shows both ... |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | maxRecords | number | no | The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrie... |
  | showNodeGroupConfig | boolean | no | A Boolean value which if true, the node group (shard) configuration is included in the snapshot description. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | Snapshots | array<object> | A list of snapshots. Each item in the list contains detailed information about one snapshot. |


## com.datadoghq.aws.elasticache.describeUpdateActions
**Describe update actions** — Returns details of the update actions.
- Stability: stable
- Permissions: `elasticache:DescribeUpdateActions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceUpdateName | string | no | The unique ID of the service update |
  | replicationGroupIds | array<string> | no | The replication group IDs |
  | cacheClusterIds | array<string> | no | The cache cluster IDs |
  | engine | string | no | The Elasticache engine to which the update applies. Either Redis OSS or Memcached. |
  | serviceUpdateStatus | array<string> | no | The status of the service update |
  | serviceUpdateTimeRange | object | no | The range of time specified to search for service updates that are in available status |
  | updateActionStatus | array<string> | no | The status of the update action. |
  | showNodeLevelUpdateStatus | boolean | no | Dictates whether to include node level update status in the response |
  | maxRecords | number | no | The maximum number of records to include in the response |
  | marker | string | no | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Marker | string | An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker... |
  | UpdateActions | array<object> | Returns a list of update actions |


## com.datadoghq.aws.elasticache.disassociateGlobalReplicationGroup
**Disassociate global replication group** — Remove a secondary cluster from the Global datastore using the Global datastore name. The secondary cluster will no longer receive updates from the primary cluster, but will remain as a standalone cluster in that Amazon region.
- Stability: stable
- Permissions: `elasticache:DisassociateGlobalReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | replicationGroupId | string | yes | The name of the secondary cluster you wish to remove from the Global datastore |
  | replicationGroupRegion | string | yes | The Amazon region of secondary cluster you wish to remove from the Global datastore |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.exportServerlessCacheSnapshot
**Export serverless cache snapshot** — Provides the functionality to export the serverless cache snapshot data to Amazon S3. Available for Redis OSS only.
- Stability: stable
- Permissions: `elasticache:ExportServerlessCacheSnapshot`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheSnapshotName | string | yes | The identifier of the serverless cache snapshot to be exported to S3. Available for Redis OSS only. |
  | s3BucketName | string | yes | Name of the Amazon S3 bucket to export the snapshot to. The Amazon S3 bucket must also be in same region as the snapshot. Available for Redis OSS only. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCacheSnapshot | object | The state of a serverless cache at a specific point in time, to the millisecond. Available for Redis OSS and Serverless Memcached only. |


## com.datadoghq.aws.elasticache.failoverGlobalReplicationGroup
**Failover global replication group** — Used to failover the primary region to a secondary region. The secondary region will become primary, and all other clusters will become secondary.
- Stability: stable
- Permissions: `elasticache:FailoverGlobalReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | primaryRegion | string | yes | The Amazon region of the primary cluster of the Global datastore |
  | primaryReplicationGroupId | string | yes | The name of the primary replication group |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.increaseNodeGroupsInGlobalReplicationGroup
**Increase node groups in global replication group** — Increase the number of node groups in the Global datastore.
- Stability: stable
- Permissions: `elasticache:IncreaseNodeGroupsInGlobalReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | nodeGroupCount | number | yes | Total number of node groups you want |
  | regionalConfigurations | array<object> | no | Describes the replication group IDs, the Amazon regions where they are stored and the shard configuration for each that comprise the Global datastore |
  | applyImmediately | boolean | yes | Indicates that the process begins immediately. At present, the only permitted value for this parameter is true. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.increaseReplicaCount
**Increase replica count** — Dynamically increases the number of replicas in a Redis OSS (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Redis OSS (cluster mode enabled) replication group.
- Stability: stable
- Permissions: `elasticache:IncreaseReplicaCount`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The id of the replication group to which you want to add replica nodes. |
  | newReplicaCount | number | no | The number of read replica nodes you want at the completion of this operation. For Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group... |
  | replicaConfiguration | array<object> | no | A list of ConfigureShard objects that can be used to configure each shard in a Redis OSS (cluster mode enabled) replication group. The ConfigureShard has three members: NewReplicaCount, NodeGroupId... |
  | applyImmediately | boolean | yes | If True, the number of replica nodes is increased immediately. ApplyImmediately=False is not currently supported. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.listAllowedNodeTypeModifications
**List allowed node type modifications** — Lists all available node types that you can scale your Redis OSS cluster&#x27;s or replication group&#x27;s current node type. When you use the ModifyCacheCluster or ModifyReplicationGroup operations to scale your cluster or replication group, the value of the CacheNodeType parameter must be one of the node types returned by this operation.
- Stability: stable
- Permissions: `elasticache:ListAllowedNodeTypeModifications`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | no | The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of nod... |
  | replicationGroupId | string | no | The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ScaleUpModifications | array<string> | A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group. When scaling up a Redis OSS cluster or replication group using ModifyC... |
  | ScaleDownModifications | array<string> | A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group. When scaling down a Redis OSS cluster or replication group using Modif... |


## com.datadoghq.aws.elasticache.listTagsForResource
**List tags for resource** — Lists all tags currently on a named resource.
- Stability: stable
- Permissions: `elasticache:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceName | string | yes | The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:012345678... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TagList | array<object> | A list of tags as key-value pairs. |


## com.datadoghq.aws.elasticache.modifyCacheCluster
**Modify cache cluster** — Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.
- Stability: stable
- Permissions: `elasticache:ModifyCacheCluster`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | yes | The cluster identifier. This value is stored as a lowercase string. |
  | numCacheNodes | number | no | The number of cache nodes that the cluster should have. If the value for NumCacheNodes is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (w... |
  | cacheNodeIdsToRemove | array<string> | no | A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when NumCacheNodes is less than the existing number of cache nodes. The nu... |
  | aZMode | string | no | Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones. Valid values: single-az \| cross-az. This optio... |
  | newAvailabilityZones | array<string> | no | This option is only supported on Memcached clusters.  The list of Availability Zones where the new Memcached cache nodes are created. This parameter is only valid when NumCacheNodes in the request ... |
  | cacheSecurityGroupNames | array<string> | no | A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible. You can use this parameter only with clusters that are created outside ... |
  | securityGroupIds | array<string> | no | Specifies the VPC Security Groups associated with the cluster. This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC). |
  | preferredMaintenanceWindow | string | no | Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance windo... |
  | notificationTopicArn | string | no | The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.  The Amazon SNS topic owner must be same as the cluster owner. |
  | cacheParameterGroupName | string | no | The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately parameter is specified as true for... |
  | notificationTopicStatus | string | no | The status of the Amazon SNS notification topic. Notifications are sent only if the status is active. Valid values: active \| inactive |
  | applyImmediately | boolean | no | If true, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow se... |
  | engineVersion | string | no | The upgraded version of the cache engine to be run on the cache nodes.  Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version), but you cannot downgrade to ... |
  | autoMinorVersionUpgrade | boolean | no | If you are running Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous ve... |
  | snapshotRetentionLimit | number | no | The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained f... |
  | snapshotWindow | string | no | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster. |
  | cacheNodeType | string | no | A valid cache node type that you want to scale this cluster up to. |
  | logDeliveryConfigurations | array<object> | no | Specifies the destination, format and type of the logs. |
  | ipDiscovery | string | no | The network type you choose when modifying a cluster, either ipv4 \| ipv6. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all instance... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheCluster | object |  |


## com.datadoghq.aws.elasticache.modifyCacheParameterGroup
**Modify cache parameter group** — Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.
- Stability: stable
- Permissions: `elasticache:ModifyCacheParameterGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | yes | The name of the cache parameter group to modify. |
  | parameterNameValues | array<object> | yes | An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheParameterGroupName | string | The name of the cache parameter group. |


## com.datadoghq.aws.elasticache.modifyCacheSubnetGroup
**Modify cache subnet group** — Modifies an existing cache subnet group.
- Stability: stable
- Permissions: `elasticache:ModifyCacheSubnetGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSubnetGroupName | string | yes | The name for the cache subnet group. This value is stored as a lowercase string. Constraints: Must contain no more than 255 alphanumeric characters or hyphens. Example: mysubnetgroup |
  | cacheSubnetGroupDescription | string | no | A description of the cache subnet group. |
  | subnetIds | array<string> | no | The EC2 subnet IDs for the cache subnet group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheSubnetGroup | object |  |


## com.datadoghq.aws.elasticache.modifyGlobalReplicationGroup
**Modify global replication group** — Modifies the settings for a Global datastore.
- Stability: stable
- Permissions: `elasticache:ModifyGlobalReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | applyImmediately | boolean | yes | This parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible. Modifications to Global Replication Groups cannot be req... |
  | cacheNodeType | string | no | A valid cache node type that you want to scale this Global datastore to. |
  | engineVersion | string | no | The upgraded version of the cache engine to be run on the clusters in the Global datastore. |
  | cacheParameterGroupName | string | no | The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore. |
  | globalReplicationGroupDescription | string | no | A description of the Global datastore |
  | automaticFailoverEnabled | boolean | no | Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.modifyReplicationGroup
**Modify replication group** — Modifies the settings for a replication group. This is limited to Valkey and Redis OSS 7 and above.
- Stability: stable
- Permissions: `elasticache:ModifyReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The identifier of the replication group to modify. |
  | replicationGroupDescription | string | no | A description for the replication group. Maximum length is 255 characters. |
  | primaryClusterId | string | no | For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all oth... |
  | snapshottingClusterId | string | no | The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis OSS (cluster mode enabled) replication groups. |
  | automaticFailoverEnabled | boolean | no | Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure. Valid values: true \| false |
  | multiAZEnabled | boolean | no | A flag to indicate MultiAZ is enabled. |
  | nodeGroupId | string | no | Deprecated. This parameter is not used. |
  | cacheSecurityGroupNames | array<string> | no | A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible. This parameter can be used only with replica... |
  | securityGroupIds | array<string> | no | Specifies the VPC Security Groups associated with the clusters in the replication group. This parameter can be used only with replication group containing clusters running in an Amazon Virtual Priv... |
  | preferredMaintenanceWindow | string | no | Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance windo... |
  | notificationTopicArn | string | no | The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.  The Amazon SNS topic owner must be same as the replication group owner. |
  | cacheParameterGroupName | string | no | The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ApplyImmediately p... |
  | notificationTopicStatus | string | no | The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is active. Valid values: active \| inactive |
  | applyImmediately | boolean | no | If true, this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the PreferredMaintenanceWindow se... |
  | engineVersion | string | no | The upgraded version of the cache engine to be run on the clusters in the replication group.  Important: You can upgrade to a newer engine version (see Selecting a Cache Engine and Version), but yo... |
  | autoMinorVersionUpgrade | boolean | no | If you are running Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous ve... |
  | snapshotRetentionLimit | number | no | The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is... |
  | snapshotWindow | string | no | The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by SnapshottingClusterId. Example: 05:00-09:00  If you do not specify this ... |
  | cacheNodeType | string | no | A valid cache node type that you want to scale this replication group to. |
  | userGroupIdsToAdd | array<string> | no | The ID of the user group you are associating with the replication group. |
  | userGroupIdsToRemove | array<string> | no | The ID of the user group to disassociate from the replication group, meaning the users in the group no longer can access the replication group. |
  | removeUserGroups | boolean | no | Removes the user group associated with this replication group. |
  | logDeliveryConfigurations | array<object> | no | Specifies the destination, format and type of the logs. |
  | ipDiscovery | string | no | The network type you choose when modifying a cluster, either ipv4 \| ipv6. IPv6 is supported for workloads using Redis OSS engine version 6.2 onward or Memcached engine version 1.6.6 on all instance... |
  | transitEncryptionEnabled | boolean | no | A flag that enables in-transit encryption when set to true. If you are enabling in-transit encryption for an existing cluster, you must also set TransitEncryptionMode to preferred. |
  | transitEncryptionMode | string | no | A setting that allows you to migrate your clients to use in-transit encryption, with no downtime. You must set TransitEncryptionEnabled to true, for your existing cluster, and set TransitEncryption... |
  | clusterMode | string | no | Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Redis OSS clients to connect using both cluster ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.modifyReplicationGroupShardConfiguration
**Modify replication group shard configuration** — Modifies a replication group&#x27;s shards (node groups) by allowing you to add shards, remove shards, or rebalance the keyspaces among existing shards.
- Stability: stable
- Permissions: `elasticache:ModifyReplicationGroupShardConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The name of the Redis OSS (cluster mode enabled) cluster (replication group) on which the shards are to be configured. |
  | nodeGroupCount | number | yes | The number of node groups (shards) that results from the modification of the shard configuration. |
  | applyImmediately | boolean | yes | Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true. Value: true |
  | reshardingConfiguration | array<object> | no | Specifies the preferred availability zones for each node group in the cluster. If the value of NodeGroupCount is greater than the current number of node groups (shards), you can use this parameter ... |
  | nodeGroupsToRemove | array<string> | no | If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRemove is a list of NodeGroupId... |
  | nodeGroupsToRetain | array<string> | no | If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. NodeGroupsToRetain is a list of NodeGroupId... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.modifyServerlessCache
**Modify serverless cache** — This API modifies the attributes of a serverless cache.
- Stability: stable
- Permissions: `elasticache:ModifyServerlessCache`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serverlessCacheName | string | yes | User-provided identifier for the serverless cache to be modified. |
  | description | string | no | User provided description for the serverless cache. Default = NULL, i.e. the existing description is not removed/modified. The description has a maximum length of 255 characters. |
  | cacheUsageLimits | object | no | Modify the cache usage limit for the serverless cache. |
  | removeUserGroup | boolean | no | The identifier of the UserGroup to be removed from association with the Redis OSS serverless cache. Available for Redis OSS only. Default is NULL. |
  | userGroupId | string | no | The identifier of the UserGroup to be associated with the serverless cache. Available for Redis OSS only. Default is NULL - the existing UserGroup is not removed. |
  | securityGroupIds | array<string> | no | The new list of VPC security groups to be associated with the serverless cache. Populating this list means the current VPC security groups will be removed. This security group is used to authorize ... |
  | snapshotRetentionLimit | number | no | The number of days for which Elasticache retains automatic snapshots before deleting them. Available for Redis OSS and Serverless Memcached only. Default = NULL, i.e. the existing snapshot-retentio... |
  | dailySnapshotTime | string | no | The daily time during which Elasticache begins taking a daily snapshot of the serverless cache. Available for Redis OSS and Serverless Memcached only. The default is NULL, i.e. the existing snapsho... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ServerlessCache | object | The response for the attempt to modify the serverless cache. |


## com.datadoghq.aws.elasticache.rebalanceSlotsInGlobalReplicationGroup
**Rebalance slots in global replication group** — Redistribute slots to ensure uniform distribution across existing shards in the cluster.
- Stability: stable
- Permissions: `elasticache:RebalanceSlotsInGlobalReplicationGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | globalReplicationGroupId | string | yes | The name of the Global datastore |
  | applyImmediately | boolean | yes | If True, redistribution is applied immediately. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GlobalReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.rebootCacheCluster
**Reboot cache cluster** — Reboots some, or all, of the cache nodes within a provisioned cluster. The reboot causes the contents of the cache (for each cache node being rebooted) to be lost. Rebooting a cluster is currently supported on Memcached and Redis OSS (cluster mode disabled) clusters.
- Stability: stable
- Permissions: `elasticache:RebootCacheCluster`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheClusterId | string | yes | The cluster identifier. This parameter is stored as a lowercase string. |
  | cacheNodeIdsToReboot | array<string> | yes | A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheCluster | object |  |


## com.datadoghq.aws.elasticache.removeTagsFromResource
**Remove tags from resource** — Removes the tags identified by the TagKeys list from the named resource.
- Stability: stable
- Permissions: `elasticache:RemoveTagsFromResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceName | string | yes | The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster or arn:aws:elasticache:us-west-2:01234567... |
  | tagKeys | array<string> | yes | A list of TagKeys identifying the tags you want removed from the named resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TagList | array<object> | A list of tags as key-value pairs. |


## com.datadoghq.aws.elasticache.resetCacheParameterGroup
**Reset cache parameter group** — Modifies the parameters of a cache parameter group to the engine or system default value.
- Stability: stable
- Permissions: `elasticache:ResetCacheParameterGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheParameterGroupName | string | yes | The name of the cache parameter group to reset. |
  | resetAllParameters | boolean | no | If true, all parameters in the cache parameter group are reset to their default values. If false, only the parameters listed by ParameterNameValues are reset to their default values. Valid values: ... |
  | parameterNameValues | array<object> | no | An array of parameter names to reset to their default values. If ResetAllParameters is true, do not use ParameterNameValues. If ResetAllParameters is false, you must specify the name of at least on... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheParameterGroupName | string | The name of the cache parameter group. |


## com.datadoghq.aws.elasticache.revokeCacheSecurityGroupIngress
**Revoke cache security group ingress** — Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon EC2 security group that had been previously authorized.
- Stability: stable
- Permissions: `elasticache:RevokeCacheSecurityGroupIngress`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cacheSecurityGroupName | string | yes | The name of the cache security group to revoke ingress from. |
  | eC2SecurityGroupName | string | yes | The name of the Amazon EC2 security group to revoke access from. |
  | eC2SecurityGroupOwnerId | string | yes | The Amazon account number of the Amazon EC2 security group owner. Note that this is not the same thing as an Amazon access key ID - you must provide a valid Amazon account number for this parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CacheSecurityGroup | object |  |


## com.datadoghq.aws.elasticache.startMigration
**Start migration** — Start the migration of data.
- Stability: stable
- Permissions: `elasticache:StartMigration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The ID of the replication group to which data should be migrated. |
  | customerNodeEndpointList | array<object> | yes | List of endpoints from which data should be migrated. For Redis OSS (cluster mode disabled), list should have only one element. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.testFailover
**Test failover** — Represents the input of a TestFailover operation which tests automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console). A customer can use this operation to test automatic failover on up to 15 shards in any rolling 24-hour period.
- Stability: stable
- Permissions: `elasticache:TestFailover`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The name of the replication group (console: cluster) whose automatic failover is being tested by this operation. |
  | nodeGroupId | string | yes | The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 15 node groups in any rollin... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |


## com.datadoghq.aws.elasticache.testMigration
**Test migration** — Async API to test connection between source and target replication group.
- Stability: stable
- Permissions: `elasticache:TestMigration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationGroupId | string | yes | The ID of the replication group to which data is to be migrated. |
  | customerNodeEndpointList | array<object> | yes | List of endpoints from which data should be migrated. List should have only one element. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReplicationGroup | object |  |

