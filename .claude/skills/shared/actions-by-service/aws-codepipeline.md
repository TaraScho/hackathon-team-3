# AWS CodePipeline Actions
Bundle: `com.datadoghq.aws.codepipeline` | 35 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecodepipeline)

## com.datadoghq.aws.codepipeline.acknowledgeJob
**Acknowledge job** — Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
- Stability: stable
- Permissions: `codepipeline:AcknowledgeJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobId | string | yes | The unique system-generated ID of the job for which you want to confirm receipt. |
  | nonce | string | yes | A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the PollForJobs request that returned ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | status | string | Whether the job worker has received the specified job. |


## com.datadoghq.aws.codepipeline.createCustomActionType
**Create custom action type** — Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.
- Stability: stable
- Permissions: `codepipeline:CreateCustomActionType`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | category | string | yes | The category of the custom action, such as a build action or a test action. |
  | provider | string | yes | The provider of the service used in the custom action, such as CodeDeploy. |
  | version | string | yes | The version identifier of the custom action. |
  | settings | object | no | URLs that provide users information about this custom action. |
  | configurationProperties | array<object> | no | The configuration properties for the custom action.  You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, ... |
  | inputArtifactDetails | object | yes | The details of the input artifact for the action, such as its commit ID. |
  | outputArtifactDetails | object | yes | The details of the output artifact of the action, such as its commit ID. |
  | tags | any | no | The tags for the custom action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | actionType | object | Returns information about the details of an action type. |
  | tags | array<object> | Specifies the tags applied to the custom action. |


## com.datadoghq.aws.codepipeline.createPipeline
**Create pipeline** — Creates a pipeline.  In the pipeline structure, you must include either artifactStore or artifactStores in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use artifactStores.
- Stability: stable
- Permissions: `codepipeline:CreatePipeline`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipeline | object | yes | Represents the structure of actions and stages to be performed in the pipeline. |
  | tags | any | no | The tags for the pipeline. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipeline | object | Represents the structure of actions and stages to be performed in the pipeline. |
  | tags | array<object> | Specifies the tags applied to the pipeline. |


## com.datadoghq.aws.codepipeline.deleteCustomActionType
**Delete custom action type** — Marks a custom action as deleted. PollForJobs for the custom action fails after the action is marked for deletion. Used for custom actions only.  To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.
- Stability: stable
- Permissions: `codepipeline:DeleteCustomActionType`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | category | string | yes | The category of the custom action that you want to delete, such as source or deploy. |
  | provider | string | yes | The provider of the service used in the custom action, such as CodeDeploy. |
  | version | string | yes | The version of the custom action to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.deletePipeline
**Delete pipeline** — Deletes the specified pipeline.
- Stability: stable
- Permissions: `codepipeline:DeletePipeline`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the pipeline to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.deleteWebhook
**Delete webhook** — Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.
- Stability: stable
- Permissions: `codepipeline:DeleteWebhook`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the webhook you want to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.deregisterWebhookWithThirdParty
**Deregister webhook with third party** — Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
- Stability: stable
- Permissions: `codepipeline:DeregisterWebhookWithThirdParty`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webhookName | string | no | The name of the webhook you want to deregister. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.disableStageTransition
**Disable stage transition** — Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.
- Stability: stable
- Permissions: `codepipeline:DisableStageTransition`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline in which you want to disable the flow of artifacts from one stage to another. |
  | stageName | string | yes | The name of the stage where you want to disable the inbound or outbound transition of artifacts. |
  | transitionType | string | yes | Specifies whether artifacts are prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they hav... |
  | reason | string | yes | The reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.enableStageTransition
**Enable stage transition** — Enables artifacts in a pipeline to transition to a stage in a pipeline.
- Stability: stable
- Permissions: `codepipeline:EnableStageTransition`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline in which you want to enable the flow of artifacts from one stage to another. |
  | stageName | string | yes | The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound). |
  | transitionType | string | yes | Specifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.getActionType
**Get action type** — Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.
- Stability: stable
- Permissions: `codepipeline:GetActionType`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | category | string | yes | Defines what kind of action can be taken in the stage. The following are the valid values:    Source     Build     Test     Deploy     Approval     Invoke |
  | owner | string | yes | The creator of an action type that was created with any supported integration model. There are two valid values: AWS and ThirdParty. |
  | provider | string | yes | The provider of the action type being called. The provider name is specified when the action type is created. |
  | version | string | yes | A string that describes the action type version. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | actionType | object | The action type information for the requested action type, such as the action type ID. |


## com.datadoghq.aws.codepipeline.getJobDetails
**Get job details** — Returns information about a job. Used for custom actions only.  When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.
- Stability: stable
- Permissions: `codepipeline:GetJobDetails`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobId | string | yes | The unique system-generated ID for the job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobDetails | object | The details of the job.  If AWSSessionCredentials is used, a long-running job can call GetJobDetails again to obtain new credentials. |


## com.datadoghq.aws.codepipeline.getPipeline
**Get pipeline** — Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with UpdatePipeline.
- Stability: stable
- Permissions: `codepipeline:GetPipeline`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the pipeline for which you want to get information. Pipeline names must be unique in an Amazon Web Services account. |
  | version | number | no | The version number of the pipeline. If you do not specify a version, defaults to the current version. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipeline | object | Represents the structure of actions and stages to be performed in the pipeline. |
  | metadata | object | Represents the pipeline metadata information returned as part of the output of a GetPipeline action. |


## com.datadoghq.aws.codepipeline.getPipelineExecution
**Get pipeline execution** — Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
- Stability: stable
- Permissions: `codepipeline:GetPipelineExecution`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline about which you want to get execution details. |
  | pipelineExecutionId | string | yes | The ID of the pipeline execution about which you want to get execution details. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineExecution | object | Represents information about the execution of a pipeline. |


## com.datadoghq.aws.codepipeline.getPipelineState
**Get pipeline state** — Returns information about the state of a pipeline, including the stages and actions.  Values returned in the revisionId and revisionUrl fields indicate the source revision information, such as the commit ID, for the current state.
- Stability: stable
- Permissions: `codepipeline:GetPipelineState`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the pipeline about which you want to get information. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineName | string | The name of the pipeline for which you want to get the state. |
  | pipelineVersion | number | The version number of the pipeline.  A newly created pipeline is always assigned a version number of 1. |
  | stageStates | array<object> | A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data. |
  | created | string | The date and time the pipeline was created, in timestamp format. |
  | updated | string | The date and time the pipeline was last updated, in timestamp format. |


## com.datadoghq.aws.codepipeline.listActionExecutions
**List action executions** — Lists the action executions that have occurred in a pipeline.
- Stability: stable
- Permissions: `codepipeline:ListActionExecutions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline for which you want to list action execution history. |
  | filter | object | no | Input information used to filter action execution history. |
  | maxResults | number | no | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Action execution history is retained for up to 12 m... |
  | nextToken | string | no | The token that was returned from the previous ListActionExecutions call, which can be used to return the next set of action executions in the list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | actionExecutionDetails | array<object> | The details for a list of recent executions, such as action execution ID. |
  | nextToken | string | If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListActionExecutions call to return the next set of action executions in... |


## com.datadoghq.aws.codepipeline.listActionTypes
**List action types** — Gets a summary of all CodePipeline action types associated with your account.
- Stability: stable
- Permissions: `codepipeline:ListActionTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | actionOwnerFilter | string | no | Filters the list of action types to those created by a specified entity. |
  | nextToken | string | no | An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list. |
  | regionFilter | string | no | The Region to filter on for the list of action types. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | actionTypes | array<object> | Provides details of the action types. |
  | nextToken | string | If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list action types call to return the next set of action types in the list. |


## com.datadoghq.aws.codepipeline.listPipelineExecutions
**List pipeline executions** — Gets a summary of the most recent executions for a pipeline.  When applying the filter for pipeline executions that have succeeded in the stage, the operation returns all executions in the current pipeline version beginning on February 1, 2024.
- Stability: stable
- Permissions: `codepipeline:ListPipelineExecutions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline for which you want to get execution summary information. |
  | maxResults | number | no | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 m... |
  | filter | object | no | The pipeline execution to filter on. |
  | nextToken | string | no | The token that was returned from the previous ListPipelineExecutions call, which can be used to return the next set of pipeline executions in the list. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineExecutionSummaries | array<object> | A list of executions in the history of a pipeline. |
  | nextToken | string | A token that can be used in the next ListPipelineExecutions call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned. |


## com.datadoghq.aws.codepipeline.listPipelines
**List pipelines** — Gets a summary of all of the pipelines associated with your account.
- Stability: stable
- Permissions: `codepipeline:ListPipelines`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | An identifier that was returned from the previous list pipelines call. It can be used to return the next set of pipelines in the list. |
  | maxResults | number | no | The maximum number of pipelines to return in a single call. To retrieve the remaining pipelines, make another call with the returned nextToken value. The minimum value you can specify is 1. The max... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelines | array<object> | The list of pipelines. |
  | nextToken | string | If the amount of returned information is significantly large, an identifier is also returned. It can be used in a subsequent list pipelines call to return the next set of pipelines in the list. |


## com.datadoghq.aws.codepipeline.listTagsForResource
**List tags for resource** — Gets the set of key-value pairs (metadata) that are used to manage the resource.
- Stability: stable
- Permissions: `codepipeline:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource to get tags for. |
  | nextToken | string | no | The token that was returned from the previous API call, which would be used to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use p... |
  | maxResults | number | no | The maximum number of results to return in a single call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tags | array<object> | The tags for the resource. |
  | nextToken | string | If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent API call to return the next page of the list. The ListTagsforResource ca... |


## com.datadoghq.aws.codepipeline.listWebhooks
**List webhooks** — Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.  If a secret token was provided, it will be redacted in the response.
- Stability: stable
- Permissions: `codepipeline:ListWebhooks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The token that was returned from the previous ListWebhooks call, which can be used to return the next set of webhooks in the list. |
  | maxResults | number | no | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | webhooks | array<object> | The JSON detail returned for each webhook in the list output for the ListWebhooks call. |
  | NextToken | string | If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent ListWebhooks call to return the next set of webhooks in the list. |


## com.datadoghq.aws.codepipeline.pollForJobs
**Poll for jobs** — Returns information about any jobs for CodePipeline to act on. PollForJobs is valid only for action types with &quot;Custom&quot; in the owner field. If the action type contains AWS or ThirdParty in the owner field, the PollForJobs action returns an error.  When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.
- Stability: stable
- Permissions: `codepipeline:PollForJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | actionTypeId | object | yes | Represents information about an action type. |
  | maxBatchSize | number | no | The maximum number of jobs to return in a poll for jobs call. |
  | queryParam | object | no | A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that prop... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobs | array<object> | Information about the jobs to take action on. |


## com.datadoghq.aws.codepipeline.pollForThirdPartyJobs
**Poll for third party jobs** — Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.  When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.
- Stability: stable
- Permissions: `codepipeline:PollForThirdPartyJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | actionTypeId | object | yes | Represents information about an action type. |
  | maxBatchSize | number | no | The maximum number of jobs to return in a poll for jobs call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobs | array<object> | Information about the jobs to take action on. |


## com.datadoghq.aws.codepipeline.putActionRevision
**Put action revision** — Provides information to CodePipeline about new revisions to a source.
- Stability: stable
- Permissions: `codepipeline:PutActionRevision`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline that starts processing the revision to the source. |
  | stageName | string | yes | The name of the stage that contains the action that acts on the revision. |
  | actionName | string | yes | The name of the action that processes the revision. |
  | actionRevision | object | yes | Represents information about the version (or revision) of an action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | newRevision | boolean | Indicates whether the artifact revision was previously used in an execution of the specified pipeline. |
  | pipelineExecutionId | string | The ID of the current workflow state of the pipeline. |


## com.datadoghq.aws.codepipeline.putApprovalResult
**Put approval result** — Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.
- Stability: stable
- Permissions: `codepipeline:PutApprovalResult`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline that contains the action. |
  | stageName | string | yes | The name of the stage that contains the action. |
  | actionName | string | yes | The name of the action for which approval is requested. |
  | result | object | yes | Represents information about the result of the approval request. |
  | token | string | yes | The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the GetPipelineState action. It is used to validate that the ap... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | approvedAt | string | The timestamp showing when the approval or rejection was submitted. |


## com.datadoghq.aws.codepipeline.putJobFailureResult
**Put job failure result** — Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
- Stability: stable
- Permissions: `codepipeline:PutJobFailureResult`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobId | string | yes | The unique system-generated ID of the job that failed. This is the same ID returned from PollForJobs. |
  | failureDetails | object | yes | The details about the failure of a job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.putJobSuccessResult
**Put job success result** — Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
- Stability: stable
- Permissions: `codepipeline:PutJobSuccessResult`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobId | string | yes | The unique system-generated ID of the job that succeeded. This is the same ID returned from PollForJobs. |
  | currentRevision | object | no | The ID of the current revision of the artifact successfully worked on by the job. |
  | continuationToken | string | no | A token generated by a job worker, such as a CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs use this token to identify the running ins... |
  | executionDetails | object | no | The execution details of the successful job, such as the actions taken by the job worker. |
  | outputVariables | object | no | Key-value pairs produced as output by a job worker that can be made available to a downstream action configuration. outputVariables can be included only when there is no continuation token on the r... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.putWebhook
**Put webhook** — Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there&#x27;s a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.  When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.   If a secret token was provided, it will be redacted in the response.
- Stability: stable
- Permissions: `codepipeline:PutWebhook`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webhook | object | yes | The detail provided in an input file to create the webhook, such as the webhook name, the pipeline name, and the action name. Give the webhook a unique name that helps you identify it. You might na... |
  | tags | any | no | The tags for the webhook. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | webhook | object | The detail returned from creating the webhook, such as the webhook name, webhook URL, and webhook ARN. |


## com.datadoghq.aws.codepipeline.registerWebhookWithThirdParty
**Register webhook with third party** — Configures a connection between the webhook that was created and the external tool with events to be detected.
- Stability: stable
- Permissions: `codepipeline:RegisterWebhookWithThirdParty`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webhookName | string | no | The name of an existing webhook created with PutWebhook to register with a supported third party. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.retryStageExecution
**Retry stage execution** — You can retry a stage that has failed without having to run a pipeline again from the beginning. You do this by either retrying the failed actions in a stage or by retrying all actions in the stage starting from the first action in the stage. When you retry the failed actions in a stage, all actions that are still in progress continue working, and failed actions are triggered again. When you retry a failed stage from the first action in the stage, the stage cannot have any actions in progress. Before a stage can be retried, it must either have all actions failed or some actions failed and some succeeded.
- Stability: stable
- Permissions: `codepipeline:RetryStageExecution`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline that contains the failed stage. |
  | stageName | string | yes | The name of the failed stage to be retried. |
  | pipelineExecutionId | string | yes | The ID of the pipeline execution in the failed stage to be retried. Use the GetPipelineState action to retrieve the current pipelineExecutionId of the failed stage |
  | retryMode | string | yes | The scope of the retry attempt. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineExecutionId | string | The ID of the current workflow execution in the failed stage. |


## com.datadoghq.aws.codepipeline.startPipelineExecution
**Start pipeline execution** — Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.
- Stability: stable
- Permissions: `codepipeline:StartPipelineExecution`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the pipeline to start. |
  | variables | array<object> | no | A list that overrides pipeline variables for a pipeline execution that's being started. Variable names must match [A-Za-z0-9@\-_]+, and the values can be anything except an empty string. |
  | clientRequestToken | string | no | The system-generated unique ID used to identify a unique execution request. |
  | sourceRevisions | array<object> | no | A list that allows you to specify, or override, the source revision for a pipeline execution that's being started. A source revision is the version with all the changes to your application code, or... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineExecutionId | string | The unique system-generated ID of the pipeline execution that was started. |


## com.datadoghq.aws.codepipeline.stopPipelineExecution
**Stop pipeline execution** — Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a Stopping state. After all in-progress actions are completed or abandoned, the pipeline execution is in a Stopped state.
- Stability: stable
- Permissions: `codepipeline:StopPipelineExecution`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipelineName | string | yes | The name of the pipeline to stop. |
  | pipelineExecutionId | string | yes | The ID of the pipeline execution to be stopped in the current stage. Use the GetPipelineState action to retrieve the current pipelineExecutionId. |
  | abandon | boolean | no | Use this option to stop the pipeline execution by abandoning, rather than finishing, in-progress actions.  This option can lead to failed or out-of-sequence tasks. |
  | reason | string | no | Use this option to enter comments, such as the reason the pipeline was stopped. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipelineExecutionId | string | The unique system-generated ID of the pipeline execution that was stopped. |


## com.datadoghq.aws.codepipeline.tagResource
**Tag resource** — Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.
- Stability: stable
- Permissions: `codepipeline:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource you want to add tags to. |
  | tags | any | yes | The tags you want to modify or add to the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.untagResource
**Untag resource** — Removes tags from an Amazon Web Services resource.
- Stability: stable
- Permissions: `codepipeline:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource to remove tags from. |
  | tagKeys | array<string> | yes | The list of keys for the tags to be removed from the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.updateActionType
**Update action type** — Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and UpdateActionType to provide the full structure.
- Stability: stable
- Permissions: `codepipeline:UpdateActionType`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | actionType | object | yes | The action type definition for the action type to be updated. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codepipeline.updatePipeline
**Update pipeline** — Updates a specified pipeline with edits or changes to its structure. Updating the pipeline increases the version number of the pipeline by 1.
- Stability: stable
- Permissions: `codepipeline:UpdatePipeline`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pipeline | object | yes | Represents the structure of actions and stages to be performed in the pipeline. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pipeline | object | The structure of the updated pipeline. |

