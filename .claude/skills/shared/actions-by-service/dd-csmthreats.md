# Datadog CSM Threats Actions
Bundle: `com.datadoghq.dd.csmthreats` | 10 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecsmthreats)

## com.datadoghq.dd.csmthreats.createCSMThreatsAgentRule
**Create CSM threats Agent rule** — Create a new Workload Protection agent rule with the given parameters.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | actions | array<object> | no | The array of actions the rule can perform if triggered. |
  | blocking | array<string> | no | The blocking policies that the rule belongs to. |
  | description | string | no | The description of the Agent rule. |
  | disabled | array<string> | no | The disabled policies that the rule belongs to. |
  | enabled | boolean | no | Whether the Agent rule is enabled. |
  | expression | string | yes | The SECL expression of the Agent rule. |
  | filters | array<string> | no | The platforms the Agent rule is supported on. |
  | monitoring | array<string> | no | The monitoring policies that the rule belongs to. |
  | name | string | yes | The name of the Agent rule. |
  | policy_id | string | no | The ID of the policy where the Agent rule is saved. |
  | product_tags | array<string> | no | The list of product tags associated with the rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |


## com.datadoghq.dd.csmthreats.createCWSAgentRule
**Create CWS Agent rule** — Create a new agent rule with the given parameters.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | actions | array<object> | no | The array of actions the rule can perform if triggered. |
  | blocking | array<string> | no | The blocking policies that the rule belongs to. |
  | description | string | no | The description of the Agent rule. |
  | disabled | array<string> | no | The disabled policies that the rule belongs to. |
  | enabled | boolean | no | Whether the Agent rule is enabled. |
  | expression | string | yes | The SECL expression of the Agent rule. |
  | filters | array<string> | no | The platforms the Agent rule is supported on. |
  | monitoring | array<string> | no | The monitoring policies that the rule belongs to. |
  | name | string | yes | The name of the Agent rule. |
  | policy_id | string | no | The ID of the policy where the Agent rule is saved. |
  | product_tags | array<string> | no | The list of product tags associated with the rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |


## com.datadoghq.dd.csmthreats.deleteCSMThreatsAgentRule
**Delete CSM threats Agent rule** — Delete a specific Workload Protection agent rule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |
  | policy_id | string | no | The ID of the Agent policy. |


## com.datadoghq.dd.csmthreats.deleteCWSAgentRule
**Delete CWS Agent rule** — Delete a specific agent rule.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |


## com.datadoghq.dd.csmthreats.getCSMThreatsAgentRule
**Get CSM threats Agent rule** — Get the details of a specific Workload Protection agent rule.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |
  | policy_id | string | no | The ID of the Agent policy. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |


## com.datadoghq.dd.csmthreats.getCWSAgentRule
**Get CWS Agent rule** — Get the details of a specific agent rule.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |


## com.datadoghq.dd.csmthreats.listCSMThreatsAgentRules
**List CSM threats Agent rules** — Get the list of Workload Protection agent rules.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policy_id | string | no | The ID of the Agent policy. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of Agent rules objects. |


## com.datadoghq.dd.csmthreats.listCWSAgentRules
**List CWS Agent rules** — Get the list of agent rules.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | A list of Agent rules objects. |


## com.datadoghq.dd.csmthreats.updateCSMThreatsAgentRule
**Update CSM threats Agent rule** — Update a specific Workload Protection Agent rule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |
  | policy_id | string | no | The ID of the policy where the Agent rule is saved. |
  | actions | array<object> | no | The array of actions the rule can perform if triggered. |
  | blocking | array<string> | no | The blocking policies that the rule belongs to. |
  | description | string | no | The description of the Agent rule. |
  | disabled | array<string> | no | The disabled policies that the rule belongs to. |
  | enabled | boolean | no | Whether the Agent rule is enabled. |
  | expression | string | no | The SECL expression of the Agent rule. |
  | monitoring | array<string> | no | The monitoring policies that the rule belongs to. |
  | product_tags | array<string> | no | The list of product tags associated with the rule. |
  | id | string | no | The ID of the Agent rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |


## com.datadoghq.dd.csmthreats.updateCWSAgentRule
**Update CWS Agent rule** — Update a specific agent rule.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | agent_rule_id | string | yes | The ID of the Agent rule. |
  | actions | array<object> | no | The array of actions the rule can perform if triggered. |
  | blocking | array<string> | no | The blocking policies that the rule belongs to. |
  | description | string | no | The description of the Agent rule. |
  | disabled | array<string> | no | The disabled policies that the rule belongs to. |
  | enabled | boolean | no | Whether the Agent rule is enabled. |
  | expression | string | no | The SECL expression of the Agent rule. |
  | monitoring | array<string> | no | The monitoring policies that the rule belongs to. |
  | policy_id | string | no | The ID of the policy where the Agent rule is saved. |
  | product_tags | array<string> | no | The list of product tags associated with the rule. |
  | id | string | no | The ID of the Agent rule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single Agent rule. |

