# Datadog AWS Logs Integration Actions
Bundle: `com.datadoghq.dd.integration.awslogs` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Eawslogs)

## com.datadoghq.dd.integration.awslogs.checkAWSLogsLambdaAsync
**Check AWS Logs lambda async** — Test if permissions are present to add log-forwarding triggers for the given services and AWS account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your AWS Account ID without dashes. |
  | lambda_arn | string | yes | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | errors | array<object> | List of errors. |
  | status | string | Status of the properties. |


## com.datadoghq.dd.integration.awslogs.checkAWSLogsServicesAsync
**Check AWS Logs services async** — Test if permissions are present to add log-forwarding triggers for the given services and AWS account.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your AWS Account ID without dashes. |
  | services | array<string> | yes | Array of services IDs set to enable automatic log collection. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | errors | array<object> | List of errors. |
  | status | string | Status of the properties. |


## com.datadoghq.dd.integration.awslogs.createAWSLambdaARN
**Create AWS Lambda ARN** — To enable log collection, attach the Lambda ARN, created for Datadog-AWS log collection, to your AWS account ID.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your AWS Account ID without dashes. |
  | lambda_arn | string | yes | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |


## com.datadoghq.dd.integration.awslogs.deleteAWSLambdaARN
**Delete AWS Lambda ARN** — Delete a Datadog-AWS logs configuration by removing the specific Lambda ARN associated with a given AWS account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your AWS Account ID without dashes. |
  | lambda_arn | string | yes | ARN of the Datadog Lambda created during the Datadog-Amazon Web services Log collection setup. |


## com.datadoghq.dd.integration.awslogs.enableAWSLogServices
**Enable AWS log services** — Enable automatic log collection for a list of services.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your AWS Account ID without dashes. |
  | services | array<string> | yes | Array of services IDs set to enable automatic log collection. |

