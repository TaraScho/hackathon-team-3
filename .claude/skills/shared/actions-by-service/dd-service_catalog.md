# Datadog Service Catalog Actions
Bundle: `com.datadoghq.dd.service_catalog` | 10 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eservice_catalog)

## com.datadoghq.dd.service_catalog.getScores
**Get scores** — Get all scores organized by rule, service, or team.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | type | string | yes | The aggregation type of the score: `rule`, `service`, or `team`. |
  | tags | array<string> | no | Filter scores by service or rule tags. |
  | ordering | string | no | Order scores in ascending or descending order. |
  | limit | number | no | Limit the number of results returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | scores | array<object> | Aggregated scores. |
  | url | string | URL to the Scorecard page. |


## com.datadoghq.dd.service_catalog.getServiceDefinition
**Get service definition** — Get a single service definition from the Datadog Service Catalog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service | string | yes | The name of the service. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Service definition data. |


## com.datadoghq.dd.service_catalog.getServiceDependencies
**Get service dependencies** — Get a specific service’s immediate upstream and downstream services. The services retrieved are filtered by environment and a primary tag, if one is defined.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service | string | yes | The name of the service to get dependencies for. |
  | env | string | yes | Specify what APM environment to query service dependencies by. |
  | primary_tag | string | no | Specify what primary tag to query service dependencies by. |
  | time | any | no | The timeframe to query for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string |  |
  | name | string | Name of the APM service being searched for. |
  | calls | array<string> | List of service names called by the given service. |
  | called_by | array<string> | List of service names that call the given service. |


## com.datadoghq.dd.service_catalog.getServicePagerdutyOncall
**Get service pagerduty oncall** — Get the service pagerduty oncall information.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | service | string | yes | The name of the service. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Service pagerduty oncall information. |


## com.datadoghq.dd.service_catalog.listScorecardOutcomes
**List scorecard outcomes** — Fetches all rule outcomes.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |
  | include | string | no | Include related rule details in the response. |
  | fields_outcome | string | no | Return only specified values in the outcome attributes. |
  | fields_rule | string | no | Return only specified values in the included rule details. |
  | filter_outcome_service_name | string | no | Filter the outcomes on a specific service name. |
  | filter_outcome_state | string | no | Filter the outcomes by a specific state. |
  | filter_rule_enabled | boolean | no | Filter outcomes on whether a rule is enabled/disabled. |
  | filter_rule_id | string | no | Filter outcomes based on rule ID. |
  | filter_rule_name | string | no | Filter outcomes based on rule name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of rule outcomes. |
  | included | array<object> | Array of rule details. |
  | links | object | Links attributes. |


## com.datadoghq.dd.service_catalog.listScorecardRules
**List scorecard rules** — Fetch all rules.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_offset | number | no | Specific offset to use as the beginning of the returned page. |
  | include | string | no | Include related scorecard details in the response. |
  | filter_rule_id | string | no | Filter the rules on a rule ID. |
  | filter_rule_enabled | boolean | no | Filter for enabled rules only. |
  | filter_rule_custom | boolean | no | Filter for custom rules only. |
  | filter_rule_name | string | no | Filter rules on the rule name. |
  | filter_rule_description | string | no | Filter rules on the rule description. |
  | fields_rule | string | no | Return only specific fields in the response for rule attributes. |
  | fields_scorecard | string | no | Return only specific fields in the included response for scorecard attributes. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of rule details. |
  | links | object | Links attributes. |


## com.datadoghq.dd.service_catalog.listServiceDefinitions
**List service definitions** — Get a list of all service definitions from the Datadog Service Catalog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | limit | number | no | The maximum number of service definitions in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of service definitions data. |


## com.datadoghq.dd.service_catalog.listServiceDefinitionsV2
**List service definitions** — Get a list of all service definitions from the Datadog Service Catalog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | schema_version | string | no | The schema version desired in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Data representing service definitions. |


## com.datadoghq.dd.service_catalog.updateScorecardOutcomesAsync
**Update scorecard outcomes async** — Updates multiple scorecard rule outcomes in a single batched request.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | results | array<object> | no | Set of scorecard outcomes to update asynchronously. |


## com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome
**Update scorecard rule outcome** — Update scorecard rule outcome for a single service.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scorecardRuleId | string | yes | Scorecard rule to update outcomes for. |
  | serviceName | string | yes | Service name to update outcomes for. |
  | state | string | yes | Outcome state for the service and rule. |
  | remarks | string | no | Remarks to be associated with the outcome. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | total_outcomes | number | Total count of outcomes. |
  | total_updated | number | Total count of outcomes updated. |

