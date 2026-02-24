# AWS EventBridge Actions
Bundle: `com.datadoghq.aws.eventbridge` | 17 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eeventbridge)

## com.datadoghq.aws.eventbridge.activate_event_source
**Activate event source** — Activate a partner event source that was previously deactivated. Once activated, the matching event bus starts receiving events from the event source.
- Stability: stable
- Permissions: `events:ActivateEventSource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the partner event source to activate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.cancel_replay
**Cancel replay** — Cancel a replay.
- Stability: stable
- Permissions: `events:CancelReplay`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the replay to cancel. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | replayArn | string | The ARN of the replay to cancel. |
  | state | string | The current state of the replay. |
  | stateReason | string | The reason that the replay is in the current state. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.create_archive
**Create archive** — Create an archive of events with the specified settings. Incoming events may not immediately start being sent to the archive, so allow a short period of time for changes to take effect.
- Stability: stable
- Permissions: `events:CreateArchive`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the archive to create. |
  | eventSourceArn | string | yes | The ARN of the event bus that sends events to the archive. |
  | retentionDays | number | no |  |
  | eventPattern | object | no | An event pattern to filter events sent to the archive. Specify only the fields of an event that you want the event pattern to match. |
  | description | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | archiveArn | string | The ARN of the archive that was created. |
  | state | string | The state of the archive that was created. |
  | stateReason | string | The reason that the archive is in the state. |
  | creationTime | string | The time at which the archive was created. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.deactivate_event_source
**Deactivate event source** — Temporarily stop receiving events from a partner event source. The matching event bus is not deleted. When you deactivate a partner event source, the source goes into `PENDING` state. If it remains in `PENDING` state for more than two weeks, it is deleted. To activate a deactivated partner event source, use `ActivateEventSource`.
- Stability: stable
- Permissions: `events:DeactivateEventSource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the partner event source to deactivate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.delete_archive
**Delete archive** — Delete an archive.
- Stability: stable
- Permissions: `events:DeleteArchive`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the archive to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.describe_event_source
**Describe event source** — List details about a partner event source shared with your account.
- Stability: stable
- Permissions: `events:DescribeEventSource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the partner event source for which to display the details. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | arn | string | The ARN of the partner event source. |
  | createdBy | string | The name of the SaaS partner that created the event source. |
  | creationTime | string | The date and time that the event source was created. |
  | expirationTime | string | The date and time that the event source will expire if you do not create a matching event bus. |
  | name | string | The name of the partner event source. |
  | state | string | The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.describe_replay
**Describe replay** — Retrieve details about a replay. Use `DescribeReplay` to determine the progress of a running replay.
- Stability: stable
- Permissions: `events:DescribeReplay`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the replay to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | replayName | string | The name of the replay. |
  | replayArn | string | The ARN of the replay. |
  | description | string | The description of the replay. |
  | state | string | The current state of the replay. |
  | stateReason | string | The reason that the replay is in the current state. |
  | eventSourceArn | string | The ARN of the archive events were replayed from. |
  | destination | object | A `ReplayDestination` object that contains details about the replay. |
  | eventStartTime | string | The time stamp of the first event that was last replayed from the archive. |
  | eventEndTime | string | The time stamp for the last event that was replayed from the archive. |
  | eventLastReplayedTime | string | The time that the event was last replayed. |
  | replayStartTime | string | A time stamp for the time that the replay started. |
  | replayEndTime | string | A time stamp for the time that the replay stopped. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.disable_rule
**Disable rule** — Disable a rule. A disabled rule does not match any events nor self-trigger if it has a schedule expression. Incoming events may continue to match to the disabled rule, so allow a short period of time for changes to take effect.
- Stability: stable
- Permissions: `events:DisableRule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the rule. |
  | eventBusName | string | no | The name or ARN of the event bus to associate with this rule. If omitted, the default event bus is used. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.enable_rule
**Enable rule** — Enable a rule. If the rule does not exist, the operation fails. Incoming events may not immediately match to a newly enabled rule, so allow a short period of time for changes to take effect.
- Stability: stable
- Permissions: `events:EnableRule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the rule. |
  | eventBusName | string | no | The name or ARN of the event bus to associate with this rule. If omitted, the default event bus is used. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.getAWSEventsArchive
**Describe archive** — Get details about an archive.
- Stability: stable
- Permissions: `events:DescribeArchive`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | archive | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.listAWSEventsArchive
**List archives** — List archives.
- Stability: stable
- Permissions: `events:ListArchives`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | archives | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.list_event_sources
**List event source** — List all the partner event sources that have been shared with your AWS account. For more information about partner event sources, see [CreateEventBus](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html "{isExternal}") in the EventBridge documentation.
- Stability: stable
- Permissions: `events:ListEventSources`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | namePrefix | string | no | Limit the results to only those partner event sources with names that start with the specified prefix. |
  | limit | number | no | Limit the number of results returned by this operation. The operation also returns a `NextToken` which can be used in a subsequent operation to retrieve the next set of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | eventSources | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.list_replays
**List replays** — List all replays or provide a prefix to match to replay names. Filter parameters are exclusive.
- Stability: stable
- Permissions: `events:ListReplays`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | eventSourceArn | string | no | The ARN of the archive from which the events are replayed. |
  | limit | number | no | The maximum number of replays to retrieve. |
  | namePrefix | string | no | A name prefix to filter the replays returned. Only replays with names that match the prefix are returned. |
  | state | string | no | The state of the replay. |
  | nextToken | any | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | replays | array<object> | An array of Replay objects that contain information about the replay. |
  | nextToken | any | The token returned by a previous call to retrieve the next set of results. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.put_event
**Put event** — Send a single event to Amazon EventBridge.
- Stability: stable
- Permissions: `events:PutEvents`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | source | string | yes | The source of the event. |
  | resources | array<string> | no | Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present. |
  | detailType | string | no | Free-form string used to decide what fields to include in the event detail. |
  | detail | object | no | A valid JSON object. There is no other schema imposed. The JSON object may contain fields and nested subobjects. |
  | eventBusName | string | no | The name or ARN of the event bus to receive the event. Only rules associated with this event bus are used to match the event. If omitted, the default event bus is used. If you are entering the ARN ... |
  | traceHeader | string | no | An X-Ray trace header, an HTTP header (`X-Amzn-Trace-Id`) that contains the `trace-id` associated with the event. To learn more about X-Ray trace headers, see [Tracing header](https://docs.aws.amaz... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | eventId | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.put_events
**Put events** — Send custom events to Amazon EventBridge.
- Stability: stable
- Permissions: `events:PutEvents`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | entries | array<object> | yes | The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | failedEntryCount | number | The number of failed entries. |
  | entries | array<object> | The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify t... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.start_replay
**Start replay** — Start a replay. Events may not be replayed in the same order they were added to the archive. See [StartReplay](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_StartReplay.html "{isExternal}") in the EventBridge documentation for more information.
- Stability: stable
- Permissions: `events:StartReplay`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the replay to start. |
  | eventSourceArn | string | yes | The ARN of the archive from which to replay events. |
  | eventTimeRange | any | yes | The time period from which to replay events. |
  | destinationEventBusName | string | yes | The ARN of the event bus to replay events to. |
  | ruleNamesToApply | array<string> | no | List of rule ARNs to apply to replayed events. |
  | description | string | no | A description for the replay to start. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | replayArn | string | The ARN of the replay. |
  | state | string | The state of the replay. |
  | stateReason | string | The reason that the replay is in the state. |
  | replayStartTime | string | The time at which the replay started. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eventbridge.update_archive
**Update archive** — Update an archive.
- Stability: stable
- Permissions: `events:UpdateArchive`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the archive to update. |
  | retentionDays | number | no |  |
  | eventPattern | object | no | An event pattern to filter events sent to the archive. Specify only the fields of an event that you want the event pattern to match. |
  | description | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | archiveArn | string | The ARN of the archive. |
  | state | string | The state of the archive. |
  | stateReason | string | The reason that the archive is in the current state. |
  | creationTime | string | The time at which the archive was updated. |
  | amzRequestId | string | The unique identifier for the request. |

