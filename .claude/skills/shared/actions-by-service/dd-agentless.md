# Datadog Agentless Scanning Actions
Bundle: `com.datadoghq.dd.agentless` | 7 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eagentless)

## com.datadoghq.dd.agentless.createAwsOnDemandTask
**Create AWS on-demand task** — Trigger the scan of an AWS resource with a high priority.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | arn | string | yes | The arn of the resource to scan. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Single AWS on demand task. |


## com.datadoghq.dd.agentless.createAwsScanOptions
**Create AWS scan options** — Activate Agentless scan options for an AWS account.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | lambda | boolean | yes | Indicates if scanning of Lambda functions is enabled. |
  | sensitive_data | boolean | yes | Indicates if scanning for sensitive data is enabled. |
  | vuln_containers_os | boolean | yes | Indicates if scanning for vulnerabilities in containers is enabled. |
  | vuln_host_os | boolean | yes | Indicates if scanning for vulnerabilities in hosts is enabled. |
  | id | string | yes | The ID of the AWS account. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Single AWS Scan Options entry. |


## com.datadoghq.dd.agentless.deleteAwsScanOptions
**Delete AWS scan options** — Delete Agentless scan options for an AWS account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | The ID of an AWS account. |


## com.datadoghq.dd.agentless.getAwsOnDemandTask
**Get AWS on-demand task** — Fetch the data of a specific on demand task.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | task_id | string | yes | The UUID of the task. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Single AWS on demand task. |


## com.datadoghq.dd.agentless.listAwsOnDemandTasks
**List AWS on-demand tasks** — Fetches the most recent 1000 AWS on demand tasks.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of on demand tasks. |


## com.datadoghq.dd.agentless.listAwsScanOptions
**List AWS scan options** — Fetches the scan options configured for AWS accounts.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of AWS scan options. |


## com.datadoghq.dd.agentless.updateAwsScanOptions
**Update AWS scan options** — Update the Agentless scan options for an activated account.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | The ID of an AWS account. |
  | lambda | boolean | no | Indicates if scanning of Lambda functions is enabled. |
  | sensitive_data | boolean | no | Indicates if scanning for sensitive data is enabled. |
  | vuln_containers_os | boolean | no | Indicates if scanning for vulnerabilities in containers is enabled. |
  | vuln_host_os | boolean | no | Indicates if scanning for vulnerabilities in hosts is enabled. |
  | id | string | yes | The ID of the AWS account. |

