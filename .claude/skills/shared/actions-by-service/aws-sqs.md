# AWS SQS Actions
Bundle: `com.datadoghq.aws.sqs` | 19 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Esqs)

## com.datadoghq.aws.sqs.cancelMessageMoveTask
**Cancel message move task** — Cancels a specified message movement task. A message movement can only be cancelled when the current status is RUNNING. Cancelling a message movement task does not revert the messages that have already been moved. It can only stop the messages that have not been moved yet.    This action is currently limited to supporting message redrive from dead-letter queues (DLQs) only. In this context, the source queue is the dead-letter queue (DLQ), while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.    Only one active message movement task is supported per queue at any given time.
- Stability: stable
- Permissions: `sqs:CancelMessageMoveTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | taskHandle | string | yes | An identifier associated with a message movement task. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ApproximateNumberOfMessagesMoved | number | The approximate number of messages already moved to the destination queue. |


## com.datadoghq.aws.sqs.createQueue
**Create queue** — Creates a new standard or FIFO queue.
- Stability: stable
- Permissions: `sqs:CreateQueue`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes | The name of the new queue. The following limits apply to this name:   A queue name can have up to 80 characters.   Valid values: alphanumeric characters, hyphens (-), and underscores (_).   A FIFO ... |
  | attributes | object | no | A map of attributes with their corresponding values. The following lists the names, descriptions, and values of the special request parameters that the CreateQueue action uses:    DelaySeconds – Th... |
  | tags | any | no | Add cost allocation tags to the specified Amazon SQS queue. For an overview, see Tagging Your Amazon SQS Queues in the Amazon SQS Developer Guide. When you use queue tags, keep the following guidel... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | QueueUrl | string | The URL of the created Amazon SQS queue. |


## com.datadoghq.aws.sqs.deleteQueue
**Delete queue** — Deletes the queue specified by the QueueUrl, regardless of the queues contents.
- Stability: stable
- Permissions: `sqs:DeleteQueue`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueUrl | string | yes | The URL of the Amazon SQS queue to delete. Queue URLs and names are case-sensitive. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.delete_messages
**Delete messages** — Delete messages from a queue.
- Stability: stable
- Permissions: `sqs:DeleteMessage`, `sqs:GetQueueUrl`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes |  |
  | messageReceiptHandles | array<string> | yes | The receipt handle associated with the message to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | successful | array<string> |  |
  | failedToDelete | array<object> |  |


## com.datadoghq.aws.sqs.getAWSSQSQueue
**Describe queue** — Get details about a queue.
- Stability: stable
- Permissions: `sqs:GetQueueAttributes`, `sqs:ListQueueTags`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | queue | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.get_queue_attributes
**Get queue attributes** — Get attributes for a queue.
- Stability: stable
- Permissions: `sqs:GetQueueAttributes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes |  |
  | attributeNames | array<string> | no | A list of attributes for which to retrieve information. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | attributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.listMessageMoveTasks
**List message move tasks** — Gets the most recent message movement tasks (up to 10) under a specific source queue.    This action is currently limited to supporting message redrive from dead-letter queues (DLQs) only. In this context, the source queue is the dead-letter queue (DLQ), while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.    Only one active message movement task is supported per queue at any given time.
- Stability: stable
- Permissions: `sqs:ListMessageMoveTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceArn | string | yes | The ARN of the queue whose message movement tasks are to be listed. |
  | maxResults | number | no | The maximum number of results to include in the response. The default is 1, which provides the most recent message movement task. The upper limit is 10. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Results | array<object> | A list of message movement tasks and their attributes. |


## com.datadoghq.aws.sqs.listQueueTags
**List queue tags** — List all cost allocation tags added to the specified Amazon SQS queue. For an overview, see Tagging Your Amazon SQS Queues in the Amazon SQS Developer Guide.  Cross-account permissions don&#x27;t apply to this action. For more information, see Grant cross-account permissions to a role and a username in the Amazon SQS Developer Guide.
- Stability: stable
- Permissions: `sqs:ListQueueTags`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueUrl | string | yes | The URL of the queue. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Tags | object | The list of all tags added to the specified queue. |


## com.datadoghq.aws.sqs.list_queues
**List queues** — Return a list of queues in the current region. The response includes a maximum of 1,000 results. If you specify a value for the optional `QueueNamePrefix` parameter, only queues with names that begin with the specified value are returned.
- Stability: stable
- Permissions: `sqs:ListQueues`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueNamePrefix | string | no | A string used to filter the list results. Only queues with names beginning with the string are returned. Queue URLs and names are case-sensitive. |
  | maxResults | number | no | The maximum number of results to include in the response. You must set MaxResults to receive a value for NextToken in the response. |
  | nextToken | string | no | Pagination token to request the next set of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | queues | array<string> |  |
  | nextToken | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.list_queues_with_attributes
**List queues with attributes** — Return a list of queues in the current region with their attributes . The response includes a maximum of 1,000 results. If you specify a value for the optional `QueueNamePrefix` parameter, only queues with names that begin with the specified value are returned.
- Stability: stable
- Permissions: `sqs:ListQueues`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueNamePrefix | string | no | A string used to filter the list results. Only queues with names beginning with the string are returned. Queue URLs and names are case-sensitive. |
  | maxResults | number | no | The maximum number of results to include in the response. You must set MaxResults to receive a value for NextToken in the response. |
  | nextToken | string | no | Pagination token to request the next set of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | queues | array<object> |  |
  | nextToken | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.move_messages
**Move messages** — Send messages from one queue to another queue.
- Stability: stable
- Permissions: `sqs:SendMessage`, `sqs:ReceiveMessage`, `sqs:DeleteMessage`, `sqs:GetQueueUrl`
- Access: read, create, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | fromQueueName | string | yes |  |
  | toQueueName | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | successful | array<string> |  |
  | failedToMove | array<object> |  |


## com.datadoghq.aws.sqs.purge_queue
**Purge queue** — Delete the messages in a queue specified by the `Queue name` parameter. Any messages deleted from a queue through this action are irretrievable. The message deletion process takes up to 60 seconds.
- Stability: stable
- Permissions: `sqs:PurgeQueue`, `sqs:GetQueueUrl`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes | The name of the queue |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.receiveMessageV2
**Receive message** — Retrieves one or more messages, from the specified queue. Using the WaitTimeSeconds parameter enables long-poll support. Short poll is the default behavior where a weighted random set of machines is sampled.
- Stability: stable
- Permissions: `sqs:ReceiveMessage`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueUrl | string | yes | The URL of the Amazon SQS queue from which messages are received. Queue URLs and names are case-sensitive. |
  | attributeNames | array<string> | no | <important> This parameter has been discontinued but will be supported for backward compatibility. To provide attribute names, you are encouraged to use MessageSystemAttributeNames. </important> A ... |
  | messageSystemAttributeNames | array<string> | no | A list of attributes that need to be returned along with each message. These attributes include: All – Returns all values. ApproximateFirstReceiveTimestamp – Returns the time the message was first ... |
  | messageAttributeNames | array<string> | no | The name of the message attribute, where N is the index. The name can contain alphanumeric characters and the underscore (_), hyphen (-), and period (.). The name is case-sensitive and must be uniq... |
  | maxNumberOfMessages | number | no | The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1. |
  | visibilityTimeout | number | no | The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request. If not specified, the default visibility timeout... |
  | waitTimeSeconds | number | no | The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds. If no messages are... |
  | receiveRequestAttemptId | string | no | This parameter applies only to FIFO (first-in-first-out) queues. The token used for deduplication of ReceiveMessage calls. If a networking issue occurs after a ReceiveMessage action, and instead of... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Messages | array<object> | A list of messages. |


## com.datadoghq.aws.sqs.receive_messages
**Receive messages** — Receive messages from a queue.
- Stability: stable
- Permissions: `sqs:ReceiveMessage`, `sqs:DeleteMessage`, `sqs:GetQueueUrl`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes |  |
  | maxNumberOfMessages | number | no | The maximum number of messages to return. |
  | messageAttributeNames | array<string> | no | When using ReceiveMessage, you can send a list of attribute names to receive, or you can return all of the attributes by specifying All or .* in your request. You can also use all message attribute... |
  | deleteMessages | boolean | no | Enable automatic deletion of received messages. Defaults to `true`. If set to `false`, received messages must be manually deleted with the `Delete Messages` action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | messages | array<object> |  |


## com.datadoghq.aws.sqs.send_message
**Send message** — Deliver a message to a queue.
- Stability: stable
- Permissions: `sqs:SendMessage`, `sqs:GetQueueUrl`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes |  |
  | messageBody | string | yes | The message to send. The minimum size is one character. The maximum size is 256 KB.  A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed:  `#x9`... |
  | messageAttributes | object | no | A map of message attributes to send. The value of each attribute can be a string or a number. |
  | messageSystemAttributes | object | no | A map of message system attributes to send. Only the system attribute `AWSTraceHeader` is supported. Its value must be a correctly formatted AWS X-Ray trace header string. |
  | messageGroupId | string | no | Applicable to FIFO topics only. `MessageGroupId` is a tag associating a message to a message group, and is required for FIFO topics. |
  | delaySeconds | number | no | The length of time to delay a specific message. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.set_queue_attributes
**Set queue attributes** — Set attributes for a queue.
- Stability: stable
- Permissions: `sqs:SetQueueAttributes`, `sqs:GetQueueUrl`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueName | string | yes |  |
  | attributes | object | yes | Map of attributes with their values. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.startMessageMoveTask
**Start message move task** — Starts an asynchronous task to move messages from a specified source queue to a specified destination queue.    This action is currently limited to supporting message redrive from queues that are configured as dead-letter queues (DLQs) of other Amazon SQS queues only. Non-SQS queue sources of dead-letter queues, such as Lambda or Amazon SNS topics, are currently not supported.   In dead-letter queues redrive context, the StartMessageMoveTask the source queue is the DLQ, while the destination queue can be the original source queue (from which the messages were driven to the dead-letter-queue), or a custom destination queue.   Only one active message movement task is supported per queue at any given time.
- Stability: stable
- Permissions: `sqs:StartMessageMoveTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceArn | string | yes | The ARN of the queue that contains the messages to be moved to another queue. Currently, only ARNs of dead-letter queues (DLQs) whose sources are other Amazon SQS queues are accepted. DLQs whose so... |
  | destinationArn | string | no | The ARN of the queue that receives the moved messages. You can use this field to specify the destination queue where you would like to redrive messages. If this field is left blank, the messages wi... |
  | maxNumberOfMessagesPerSecond | number | no | The number of messages to be moved per second (the message movement rate). You can use this field to define a fixed message movement rate. The maximum value for messages per second is 500. If this ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskHandle | string | An identifier associated with a message movement task. You can use this identifier to cancel a specified message movement task using the CancelMessageMoveTask action. |


## com.datadoghq.aws.sqs.tagQueue
**Tag queue** — Add cost allocation tags to the specified Amazon SQS queue.
- Stability: stable
- Permissions: `sqs:TagQueue`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueUrl | string | yes | The URL of the queue. |
  | tags | any | yes | The list of tags to be added to the specified queue. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.sqs.untagQueue
**Untag queue** — Remove cost allocation tags from the specified Amazon SQS queue.
- Stability: stable
- Permissions: `sqs:UntagQueue`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | queueUrl | string | yes | The URL of the queue. |
  | tagKeys | array<string> | yes | The list of tags to be removed from the specified queue. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

