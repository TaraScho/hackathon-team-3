# AWS GuardDuty Actions
Bundle: `com.datadoghq.aws.guardduty` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eguardduty)

## com.datadoghq.aws.guardduty.add_member
**Add member** — Invite other AWS accounts to enable GuardDuty, and allow the current AWS account to view and manage findings on their behalf as the GuardDuty administrator account.
- Stability: stable
- Permissions: `guardduty:CreateMembers`, `guardduty:InviteMembers`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | detectorId | string | yes |  |
  | accountId | string | yes |  |
  | email | string | yes |  |
  | sendInvite | boolean | no | Invite the specified account to enable GuardDuty. |
  | message | string | no | The message to send to the account being invited to enable GuardDuty. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.guardduty.archiveFindings
**Archive findings** — Archives GuardDuty findings that are specified by the list of finding IDs.  Only the administrator account can archive findings. Member accounts don&#x27;t have permission to archive findings from their accounts.
- Stability: stable
- Permissions: `guardduty:ArchiveFindings`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | detectorId | string | yes | The ID of the detector that specifies the GuardDuty service whose findings you want to archive. |
  | findingIds | array<string> | yes | The IDs of the findings that you want to archive. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.guardduty.unarchiveFindings
**Unarchive findings** — Unarchives GuardDuty findings specified by the finding IDs.
- Stability: stable
- Permissions: `guardduty:UnarchiveFindings`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | detectorId | string | yes | The ID of the detector associated with the findings to unarchive. |
  | findingIds | array<string> | yes | The IDs of the findings to unarchive. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.guardduty.update_ipset
**Update IP set** — Update the IP set specified by the IP set ID.
- Stability: stable
- Permissions: `guardduty:UpdateIPSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | detectorId | string | yes |  |
  | ipSetId | string | yes |  |
  | activate | boolean | no | The updated boolean value that specifies whether the IP set is active or not. |
  | location | string | no | The updated URI of the file that contains the IP set. |
  | name | string | no | The unique ID that specifies the IP set to update. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.guardduty.update_threatintelset
**Update threat intel set** — Update the threat intelligence set specified by the threat intelligence set ID.
- Stability: stable
- Permissions: `guardduty:UpdateThreatIntelSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | detectorId | string | yes |  |
  | threatIntelId | string | yes |  |
  | activate | boolean | no | The updated boolean value that specifies whether the threat intelligence set is active or not. |
  | location | string | no | The updated URI of the file that contains the threat intelligence set. |
  | name | string | no | The unique ID that specifies the threat intelligence set that you want to update. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

