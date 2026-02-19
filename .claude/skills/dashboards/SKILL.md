---
name: dashboards
description: >
  Creates and manages Datadog dashboards for IaC visibility, security posture,
  service health, and operations control planes — via Terraform, the Datadog Python
  API, or JSON templates. Use this skill when you need to: create a dashboard from
  a JSON file, write Terraform for datadog_dashboard or datadog_dashboard_json
  resources, embed App Builder apps inside dashboard widgets, inject app IDs into
  dashboard templates via placeholder substitution, build SRE/OTel/cloud security
  dashboards, create monitors and link them to dashboards, or send custom metrics
  and logs to power dashboard widgets. Trigger phrases: "create dashboard",
  "dashboard JSON", "embed app in dashboard", "datadog_dashboard_json terraform",
  "SRE dashboard", "OTel collector dashboard", "app ID placeholder", "dashboard template".
metadata:
  author: hackathon-team-3
  version: 1.0.0
  tags: [dashboards, terraform, monitoring, sre, otel, app-builder, visualizations]
  category: observability
---

# Dashboards Skill

## Overview

Dashboards aggregate metrics, logs, traces, monitors, and interactive App Builder widgets into a single pane of glass. There are three authoring paths:

1. **JSON API** — upload a complete dashboard definition (from a template file) to `POST /api/v1/dashboard`. Fastest for complex layouts.
2. **Terraform HCL** — use `datadog_dashboard` with nested widget blocks when monitor IDs must be Terraform references. Use `datadog_dashboard_json` with `file()` for complex JSON that would be unreadable in HCL.
3. **Composite with app embeds** — load a JSON template that contains app ID placeholders, substitute real app IDs (from the app-builder step), then POST. Used when dashboards include App Builder widgets.

### Dependency Diagram

```
action-connections ──► app-builder ──► dashboards
```

Dashboards are the final consumer in the pipeline. They need app IDs (from app-builder) and optionally monitor IDs (created in the dashboards step itself or externally).

---

## When to Use

- You want to deploy a dashboard from one of the existing JSON templates
- You need Terraform to manage dashboards alongside the rest of your IaC
- You are building a control-plane dashboard that embeds App Builder apps for live AWS management
- You need to create monitors and reference their IDs inside dashboard widgets
- You are sending custom metrics or logs from your application and want to visualize them
- You need an SRE golden-signals dashboard, an OTel collector health dashboard, or a cloud security posture dashboard

---

## Available Templates

Seven ready-to-use JSON templates are in `examples/json/`:

| File | Purpose |
|---|---|
| `dd101-sre-dashboard.json` | SRE golden signals: latency, traffic, errors, saturation |
| `otel-collector-health-dashboard.json` | OpenTelemetry collector pipeline health and throughput |
| `otel-tailsampling-dashboard.json` | OTel tail-based sampling decision rates and pipeline |
| `storedog-frontend-dashboard.json` | E-commerce frontend service health (Storedog reference app) |
| `estimated-usage-dashboard.json` | Datadog log management estimated usage metrics |
| `techstories-dashboard-demo.json` | Demo version of TechStories ops dashboard |
| `techstories-dashboard-full.json` | Full TechStories ops dashboard with embedded App Builder app placeholders |

---

## API: Create and Update

### Create a dashboard

```
POST /api/v1/dashboard
Content-Type: application/json
DD-API-KEY: {api_key}
DD-APPLICATION-KEY: {app_key}
```

Body: the full dashboard JSON object (the contents of a template file, or built programmatically).

Returns: `id` — the dashboard ID (used in the URL and for updates).

### Update an existing dashboard

```
PUT /api/v1/dashboard/{dashboard_id}
```

Full replacement — the body must contain the complete dashboard definition, not a partial patch.

### URL construction note

Dashboard URLs follow the pattern:
```
https://app.datadoghq.com/dashboard/{dashboard_id}
```

---

## Terraform: Two Patterns

### Pattern 1 — `datadog_dashboard_json` with `file()`

Best for complex dashboards where writing HCL widgets would be unwieldy:

```hcl
resource "datadog_dashboard_json" "sample_apps_kpi" {
  count = var.create_dashboards ? 1 : 0

  dashboard = file("${path.module}/estimated-usage-dashboard.json")
}
```

The JSON file path is relative to the module directory. The dashboard JSON must be valid Datadog dashboard JSON (same format as the API body).

See `examples/terraform/automating-meaningful-actions-dashboards.tf`.

### Pattern 2 — `datadog_dashboard` HCL widgets

Use when other Terraform resources (monitors) produce IDs that must be injected as widget references:

```hcl
resource "datadog_dashboard" "ops_dashboard" {
  title       = "Operations Dashboard"
  layout_type = "ordered"
  reflow_type = "fixed"

  widget {
    alert_graph_definition {
      alert_id  = datadog_monitor.redis_cpu.id   # Terraform reference
      live_span = "30m"
      title     = "Redis CPU"
      viz_type  = "timeseries"
    }
    widget_layout { height = "2"; width = "4"; x = "0"; y = "0" }
  }

  widget {
    manage_status_definition {
      query        = "service:\"my-service\""
      summary_type = "monitors"
    }
    widget_layout { height = "2"; width = "4"; x = "4"; y = "0" }
  }
}
```

See `examples/terraform/dd-api-automation-dashboards.tf` for a multi-widget example with timeseries, manage_status, list_stream, and group widgets.

---

## App Embedding Pattern

When a dashboard should contain a live App Builder widget, the template JSON has placeholders:

```json
{
  "type": "app",
  "requests": [{"query": {"app_id": "APP_ID_PLACEHOLDER_EC2_MANAGEMENT"}}]
}
```

The `create_dashboard_with_embedded_apps()` function in `examples/python/datadog_helpers.py` handles substitution:

```python
APP_NAME_TO_KEY = {
    "ec2-management-console": "APP_ID_PLACEHOLDER_EC2_MANAGEMENT",
    "manage-ecs-tasks":       "APP_ID_PLACEHOLDER_ECS_MANAGEMENT",
    "explore-s3":             "APP_ID_PLACEHOLDER_S3_EXPLORER",
    "manage-dynamodb":        "APP_ID_PLACEHOLDER_DYNAMODB",
    "manage-sqs":             "APP_ID_PLACEHOLDER_SQS",
    "lambda-function-manager":"APP_ID_PLACEHOLDER_LAMBDA",
}

def create_dashboard_with_embedded_apps(api_key, app_key, template_file, created_app_ids):
    # Build placeholder → real ID map
    app_id_map = {APP_NAME_TO_KEY[name]: id for name, id in created_app_ids.items()}

    # Load template and replace all placeholders
    with open(template_file) as f:
        dashboard_json = f.read()
    for placeholder, real_id in app_id_map.items():
        dashboard_json = dashboard_json.replace(placeholder, real_id)

    # POST to create
    return create_dashboard(api_key, app_key, json.loads(dashboard_json))
```

Use `techstories-dashboard-full.json` as the template — it contains placeholders for all nine app types.

---

## Monitor Management

Monitors can be created independently and then referenced inside dashboard widgets.

### Idempotent create-or-update

The `create_or_update_monitor()` helper checks for an existing monitor by name before creating:

```python
existing = get_existing_monitors(api_key, app_key, monitor_name)
if existing:
    # PUT /api/v1/monitor/{id}
    update_monitor(api_key, app_key, existing["id"], monitor_config)
else:
    # POST /api/v1/monitor
    create_monitor(api_key, app_key, monitor_config)
```

### Monitor config fields

```json
{
  "name": "High CPU on EC2",
  "type": "metric alert",
  "query": "avg(last_5m):avg:aws.ec2.cpuutilization{*} > 90",
  "message": "CPU is above 90% @pagerduty",
  "tags": ["env:prod", "service:ec2"],
  "priority": 3,
  "options": {
    "thresholds": {"critical": 90, "warning": 80},
    "notify_no_data": true,
    "no_data_timeframe": 10
  }
}
```

---

## Custom Metrics and Logs

### Send custom metrics

```
POST /api/v2/series
Content-Type: application/json
```

```python
payload = {
    "series": [{
        "metric": "my.app.event_count",
        "type": 1,         # 0=unspecified, 1=count, 2=rate, 3=gauge
        "points": [{"timestamp": int(time.time()), "value": 42.0}],
        "tags": ["env:prod", "service:my-service"],
        "resources": [{"name": "my-host", "type": "host"}]
    }]
}
```

### Send logs

```
POST https://http-intake.logs.datadoghq.com/api/v2/logs
```

```python
payload = [{
    "ddsource": "my-lambda",
    "ddtags": "env:prod,service:my-service",
    "hostname": "lambda-function",
    "message": "User action completed",
    "status": "info"
}]
```

---

## Cross-Skill Notes

- **Requires app-builder**: If embedding App Builder widgets, collect all app IDs from the app-builder step before creating the dashboard.
- **Monitor IDs feed workflow-automation**: Monitors created here can be used as `monitorTrigger` sources in workflow-automation. Export the monitor ID after creation.
- **Standalone use**: Dashboards can be created without App Builder apps — just use any of the JSON templates that do not contain app placeholders (e.g., `dd101-sre-dashboard.json`, `otel-collector-health-dashboard.json`).

---

## Level 3 References

- `examples/python/datadog_helpers.py` — `create_dashboard()`, `create_dashboard_with_embedded_apps()`, `create_or_update_monitor()`, `send_metrics()`, `send_logs()`, team/service entity management
- `examples/terraform/automating-meaningful-actions-dashboards.tf` — `datadog_dashboard_json` with `file()` pattern
- `examples/terraform/dd-api-automation-dashboards.tf` — `datadog_dashboard` HCL with Terraform-managed monitor ID references
- `examples/json/techstories-dashboard-full.json` — composite dashboard with App Builder app ID placeholders
