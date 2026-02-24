# Datadog Bits AI SRE Actions
Bundle: `com.datadoghq.dd.bitsai.sre` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ebitsai%2Esre)

## com.datadoghq.dd.bitsai.sre.getInvestigation
**Get investigation** — Retrieves the details of a specific investigation by its ID.
- Stability: beta
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | investigation_id | string | yes | The ID of the investigation to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The details of the investigation. |


## com.datadoghq.dd.bitsai.sre.listInvestigations
**List investigations** — Lists investigations for a given monitor and event.
- Stability: beta
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | number | yes | The ID of the monitor to get the investigation for. |
  | event_id | string | yes | The ID of the event to get the investigation for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | investigations | array<object> | The list of investigations for the given monitor and event. |


## com.datadoghq.dd.bitsai.sre.triggerInvestigation
**Trigger investigation** — Triggers an investigation for a given monitor and event.
- Stability: beta
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_id | number | yes | The ID of the monitor to get the investigation for. |
  | event_id | string | yes | The ID of the event to get the investigation for. |
  | event_ts | number | yes | The timestamp of the event in Unix milliseconds. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | investigation_id | string | The ID of the triggered investigation. |

