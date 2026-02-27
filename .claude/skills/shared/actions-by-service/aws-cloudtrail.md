# AWS CloudTrail Actions
Bundle: `com.datadoghq.aws.cloudtrail` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecloudtrail)

## com.datadoghq.aws.cloudtrail.getAWSCloudTrailTrail
**Describe trail** — Get details about a trail.
- Stability: stable
- Permissions: `CloudTrail:GetTrail`, `CloudTrail:GetTrailStatus`, `CloudTrail:ListTags`, `CloudTrail:GetEventSelectors`, `CloudTrail:GetInsightSelectors`, `CloudTrail:DescribeTrails`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | trail | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.cloudtrail.listAWSCloudTrailTrail
**List trails** — List trails.
- Stability: stable
- Permissions: `CloudTrail:ListTrails`, `CloudTrail:GetTrail`, `CloudTrail:GetTrailStatus`, `CloudTrail:ListTags`, `CloudTrail:GetEventSelectors`, `CloudTrail:GetInsightSelectors`, `CloudTrail:DescribeTrails`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | trails | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.cloudtrail.updateCloudTrail
**Update trail** — Update trail settings that control the events being logged, and how to handle log files.
- Stability: stable
- Permissions: `cloudtrail:UpdateTrail`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trail or trail ARN. |
  | s3BucketName | string | no | The name of the Amazon S3 bucket designated for publishing log files. |
  | s3KeyPrefix | string | no | The Amazon S3 key prefix that comes after the name of the bucket designated for log file delivery. |
  | isMultiRegionTrail | boolean | no | Apply the trail only to the current region or to all regions. |
  | enableLogFileValidation | boolean | no | Enable log file validation. See the note under **Digest file chaining** in the AWS [CloudTrail digest file structure documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudt... |
  | cloudWatchLogsRoleArn | string | no | Specify the role for the CloudWatch Logs endpoint to assume to write to a user's log group. |
  | cloudWatchLogsLogGroupArn | string | no | Specify a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered. Not required unless you specify Cloud watch l... |
  | kmsKeyId | string | no | Specify the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by `alias/`, a fully specified ARN to an alias, a fully specified ARN to a key, or... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | Name | string | Specifies the name of the trail. |
  | S3BucketName | string | Specifies the name of the Amazon S3 bucket designated for publishing log files. |
  | S3KeyPrefix | string | Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your IAM Log Files. |
  | SnsTopicName | string | This field is no longer in use. Use SnsTopicARN. |
  | SnsTopicARN | string | Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.  arn:aws:sns:us-east-2:123456789012:My... |
  | IncludeGlobalServiceEvents | boolean | Specifies whether the trail is publishing events from global services such as IAM to the log files. |
  | IsMultiRegionTrail | boolean | Specifies whether the trail exists in one Region or in all Regions. |
  | TrailARN | string | Specifies the ARN of the trail that was updated. The following is the format of a trail ARN.  arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail |
  | LogFileValidationEnabled | boolean | Specifies whether log file integrity validation is enabled. |
  | CloudWatchLogsLogGroupArn | string | Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs are delivered. |
  | CloudWatchLogsRoleArn | string | Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. |
  | KmsKeyId | string | Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.  arn:aws:kms:us-east-2:123456789012:key/12345678-12... |
  | IsOrganizationTrail | boolean | Specifies whether the trail is an organization trail. |
  | amzRequestId | string | The unique identifier for the request. |

