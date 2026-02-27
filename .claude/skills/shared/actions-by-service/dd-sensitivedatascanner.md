# Datadog Sensitive Data Scanner Actions
Bundle: `com.datadoghq.dd.sensitivedatascanner` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Esensitivedatascanner)

## com.datadoghq.dd.sensitivedatascanner.deleteScanningGroup
**Delete scanning group** — Delete a given group.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | group_id | string | yes | The ID of a group of rules. |
  | version | number | no | Version of the API (optional). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | meta | object | Meta payload containing information about the API. |


## com.datadoghq.dd.sensitivedatascanner.deleteScanningRule
**Delete scanning rule** — Delete a given rule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | rule_id | string | yes | The ID of the rule. |
  | version | number | no | Version of the API (optional). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | meta | object | Meta payload containing information about the API. |


## com.datadoghq.dd.sensitivedatascanner.listScanningGroups
**List scanning groups** — List all the Scanning groups in your organization.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Response data related to the scanning groups. |
  | included | array<object> | Included objects from relationships. |
  | meta | object | Meta response containing information about the API. |


## com.datadoghq.dd.sensitivedatascanner.listStandardPatterns
**List standard patterns** — Returns all standard patterns.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List Standard patterns response. |


## com.datadoghq.dd.sensitivedatascanner.reorderScanningGroups
**Reorder scanning groups** — Reorder the list of groups.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | data | object | yes | Data related to the reordering of scanning groups. |
  | meta | object | yes | Meta payload containing information about the API. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | meta | object | Meta response containing information about the API. |

