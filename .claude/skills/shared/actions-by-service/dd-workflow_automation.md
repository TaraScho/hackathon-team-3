# Datadog Workflow Automation Execute Actions
Bundle: `com.datadoghq.dd.workflow_automation` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eworkflow_automation)

## com.datadoghq.dd.workflow_automation.triggerWorkflow
**Trigger workflow** — Kick-off a child workflow.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes | Name of the workflow that you would like to kick off. |
  | workflowInputs | object | no | Inputs to pass to the sub workflow. |
  | timeoutHours | number | no |  |
  | timeoutSeconds | number | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceId | string |  |
  | workflowId | string |  |
  | workflowOutputs | object |  |
  | workflowUrl | string |  |


## com.datadoghq.dd.workflow_automation.triggerWorkflowAsync
**Trigger workflow** — Kick-off a child workflow. Please specify output parameters on your workflow if you require access to your workflow result.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes | Name of the workflow that you would like to kick off. |
  | workflowInputs | object | no | Inputs to pass to the sub workflow. |
  | timeoutSeconds | number | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceId | string |  |
  | workflowId | string |  |

