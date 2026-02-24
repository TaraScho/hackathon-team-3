# Datadog Metrics Actions
Bundle: `com.datadoghq.dd.metrics` | 21 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Emetrics)

## com.datadoghq.dd.metrics.createBulkTagsMetricsConfiguration
**Create bulk tags metrics configuration** — Create and define a list of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | emails | array<string> | no | A list of account emails to notify when the configuration is applied. |
  | exclude_tags_mode | boolean | no | When set to true, the configuration will exclude the configured tags and include any other submitted tags. |
  | include_actively_queried_tags_window | number | no | When provided, all tags that have been actively queried are configured (and, therefore, remain queryable) for each metric that matches the given prefix. |
  | override_existing_configurations | boolean | no | When set to true, the configuration overrides any existing configurations for the given metric with the new set of tags in this configuration request. |
  | tags | array<string> | no | A list of tag names to apply to the configuration. |
  | id | string | yes | A text prefix to match against metric names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The status of a request to bulk configure metric tags. |


## com.datadoghq.dd.metrics.createTagConfiguration
**Create tag configuration** — Create and define a list of queryable tag keys for an existing metric.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metricName | string | yes | The name of the metric. |
  | metricType | string | yes | The metric's type. |
  | tags | array<string> | no | A list of tag keys that will be queryable for your metric. |
  | aggregations | array<object> | no | A list of queryable aggregation combinations for a count, rate, or gauge metric. By default, count and rate metrics require the (time: sum, space: sum) aggregation and Gauge metrics require the (ti... |
  | includePercentiles | boolean | no | Toggle to include/exclude percentiles for a distribution metric. Can only be applied to metrics that have a metric type of 'distribution'. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | attributes | object |  |
  | id | string |  |
  | type | string |  |


## com.datadoghq.dd.metrics.deleteBulkTagsMetricsConfiguration
**Delete bulk tags metrics configuration** — Delete all custom lists of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | emails | array<string> | no | A list of account emails to notify when the configuration is applied. |
  | id | string | yes | A text prefix to match against metric names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The status of a request to bulk configure metric tags. |


## com.datadoghq.dd.metrics.deleteTagConfiguration
**Delete tag configuration** — Deletes a metric's tag configuration.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the metric. |


## com.datadoghq.dd.metrics.estimateMetricsOutputSeries
**Estimate metrics output series** — Returns the estimated cardinality for a metric with a given tag, percentile, and number of aggregations configuration using Metrics without Limits&trade;.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the metric. |
  | filter_groups | string | no | Filtered tag keys that the metric is configured to query with. |
  | filter_hours_ago | number | no | The number of hours of look back (from now) to estimate cardinality with. |
  | filter_num_aggregations | number | no | Deprecated. |
  | filter_pct | boolean | no | A boolean, for distribution metrics only, to estimate cardinality if the metric includes additional percentile aggregators. |
  | filter_timespan_h | number | no | A window, in hours, from the look back to estimate cardinality with. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a metric cardinality estimate. |


## com.datadoghq.dd.metrics.getMetricMetadata
**Get metric metadata** — Get metadata about a specific metric.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | Name of the metric for which to get metadata. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | type | string | Metric type such as `gauge` or `rate`. |
  | description | string | Metric description. |
  | short_name | string | A more human-readable and abbreviated version of the metric name. |
  | integration | string | Name of the integration that sent the metric if applicable. |
  | statsd_interval | number | StatsD flush interval of the metric in seconds if applicable. |
  | unit | string | Primary unit of the metric such as `byte` or `operation`. |
  | per_unit | string | Per unit of the metric such as `second` in `bytes per second`. |
  | url | string | The URL of the metric. |


## com.datadoghq.dd.metrics.getTagConfiguration
**Get tag configuration** — Get the tag configuration for the given metric name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metricName | string | yes | The name of the metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | metricTagConfiguration | object |  |


## com.datadoghq.dd.metrics.listActiveMetrics
**List active metrics** — Get the list of actively reporting metrics from a given time until now.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | string | yes | The queried time period range |
  | host | string | no | Hostname for filtering the list of metrics returned. |
  | tag_filter | string | no | Filter metrics that have been submitted with the given tags. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | metrics | array<string> | List of metric names. |
  | from | string | Time when the metrics were active, seconds since the Unix epoch. |


## com.datadoghq.dd.metrics.listActiveTagsAndAggregations
**List active tags and aggregations** — List tags and aggregations that are actively queried on
dashboards and monitors for a given metric name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metricName | string | yes | The name of the metric. |
  | window | number | no | The number of seconds of look back (from now). Default value is 604,800 (1 week), minimum value is 7200 (2 hours), maximum value is 2,630,000 (1 month). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | activeTags | array<string> |  |
  | activeAggregations | array<object> | List of aggregation combinations that have been actively queried. |


## com.datadoghq.dd.metrics.listMetricAssets
**List metric assets** — Returns dashboards, monitors, notebooks, and SLOs that a metric is stored in, if any.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Metric assets response data. |
  | included | array<object> | Array of objects related to the metric assets. |


## com.datadoghq.dd.metrics.listMetrics
**Search metrics** — Search for metrics from the last 24 hours in Datadog.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | q | string | yes | Query string to search metrics upon. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | results | object | Search result. |


## com.datadoghq.dd.metrics.listTagConfigurationByName
**List tag configuration by name** — Returns the tag configuration for the given metric name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Object for a single metric tag configuration. |


## com.datadoghq.dd.metrics.listTagConfigurations
**List tag configurations** — Returns all metrics that can be configured in the Metrics Summary page or with Metrics without Limits™ (matching additional filters if specified).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | filter_configured | boolean | no | Filter custom metrics that have configured tags. |
  | filter_tags_configured | string | no | Filter tag configurations by configured tags. |
  | filter_metric_type | string | no | Filter metrics by metric type. |
  | filter_include_percentiles | boolean | no | Filter distributions with additional percentile aggregations enabled or disabled. |
  | filter_queried | boolean | no | (Preview) Filter custom metrics that have or have not been queried in the specified window[seconds]. |
  | filter_tags | string | no | Filter metrics that have been submitted with the given tags. |
  | filter_related_assets | boolean | no | (Preview) Filter metrics that are used in dashboards, monitors, notebooks, SLOs. |
  | window_seconds | number | no | The number of seconds of look back (from now) to apply to a filter[tag] or filter[queried] query. |
  | page_size | number | no | Maximum number of results returned. |
  | page_cursor | ['string', 'null'] | no | String to query the next page of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of metrics and metric tag configurations. |
  | links | object | Pagination links. |
  | meta | object | Response metadata object. |


## com.datadoghq.dd.metrics.listTagsByMetricName
**List tags by metric name** — View indexed tag key-value pairs for a given metric name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metricName | string | yes | The name of the metric to list tags for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tags | array<string> | List of indexed tag value pairs. |


## com.datadoghq.dd.metrics.listVolumesByMetricName
**List volumes by metric name** — View distinct metrics volumes for the given metric name.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the metric. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | any | Possible response objects for a metric's volume. |


## com.datadoghq.dd.metrics.queryMetrics
**Get timeseries points** — Query timeseries points for a given metric.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | time | any | yes | The queried time period range |
  | query | string | yes | Query string. |
  | limit | number | no | Maximum number of time series points to return **from the beginning of the time range**. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | status | string | Status of the query. |
  | res_type | string | Type of response. |
  | series | array<object> | List of timeseries queried. |
  | to_date | number | End of requested time window, milliseconds since Unix epoch. |
  | from_date | number | Start of requested time window, milliseconds since Unix epoch. |
  | group_by | array<string> | List of tag keys on which to group. |
  | query | string | Query string. |
  | message | string | Message indicating `success` if status is `ok`. |
  | error | string | Message indicating the errors if status is not `ok`. |


## com.datadoghq.dd.metrics.queryScalarData
**Query scalar data** — Query scalar values (as seen on Query Value, Table, and Toplist widgets).
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | range | any | yes | Query window in milliseconds. This value is inclusive for start and end. |
  | formulas | array<object> | no | List of formulas to be calculated and returned as responses. |
  | queries | array<object> | yes | List of queries to be run and used as inputs to the formulas. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A message containing the response to a scalar query. |
  | errors | string | An error generated when processing a request. |


## com.datadoghq.dd.metrics.queryTimeseriesData
**Query timeseries data** — Query timeseries data across various data sources and process the data by applying formulas and functions.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | range | any | yes | Query window in milliseconds. This value is inclusive for start and end. |
  | formulas | array<object> | no | List of formulas to be calculated and returned as responses. |
  | interval | number | no | A time interval in milliseconds. |
  | queries | array<object> | yes | List of queries to be run and used as inputs to the formulas. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | A message containing the response to a timeseries query. |
  | errors | string | The error generated by the request. |


## com.datadoghq.dd.metrics.submitMetric
**Submit metric** — The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | The name of the timeseries. |
  | type | string | no | The type of the metric either unspecified, count, rate, and gauge. |
  | interval | number | no | If the type of the metric is rate or count, define the corresponding interval. The rate metric type takes the value and divides it by the length of the time interval. For example, this is useful if... |
  | value | number | yes | The value to be submitted for the metric. |
  | timestamp | number | no | The timestamp should be in seconds and current. Current is defined as not more than 10 minutes in the future or more than 1 hour in the past. |
  | tags | any | no | A list of tags associated with the metric. |
  | unit | string | no | The unit of point value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | errors | array<string> |  |


## com.datadoghq.dd.metrics.updateMetricMetadata
**Update metric metadata** — Edit metadata of a specific metric.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metric_name | string | yes | Name of the metric for which to edit metadata. |
  | description | string | no | Metric description. |
  | integration | string | no | Name of the integration that sent the metric if applicable. |
  | per_unit | string | no | Per unit of the metric such as `second` in `bytes per second`. |
  | short_name | string | no | A more human-readable and abbreviated version of the metric name. |
  | statsd_interval | number | no | StatsD flush interval of the metric in seconds if applicable. |
  | type | string | no | Metric type such as `gauge` or `rate`. |
  | unit | string | no | Primary unit of the metric such as `byte` or `operation`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | type | string | Metric type such as `gauge` or `rate`. |
  | description | string | Metric description. |
  | short_name | string | A more human-readable and abbreviated version of the metric name. |
  | integration | string | Name of the integration that sent the metric if applicable. |
  | statsd_interval | number | StatsD flush interval of the metric in seconds if applicable. |
  | unit | string | Primary unit of the metric such as `byte` or `operation`. |
  | per_unit | string | Per unit of the metric such as `second` in `bytes per second`. |
  | url | string | The URL of the metric. |


## com.datadoghq.dd.metrics.updateTagConfiguration
**Update tag configuration** — Update the tag configuration of a metric.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | metricName | string | yes | The name of the metric. |
  | tags | array<string> | no | A list of tag keys that will be queryable for your metric. |
  | aggregations | array<object> | no | A list of queryable aggregation combinations for a count, rate, or gauge metric. By default, count and rate metrics require the (time: sum, space: sum) aggregation and Gauge metrics require the (ti... |
  | includePercentiles | boolean | no | Toggle to include/exclude percentiles for a distribution metric. Can only be applied to metrics that have a metric type of 'distribution'. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | attributes | object |  |
  | id | string |  |
  | type | string |  |

