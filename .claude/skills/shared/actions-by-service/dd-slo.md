# Datadog Service Level Objectives Actions
Bundle: `com.datadoghq.dd.slo` | 15 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eslo)

## com.datadoghq.dd.slo.checkCanDeleteSLO
**Check can delete SLO** — Check if an SLO can be safely deleted.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | ids | string | yes | A comma separated list of the IDs of the service level objectives objects. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | An array of service level objective objects. |
  | errors | object | A mapping of SLO id to it's current usages. |


## com.datadoghq.dd.slo.createMetricTypeSlo
**Create metric-based SLO** — Create a service level objective based on a metric.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | numeratorQuery | string | yes | A Datadog metric query for good events. |
  | denominatorQuery | string | yes | A Datadog metric query for total (valid) events. |
  | name | string | yes | The name of the service level objective object. |
  | description | string | no | The description of the service level objective. |
  | tags | array<string> | no | A list of tags associated with the service level objective. |
  | target_threshold | number | yes | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met. |
  | warning_threshold | number | no | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. Th... |
  | timeframe | string | yes | The SLO time window options. Allowed values: 7d,30d,90d |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | slo | object | The metric-based service level objective object that has been created. |


## com.datadoghq.dd.slo.createMonitorTypeSlo
**Create monitor-based SLO** — Create a service level objective based on a set of monitors.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | monitor_ids | array<number> | yes | A list of monitor IDs that defines the scope of a monitor service level objective. |
  | groups | array<string> | no | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective. It may only be used when the length of the monitor_ids field is one. |
  | name | string | yes | The name of the service level objective object. |
  | description | string | no | The description of the service level objective. |
  | tags | array<string> | no | A list of tags associated with the service level objective. |
  | target_threshold | number | yes | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met. |
  | warning_threshold | number | no | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. Th... |
  | timeframe | string | yes | The SLO time window options. Allowed values: 7d,30d,90d |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | slo | object | The monitor-based service level objective object that has been created. |


## com.datadoghq.dd.slo.createSLO
**Create SLO** — Create a service level objective object.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | description | string | no | A user-defined description of the service level objective. |
  | groups | array<string> | no | A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective. |
  | monitor_ids | array<number> | no | A list of monitor IDs that defines the scope of a monitor service level objective. |
  | name | string | yes | The name of the service level objective object. |
  | query | object | no | A metric-based SLO. |
  | sli_specification | object | no | A generic SLI specification. |
  | tags | array<string> | no | A list of tags associated with this service level objective. |
  | target_threshold | number | no | The target threshold such that when the service level indicator is above this threshold over the given timeframe, the objective is being met. |
  | thresholds | array<object> | yes | The thresholds (timeframes and associated targets) for this service level objective object. |
  | timeframe | string | no | The SLO time window options. |
  | type | string | yes | The type of the service level objective. |
  | warning_threshold | number | no | The optional warning threshold such that when the service level indicator is below this value for the given threshold, but above the target threshold, the objective appears in a "warning" state. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An array of service level objective objects. |
  | errors | array<string> | An array of error messages. |
  | metadata | object | The metadata object containing additional information about the list of SLOs. |


## com.datadoghq.dd.slo.createSLOCorrection
**Create SLO correction** — Create an SLO Correction.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | yes | Time range of the correction. |
  | category | string | yes | Category the SLO correction belongs to. |
  | description | string | no | Description of the correction being made. |
  | duration | number | no | Length of time (in seconds) for a specified `rrule` recurring SLO correction. |
  | rrule | string | no | The recurrence rules as defined in the iCalendar RFC 5545. |
  | slo_id | string | yes | ID of the SLO that this correction applies to. |
  | timezone | string | no | The timezone to display in the UI for the correction times (defaults to "UTC"). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The response object of a list of SLO corrections. |


## com.datadoghq.dd.slo.deleteSLO
**Delete SLO** — Permanently delete the specified service level objective object.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | slo_id | string | yes | The ID of the service level objective. |
  | force | string | no | Delete the monitor even if it's referenced by other resources (for example SLO, composite monitor). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<string> | An array containing the ID of the deleted service level objective object. |
  | errors | object | An dictionary containing the ID of the SLO as key and a deletion error as value. |


## com.datadoghq.dd.slo.deleteSLOCorrection
**Delete SLO correction** — Permanently delete the specified SLO correction object.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | slo_correction_id | string | yes | The ID of the SLO correction object. |


## com.datadoghq.dd.slo.getSLO
**Get SLO** — Get a service level objective object.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | slo_id | string | yes | The ID of the service level objective object. |
  | with_configured_alert_ids | boolean | no | Get the IDs of SLO monitors that reference this SLO. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A service level objective object includes a service level indicator, thresholds for one or more timeframes, and metadata (`name`, `description`, `tags`, etc.). |
  | errors | array<string> | An array of error messages. |


## com.datadoghq.dd.slo.getSLOCorrection
**Get SLO correction** — Get an SLO correction.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | slo_correction_id | string | yes | The ID of the SLO correction object. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The response object of a list of SLO corrections. |


## com.datadoghq.dd.slo.getSLOCorrections
**Get SLO corrections** — Get corrections applied to an SLO.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | slo_id | string | yes | The ID of the service level objective object. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list of SLO corrections objects. |
  | meta | object | Object describing meta attributes of response. |


## com.datadoghq.dd.slo.getSLOHistory
**Get SLO history** — Get a specific SLO’s history, regardless of its SLO type.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | yes | Query window for requested SLO history. |
  | slo_id | string | yes | The ID of the service level objective object. |
  | target | number | no | The SLO target. |
  | apply_correction | boolean | no | Defaults to `true`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | An array of service level objective objects. |
  | errors | array<object> | A list of errors while querying the history data for the service level objective. |


## com.datadoghq.dd.slo.getSLOReportJobStatus
**Get SLO report job status** — Get the status of the SLO report job.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | report_id | string | yes | The ID of the report job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The data portion of the SLO report status response. |


## com.datadoghq.dd.slo.listSLOCorrection
**List SLO corrections** — Get all Service Level Objective corrections.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | offset | number | no | The specific offset to use as the beginning of the returned response. |
  | limit | number | no | The number of SLO corrections to return in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | The list of SLO corrections objects. |
  | meta | object | Object describing meta attributes of response. |


## com.datadoghq.dd.slo.searchSLO
**Search SLO** — Get a list of service level objective objects for your organization.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | query | string | no | The query string to filter results based on SLO names. |
  | page_size | number | no | The number of files to return in the response `[default=10]`. |
  | page_number | number | no | The identifier of the first page to return. |
  | include_facets | boolean | no | Whether or not to return facet information in the response `[default=false]`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Data from search SLO response. |
  | links | object | Pagination links. |
  | meta | object | Searches metadata returned by the API. |


## com.datadoghq.dd.slo.updateSLOCorrection
**Update SLO correction** — Update the specified SLO correction object.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | timeframe | any | no | Time range of the correction. |
  | slo_correction_id | string | yes | The ID of the SLO correction object. |
  | category | string | no | Category the SLO correction belongs to. |
  | description | string | no | Description of the correction being made. |
  | duration | number | no | Length of time (in seconds) for a specified `rrule` recurring SLO correction. |
  | rrule | string | no | The recurrence rules as defined in the iCalendar RFC 5545. |
  | timezone | string | no | The timezone to display in the UI for the correction times (defaults to "UTC"). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The response object of a list of SLO corrections. |

