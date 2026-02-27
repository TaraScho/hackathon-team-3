---
name: dashboard-creator
description: >
  Builds Datadog dashboards via JSON API or Terraform from a dashboard-design.json
  spec or standalone examples. Handles styling, widget sizing, template variables,
  and embedded App Builder / Workflow Automation widgets.
  Trigger phrases: "create dashboard", "dashboard JSON", "embed app in dashboard",
  "datadog_dashboard_json terraform", "app ID placeholder", "example dashboard",
  "build dashboard".
metadata:
  author: hackathon-team-3
  tags: [dashboards, monitoring, sre, app-builder, visualizations]
  category: observability
---

# Dashboard Creator Skill

## Overview

Builds Datadog dashboards from a `dashboard-design.json` spec (produced by `dashboard-designer`) or standalone examples. Handles all technical execution: API calls, Terraform generation, styling, and widget placement.

---

## Inputs

| Source | File | When |
|---|---|---|
| `dashboard-designer` | `{RUN_DIR}/dashboard-design.json` | Orchestrated mode |
| Manual / standalone | Example JSON from `examples/json/` | Standalone use |

---

## Doc Fetch URLs

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/dashboards.md` |
| Template variables | `https://docs.datadoghq.com/dashboards/template_variables.md` |
| Widget reference | `https://docs.datadoghq.com/dashboards/widgets.md` |
| Terraform provider | TF MCP → `datadog_dashboard_json` |

---

## Output Mode

Read `preferred_output_format` from `{RUN_DIR}/repo-analysis.json` (orchestrated) or `{repo_path}/repo-analysis.json` (standalone):

| `preferred_output_format` | Execution path | Output location |
|---|---|---|
| `terraform` | Query TF MCP for schemas, generate `.tf` | `{RUN_DIR}/terraform/dashboard_composite.tf` |
| `shell` | Execute `curl` + `jq` via Bash | `{RUN_DIR}/manifest.json` (append entry) |

---

## Styling & Aesthetic Conventions

Use the example dashboards in `examples/json/` as styling references.

### Dashboard-Level

| Property | Value |
|---|---|
| `layout_type` | `"ordered"` |
| `reflow_type` | `"fixed"` |

### Widget Sizing

| Widget type | Width | Height |
|---|---|---|
| Header note / command-center group | `12` (full grid) | -- |
| Embedded app (standalone) | `12` | `6` |
| Embedded app (paired with metrics) | `6` | `5` |
| Timeseries alongside app | `6` | `3` |

### Group Widget Colors

| Group | `background_color` |
|---|---|
| Header / command-center | `"purple"` |
| Per-service content groups | none -- use `banner_img` instead |

### Note Widgets

| Property | Value |
|---|---|
| `font_size` | `"18"` |
| `vertical_align` | `"center"` |
| `has_padding` | `true` |
| `show_tick` | `true` |
| `tick_edge` | `"bottom"` |
| `tick_pos` | `"50%"` |
| Background -- description | `"green"` |
| Background -- architecture | `"blue"` |

### App Widgets (embedded_app)

**CRITICAL: The correct widget type is `"embedded_app"`, NOT `"app"`.** Definition has only `type` and `app_id` -- no `title`, `title_size`, or `requests`.

```json
{"definition": {"type": "embedded_app", "app_id": "<uuid>"}, "layout": {"x": 0, "y": 0, "width": 12, "height": 6}}
```

### Timeseries Widgets

| Property | Value |
|---|---|
| `palette` | `"dog_classic"` |
| `line_type` | `"solid"` |

### Monitor Status Widgets

| Property | Value |
|---|---|
| `display_format` | `"countsAndList"` |
| `hide_zero_counts` | `true` |

### Service Group Banner Images

For AWS service groups, set `banner_img` to: `/static/images/integration_dashboard/{service}_hero_1.png`

---

## Core Workflow -- Terraform Mode

1. **Query TF MCP** for resource schema: `datadog_dashboard_json`
2. **Generate `.tf` file** at `{RUN_DIR}/terraform/dashboard_composite.tf` containing:
   - `datadog_dashboard_json` resource with `jsonencode()` body
   - Reference app/workflow IDs from other `.tf` outputs (e.g., `datadog_app_builder_app.app_ecs_tasks.id`)
3. **Export `output` block:** `dashboard_url`
4. **Validate:** `cd {RUN_DIR}/terraform && terraform validate`

---

## Core Workflow -- Shell Mode

All API calls require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### From design spec (orchestrated)

1. Read `{RUN_DIR}/dashboard-design.json`
2. For each group, load the `source_example` from `examples/json/`
3. Extract only the `selected_widget_groups`, apply app/workflow placements
4. Assemble into dashboard JSON with styling conventions applied
5. `POST /api/v1/dashboard`

### Standalone dashboard (no design spec)

1. Load an example JSON from `examples/json/`
2. Substitute `__APP_ID_*__` placeholders with real UUIDs if applicable
3. `POST /api/v1/dashboard`
4. Response `url` field gives full URL: `https://app.datadoghq.com{url}`

### Additive composite pattern

Build the dashboard additively -- one widget per created resource. Include `[{repo_id}]` in the dashboard `title` (e.g., `"Stickerlandia Operations [A3F7]"`).

1. **Header group** (`background_color: "purple"`, `width: 12`):
   - Note widget with `background_color: "green"` for project description, `"blue"` for architecture context
2. **One group per service** -- use `banner_img: "/static/images/integration_dashboard/{service}_hero_1.png"`:
   - **App widget** (`type: "embedded_app"`): full-width or half-width per sizing table
   - **Timeseries widget** (optional): alongside app per sizing table
   - **Workflow trigger button** (`type: "run_workflow"`): at bottom of group
     ```json
     {"definition": {"type": "run_workflow", "title": "Run ECS Rollback", "workflow_id": "<uuid>", "inputs": [{"name": "service_name", "value": "$service.value"}]}}
     ```
3. Assemble with `layout_type: "ordered"`, `reflow_type: "fixed"`
4. POST to API

---

## Template Variables

```json
{
  "template_variables": [
    {"name": "env",     "prefix": "env",     "default": "*", "available_values": []},
    {"name": "service", "prefix": "service", "default": "*", "available_values": []},
    {"name": "team",    "prefix": "team",    "default": "*", "available_values": []}
  ]
}
```

Always include `team`. Use `$var` (value), `$var.key` (tag key), `$var.value` (explicit value) in widget queries.

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **Full replacement on PUT** | Dashboard update requires complete object -- omitted fields reset to defaults |
| **Dashboard URL** | Use `url` field from response -- full URL is `https://app.datadoghq.com{url}` |
| **Monitor search returns array** | `GET /api/v1/monitor?name=...` returns JSON array, not object |
| **Rollup pitfall** | `sum` rollup on gauge metrics inflates values -- use `avg` for gauges, `sum` for counts |
| **Conditional formatting** | Comparators: `>`, `>=`, `<`, `<=`, `=` only. Palettes: `white_on_red`, `white_on_yellow`, `white_on_green` |
| **Run workflow widget** | Workflow must include `dashboardTrigger` in triggers |
| **Placeholder format** | All app ID placeholders use `__APP_ID_{SERVICE_NAME}__` double-underscore format |
| **Use `datadog_dashboard_json` not `datadog_dashboard`** | `datadog_dashboard` has a ~511K-char schema -- always use `datadog_dashboard_json` (raw JSON string) |

---

## Cross-Skill Notes

- **Requires `dashboard-designer`** (orchestrated): reads `dashboard-design.json` for widget selection and layout
- **Requires `app-builder`**: app UUIDs for embedded app widgets
- **Requires `workflow-automation`**: workflow UUIDs for `run_workflow` widgets; workflows must include `dashboardTrigger`
- **Terraform mode:** reads outputs from other `.tf` files -- use `datadog_app_builder_app.app_{label}.id` and `datadog_workflow_automation.wf_{label}.id`
- **Shell mode:** UUIDs from `{RUN_DIR}/onboarding-uuids.json` substituted into dashboard JSON
- **Standalone use**: dashboards can be created without a design spec using any JSON example
