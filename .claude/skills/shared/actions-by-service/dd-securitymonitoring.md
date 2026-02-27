# Datadog Security Monitoring Actions
Bundle: `com.datadoghq.dd.securitymonitoring` | 31 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Esecuritymonitoring)

## com.datadoghq.dd.securitymonitoring.addSecurityMonitoringSignalToIncident
**Add security monitoring signal to incident** — Add a security signal to an incident.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signal_id | string | yes | The ID of the signal. |
  | add_to_signal_timeline | boolean | no | Whether to post the signal on the incident timeline. |
  | incident_id | number | yes | Public ID attribute of the incident to which the signal will be added. |
  | version | number | no | Version of the updated signal. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | status | string | Status of the response. |


## com.datadoghq.dd.securitymonitoring.attachCase
**Attach security findings to a case** — Attach security findings to a case.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | case_id | string | yes | The unique identifier of the case to attach security findings to. |
  | finding_ids | array<string> | yes | The unique identifiers of the security findings. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data of the case. |


## com.datadoghq.dd.securitymonitoring.attachJiraIssue
**Attach security findings to a Jira issue** — Attach security findings to a Jira issue by providing the Jira issue URL.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | The unique identifier of the case management project. The project must have Jira integration enabled. Learn more about how to configure Jira integration here: https://docs.datadoghq.com/security/ti... |
  | finding_ids | array<string> | yes | The unique identifiers of the security findings. |
  | jira_issue_url | string | yes | The URL of the Jira issue to attach security findings to. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data of the case. |


## com.datadoghq.dd.securitymonitoring.convertExistingSecurityMonitoringRule
**Convert existing security monitoring rule** — Convert an existing rule from JSON to Terraform for Datadog provider resource `datadog_security_monitoring_rule`.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | rule_id | string | yes | The ID of the rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ruleId | string | the ID of the rule. |
  | terraformContent | string | Terraform string as a result of converting the rule from JSON. |


## com.datadoghq.dd.securitymonitoring.createCase
**Create case for security findings** — Create case for security findings.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | The unique identifier of the case management project. |
  | finding_ids | array<string> | yes | The unique identifiers of the security findings. |
  | title | string | no | The title of the case. If not provided, the title will be generated based on the findings. |
  | description | string | no | The description of the case. If not provided, the description will be generated based on the findings. |
  | priority | string | no | The priority of the case. |
  | assignee_id | string | no | The unique identifier of the user assigned to the case. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data of the case. |


## com.datadoghq.dd.securitymonitoring.createJiraIssue
**Create Jira issue for security findings** — Create Jira issue for security findings.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | project_id | string | yes | The unique identifier of the case management project. The project must have Jira integration enabled. Learn more about how to configure Jira integration here: https://docs.datadoghq.com/security/ti... |
  | finding_ids | array<string> | yes | The unique identifiers of the security findings. |
  | title | string | no | The title of the Jira issue. If not provided, the title will be generated based on the findings. |
  | description | string | no | The description of the Jira issue. If not provided, the description will be generated based on the findings. |
  | priority | string | no | The priority of the Jira issue. |
  | assignee_id | string | no | The unique identifier of the user assigned to the Jira issue. |
  | customFields | object | no | Custom fields of the Jira issue to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data of the case. |


## com.datadoghq.dd.securitymonitoring.createSignalNotificationRule
**Create signal notification rule** — Create a new notification rule for security signals and return the created rule.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | The query is composed of one or several key:value pairs, which can be used to filter security issues on tags and attributes. |
  | rule_types | array<string> | no | Security rule types used as filters in security rules. |
  | severities | array<string> | no | The security rules severities to consider. |
  | trigger_source | string | yes | The type of security issues on which the rule applies. |
  | enabled | boolean | no | Field used to enable or disable the rule. |
  | name | string | yes | Name of the notification rule. |
  | targets | array<string> | yes | List of recipients to notify when a notification rule is triggered. |
  | time_aggregation | number | no | Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.createVulnerabilityNotificationRule
**Create vulnerability notification rule** — Create a new notification rule for security vulnerabilities and return the created rule.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | The query is composed of one or several key:value pairs, which can be used to filter security issues on tags and attributes. |
  | rule_types | array<string> | no | Security rule types used as filters in security rules. |
  | severities | array<string> | no | The security rules severities to consider. |
  | trigger_source | string | yes | The type of security issues on which the rule applies. |
  | enabled | boolean | no | Field used to enable or disable the rule. |
  | name | string | yes | Name of the notification rule. |
  | targets | array<string> | yes | List of recipients to notify when a notification rule is triggered. |
  | time_aggregation | number | no | Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.deleteSecurityFilter
**Delete security filter** — Delete a specific security filter.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | security_filter_id | string | yes | The ID of the security filter. |


## com.datadoghq.dd.securitymonitoring.deleteSecurityMonitoringRule
**Delete security monitoring rule** — Delete an existing rule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | rule_id | string | yes | The ID of the rule. |


## com.datadoghq.dd.securitymonitoring.deleteSecurityMonitoringSuppression
**Delete security monitoring suppression** — Delete a specific suppression rule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | suppression_id | string | yes | The ID of the suppression rule. |


## com.datadoghq.dd.securitymonitoring.deleteSignalNotificationRule
**Delete signal notification rule** — Delete a notification rule for security signals.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the notification rule. |


## com.datadoghq.dd.securitymonitoring.deleteVulnerabilityNotificationRule
**Delete vulnerability notification rule** — Delete a notification rule for security vulnerabilities.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the notification rule. |


## com.datadoghq.dd.securitymonitoring.detachCase
**Detach security findings from their case** — Detach security findings from their case.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | finding_ids | array<string> | yes | The unique identifiers of the security findings. |


## com.datadoghq.dd.securitymonitoring.editSecurityMonitoringSignalAssignee
**Edit security monitoring signal assignee** — Modify the triage assignee of a security signal.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signal_id | string | yes | The ID of the signal. |
  | handle | string | no | The handle for this user account. |
  | icon | string | no | Gravatar icon associated to the user. |
  | id | number | no | Numerical ID assigned by Datadog to this user account. |
  | name | string | no | The name for this user account. |
  | uuid | string | yes | UUID assigned by Datadog to this user account. |
  | version | number | no | Version of the updated signal. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data containing the updated triage attributes of the signal. |


## com.datadoghq.dd.securitymonitoring.editSecurityMonitoringSignalIncidents
**Edit security monitoring signal incidents** — Change the related incidents for a security signal.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | signal_id | string | yes | The ID of the signal. |
  | incident_ids | array<number> | yes | Array of incidents that are associated with this signal. |
  | version | number | no | Version of the updated signal. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data containing the updated triage attributes of the signal. |


## com.datadoghq.dd.securitymonitoring.getSBOM
**Get SBOM** — Get a single SBOM related to an asset by its type and name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | asset_type | string | yes | The type of the asset for the SBOM request. |
  | filter_asset_name | string | yes | The name of the asset for the SBOM request. |
  | filter_repo_digest | string | no | The container image `repo_digest` for the SBOM request. |
  | ext_format | string | no | The standard of the SBOM. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A single SBOM. |


## com.datadoghq.dd.securitymonitoring.getSecurityFilter
**Get security filter** — Get the details of a specific security filter.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | security_filter_id | string | yes | The ID of the security filter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The security filter's properties. |
  | meta | object | Optional metadata associated to the response. |


## com.datadoghq.dd.securitymonitoring.getSecurityMonitoringSuppression
**Get security monitoring suppression** — Get the details of a specific suppression rule.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | suppression_id | string | yes | The ID of the suppression rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The suppression rule's properties. |


## com.datadoghq.dd.securitymonitoring.getSignalNotificationRule
**Get signal notification rule** — Get the details of a notification rule for security signals.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the notification rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.getSignalNotificationRules
**Get signal notification rules** — Returns the list of notification rules for security signals.
- Stability: stable
- Access: read

## com.datadoghq.dd.securitymonitoring.getVulnerabilityNotificationRule
**Get vulnerability notification rule** — Get the details of a notification rule for security vulnerabilities.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | ID of the notification rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.getVulnerabilityNotificationRules
**Get vulnerability notification rules** — Returns the list of notification rules for security vulnerabilities.
- Stability: stable
- Access: read

## com.datadoghq.dd.securitymonitoring.listSecurityFilters
**List security filters** — Get the list of configured security filters with their definitions.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of security filters objects. |
  | meta | object | Optional metadata associated to the response. |


## com.datadoghq.dd.securitymonitoring.listSecurityMonitoringSignals
**List security monitoring signals** — List security monitoring signals matching a certain query and other filters.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_query | string | no | The search query for security signals. |
  | time_range | any | no | The time range for which to search security signals. |
  | sort | string | no | The order of the security signals in results. |
  | page_cursor | ['string', 'null'] | no | A list of results using the cursor provided in the previous query. |
  | page_limit | number | no | The maximum number of security signals in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of security signals matching the request. |
  | links | object | Links attributes. |
  | meta | object | Meta attributes. |


## com.datadoghq.dd.securitymonitoring.listSecurityMonitoringSuppressions
**List security monitoring suppressions** — Get the list of all suppression rules.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | Query string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of suppressions objects. |


## com.datadoghq.dd.securitymonitoring.patchSignalNotificationRule
**Patch signal notification rule** — Partially update the notification rule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | The ID of a notification rule. |
  | enabled | boolean | no | Field used to enable or disable the rule. |
  | name | string | no | Name of the notification rule. |
  | selectors | object | no | Selectors are used to filter security issues for which notifications should be generated. |
  | targets | array<string> | no | List of recipients to notify when a notification rule is triggered. |
  | time_aggregation | number | no | Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation. |
  | version | number | no | Version of the notification rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.patchVulnerabilityNotificationRule
**Patch vulnerability notification rule** — Partially update the notification rule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | id | string | yes | The ID of a notification rule. |
  | enabled | boolean | no | Field used to enable or disable the rule. |
  | name | string | no | Name of the notification rule. |
  | selectors | object | no | Selectors are used to filter security issues for which notifications should be generated. |
  | targets | array<string> | no | List of recipients to notify when a notification rule is triggered. |
  | time_aggregation | number | no | Time aggregation period (in seconds) is used to aggregate the results of the notification rule evaluation. |
  | version | number | no | Version of the notification rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Notification rules allow full control over notifications generated by the various Datadog security products. |


## com.datadoghq.dd.securitymonitoring.searchSecurityMonitoringSignals
**Search security monitoring signals** — Returns security signals that match a search query.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Timestamp range for requested signals. |
  | query | string | no | Search query for listing security signals. |
  | cursor | string | no | A list of results using the cursor provided in the previous query. |
  | limit | number | no | The maximum number of security signals in the response. |
  | sort | string | no | The sort parameters used for querying security signals. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of security signals matching the request. |
  | links | object | Links attributes. |
  | meta | object | Meta attributes. |


## com.datadoghq.dd.securitymonitoring.testSecurityMonitoringRule
**Test security monitoring rule** — Test a rule.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | rule | object | no | Test a rule. |
  | ruleQueryPayloads | array<object> | no | Data payloads used to test rules query with the expected result. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | results | array<boolean> | Assert results are returned in the same order as the rule query payloads. |


## com.datadoghq.dd.securitymonitoring.updateSecurityMonitoringSuppression
**Update security monitoring suppression** — Update a specific suppression rule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | expiration_date | any | no | A Unix millisecond timestamp giving an expiration date for the suppression rule. After this date, it won't suppress signals anymore. If unset, the expiration date of the suppression rule is left un... |
  | start_date | any | no | A Unix millisecond timestamp giving the start date for the suppression rule. |
  | suppression_id | string | yes | The ID of the suppression rule. |
  | data_exclusion_query | string | no | An exclusion query on the input data of the security rules, which could be logs, Agent events, or other types of data based on the security rule. |
  | description | string | no | A description for the suppression rule. |
  | enabled | boolean | no | Whether the suppression rule is enabled. |
  | name | string | no | The name of the suppression rule. |
  | rule_query | string | no | The rule query of the suppression rule, with the same syntax as the search bar for detection rules. |
  | suppression_query | string | no | The suppression query of the suppression rule. |
  | tags | array<string> | no | List of tags associated with the suppression rule. |
  | version | number | no | The current version of the suppression. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The suppression rule's properties. |

