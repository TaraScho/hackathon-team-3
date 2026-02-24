# Embedded Apps Reference

Guide to embedding Datadog App Builder apps in dashboards, notebooks, and the Software Catalog.

---

## Dashboard Embedding

App Builder apps are embedded in dashboards using the `app` widget type. The app renders inside the dashboard and can synchronize with dashboard template variables and time frames.

### Dashboard Widget Configuration

Add an app widget to a dashboard JSON template:

```json
{
  "definition": {
    "type": "app",
    "app_id": "12345678-abcd-efgh-ijkl-123456789012",
    "custom_links": [],
    "title": "EC2 Management",
    "title_size": "16",
    "title_align": "left"
  },
  "layout": {
    "x": 0,
    "y": 0,
    "width": 12,
    "height": 6
  }
}
```

**Layout sizing guidelines:**

| App Complexity | Width | Height | Notes |
|----------------|-------|--------|-------|
| Single table | 8-12 | 4-6 | Minimum usable size |
| Table + filters | 12 | 5-7 | Full-width recommended |
| Table + details panel | 12 | 7-10 | Needs vertical space for side content |
| Multi-tab app | 12 | 8-12 | Tabs need room for content |
| Dashboard-only stat | 4-6 | 2-3 | Compact metric display |

Width is measured in dashboard grid units (max 12). Height is in grid units (each unit is approximately 40px).

### Input Parameters

Apps can receive input parameters from the dashboard at embed time. Define parameters in the app, then pass values from the widget configuration.

**In the app JSON (query input):**
```json
{
  "name": "listInstances",
  "type": "action",
  "properties": {
    "inputs": {
      "region": "{{ global.inputParameters.region || 'us-east-1' }}"
    }
  }
}
```

**In the dashboard widget:**
```json
{
  "definition": {
    "type": "app",
    "app_id": "...",
    "parameters": {
      "region": "us-west-2"
    }
  }
}
```

Input parameters let you reuse the same app across multiple dashboards with different configurations. For example, one dashboard embeds the EC2 app filtered to `us-east-1`, another to `eu-west-1`.

---

## Template Variable Synchronization

When an app is embedded in a dashboard, it can read the dashboard's template variables to stay in sync with dashboard filters.

### Reading Template Variables

Access template variables via the `global.dashboard.templateVariables` object:

```
{{ global?.dashboard?.templateVariables }}
```

This returns an object where keys are template variable names and values are arrays of selected values:

```json
{
  "region": ["us-east-1"],
  "environment": ["production", "staging"],
  "team": ["platform"]
}
```

### Using Template Variables in Queries

Reference a template variable in a query input:

```json
{
  "name": "listInstances",
  "type": "action",
  "properties": {
    "inputs": {
      "region": "{{ global?.dashboard?.templateVariables?.region?.[0] || 'us-east-1' }}"
    }
  }
}
```

Always use optional chaining (`?.`) because `global.dashboard` is `undefined` when the app runs standalone (not embedded).

### Filtering Table Data by Template Variables

Use a DataTransform to filter action query results by template variable values:

```json
{
  "name": "filteredInstances",
  "type": "dataTransform",
  "properties": {
    "expression": "const instances = queries.listInstances.data.instances; const envFilter = global?.dashboard?.templateVariables?.environment; if (!envFilter || envFilter.length === 0) return instances; return instances.filter(i => { const envTag = i.tags?.find(t => t.key === 'env'); return envTag && envFilter.includes(envTag.value); })"
  }
}
```

### Handling the Standalone Case

Apps should work both embedded and standalone. Use fallback defaults:

```
{{ global?.dashboard?.templateVariables?.region?.[0] || state.defaultRegion || 'us-east-1' }}
```

This checks: dashboard template variable first, then app-level state variable, then hardcoded default.

---

## Time Frame Synchronization

Embedded apps can read the dashboard's time frame selection:

```
{{ global?.dashboard?.timeframe }}
```

Returns an object:
```json
{
  "from": 1708700000000,
  "to": 1708786400000,
  "live": true
}
```

- `from` / `to`: Unix timestamps in milliseconds
- `live`: `true` if the dashboard is using a relative time frame (e.g., "Past 1 hour")

Use the time frame in metric queries or to display time-bounded data:

```json
{
  "name": "getMetrics",
  "type": "action",
  "properties": {
    "inputs": {
      "from": "{{ global?.dashboard?.timeframe?.from || Date.now() - 3600000 }}",
      "to": "{{ global?.dashboard?.timeframe?.to || Date.now() }}"
    }
  }
}
```

---

## Software Catalog Self-Service Actions

App Builder apps can be registered as self-service actions in the Datadog Software Catalog. This lets service owners trigger apps directly from their service's catalog page.

### Registering an App as a Self-Service Action

In the service entity definition (v3 schema), add an `extensions` block:

```yaml
apiVersion: v3
kind: service
metadata:
  name: payment-service
spec:
  owner: platform-team
  # ...
extensions:
  datadogAppBuilder:
    selfServiceActions:
      - name: "Manage EC2 Instances"
        appId: "12345678-abcd-efgh-ijkl-123456789012"
        description: "Start, stop, and reboot EC2 instances for this service"
        parameters:
          environment: "production"
          service: "payment-service"
```

When a user views the `payment-service` page in the catalog, they see a "Manage EC2 Instances" action button that opens the app with the specified parameters pre-filled.

### Dynamic Parameters from Catalog Context

The app receives catalog context via `global.inputParameters`:

```json
{
  "inputs": {
    "serviceName": "{{ global.inputParameters.service }}",
    "environment": "{{ global.inputParameters.environment }}"
  }
}
```

---

## Embedding in Notebooks

App Builder apps can be embedded in Datadog Notebooks using the app cell type. This is useful for runbooks and incident response documentation.

### Notebook Cell Configuration

```json
{
  "type": "app",
  "app_id": "12345678-abcd-efgh-ijkl-123456789012",
  "width": "full",
  "height": 400,
  "parameters": {
    "region": "us-east-1"
  }
}
```

- `width`: `"full"` (spans the notebook width) or `"half"`
- `height`: Height in pixels (minimum 200)
- `parameters`: Same input parameter mechanism as dashboard embedding

### Notebook Use Cases

- **Incident runbooks:** Embed an EC2 management app next to remediation steps so responders can act without switching tools
- **Onboarding guides:** Embed apps alongside explanatory markdown cells
- **Post-mortem templates:** Include apps that show the state of infrastructure at the time of the incident

---

## Placeholder Substitution Pattern

When deploying apps and dashboards together programmatically, dashboard templates use placeholder strings for app IDs. These are replaced after the apps are created.

### Standard Placeholder Convention

```
APP_ID_PLACEHOLDER_{SERVICE_NAME}
```

Examples:
- `APP_ID_PLACEHOLDER_EC2_MANAGEMENT`
- `APP_ID_PLACEHOLDER_ECS_MANAGEMENT`
- `APP_ID_PLACEHOLDER_S3_EXPLORER`

### Substitution Flow

1. Create all apps via the App Builder API (collect their UUIDs)
2. Load the dashboard JSON template
3. Replace each placeholder with the real app UUID
4. Create the dashboard via the Dashboard API

```python
APP_NAME_TO_KEY = {
    "ec2-management-console": "APP_ID_PLACEHOLDER_EC2_MANAGEMENT",
    "manage-ecs-tasks":       "APP_ID_PLACEHOLDER_ECS_MANAGEMENT",
    "explore-s3":             "APP_ID_PLACEHOLDER_S3_EXPLORER",
}

app_id_map = {
    APP_NAME_TO_KEY[name]: app_id
    for name, app_id in created_apps.items()
}

dashboard_json = load_template("dashboard-template.json")
for placeholder, real_id in app_id_map.items():
    dashboard_json = dashboard_json.replace(placeholder, real_id)
```

This pattern is implemented in `../dashboards/examples/python/datadog_helpers.py` via the `create_dashboard_with_embedded_apps()` function.
