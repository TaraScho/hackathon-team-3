# AWS Batch Actions
Bundle: `com.datadoghq.aws.batch` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ebatch)

## com.datadoghq.aws.batch.updateComputeEnvironment
**Update compute environment** — Updates an Batch compute environment.
- Stability: stable
- Permissions: `batch:UpdateComputeEnvironment`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | computeEnvironment | string | yes | The name or full Amazon Resource Name (ARN) of the compute environment to update. |
  | state | string | no | The state of the compute environment. Compute environments in the ENABLED state can accept jobs from a queue and scale in or out automatically based on the workload demand of its associated queues.... |
  | unmanagedvCpus | number | no | The maximum number of vCPUs expected to be used for an unmanaged compute environment. Don't specify this parameter for a managed compute environment. This parameter is only used for fair share sche... |
  | computeResources | object | no | Details of the compute resources managed by the compute environment. Required for a managed compute environment. For more information, see Compute Environments in the Batch User Guide. |
  | serviceRole | string | no | The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see Batch service IAM role in the Bat... |
  | updatePolicy | object | no | Specifies the updated infrastructure update policy for the compute environment. For more information about infrastructure updates, see Updating compute environments in the Batch User Guide. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | computeEnvironmentName | string | The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_). |
  | computeEnvironmentArn | string | The Amazon Resource Name (ARN) of the compute environment. |

