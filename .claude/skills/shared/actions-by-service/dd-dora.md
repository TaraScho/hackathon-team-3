# Datadog DORA Metrics Actions
Bundle: `com.datadoghq.dd.dora` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Edora)

## com.datadoghq.dd.dora.createDORADeployment
**Create DORA deployment** — Use this API endpoint to provide data about deployments for DORA metrics.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | custom_tags | array<string> | no | A list of user-defined tags. |
  | env | string | no | Environment name to where the service was deployed. |
  | finished_at | number | yes | Unix timestamp when the deployment finished. |
  | git | object | no | Git info for DORA Metrics events. |
  | id | string | no | Deployment ID. |
  | service | string | yes | Service name. |
  | started_at | number | yes | Unix timestamp when the deployment started. |
  | team | string | no | Name of the team owning the deployed service. |
  | version | string | no | Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The JSON:API data. |


## com.datadoghq.dd.dora.createDORAFailure
**Create DORA failure** — Use this API endpoint to provide failure data for DORA metrics.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | custom_tags | array<string> | no | A list of user-defined tags. |
  | env | string | no | Environment name that was impacted by the failure. |
  | finished_at | number | no | Unix timestamp when the failure finished. |
  | git | object | no | Git info for DORA Metrics events. |
  | id | string | no | Failure ID. |
  | name | string | no | Failure name. |
  | services | array<string> | no | Service names impacted by the failure. |
  | severity | string | no | Failure severity. |
  | started_at | number | yes | Unix timestamp when the failure started. |
  | team | string | no | Name of the team owning the services impacted. |
  | version | string | no | Version to correlate with [APM Deployment Tracking](https://docs.datadoghq.com/tracing/services/deployment_tracking/). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Response after receiving a DORA failure event. |


## com.datadoghq.dd.dora.getDORADeployment
**Get DORA deployment** — Use this API endpoint to get a deployment event.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | deployment_id | string | yes | The ID of the deployment event. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A DORA event. |


## com.datadoghq.dd.dora.getDORAFailure
**Get DORA failure** — Use this API endpoint to get a failure event.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | failure_id | string | yes | The ID of the failure event. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A DORA event. |


## com.datadoghq.dd.dora.listDORADeployments
**List DORA deployments** — Use this API endpoint to get a list of deployment events.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Only include deployments created between the specified date range. |
  | limit | number | no | Maximum number of events in the response. |
  | query | string | no | Search query with event platform syntax. |
  | sort | string | no | Sort order (prefixed with `-` for descending). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list of DORA events. |


## com.datadoghq.dd.dora.listDORAFailures
**List DORA failures** — Use this API endpoint to get a list of failure events.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Only include deployments created between the specified date range. |
  | limit | number | no | Maximum number of events in the response. |
  | query | string | no | Search query with event platform syntax. |
  | sort | string | no | Sort order (prefixed with `-` for descending). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list of DORA events. |

