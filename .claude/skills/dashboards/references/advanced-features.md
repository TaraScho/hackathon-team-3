# Dashboards Skill — Advanced Features Reference

Deep-dive into template variables, refresh behavior, permissions, sharing, advanced query functions, and other power-user features for Datadog dashboards.

---

## Template Variables

Template variables add interactive filters to dashboards, letting users scope data without editing queries. They appear as dropdowns at the top of the dashboard.

### Definition

In the dashboard JSON:

```json
{
  "template_variables": [
    {
      "name": "env",
      "prefix": "env",
      "default": "prod",
      "available_values": ["prod", "staging", "dev"]
    },
    {
      "name": "service",
      "prefix": "service",
      "default": "*",
      "available_values": []
    },
    {
      "name": "region",
      "prefix": "aws_region",
      "default": "*",
      "available_values": []
    }
  ]
}
```

- `name`: The variable name used in queries (referenced as `$name`).
- `prefix`: The tag key this variable maps to. Must match a real tag key in your data.
- `default`: The default selected value. Use `"*"` for "all values."
- `available_values`: Restrict the dropdown options. Empty array `[]` means auto-populate from tag values.

### Syntax in Queries

There are three syntaxes depending on the query context:

| Syntax | Expands To | Use Case |
|---|---|---|
| `$var` | The selected tag value | Simple filtering: `avg:cpu{env:$env}` |
| `$var.key` | The tag key (prefix) | Building dynamic tag filters: `{$env.key:$env.value}` |
| `$var.value` | The selected tag value | Explicit value reference: `{env:$env.value}` |

In most widget queries, `$var` is sufficient:

```
avg:system.cpu.user{env:$env, service:$service, aws_region:$region}
```

The `$var.key` / `$var.value` syntax is useful in advanced scenarios where you need to dynamically construct the full `key:value` tag pair, such as in notebook-style parameterized queries or when the variable prefix differs from the tag key used in a particular metric.

### Wildcard Behavior

When `*` is selected (the default for "all"):
- `{env:$env}` becomes `{env:*}` which matches all values of the `env` tag.
- This is equivalent to omitting the tag filter entirely.
- Multiple wildcard variables combine correctly: `{env:*, service:*}` returns all data.

### Associated Template Variables

Template variables can be linked so that selecting a value in one variable filters the options available in another. This is configured in the dashboard settings UI under "Saved Views." The API representation appears in `template_variable_presets`:

```json
{
  "template_variable_presets": [
    {
      "name": "Production US",
      "template_variables": [
        { "name": "env", "value": "prod" },
        { "name": "region", "value": "us-east-1" }
      ]
    },
    {
      "name": "Staging EU",
      "template_variables": [
        { "name": "env", "value": "staging" },
        { "name": "region", "value": "eu-west-1" }
      ]
    }
  ]
}
```

### Saved Views

Saved views preserve a combination of template variable selections, time range, and other dashboard state. They appear as tabs at the top of the dashboard. Each saved view is a `template_variable_presets` entry. The first preset in the array is the default view when no other is explicitly selected.

---

## Refresh Rates

Dashboards automatically refresh data at intervals that depend on the selected time window:

| Time Window | Auto-Refresh Interval | Notes |
|---|---|---|
| Live / Past 5 minutes | Every 10 seconds | Real-time mode. Widgets stream data continuously. |
| Past 15 minutes | Every 15 seconds | Near-real-time. |
| Past 1 hour | Every 30 seconds | |
| Past 4 hours | Every 2 minutes | |
| Past 1 day | Every 5 minutes | |
| Past 2 days | Every 10 minutes | |
| Past 1 week | Every 30 minutes | |
| Past 1 month | Every 2 hours | |
| Custom range (fixed) | No auto-refresh | Static snapshot. Manual refresh only. |

**Forcing a refresh:** Click the refresh button or set the time selector to a live window. The API does not control refresh; it is a UI-only behavior.

**TV Mode refresh:** When a dashboard is in TV Mode (full-screen kiosk display), refresh intervals remain the same but the UI removes all navigation chrome. Activate via the dashboard menu or by appending `?tv_mode=true` to the URL.

---

## Permissions and RBAC

Datadog dashboards support role-based access control at the individual dashboard level.

### Permission Levels

| Level | Description |
|---|---|
| **Author** | Full control: edit, delete, manage permissions. Automatically assigned to creator. |
| **Editor** | Can modify the dashboard content (widgets, layout, template variables). Cannot delete or change permissions. |
| **Viewer** | Read-only access. Can view the dashboard and interact with template variables but cannot save changes. |

### API Fields

In the dashboard JSON:

- `is_read_only`: Boolean. When `true`, only the author can edit. Deprecated in favor of the restricted_roles approach.
- `restricted_roles`: Array of role UUIDs. Only users with these roles can edit the dashboard. If empty, all users with the `dashboards_write` permission can edit.

```json
{
  "restricted_roles": [
    "role-uuid-for-sre-team",
    "role-uuid-for-platform-team"
  ]
}
```

### Permission Hierarchy

1. **Organization-level:** The `dashboards_read` and `dashboards_write` permissions control base access.
2. **Dashboard-level:** `restricted_roles` further narrows who can edit a specific dashboard.
3. **Team-level:** Dashboards associated with Datadog Teams inherit team visibility settings.

---

## Sharing

### Public (Shareable) Links

Generate a public URL that allows anyone with the link to view the dashboard without authentication:

```bash
# Enable sharing and get a public URL
curl -X POST "https://api.datadoghq.com/api/v1/dashboard/public" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"dashboard_id": "abc-def-ghi", "dashboard_type": "custom_timeboard"}'
```

The response includes a `public_url` field. Public dashboards are read-only and respect template variable defaults.

### Embeds

Dashboards can be embedded in external pages using the embeddable graphs API or iframe-based sharing:

- **Individual graph embed:** `GET /api/v1/graph/embed` generates a standalone embed token for a single widget.
- **Full dashboard embed:** Use the public URL in an iframe. Append `?tpl_var_env=prod` to pre-set template variables.

### Scheduled Reports

Dashboard snapshots can be sent on a schedule via email. Configured in the dashboard UI under "Share > Schedule a Report." Reports render the dashboard as a PDF/image at the scheduled time and email it to the configured recipients. This feature is not available via the API; it must be configured through the Datadog UI or Terraform using the `datadog_dashboard` resource's notification list.

---

## Advanced Query Functions

Beyond basic metric queries, dashboard widgets support powerful analytical functions.

### Rollup

Controls how data points are aggregated over time buckets:

```
avg:system.cpu.user{*}.rollup(avg, 300)
```

- **Methods:** `avg`, `sum`, `min`, `max`, `count`.
- **Interval:** Duration in seconds. If omitted, Datadog auto-selects based on the time window.
- A common pitfall: using `sum` rollup on a gauge metric inflates values. Use `avg` for gauges and `sum` for counts.

### Timeshift

Compare current data with historical data:

```
avg:system.cpu.user{*}, hour_before(avg:system.cpu.user{*})
```

**Functions:** `hour_before()`, `day_before()`, `week_before()`, `month_before()`, `timeshift(<query>, -86400)` for arbitrary offsets (in seconds).

### Smoothing

Reduce noise in time series:

- `ewma_3()`, `ewma_5()`, `ewma_10()`, `ewma_20()` — Exponentially Weighted Moving Average with span of 3, 5, 10, or 20 data points.
- `median_3()`, `median_5()`, `median_7()`, `median_9()` — Moving median over 3, 5, 7, or 9 data points.

```
ewma_5(avg:system.cpu.user{*})
```

### Anomaly Detection

Overlay anomaly bands on time series:

```
anomalies(avg:system.cpu.user{*}, 'basic', 2)
```

**Algorithms:** `basic` (simple lagging), `agile` (adapts quickly to level shifts), `robust` (ignores recent anomalies when predicting), `adaptive` (adjusts to changing trends).

**Bounds:** The second parameter sets the number of standard deviations for the band width (1, 2, or 3).

### Outlier Detection

Identify groups that behave differently from their peers:

```
outliers(avg:system.cpu.user{*} by {host}, 'dbscan', 3)
```

**Algorithms:** `dbscan` (density-based clustering), `mad` (Median Absolute Deviation).

### Forecast

Project future metric values:

```
forecast(avg:system.disk.in_use{*}, 'linear', 1)
```

**Algorithms:** `linear`, `seasonal` (hourly, daily, or weekly seasonality).

**Intervals:** The second parameter specifies how many seasonal periods to forecast ahead.

### Interpolation and Regression

- `default_zero()` — Replace missing data points with zero.
- `trend_line()` — Fit a linear trend to the data.
- `robust_trend()` — Fit a robust linear trend that is resistant to outliers.

---

## JSON Graphing Editor

Every widget in the Datadog UI has a JSON tab that exposes the raw widget definition. This is the fastest way to prototype:

1. Build the widget visually in the UI.
2. Click the JSON tab to copy the definition.
3. Paste into your template JSON file.
4. Replace hardcoded tag values with template variable references (`$var`).

The JSON editor validates the definition in real time and shows errors inline. It is the authoritative source for the exact schema a widget type expects.

---

## TV Mode

Full-screen kiosk display mode for wall-mounted monitors and NOC screens.

- Activate from the UI: Dashboard menu > "Enter TV Mode."
- Activate via URL: Append `?tv_mode=true` to the dashboard URL.
- In TV mode: navigation chrome is hidden, widgets auto-scale to fill the viewport, and the auto-refresh interval stays the same as the selected time window.
- Cycle multiple dashboards: Use a browser extension or script to rotate between dashboard URLs on a timer.

---

## Version History

Datadog automatically tracks changes to dashboards. Each edit creates a new version.

- **View history:** Dashboard settings > "Version History" in the UI.
- **Restore a version:** Select a previous version and click "Restore."
- **API access:** The `GET /api/v1/dashboard/{id}` response includes `modified_at` and `author_handle` for the latest version. Full version history is only accessible through the UI; there is no dedicated API endpoint for listing all versions.
- **Best practice:** When managing dashboards as code (Terraform or JSON templates in git), rely on git history rather than Datadog's version history for change tracking and rollback.
