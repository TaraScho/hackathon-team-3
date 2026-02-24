# AWS Step Functions Actions
Bundle: `com.datadoghq.aws.stepfunctions` | 7 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Estepfunctions)

## com.datadoghq.aws.stepfunctions.describeExecution
**Describe execution** — Provide information about a state machine execution, such as the state machine associated with the execution, the execution input and output, and relevant execution metadata.
- Stability: stable
- Permissions: `states:DescribeExecution`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | executionArn | string | yes | The Amazon Resource Name (ARN) of the execution to describe. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | execution | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.stepfunctions.describeStateMachine
**Describe state machine** — Provide information about a state machine's definition, its IAM role Amazon Resource Name (ARN), and configuration.
- Stability: stable
- Permissions: `states:DescribeStateMachine`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | stateMachineArn | string | yes | The Amazon Resource Name (ARN) of the state machine for which you want the information. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | stateMachine | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.stepfunctions.listExecutions
**List executions** — List all executions of a state machine by specifying a state machine Amazon Resource Name (ARN).
- Stability: stable
- Permissions: `states:GetExecutionHistory`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | stateMachineArn | string | yes | The Amazon Resource Name (ARN) of the state machine whose executions are listed. |
  | maxResults | number | no | The maximum number of results that are returned per call. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default. |
  | statusFilter | string | no | If specified, only list the executions whose current execution status matches the given filter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | executions | array<object> | The list of matching executions. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.stepfunctions.listStateMachines
**List state machines** — List the existing state machines.
- Stability: stable
- Permissions: `states:ListStateMachines`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum number of results that are returned per call. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | stateMachines | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.stepfunctions.redriveExecution
**Redrive execution** — Restarts unsuccessful executions of Standard workflows that didn&#x27;t complete successfully in the last 14 days. These include failed, aborted, or timed out executions.
- Stability: stable
- Permissions: `stepfunctions:RedriveExecution`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | executionArn | string | yes | The Amazon Resource Name (ARN) of the execution to be redriven. |
  | clientToken | string | no | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don’t specify a client token, the Amazon Web Services SDK automatically generates a client toke... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | redriveDate | string | The date the execution was last redriven. |


## com.datadoghq.aws.stepfunctions.startExecution
**Start execution** — Start a state machine execution.
- Stability: stable
- Permissions: `states:StartExecution`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | stateMachineArn | string | yes | The Amazon Resource Name (ARN) of the state machine to execute. |
  | name | string | no | Optional name of the execution. This name must be unique for your AWS account, Region, and state machine for 90 days. For more information, see [Limits Related to State Machine Executions](https://... |
  | input | object | no | The string that contains the JSON input data for the execution |
  | traceHeader | string | no | Optional X-ray trace header. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | execution | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.stepfunctions.stopExecution
**Stop execution** — Stop an execution.
- Stability: stable
- Permissions: `states:StopExecution`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | executionArn | string | yes | The Amazon Resource Name (ARN) of the execution to stop. |
  | cause | string | no | More detailed explanation of the cause of the failure. |
  | error | string | no | The error code of the failure. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | execution | object |  |
  | amzRequestId | string | The unique identifier for the request. |

