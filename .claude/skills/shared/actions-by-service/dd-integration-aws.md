# Datadog AWS Integration Actions
Bundle: `com.datadoghq.dd.integration.aws` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Eaws)

## com.datadoghq.dd.integration.aws.listAWSEventBridgeSources
**List AWS EventBridge sources** — Get all Amazon EventBridge sources.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | accounts | array<object> | List of accounts with their event sources. |
  | isInstalled | boolean | True if the EventBridge sub-integration is enabled for your organization. |


## com.datadoghq.dd.integration.aws.listAWSTagFilters
**List AWS tag filters** — Get all AWS tag filters.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Only return AWS filters that matches this `account_id`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | filters | array<object> | An array of tag filters. |

