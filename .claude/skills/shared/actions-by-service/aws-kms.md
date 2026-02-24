# AWS KMS Actions
Bundle: `com.datadoghq.aws.kms` | 1 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ekms)

## com.datadoghq.aws.kms.listKeys
**List keys** — Gets a list of all KMS keys in the caller&#x27;s Amazon Web Services account and Region.
- Stability: stable
- Permissions: `kms:ListKeys`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no | Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer. This value i... |
  | marker | string | no | Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of NextMarker from the truncated response you just received. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Keys | array<object> | A list of KMS keys. |
  | NextMarker | string | When Truncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent request. |
  | Truncated | boolean | A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the NextMarker element in this ... |

