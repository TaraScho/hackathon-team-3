---
name: dashboards
description: >
  Creates Datadog dashboards via JSON API or Terraform with embedded App Builder
  widgets. Manages monitors and composite templates.
  Includes 7 ready-to-use templates (SRE, OTel, usage, composite).
  Trigger phrases: "create dashboard", "dashboard JSON", "embed app in dashboard",
  "datadog_dashboard_json terraform", "SRE dashboard", "OTel collector dashboard",
  "app ID placeholder", "dashboard template".
  Do NOT use for App Builder apps (use app-builder), workflow specs
  (use workflow-automation), or IAM connections (use action-connections).
metadata:
  author: hackathon-team-3
  tags: [dashboards, monitoring, sre, otel, app-builder, visualizations]
  category: observability
---

# Dashboards Skill

## Overview

Dashboards aggregate metrics, logs, traces, monitors, and interactive App Builder widgets into a single pane of glass. This skill handles dashboard creation via JSON API and composite dashboard assembly with embedded app and workflow widgets.

### Dependency Diagram

```
[N app UUIDs from app-builder]       ──► dashboards (composite)
[M workflow UUIDs from workflow-auto] ──► dashboards (composite)

standalone dashboards (SRE, OTel)    ──► no dependencies
```

---

## Doc Fetch URLs

Before executing, fetch current API and product documentation:

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/dashboards.md` |
| Template variables | `https://docs.datadoghq.com/dashboards/template_variables.md` |
| Widget reference | `https://docs.datadoghq.com/dashboards/widgets.md` |
| Terraform provider | TF MCP → `datadog_dashboard_json` |

---

## Output Format Selection

Read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` |
| `shell` | Claude executes `curl` + `jq` commands directly via Bash tool |

---

## When to Use

- You want to deploy a dashboard from one of the JSON templates
- You are building a control-plane dashboard embedding App Builder apps
- You need to create monitors and reference them in dashboard widgets
- You need an SRE golden-signals, OTel collector, or cloud security dashboard

---

## Prerequisites

| Requirement | Details |
|---|---|
| `DD_API_KEY` | Datadog API key |
| `DD_APP_KEY` | Datadog app key |
| App UUIDs (for composite) | From app-builder skill — needed for embedded app widgets |
| Workflow UUIDs (for composite) | From workflow-automation skill — needed for run_workflow widgets |

---

## Available Templates

Seven ready-to-use JSON templates in `examples/json/`:

| File | Purpose |
|---|---|
| `dd101-sre-dashboard.json` | SRE golden signals: latency, traffic, errors, saturation |
| `otel-collector-health-dashboard.json` | OpenTelemetry collector pipeline health |
| `otel-tailsampling-dashboard.json` | OTel tail-based sampling decision rates |
| `storedog-frontend-dashboard.json` | E-commerce frontend service health |
| `estimated-usage-dashboard.json` | Datadog log management usage metrics |
| `techstories-dashboard-demo.json` | Demo TechStories ops dashboard (3 embedded apps) |
| `techstories-dashboard-full.json` | Full TechStories ops dashboard (8 embedded apps) |

The `techstories-*` templates use `__APP_ID_*__` placeholders for embedded app widgets.

---

## Core Workflow: Create a Dashboard

All API calls require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### Standalone dashboard (no app dependencies)

1. Load a template JSON from `examples/json/`
2. `POST /api/v1/dashboard` with the dashboard JSON as body
3. Response includes `url` field — full dashboard URL is `https://app.datadoghq.com{url}`

### Composite dashboard (with embedded apps)

1. Collect all app UUIDs and workflow UUIDs from upstream skills
2. Load the template and substitute `__APP_ID_*__` placeholders with real UUIDs using `jq` or string replacement
3. `POST /api/v1/dashboard` with the substituted JSON

### Additive composite pattern

Instead of using a template, build the dashboard additively — one widget per created resource:

1. **Header note widget** — project name and description
2. **One group per app** — each containing an embedded app widget:
   ```json
   {"definition": {"type": "app", "title": "EC2 Manager", "requests": [{"query": {"app_id": "<uuid>"}}]}}
   ```
3. **Workflow trigger group** — `run_workflow` button widgets:
   ```json
   {"definition": {"type": "run_workflow", "title": "Run ECS Rollback", "workflow_id": "<uuid>", "inputs": [{"name": "service_name", "value": "$service.value"}]}}
   ```
4. Assemble into dashboard JSON with `layout_type: "ordered"`
5. POST to API

---

## Template Variables

```json
{
  "template_variables": [
    {"name": "env", "prefix": "env", "default": "prod", "available_values": ["prod", "staging"]},
    {"name": "service", "prefix": "service", "default": "*", "available_values": []}
  ]
}
```

Syntax in widget queries: `$var` (value), `$var.key` (tag key), `$var.value` (explicit value).

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **Full replacement on PUT** | Dashboard update requires complete object — omitted fields reset to defaults |
| **Dashboard URL** | Use `url` field from response, not ID — full URL is `https://app.datadoghq.com{url}` |
| **Monitor search returns array** | `GET /api/v1/monitor?name=...` returns JSON array, not object — parse to extract first result |
| **Logs intake endpoint** | Use `https://http-intake.logs.datadoghq.com/api/v2/logs` (NOT `api.datadoghq.com`) |
| **Metric type values** | `0` unspecified, `1` count, `2` rate, `3` gauge (for `/api/v2/series`) |
| **Rollup pitfall** | Using `sum` rollup on gauge metrics inflates values — use `avg` for gauges, `sum` for counts |
| **Conditional formatting** | Comparators: `>`, `>=`, `<`, `<=`, `=` only (no `!=`). Palettes: `white_on_red`, `white_on_yellow`, `white_on_green` |
| **Run workflow widget** | Workflow must include `apiTrigger` in its triggers — workflows with only `securityTrigger` won't work from dashboards |
| **Placeholder format** | All app ID placeholders use `__APP_ID_{SERVICE_NAME}__` double-underscore format |

---

## Cross-Skill Notes

- **Requires app-builder**: Collect all app UUIDs before creating composite dashboards.
- **Requires workflow-automation**: Workflows must include `apiTrigger` for dashboard invocation.
- **Monitor IDs feed workflow-automation**: Monitors created here can be used as `monitorTrigger` sources.
- **Standalone use**: Dashboards can be created without apps or workflows using any JSON template.

---

## JSON Examples

Seven dashboard templates in `examples/json/`. Standalone templates can be POSTed directly. Composite templates (`techstories-*`) require app ID substitution first. See "Available Templates" table above.
