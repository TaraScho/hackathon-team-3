# Dashboards Skill — Widget Types Reference

Complete reference of all Datadog dashboard widget types, organized by category. Each widget is identified by its `type` value in the JSON definition. Widgets are placed in `ordered` or `free` layout dashboards and configured via the `definition` object.

---

## Graphs

Visual widgets that plot data over time or across dimensions.

### Timeseries (`timeseries`)
The most common widget. Plots one or more metrics, logs, or APM queries over a time window as lines, bars, or areas. Supports overlaying events and markers.

Key configuration: `requests[].queries[]` for data sources, `display_type` (line, bars, area), `yaxis` scaling (linear, log, pow, sqrt), `markers` for horizontal thresholds, `right_yaxis` for dual-axis charts, `style.palette` for color schemes.

### Top List (`toplist`)
Ranked list of groups sorted by a metric value. Useful for identifying top consumers (e.g., top hosts by CPU, top endpoints by latency).

Key configuration: `requests[].queries[]`, `style.display.type` (stacked, flat), conditional formatting with `conditional_formats[]` for color-coding thresholds.

### Change (`change`)
Shows the change in a metric value between two time periods. Displays absolute and percentage change.

Key configuration: `requests[].change_type` (absolute, percentage), `requests[].compare_to` (hour_before, day_before, week_before, month_before), `requests[].order_by` (change, name, present, past), `requests[].order_dir` (asc, desc).

### Distribution (`distribution`)
Visualizes the statistical distribution of a metric across hosts or tags. Renders as a histogram or density plot.

Key configuration: `requests[].query`, `xaxis` and `yaxis` settings, percentile markers via `markers[]`.

### Heatmap (`heatmap`)
Displays metric values across groups and time as color intensity. Ideal for spotting patterns across many hosts simultaneously.

Key configuration: `requests[].queries[]`, `yaxis` settings, color palette via `style.palette`, `events[]` overlay.

### Geomap (`geomap`)
Plots data on a world map using geographic tags. Requires data tagged with country, region, or coordinate information.

Key configuration: `requests[].queries[]`, `style.palette`, `view.focus` (WORLD, US, EUROPE, ASIA, etc.).

### Treemap (`treemap`)
Hierarchical area chart showing proportions. Each rectangle's size represents the metric value.

Key configuration: `requests[].queries[]`, `requests[].formulas[]`, color grouping.

### Pie Chart (`sunburst`)
Displays proportions as slices of a circle. Can be nested (sunburst) for hierarchical data. JSON type is `sunburst` even for flat pie charts.

Key configuration: `requests[].queries[]`, `requests[].formulas[]`, `legend.type` (automatic, inline, table, none), `hide_total` boolean.

### Funnel (`funnel`)
Visualizes sequential conversion steps. Shows drop-off between stages.

Key configuration: `requests[].queries[]` with RUM or logs data sources, color settings.

### Scatter Plot (`scatterplot`)
Plots two metrics against each other for correlation analysis. Each dot represents a group (e.g., a host).

Key configuration: `requests.x` and `requests.y` for axes, `requests.table` for the data source, `color_by_groups[]` for dimensional coloring.

---

## Groups

Container widgets that organize other widgets.

### Group (`group`)
Groups multiple widgets under a collapsible header. Supports `ordered` or `free` layout within the group. The `banner_img` field adds a header image.

Key configuration: `widgets[]` (nested widget definitions), `layout_type` (ordered), `title`, `background_color`, `show_title` boolean.

### PowerPack (`powerpack`)
Reusable group templates that can be shared across dashboards. Created in the UI and referenced by `powerpack_id`.

Key configuration: `powerpack_id`, `template_variables` for parameterization.

---

## Cloud Cost

### Cloud Cost (`cloud_cost`)
Displays cloud spending data from AWS, Azure, or GCP cost management integrations.

Key configuration: `requests[].queries[]` with `data_source: "cloud_cost"`, `time` settings, grouping by service, account, or tag.

---

## Analytics

Widgets that display aggregated values and tabular data.

### Query Value (`query_value`)
Single large number showing the current value of a metric or formula. Ideal for KPI displays.

Key configuration: `requests[].queries[]`, `requests[].formulas[]`, `precision` (decimal places), `text_align`, `autoscale` boolean, `custom_unit` string, `conditional_formats[]` for color thresholds (e.g., red above 90, yellow above 70, green otherwise).

### Table (`table`)
Tabular display of grouped metric or log data. Supports sorting, pagination, and conditional formatting.

Key configuration: `requests[].queries[]`, `requests[].formulas[]` with `cell_display_mode` (number, bar), `requests[].response_format: "scalar"`, conditional formatting rules.

### List (`list_stream`)
Streaming list of events, logs, or traces matching a query. Displays live data with configurable columns.

Key configuration: `requests[].response_format: "event_list"`, `requests[].query.data_source` (logs_stream, event_stream, rum_stream, apm_issue_stream, ci_pipeline_stream), `requests[].columns[]` for visible fields.

### SLO List (`slo_list`)
Displays a list of SLOs with their current status, error budget, and target compliance.

Key configuration: `requests[].query.query_string` (filter SLOs), `requests[].query.limit` (max SLOs shown), `requests[].request_type: "slo_list"`.

---

## Architecture

Widgets that visualize infrastructure and service topology.

### Topology Map (`topology_map`)
Displays network communication topology between services, pods, or hosts as a node graph.

Key configuration: `requests[].query.data_source` (service_map), `requests[].query.filters[]`, `requests[].request_type: "topology"`.

### Service Map (`servicemap`)
Visualizes dependencies between services as discovered by APM traces. Shows request rates, error rates, and latency.

Key configuration: `filters[]` for scoping (e.g., `env:prod`), `service` to center on a specific service, `title`.

### Hostmap (`hostmap`)
Color-coded grid of hosts grouped by tags. Color and size represent metric values. Mimics the Infrastructure > Host Map page.

Key configuration: `requests.fill.q` (metric for color), `requests.size.q` (metric for size), `group[]` for grouping tags, `scope[]` for filtering, `style.palette` (green_to_orange, yellow_to_green, etc.), `no_group_hosts` and `no_metric_hosts` booleans.

---

## Annotations and Display

Widgets for context, documentation, and non-data content.

### Event Timeline (`event_timeline`)
Horizontal bar showing event density over time for a given query. Compact visualization of event frequency.

Key configuration: `query` (event search string), `tags_execution` (and/or for tag filtering), `time`.

### Event Stream (`event_stream`)
Live feed of events matching a query. Shows event details inline.

Key configuration: `query` (event search string), `event_size` (s, l), `tags_execution`.

### Notes and Links (`note`)
Free-text markdown content. Use for documentation, runbooks, links, and annotations within dashboards.

Key configuration: `content` (markdown string), `background_color`, `font_size`, `text_align`, `vertical_align`, `show_tick` and `tick_edge` for callout arrow positioning, `has_padding` boolean.

### Image (`image`)
Displays a static image from a URL. Useful for logos, architecture diagrams, or status badges.

Key configuration: `url` (image URL), `url_dark_theme` (optional dark mode variant), `sizing` (zoom, fit, center, cover, contain), `margin` (sm, md, lg, small, large), `has_background` and `has_border` booleans.

### Iframe (`iframe`)
Embeds an external webpage. Note: many sites block iframe embedding via X-Frame-Options.

Key configuration: `url` (page URL).

---

## Lists and Status

Widgets for log streams, check statuses, and alert values.

### Log Stream (`log_stream`)
Live, scrollable list of log entries matching a query. Equivalent to the Logs Explorer filtered view.

Key configuration: `query` (log search syntax), `columns[]` (visible columns), `indexes[]` (log indexes to search), `show_date_column` and `show_message_column` booleans, `message_display` (inline, expanded_md, expanded_lg), `sort.column` and `sort.order`.

### Alert Value (`alert_value`)
Displays the current value that triggered a monitor alert as a single large number.

Key configuration: `alert_id` (monitor ID as string), `precision` (decimal places), `text_align`, `unit`.

### Check Status (`check_status`)
Shows the status of a service check (OK, WARNING, CRITICAL, UNKNOWN) as a colored indicator.

Key configuration: `check` (check name), `grouping` (check, cluster), `group` (optional specific group), `group_by[]`, `tags[]`.

### Service Summary (`service_summary`)
Displays a summary of a service check's status across all groups.

Key configuration: `env`, `service`, `span_name`, `display_format` (one_column, two_column, three_column), `show_hits`, `show_errors`, `show_latency`, `show_breakdown`, `show_distribution`, `show_resource_list`, `size_format` (small, medium, large).

---

## Alerting and SLO

Widgets related to monitor management and SLO tracking.

### Alert Graph (`alert_graph`)
Renders the metric graph for a specific monitor, showing the alert threshold line and current state.

Key configuration: `alert_id` (monitor ID as string), `viz_type` (timeseries, toplist), `live_span` (e.g., "1h", "4h", "1d"), `title`.

### Monitor Summary (`manage_status`)
Grid or list of monitors matching a query. Shows current state (OK, Alert, Warn, No Data) per group. JSON type is `manage_status`.

Key configuration: `query` (monitor search query), `summary_type` (monitors, groups, combined), `display_format` (counts_and_list, list, counts), `sort` (status_asc, status_desc, name_asc, name_desc), `color_preference` (text, background), `show_last_triggered`, `show_priority`, `count` and `start` for pagination.

### SLO (`slo`)
Displays a single SLO's status, error budget, and compliance over selected time windows.

Key configuration: `slo_id` (SLO identifier), `view_type` (detail), `time_windows[]` (e.g., "7d", "30d", "90d"), `show_error_budget`, `view_mode` (overall, component, both), `global_time_target`.

---

## Performance and Interactive

Widgets that trigger actions or embed interactive content.

### Run Workflow (`run_workflow`)
Button widget that triggers a Datadog workflow. Allows passing template variable values as workflow inputs.

Key configuration: `workflow_id`, `title`, `inputs[]` for mapping template variables to workflow parameters, `custom_links[]`.

### App Builder (`app`)
Embeds a Datadog App Builder application directly inside the dashboard. Enables interactive controls (buttons, forms, tables) inline.

Key configuration: `requests[].query.app_id` (the App Builder app UUID), `title`. The `app_id` is obtained from the app-builder skill output.

---

## Conditional Formatting

Many widgets (query_value, table, toplist, change) support `conditional_formats[]`:

```json
{
  "conditional_formats": [
    {
      "comparator": ">",
      "value": 90,
      "palette": "white_on_red",
      "custom_bg_color": "#ff0000"
    },
    {
      "comparator": ">",
      "value": 70,
      "palette": "white_on_yellow"
    },
    {
      "comparator": "<=",
      "value": 70,
      "palette": "white_on_green"
    }
  ]
}
```

**Comparators:** `>`, `>=`, `<`, `<=`, `=`.

**Palettes:** `white_on_red`, `white_on_yellow`, `white_on_green`, `red_on_white`, `yellow_on_white`, `green_on_white`, `custom_bg`, `custom_image`, `custom_text`.

---

## Formulas and Functions

All query-based widgets support formulas that combine, transform, and compute across queries:

```json
{
  "queries": [
    { "name": "a", "query": "avg:system.cpu.user{*}", "data_source": "metrics" },
    { "name": "b", "query": "avg:system.cpu.system{*}", "data_source": "metrics" }
  ],
  "formulas": [
    { "formula": "a + b", "alias": "Total CPU" },
    { "formula": "a / (a + b) * 100", "alias": "User CPU %" }
  ]
}
```

**Arithmetic:** `+`, `-`, `*`, `/`.

**Functions:** `abs()`, `log2()`, `log10()`, `cumsum()`, `integral()`, `diff()`, `derivative()`, `monotonic_diff()`, `per_second()`, `per_minute()`, `per_hour()`, `clamp_min()`, `clamp_max()`, `default_zero()`, `cutoff_min()`, `cutoff_max()`, `timeshift()`, `hour_before()`, `day_before()`, `week_before()`, `month_before()`, `ewma_3()`, `ewma_5()`, `ewma_10()`, `ewma_20()`, `median_3()`, `median_5()`, `median_7()`, `median_9()`, `top()`, `count_nonzero()`, `count_not_null()`, `anomalies()`, `outliers()`, `forecast()`, `robust_trend()`, `trend_line()`.
