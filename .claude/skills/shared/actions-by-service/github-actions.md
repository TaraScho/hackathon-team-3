# GitHub Actions Actions
Bundle: `com.datadoghq.github.actions` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Egithub%2Eactions)

## com.datadoghq.github.actions.getLatestWorkflowRun
**Get latest workflow run** — Returns the latest execution for a specific github workflow.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes |  |
  | repository | string | yes | The target repository, with the format {owner}/{repo}. |
  | branch | string | no | Filters to only return runs from the specified branch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | run | object |  |


## com.datadoghq.github.actions.getWorkflowRun
**Get github actions workflow run** — Get a specified run of a github actions workflow.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | runId | string | yes |  |
  | repository | string | yes | The target repository, with the format {owner}/{repo}. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | run | object |  |


## com.datadoghq.github.actions.listWorkflowRuns
**List github actions workflow runs** — List runs for a specified github actions workflow.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes |  |
  | repository | string | yes | The target repository, with the format {owner}/{repo}. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | runs | array<object> |  |


## com.datadoghq.github.actions.triggerWorkflowRun
**Trigger github actions workflow run** — Manually trigger a Github Actions workflow run. You must configure your GitHub Actions workflow to run when the workflow_dispatch webhook event occurs.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | workflowId | string | yes |  |
  | repository | string | yes | The target repository, with the format {owner}/{repo}. |
  | ref | string | yes | The git reference for the workflow. The reference can be a branch or tag name. |
  | inputs | object | no | Input keys and values configured in the workflow file. Inputs configured here are validated against the inputs defined in the workflow file. The maximum number of properties is 10. Any default prop... |

