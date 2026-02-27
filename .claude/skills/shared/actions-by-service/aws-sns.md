# AWS SNS Actions
Bundle: `com.datadoghq.aws.sns` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Esns)

## com.datadoghq.aws.sns.publish
**Publish a message** — Send a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify the `TargetArn`).
- Stability: stable
- Permissions: `sns:Publish`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | topicArn | string | yes |  |
  | subject | string | no | The subject of the message for email subscribers. |
  | message | string | yes | The message you want to send. If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to se... |
  | messageGroupId | string | no | Applicable to FIFO topics only. `MessageGroupId` is a tag associating a message to a message group, and is required for FIFO topics. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | messageId | string |  |
  | sequenceNumber | string | This response element applies only to FIFO (first-in-first-out) topics.  The sequence number is a large, non-consecutive number that Amazon SNS assigns to each message. The length of `SequenceNumbe... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sns.send_sms
**Send SMS** — Send a text message (SMS message) directly to a phone number.
- Stability: stable
- Permissions: `sns:Publish`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | phoneNumber | string | yes |  |
  | message | string | yes | The message you want to send. If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to se... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | messageId | string |  |
  | amzRequestId | string | The unique identifier for the request. |

