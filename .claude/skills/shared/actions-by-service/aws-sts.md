# AWS STS Actions
Bundle: `com.datadoghq.aws.sts` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ests)

## com.datadoghq.aws.sts.testConnection
**Test connection** — Test an AWS connection.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserId | string | The unique identifier of the calling entity. The exact value depends on the type of entity that is making the call. The values returned are those listed in the aws:userid column in the Principal ta... |
  | Account | string | The Amazon Web Services account ID number of the account that owns or contains the calling entity. |
  | Arn | string | The Amazon Web Services ARN associated with the calling entity. |

