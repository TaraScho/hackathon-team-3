# Datadog Cloud Security Actions
Bundle: `com.datadoghq.dd.cloudsecurity` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecloudsecurity)

## com.datadoghq.dd.cloudsecurity.changeSecuritySignalState
**Change security signal state** — Change the status of a Datadog Security Signal.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signalId | string | yes |  |
  | state | string | yes | The state to change the security signal to. |
  | archiveReason | string | no |  |
  | archiveComment | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | signal_id | string |  |
  | incident_ids | array<number> |  |
  | state | string |  |
  | state_update_timestamp | number |  |
  | state_update_user | object |  |


## com.datadoghq.dd.cloudsecurity.createDetectionRule
**Create detection rule** — Create a detection rule.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | ruleName | string | yes | Name of the new detection rule. |
  | queries | array<object> | yes | Queries for selecting logs which are part of the rule. |
  | message | string | yes | Message to be included in the Security Signal. |
  | cases | array<object> | yes | Conditions for when to generate security signals. |
  | maxSignalDuration | number | no | A signal will “close” regardless of the query being matched once the time exceeds the maximum duration. This time is calculated from the first seen timestamp. |
  | evaluationWindow | number | no | A time window is specified to match when at least one of the cases matches true. This is a sliding window and evaluates in real time. |
  | keepAlive | number | no | Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window. |
  | tags | any | no | Tags for generated signals. |


## com.datadoghq.dd.cloudsecurity.getDectectedIPs
**Get detected IPs** — Get the detected IPs for a specific security signal.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signalId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ips | array<string> |  |


## com.datadoghq.dd.cloudsecurity.getDetectionRule
**Get detection rule** — Get a rule’s details.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | ruleId | string | yes | The ID of the rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | name | string |  |
  | cases | array<object> |  |
  | createdAt | number |  |
  | queries | array<object> |  |
  | type | string |  |
  | message | string |  |
  | tags | array<string> |  |
  | tag_value | object |  |
  | tag_value_list | object |  |
  | isEnabled | boolean |  |
  | url | string |  |


## com.datadoghq.dd.cloudsecurity.getSecurityFinding
**Get security finding** — Get information about a specific security finding.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the security finding. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | finding_id | string | The unique identifier for this finding. |
  | attributes | object | Groups core attributes of the security finding that describe its nature, impact, and status. |
  | tags | array<string> | The tags associated with the finding. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | evaluation | string | The evaluation of the finding. |
  | evaluationChangedAt | number | The date on which the evaluation for the finding changed (in ms Unix epoch time). |
  | message | string | The remediation message for the finding. |
  | mute | object | Information about the mute status of the finding. |
  | resource | string | The resource name of the finding. |
  | resourceConfiguration | object | The resource configuration for the finding. |
  | resourceDiscoveryDate | number | The date on which the resource was discovered (in ms Unix epoch time). |
  | resourceType | string | The resource type of the finding. |
  | rule | object | The rule that triggered the finding. |
  | status | string | The status of the finding. |
  | id | string | ID of the finding or security issue. |
  | url | string | The URL where to get the resource details. |


## com.datadoghq.dd.cloudsecurity.getSecurityIssue
**Get security issue** — Get information about a specific security issue.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the security issue. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | evaluation | string | The evaluation of the finding. |
  | evaluationChangedAt | number | The date on which the evaluation for the finding changed (in ms Unix epoch time). |
  | message | string | The remediation message for the finding. |
  | mute | object | Information about the mute status of the finding. |
  | resource | string | The resource name of the finding. |
  | resourceConfiguration | object | The resource configuration for the finding. |
  | resourceDiscoveryDate | number | The date on which the resource was discovered (in ms Unix epoch time). |
  | resourceType | string | The resource type of the finding. |
  | rule | object | The rule that triggered the finding. |
  | status | string | The status of the finding. |
  | tags | array<string> | The tags associated with the finding. |
  | tag_value | object | A map  of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map  of tags where the keys are strings and the values are lists of strings. |
  | id | string | ID of the finding or security issue. |
  | url | string | The URL where to get the resource details. |


## com.datadoghq.dd.cloudsecurity.getSecuritySignal
**Get security signal** — Get information about a specific security signal.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signalId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securitySignal | object |  |
  | detectionRule | object |  |
  | message | string |  |
  | url | string | The URL of the security signal. |
  | id | string |  |


## com.datadoghq.dd.cloudsecurity.getSecuritySignalSource
**Get security signal source** — Get information about a specific security signal.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signalId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | detectionRule | object |  |
  | message | string |  |
  | url | string |  |
  | id | string |  |
  | tags | array<string> |  |
  | tag_value | object |  |
  | tag_value_list | object |  |
  | name | string |  |

