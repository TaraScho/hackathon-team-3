# AWS EBS Actions
Bundle: `com.datadoghq.aws.ebs` | 9 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eebs)

## com.datadoghq.aws.ebs.attach_volume
**Attach volume** — Attach an EBS volume to a running or stopped instance, and expose it to the instance with the specified device name.
- Stability: stable
- Permissions: `ec2:AttachVolume`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | volumeId | string | yes | The ID of the EBS volume. The volume and instance must be within the same Availability Zone. |
  | instanceId | string | yes | The ID of the instance. |
  | device | string | yes | The device name (for example, /dev/sdh or xvdh). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | device | string | The device name. If the volume is attached to a Fargate task, this parameter returns null. |
  | instanceId | string | The ID of the instance. If the volume is attached to a Fargate task, this parameter returns null. |
  | volumeId | string | The ID of the volume. |
  | atttachTime | string | The time stamp when the attachment initiated. |
  | state | string | The attachment state of the volume. |
  | deleteOnTermination | boolean | Indicates whether the EBS volume is deleted on instance termination. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.createSnapshot
**Create snapshot** — Create a snapshot of an EBS volume and store it in Amazon S3.
- Stability: stable
- Permissions: `ec2:CreateSnapshot`, `ec2:CreateTags`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | volumeId | string | yes | The ID of the Amazon EBS volume of which to create a snapshot. |
  | description | string | no | A description for the snapshot. |
  | tags | any | no | The tags to apply to the snapshot during creation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | snapshot | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.create_volume
**Create volume** — Create an EBS volume that can be attached to an instance in the same availability zone.
- Stability: stable
- Permissions: `ec2:CreateVolume`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | availabilityZone | string | yes | The ID of the Availability Zone in which to create the volume. For example, us-east-1a. |
  | encrypted | boolean | no | The encryption status of the volume. |
  | size | number | no | The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to ... |
  | snapshotId | string | no | The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size. |
  | volumeType | string | no | The volume type. The following values are supported: `General Purpose SSD: gp2 \| gp3`, `Provisioned IOPS SSD: io1 \| io2`, `Throughput Optimized HDD: st1`, `Cold HDD: sc1`, and `Magnetic: standard`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | attachmentSet | array<object> | This parameter is not returned by CreateVolume.  Information about the volume attachments. |
  | availabilityZone | string | The Availability Zone for the volume. |
  | createTime | string | The time stamp when volume creation was initiated. |
  | encrypted | boolean | Indicates whether the volume is encrypted. |
  | size | number | The size of the volume, in GiBs. |
  | state | string | The volume state. |
  | tagSet | array<object> | Any tags assigned to the volume. |
  | volumeId | string | The ID of the volume. |
  | volumeType | string | The volume type. |
  | tagValue | object |  |
  | tagValueList | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.delete_volume
**Delete volume** — Delete an EBS volume.
- Stability: stable
- Permissions: `ec2:DeleteVolume`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | volumeId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.describeSnapshots
**Describe snapshots** — Describes the specified EBS snapshots available to you, or all of the EBS snapshots available to you. The snapshots available to you include public snapshots, private snapshots that you own, and private snapshots owned by other Amazon Web Services accounts for which you have explicit create volume permissions.
- Stability: stable
- Permissions: `ec2:DescribeSnapshots`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | The filters |
  | maxResults | number | no | The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see Pagination. |
  | nextToken | string | no | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request. |
  | ownerIds | array<string> | no | Scopes the results to snapshots with the specified owners. You can specify a combination of Amazon Web Services account IDs, self, and amazon. |
  | restorableByUserIds | array<string> | no | The IDs of the Amazon Web Services accounts that can create volumes from the snapshot. |
  | snapshotIds | array<string> | no | The snapshot IDs. Default: Describes the snapshots for which you have create volume permissions. |
  | dryRun | boolean | no | Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is Dry... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Snapshots | array<object> | Information about the snapshots. |
  | NextToken | string | The token to include in another request to get the next page of items. This value is null when there are no more items to return. |


## com.datadoghq.aws.ebs.describeVolumes
**Describe volumes** — Describe EBS volumes.
- Stability: stable
- Permissions: `ec2:DescribeVolumes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters. |
  | volumeIds | array<string> | no | Volume IDs. |
  | maxResults | number | no | The maximum number of volume results returned by `DescribeVolumes` in paginated output. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | volumes | array<object> | Information about the volumes. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.describe_volume
**Describe volume** — Describe an EBS volume.
- Stability: stable
- Permissions: `ec2:DescribeVolume`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | volumeId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | volume | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.detach_volume
**Detach volume** — Detach an EBS volume from an instance.
- Stability: stable
- Permissions: `ec2:DetachVolume`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | volumeId | string | yes | The ID of the volume. |
  | instanceId | string | no | The ID of the instance. If you are detaching a Multi-Attach enabled volume, you must specify an instance ID. |
  | device | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | device | string | The device name. If the volume is attached to a Fargate task, this parameter returns null. |
  | instanceId | string | The ID of the instance. If the volume is attached to a Fargate task, this parameter returns null. |
  | volumeId | string | The ID of the volume. |
  | atttachTime | string | The time stamp when the attachment initiated. |
  | state | string | The attachment state of the volume. |
  | deleteOnTermination | boolean | Indicates whether the EBS volume is deleted on instance termination. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ebs.modifyVolume
**Modify volume** — Modifies the size, type, and IOPS capacity of an existing EBS volume, typically without downtime on current-generation EC2 instances. After resizing, the file system must be extended to use the new capacity, and a six-hour cooldown period is required before making additional modifications.
- Stability: stable
- Permissions: `ec2:ModifyVolume`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dryRun | boolean | no | Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is Dry... |
  | volumeId | string | yes | The ID of the volume. |
  | size | number | no | The target size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the volume. The following are the supported volumes sizes for each volume type:  ... |
  | volumeType | string | no | The target EBS volume type of the volume. For more information, see Amazon EBS volume types in the Amazon EBS User Guide. Default: The existing type is retained. |
  | iops | number | no | The target IOPS rate of the volume. This parameter is valid only for gp3, io1, and io2 volumes. The following are the supported values for each volume type:    gp3: 3,000 - 16,000 IOPS    io1: 100 ... |
  | throughput | number | no | The target throughput of the volume, in MiB/s. This parameter is valid only for gp3 volumes. The maximum value is 1,000. Default: The existing value is retained if the source and target volume type... |
  | multiAttachEnabled | boolean | no | Specifies whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16  Nitro-based instances in the same Availability Zone. This parameter is suppor... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | VolumeModification | object | Information about the volume modification. |

