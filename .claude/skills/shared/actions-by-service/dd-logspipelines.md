# Datadog Logs Pipelines Actions
Bundle: `com.datadoghq.dd.logspipelines` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Elogspipelines)

## com.datadoghq.dd.logspipelines.deleteLogsPipeline
**Delete logs pipeline** — Delete a given pipeline from your organization.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pipeline_id | string | yes | ID of the pipeline to delete. |


## com.datadoghq.dd.logspipelines.getLogsPipeline
**Get logs pipeline** — Get a specific pipeline from your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pipeline_id | string | yes | ID of the pipeline to get. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | description | string | A description of the pipeline. |
  | filter | object | Filter for logs. |
  | id | string | ID of the pipeline. |
  | is_enabled | boolean | Whether or not the pipeline is enabled. |
  | is_read_only | boolean | Whether or not the pipeline can be edited. |
  | name | string | Name of the pipeline. |
  | processors | array<object> | Ordered list of processors in this pipeline. |
  | tags | array<string> | A list of tags associated with the pipeline. |
  | type | string | Type of pipeline. |


## com.datadoghq.dd.logspipelines.getLogsPipelineOrder
**Get logs pipeline order** — Get the current order of your pipelines.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | pipeline_ids | array<string> | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |


## com.datadoghq.dd.logspipelines.listLogsPipelines
**List logs pipelines** — Get all pipelines from your organization.
- Stability: stable
- Access: read

## com.datadoghq.dd.logspipelines.updateLogsPipelineOrder
**Update logs pipeline order** — Update the order of your pipelines.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pipeline_ids | array<string> | yes | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | pipeline_ids | array<string> | Ordered Array of `<PIPELINE_ID>` strings, the order of pipeline IDs in the array define the overall Pipelines order for Datadog. |

