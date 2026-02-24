# Dashboards Skill — API Reference

All Datadog API endpoints used by the dashboards skill. Covers dashboard CRUD, monitor management, custom metrics submission, and log intake.

## Common Headers

All v1 dashboard and monitor endpoints require:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

Metrics intake (`/api/v2/series`) and logs intake (`/api/v2/logs`) require only `DD-API-KEY` (no application key).

---

## Dashboard API (v1)

### POST /api/v1/dashboard — Create Dashboard

Creates a new dashboard from a complete JSON definition.

**Request body schema:**

```json
{
  "title": "string (required)",
  "description": "string",
  "layout_type": "ordered | free (required)",
  "widgets": [
    {
      "definition": {
        "type": "string — widget type (e.g. timeseries, query_value, group)",
        "requests": [
          {
            "queries": [
              {
                "data_source": "metrics | logs | spans | ...",
                "name": "query1",
                "query": "avg:system.cpu.user{*}"
              }
            ],
            "response_format": "timeseries | scalar | list"
          }
        ],
        "title": "string"
      },
      "layout": { "x": 0, "y": 0, "width": 4, "height": 2 }
    }
  ],
  "template_variables": [
    {
      "name": "env",
      "prefix": "env",
      "default": "prod",
      "available_values": ["prod", "staging", "dev"]
    }
  ],
  "reflow_type": "fixed | auto",
  "tags": ["env:prod", "team:sre"],
  "notify_list": ["@slack-channel"],
  "is_read_only": false
}
```

**Response (200):**

```json
{
  "id": "abc-def-ghi",
  "title": "My Dashboard",
  "description": "...",
  "url": "/dashboard/abc-def-ghi/my-dashboard",
  "layout_type": "ordered",
  "widgets": [...],
  "template_variables": [...],
  "created_at": "2024-01-15T10:30:00.000000+00:00",
  "modified_at": "2024-01-15T10:30:00.000000+00:00",
  "author_handle": "user@example.com"
}
```

Key field: `id` — the dashboard identifier used in URLs and subsequent API calls.

**Status codes:** `200` success, `400` invalid definition, `403` forbidden, `429` rate limited.

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v1/dashboard" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @dashboard-template.json
```

### PUT /api/v1/dashboard/{dashboard_id} — Update Dashboard

Full replacement of the dashboard definition. The request body must contain the complete dashboard object, not a partial patch. Fields omitted from the body will be reset to defaults.

**Status codes:** `200` success, `400` invalid, `403` forbidden, `404` not found, `429` rate limited.

**curl:**

```bash
curl -X PUT "https://api.datadoghq.com/api/v1/dashboard/${DASHBOARD_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @updated-dashboard.json
```

### GET /api/v1/dashboard — List Dashboards

Returns a paginated list of dashboard summary objects.

**Query parameters:**

| Param | Type | Default | Description |
|---|---|---|---|
| `filter[shared]` | bool | false | Return only shared dashboards |
| `filter[deleted]` | bool | false | Return only soft-deleted dashboards |
| `count` | int | 100 | Maximum number of results per page |
| `start` | int | 0 | Offset index for pagination |

**Response (200):**

```json
{
  "dashboards": [
    {
      "id": "abc-def-ghi",
      "title": "My Dashboard",
      "description": "...",
      "layout_type": "ordered",
      "url": "/dashboard/abc-def-ghi/my-dashboard",
      "created_at": "2024-01-15T10:30:00.000000+00:00",
      "modified_at": "2024-01-15T10:30:00.000000+00:00",
      "author_handle": "user@example.com",
      "is_read_only": false
    }
  ],
  "total": 245
}
```

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v1/dashboard?count=50&start=0" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### GET /api/v1/dashboard/{dashboard_id} — Get Single Dashboard

Returns the full dashboard definition including all widgets, template variables, and metadata.

**Status codes:** `200` success, `403` forbidden, `404` not found.

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v1/dashboard/${DASHBOARD_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### DELETE /api/v1/dashboard/{dashboard_id} — Delete Dashboard

Soft-deletes a dashboard. Deleted dashboards can be retrieved using `filter[deleted]=true` on the list endpoint.

**Status codes:** `200` success, `403` forbidden, `404` not found.

**curl:**

```bash
curl -X DELETE "https://api.datadoghq.com/api/v1/dashboard/${DASHBOARD_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### URL Construction

Dashboard URLs follow the pattern:

```
https://app.datadoghq.com/dashboard/{dashboard_id}
https://app.datadoghq.com{url_field_from_response}
```

The `url` field in the API response already includes the slug (e.g., `/dashboard/abc-def-ghi/my-dashboard`).

---

## Monitor API (v1)

Monitors are created independently and then referenced inside dashboard widgets (alert_graph, manage_status, monitor_summary).

### POST /api/v1/monitor — Create Monitor

**Request body schema:**

```json
{
  "name": "string (required)",
  "type": "metric alert | service check | event alert | query alert | composite | ... (required)",
  "query": "string — monitor query (required)",
  "message": "string — notification body with @mentions",
  "tags": ["env:prod", "service:my-app"],
  "priority": 3,
  "options": {
    "thresholds": {
      "critical": 90,
      "warning": 80,
      "ok": 50,
      "critical_recovery": 85,
      "warning_recovery": 75
    },
    "notify_no_data": true,
    "no_data_timeframe": 10,
    "notify_audit": false,
    "require_full_window": true,
    "renotify_interval": 60,
    "renotify_occurrences": 5,
    "escalation_message": "Still alerting after 1 hour",
    "include_tags": true,
    "evaluation_delay": 300,
    "new_group_delay": 60
  }
}
```

**Monitor types:** `metric alert`, `service check`, `event alert`, `event-v2 alert`, `query alert`, `composite`, `log alert`, `trace-analytics alert`, `slo alert`, `process alert`, `rum alert`, `ci-pipelines alert`, `audit alert`, `error-tracking alert`.

**Response (200):**

```json
{
  "id": 12345678,
  "org_id": 100,
  "type": "metric alert",
  "name": "High CPU on EC2",
  "query": "avg(last_5m):avg:aws.ec2.cpuutilization{*} > 90",
  "message": "CPU is above 90% @pagerduty",
  "tags": ["env:prod", "service:ec2"],
  "overall_state": "OK",
  "created": "2024-01-15T10:30:00+00:00",
  "modified": "2024-01-15T10:30:00+00:00",
  "creator": { "handle": "user@example.com" },
  "options": { "..." }
}
```

Key field: `id` (integer) — used as `alert_id` in dashboard widget definitions and as the trigger ID in workflow-automation.

**Status codes:** `200` success, `400` invalid query/options, `403` forbidden, `429` rate limited.

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v1/monitor" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### GET /api/v1/monitor — List/Search Monitors

**Query parameters:**

| Param | Type | Default | Description |
|---|---|---|---|
| `name` | string | — | Filter by monitor name (substring match) |
| `tags` | string | — | Comma-separated scope tags (e.g., `host:host0`) |
| `monitor_tags` | string | — | Comma-separated monitor tags (e.g., `service:my-app`) |
| `page` | int | 0 | Page number (0-indexed) |
| `page_size` | int | 100 | Results per page (max 1000) |
| `id_offset` | int | — | Return monitors with IDs greater than this value |
| `group_states` | string | — | Filter by state: `alert`, `warn`, `no data`, `ok` |
| `with_downtimes` | bool | false | Include active downtime info |

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v1/monitor?name=High%20CPU&page_size=50" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### PUT /api/v1/monitor/{monitor_id} — Update Monitor

Full replacement of the monitor definition. Include all fields that should persist.

**curl:**

```bash
curl -X PUT "https://api.datadoghq.com/api/v1/monitor/${MONITOR_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @monitor-config.json
```

### DELETE /api/v1/monitor/{monitor_id} — Delete Monitor

**Status codes:** `200` success, `400` bad request, `401` unauthorized, `403` forbidden, `404` not found.

**curl:**

```bash
curl -X DELETE "https://api.datadoghq.com/api/v1/monitor/${MONITOR_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Idempotent Create-or-Update Pattern

Search by name first, then update if found or create if not:

```bash
# Step 1: Search for existing monitor by name
EXISTING=$(curl -s "https://api.datadoghq.com/api/v1/monitor?name=High%20CPU%20on%20EC2" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}")

# Step 2: Parse the response — it returns an array
MONITOR_COUNT=$(echo "$EXISTING" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")

if [ "$MONITOR_COUNT" -gt 0 ]; then
  MONITOR_ID=$(echo "$EXISTING" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['id'])")
  # Update existing monitor
  curl -X PUT "https://api.datadoghq.com/api/v1/monitor/${MONITOR_ID}" \
    -H "DD-API-KEY: ${DD_API_KEY}" \
    -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
    -H "Content-Type: application/json" \
    -d @monitor-config.json
else
  # Create new monitor
  curl -X POST "https://api.datadoghq.com/api/v1/monitor" \
    -H "DD-API-KEY: ${DD_API_KEY}" \
    -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
    -H "Content-Type: application/json" \
    -d @monitor-config.json
fi
```

The Python helper `create_or_update_monitor()` in `examples/python/datadog_helpers.py` implements this pattern with proper error handling.

---

## Custom Metrics API (v2)

### POST /api/v2/series — Submit Metrics

Submits time-series data points to Datadog. Only requires `DD-API-KEY` (no application key).

**Request body schema:**

```json
{
  "series": [
    {
      "metric": "string — metric name (required)",
      "type": 1,
      "points": [
        {
          "timestamp": 1700000000,
          "value": 42.0
        }
      ],
      "tags": ["env:prod", "service:my-service"],
      "resources": [
        { "name": "my-host", "type": "host" }
      ],
      "unit": "byte",
      "interval": 60
    }
  ]
}
```

**Type values:** `0` unspecified, `1` count, `2` rate, `3` gauge.

- `timestamp`: Unix epoch in seconds.
- `resources`: Optional; associates the metric with a host or container.
- `interval`: Required for `rate` and `count` types; the collection interval in seconds.
- `unit`: Optional metadata for display purposes.

**Response (202):** `{"errors": []}` on success. Non-empty `errors` array on partial failure.

**Status codes:** `202` accepted, `400` invalid payload, `403` forbidden, `408` request timeout, `413` payload too large, `429` rate limited.

**curl:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/series" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "series": [{
      "metric": "my.app.event_count",
      "type": 1,
      "points": [{"timestamp": '"$(date +%s)"', "value": 42.0}],
      "tags": ["env:prod", "service:my-service"]
    }]
  }'
```

---

## Logs Intake API (v2)

### POST /api/v2/logs — Submit Logs

**URL:** `https://http-intake.logs.datadoghq.com/api/v2/logs` (not `api.datadoghq.com`).

Only requires `DD-API-KEY` (no application key).

**Request body schema (array of log entries):**

```json
[
  {
    "ddsource": "string — source name (e.g., python, my-lambda)",
    "ddtags": "string — comma-separated tags (e.g., env:prod,service:my-service)",
    "hostname": "string — originating host",
    "message": "string — the log message (required)",
    "service": "string — service name",
    "status": "info | warn | error | debug | critical"
  }
]
```

- The body is a JSON array (even for a single log entry).
- Maximum payload size: 5 MB.
- Maximum array length: 1000 entries per request.
- `message` is the only required field.

**Response (202):** Empty body on success.

**Status codes:** `202` accepted, `400` invalid payload, `403` forbidden, `408` timeout, `413` payload too large, `429` rate limited.

**curl:**

```bash
curl -X POST "https://http-intake.logs.datadoghq.com/api/v2/logs" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '[{
    "ddsource": "my-lambda",
    "ddtags": "env:prod,service:my-service",
    "hostname": "lambda-function",
    "message": "User action completed",
    "service": "my-service",
    "status": "info"
  }]'
```
