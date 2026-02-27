# AWS Kinesis Actions
Bundle: `com.datadoghq.aws.kinesis` | 7 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ekinesis)

## com.datadoghq.aws.kinesis.add_tags_to_stream
**Add tags to stream** — Add or update tags for a Kinesis data stream.
- Stability: stable
- Permissions: `kinesis:AddTagsToStream`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | tagMap | any | yes | A set of up to 10 key-value pairs used to create the tags. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.describe_stream
**Describe stream** — Describe a Kinesis data stream.
- Stability: stable
- Permissions: `kinesis:DescribeStream`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | limit | number | no | The maximum number of items to list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | streamDescription | object | The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard objects that comprise the stream, and whether there are more shards available. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.list_streams
**List streams** — List your Kinesis data streams. May require multiple calls to `ListStreams`.
- Stability: stable
- Permissions: `kinesis:ListStreams`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no | The maximum number of items to list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hasMoreStreams | boolean | If set to true, there are more streams available to list. |
  | streamNames | array<string> | The names of the streams that are associated with the Amazon Web Services account making the ListStreams request. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.list_tags_for_stream
**List tags for stream** — List the tags of a Kinesis data stream.
- Stability: stable
- Permissions: `kinesis:ListTagsForStream`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | limit | number | no | The maximum number of items to list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hasMoreTags | boolean | If set to `true`, more tags are available. To request additional tags, set `ExclusiveStartTagKey` to the key of the last tag returned. |
  | tags | array<object> | A list of tags associated with `StreamName`, starting with the first tag after `ExclusiveStartTagKey` and up to the specified `Limit`. |
  | tagValue | object |  |
  | tagValueList | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.put_record
**Put record** — Write a single data record into a data stream.
- Stability: stable
- Permissions: `kinesis:PutRecord`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | data | any | yes | The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size... |
  | partitionKey | string | yes | The key used to assign the data record to a shard in the stream. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | sequenceNumber | string | The sequence number identifier that was assigned to the put data record. The sequence number for the record is unique across all records in the stream. A sequence number is the identifier associate... |
  | shardId | string | The shard ID of the shard where the data record was placed. |
  | encryptionType | string | The encryption type to use on the record. This parameter can be one of the following values:     `NONE`: Do not encrypt the records in the stream.     `KMS`: Use server-side encryption on the recor... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.put_records
**Put records** — Write multiple data records into a Kinesis data stream in a single call.
- Stability: stable
- Permissions: `kinesis:PutRecords`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | records | array<object> | yes | An array of records to put in the stream. For more information see the [`PutRecordsRequestEntry` type documentation](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecordsRequestEnt... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | recordsWritten | array<object> | An array of successfully and unsuccessfully processed record results. A record that is successfully added to a stream includes `SequenceNumber` and `ShardId` in the result. A record that fails to b... |
  | failedRecordCount | number | The number of unsuccessfully processed records in a `PutRecords` request. |
  | encryptionType | string | The encryption type used on the records. This parameter can be one of the following values:     `NONE`: Do not encrypt the records.     `KMS`: Use server-side encryption on the records using a cust... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.kinesis.remove_tags_from_stream
**Remove tags from stream** — Remove tags from a Kinesis data stream.
- Stability: stable
- Permissions: `kinesis:RemoveTagsFromStream`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | streamName | string | yes |  |
  | tagKeys | array<string> | yes | A list of tag keys to remove from the stream. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

