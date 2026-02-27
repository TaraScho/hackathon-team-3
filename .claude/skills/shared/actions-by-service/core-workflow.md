# Datadog Core Actions
Bundle: `com.datadoghq.core` | 12 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Ecore)

## com.datadoghq.core.break
**Break** — Break out of the current loop in your workflow.
- Stability: stable
- Access: read

## com.datadoghq.core.echo
**Echo** — Echo the input value. This action will replace any template expression.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | value | any | yes | The value to echo. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | value | any | The echoed value. |


## com.datadoghq.core.error
**Error** — This action always fails.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | message | string | no |  |


## com.datadoghq.core.forLoop
**For loop** — Iterate over a list of items. Each iteration's index and value are available through the Current variable.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes |  |
  | startStepNames | array<string> | yes |  |
  | parentExecContext | string | yes |  |
  | inputList | array<any> | yes | Inputs to pass to the loop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | updatedVariables | object |  |


## com.datadoghq.core.getDate
**Get date** — Get the current date with the specified format.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timezone | string | no |  |
  | format | string | no | The format of the date to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | date | ['string', 'number'] |  |


## com.datadoghq.core.if
**If condition** — Advance to the `true` branch if the expression evaluates to `true`. Otherwise, advances to the `false` branch.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | conditions | array<object> | yes |  |
  | joinOperator | string | yes |  |


## com.datadoghq.core.noop
**No op** — This action does nothing and can be used as a label in your Workflow.
- Stability: stable
- Access: read

## com.datadoghq.core.setVariable
**Set or update variable** — Set or update a variable to a specific value. You can access this variable in your workflow with {{ Variables.variableName }}.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | variableName | string | yes | Variable names must be strings with alphanumeric characters and underscores and must start with a letter. |
  | variableValue | any | yes | The value of the specified variable. |


## com.datadoghq.core.setVariables
**Set or update variables** — Set or update multiple variables to specific values. You can access these variables in your workflow with {{ Variables.variableName }}.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | variables | array<object> | yes | Array of variables to set in the format `{ name: string, value: unknown }`. |


## com.datadoghq.core.sleep
**Sleep** — Wait for the specified duration.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | durationSeconds | number | yes | Select a duration in the dropdown or enter a value in seconds. |


## com.datadoghq.core.switch
**Switch statement** — Branches the workflow based on the switch expression. The branch of the first condition that evaluates to true is taken. If none of the conditions match, the "default" branch is taken.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | switchExpression | any | yes | The value compared against each case. |
  | cases | array<object> | no | A list of cases (possible conditions) compared against the Switch expression. Advance to the first branch for the case that evaluates to true. Otherwise, advances to the `default` branch. |


## com.datadoghq.core.whileLoop
**While loop** — Loop until the conditions evaluate to true. Each iteration's index is available through the Current variable.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | conditions | array<object> | yes |  |
  | joinOperator | string | yes |  |

