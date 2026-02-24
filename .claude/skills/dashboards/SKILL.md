---
name: dashboards
description: >
  Creates Datadog dashboards via JSON API, Terraform, or composite templates with
  embedded App Builder widgets. Manages monitors, custom metrics, and logs intake.
  Includes 7 ready-to-use templates (SRE, OTel, usage, composite).
  Trigger phrases: "create dashboard", "dashboard JSON", "embed app in dashboard",
  "datadog_dashboard_json terraform", "SRE dashboard", "OTel collector dashboard",
  "app ID placeholder", "dashboard template".
  Do NOT use for App Builder apps (use app-builder), workflow specs
  (use workflow-automation), or IAM connections (use action-connections).
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars.
  For embedded app dashboards: app IDs from the app-builder skill.
metadata:
  author: hackathon-team-3
  version: 2.0.0
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

## API Endpoint Summary

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/dashboard` | Create a dashboard |
| PUT | `/api/v1/dashboard/{id}` | Update (full replace) a dashboard |
| GET | `/api/v1/dashboard` | List dashboards (paginated) |
| GET | `/api/v1/dashboard/{id}` | Get a single dashboard |
| DELETE | `/api/v1/dashboard/{id}` | Delete a dashboard |
| POST | `/api/v1/monitor` | Create a monitor |
| GET | `/api/v1/monitor` | List/search monitors |
| PUT | `/api/v1/monitor/{id}` | Update a monitor |
| DELETE | `/api/v1/monitor/{id}` | Delete a monitor |
| POST | `/api/v2/series` | Submit custom metrics (API key only) |
| POST | `/api/v2/logs` | Submit logs to `http-intake.logs.datadoghq.com` (API key only) |

Full request/response schemas, query parameter tables, curl examples, and the idempotent create-or-update pattern are in `references/api-reference.md`.

---

## Template Variables Quick Reference

Template variables add interactive dropdown filters to dashboards.

**Definition:**

```json
{
  "template_variables": [
    { "name": "env", "prefix": "env", "default": "prod", "available_values": ["prod", "staging"] },
    { "name": "service", "prefix": "service", "default": "*", "available_values": [] }
  ]
}
```

**Syntax in widget queries:**

| Syntax | Meaning | Example |
|---|---|---|
| `$var` | Selected tag value | `avg:cpu{env:$env}` |
| `$var.value` | Explicit value reference | `{env:$env.value}` |
| `$var.key` | The tag key (prefix) | `{$env.key:$env.value}` |

Use `*` as the default for "all values." Saved views (presets) persist combinations of variable selections via `template_variable_presets` in the dashboard JSON.

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
    # Build placeholder -> real ID map
    app_id_map = {APP_NAME_TO_KEY[name]: id for name, id in created_app_ids.items()}

    # Load template and replace all placeholders
    with open(template_file) as f:
        dashboard_json = f.read()
    for placeholder, real_id in app_id_map.items():
        dashboard_json = dashboard_json.replace(placeholder, real_id)

    # POST to create
    return create_dashboard(api_key, app_key, json.loads(dashboard_json))
```

Use `techstories-dashboard-full.json` as the template -- it contains placeholders for all nine app types.

---

## Cross-Skill Notes

- **Requires app-builder**: If embedding App Builder widgets, collect all app IDs from the app-builder step before creating the dashboard.
- **Monitor IDs feed workflow-automation**: Monitors created here can be used as `monitorTrigger` sources in workflow-automation. Export the monitor ID after creation.
- **Standalone use**: Dashboards can be created without App Builder apps -- just use any of the JSON templates that do not contain app placeholders (e.g., `dd101-sre-dashboard.json`, `otel-collector-health-dashboard.json`).

---

## Additional Resources

| File | Contents |
|---|---|
| `references/api-reference.md` | Full API contracts: Dashboard CRUD, Monitor CRUD, metrics intake, logs intake. Request/response schemas, query param tables, curl examples, idempotent create-or-update pattern. |
| `references/widget-types.md` | All 45+ widget types organized by category (graphs, groups, analytics, architecture, alerting, performance). Key configuration options, conditional formatting, formulas and functions. |
| `references/advanced-features.md` | Template variables deep-dive, refresh rates, permissions/RBAC, sharing (public links, embeds, scheduled reports), advanced functions (rollup, timeshift, anomaly detection, forecast), TV mode, version history. |

---

## Level 3 References

- `examples/python/datadog_helpers.py` — `create_dashboard()`, `create_dashboard_with_embedded_apps()`, `create_or_update_monitor()`, `send_metrics()`, `send_logs()`, team/service entity management
- `examples/terraform/automating-meaningful-actions-dashboards.tf` — `datadog_dashboard_json` with `file()` pattern
- `examples/terraform/dd-api-automation-dashboards.tf` — `datadog_dashboard` HCL with Terraform-managed monitor ID references
- `examples/json/techstories-dashboard-full.json` — composite dashboard with App Builder app ID placeholders
