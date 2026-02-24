# Datadog Synthetics Actions
Bundle: `com.datadoghq.dd.synthetics` | 15 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Esynthetics)

## com.datadoghq.dd.synthetics.getAPITestLatestResults
**List API test results** — Get the last 50 test results summaries for a given Synthetics API test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | no | The time period range for queried results |
  | public_id | string | yes | The ID of the test for which to search results for. |
  | probe_dc | array<string> | no | Locations for which to query results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | last_timestamp_fetched | number | Timestamp of the latest API test run. |
  | results | array<object> | Result of the latest API test run. |


## com.datadoghq.dd.synthetics.getAPITestResult
**Get API test result** — Get a specific full result from a given (API) Synthetic test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | public_id | string | yes | The ID of the API test to which the target result belongs. |
  | result_id | string | yes | The ID of the result to get. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | check_time | number | When the API test was conducted. |
  | check_version | number | Version of the API test used. |
  | probe_dc | string | Locations for which to query the API test results. |
  | result_id | string | ID of the API test result. |
  | status | string | The status of your Synthetic monitor. |
  | check | object | Object describing the API test configuration. |
  | result | object | Object containing results for your Synthetic API test. |


## com.datadoghq.dd.synthetics.getBrowserTestLatestResults
**List browser test results** — Get the last 50 test results summaries for a given Synthetics Browser test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | no | The time period range for queried results |
  | public_id | string | yes | The ID of the browser test for which to search results for. |
  | probe_dc | array<string> | no | Locations for which to query results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | last_timestamp_fetched | number | Timestamp of the latest browser test run. |
  | results | array<object> | Result of the latest browser test run. |


## com.datadoghq.dd.synthetics.getBrowserTestResult
**Get browser test result** — Get a specific full result from a given (browser) Synthetic test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | public_id | string | yes | The ID of the browser test to which the target result belongs. |
  | result_id | string | yes | The ID of the result to get. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | check_time | number | When the browser test was conducted. |
  | check_version | number | Version of the browser test used. |
  | probe_dc | string | Location from which the browser test was performed. |
  | result_id | string | ID of the browser test result. |
  | status | string | The status of your Synthetic monitor. |
  | check | object | Object describing the browser test configuration. |
  | result | object | Object containing results for your Synthetic browser test. |


## com.datadoghq.dd.synthetics.getGlobalVariable
**Get global variable** — Get the detailed configuration of a global variable.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | variable_id | string | yes | The ID of the global variable. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | description | string | Description of the global variable. |
  | id | string | Unique identifier of the global variable. |
  | name | string | Name of the global variable. |
  | tags | array<string> | Tags of the global variable. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | value | object | Value of the global variable. |
  | parse_test_public_id | string | A Synthetic test ID to use as a test to generate the variable value. |
  | parse_test_options | object | Parser options to use for retrieving a Synthetics global variable from a Synthetics Test. |
  | attributes | object | Attributes of the global variable. |


## com.datadoghq.dd.synthetics.getMobileTest
**Get mobile test** — Get the detailed configuration associated with a Synthetic Mobile test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | public_id | string | yes | The public ID of the test to get details from. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | config | object | Configuration object for a Synthetic mobile test. |
  | device_ids | array<string> | Array with the different device IDs used to run the test. |
  | message | string | Notification message associated with the test. |
  | monitor_id | number | The associated monitor ID. |
  | name | string | Name of the test. |
  | options | object | Object describing the extra options for a Synthetic test. |
  | public_id | string | The public ID of the test. |
  | status | string | Define whether you want to start (`live`) or pause (`paused`) a Synthetic test. |
  | steps | array<object> | Array of steps for the test. |
  | tags | array<string> | Array of tags attached to the test. |
  | type | string | Type of the Synthetic test, `mobile`. |


## com.datadoghq.dd.synthetics.getOnDemandConcurrencyCap
**Get on demand concurrency cap** — Get the on-demand concurrency cap.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | On-demand concurrency cap. |


## com.datadoghq.dd.synthetics.getSyntheticsDefaultLocations
**Get synthetics default locations** — Get the default locations settings.
- Stability: stable
- Access: read

## com.datadoghq.dd.synthetics.getTest
**Get test** — Get the detailed configuration associated with a Synthetics test.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | public_id | string | yes | The ID of the test to get details from. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | name | string | Name of the test. |
  | message | string | Notification message associated with the test. |
  | tags | array<string> | Array of tags attached to the test. |
  | tag_value | object | A map of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map of tags where the keys are strings and the values are lists of strings. |
  | locations | array<string> | Array of locations used to run the test. |
  | type | string | Type of the Synthetic test, either `api` or `browser`. |
  | creator | object |  |
  | subtype | string | The subtype of the Synthetic API test, `http`, `ssl`, `tcp`, `dns`, `icmp`, `udp`, `websocket`, `grpc` or `multi`. |
  | public_id | string | The test ID. |
  | config | object | Configuration object for a Synthetic test. |
  | status | string | Define whether you want to start (`live`) or pause (`paused`) a Synthetic test. |
  | steps | array<object> | For browser test, the steps of the test. |
  | options | object | Object describing the extra options for a Synthetic test. |
  | monitor_id | number | The associated monitor ID. |


## com.datadoghq.dd.synthetics.listGlobalVariables
**List global variables** — Get the list of all Synthetics global variables.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | variables | array<object> | Array of Synthetic global variables. |


## com.datadoghq.dd.synthetics.listTests
**List tests** — Get the list of all Synthetic tests.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | limit | number | no | The number of tests to return. Defaults to 50. Max 200. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tests | array<object> | Array of Synthetic tests configuration. |


## com.datadoghq.dd.synthetics.searchTests
**Search tests** — Search for Synthetic tests and Test Suites.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | text | string | no | The search query. |
  | include_full_config | boolean | no | If true, include the full configuration for each test in the response. |
  | search_suites | boolean | no | If true, returns suites instead of tests. |
  | facets_only | boolean | no | If true, return only facets instead of full test details. |
  | start | number | no | The offset from which to start returning results. |
  | count | number | no | The maximum number of results to return. |
  | sort | string | no | The sort order for the results (e.g., `name,asc` or `name,desc`). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tests | array<object> | Array of Synthetic tests configuration. |


## com.datadoghq.dd.synthetics.setOnDemandConcurrencyCap
**Set on demand concurrency cap** — Save new value for on-demand concurrency cap.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | on_demand_concurrency_cap | number | no | Value of the on-demand concurrency cap. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | On-demand concurrency cap. |


## com.datadoghq.dd.synthetics.triggerTests
**Trigger tests** — Trigger a set of Synthetics tests.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | tests | array<object> | yes | Individual synthetics test. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | results | array<object> | Information about the tests runs. |
  | triggered_check_ids | array<string> | The IDs of the Synthetics test triggered. |
  | locations | array<object> | List of Synthetics locations. |
  | batch_id | string | The test ID of the batch triggered. |


## com.datadoghq.dd.synthetics.updateTestPauseStatus
**Update test pause status** — Pause or start a Synthetics test by changing the status.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | public_id | string | yes | The ID of the Synthetic test to update. |
  | new_status | string | yes | Define whether you want to start (`live`) or pause (`paused`) a Synthetic test. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | status | string | Status of the Synthetic test. |
  | updated | boolean | A boolean that indicates if the status was updated or not. |

