# Workflow Automation Trigger Types

Triggers define what starts a workflow execution. A single workflow spec can include multiple trigger blocks (e.g., both `apiTrigger` and `monitorTrigger`), allowing the same workflow to be invoked from different sources.

All triggers are defined in the `triggers` array within the workflow spec. Each trigger object has a `startStepNames` array indicating which step(s) to begin execution from, plus a trigger-type-specific configuration object.

```json
{
  "triggers": [
    {
      "startStepNames": ["First_step"],
      "<triggerType>": { "...config..." }
    }
  ]
}
```

---

## 1. Manual Trigger (apiTrigger)

The most common trigger for workflows invoked from the Datadog UI "Run" button or via the REST API. Define an `inputSchema` to declare required parameters that the caller must supply.

```json
{
  "triggers": [
    {
      "startStepNames": ["First_step"],
      "apiTrigger": {}
    }
  ],
  "inputSchema": {
    "parameters": [
      {
        "name": "service_name",
        "label": "Service Name",
        "description": "ECS service to roll back",
        "type": "STRING",
        "defaultValue": ""
      },
      {
        "name": "image_tag",
        "label": "Image Tag",
        "description": "Target image tag for rollback",
        "type": "STRING"
      },
      {
        "name": "dry_run",
        "label": "Dry Run",
        "description": "If true, preview changes without executing",
        "type": "BOOLEAN",
        "defaultValue": "false"
      }
    ]
  }
}
```

**Supported parameter types:** `STRING`, `BOOLEAN`, `NUMBER`, `OBJECT`, `ARRAY`.

**Accessing values in steps:** `{{ Trigger.service_name }}`, `{{ Trigger.image_tag }}`, `{{ Trigger.dry_run }}`.

When triggered via the UI, Datadog renders a form based on `inputSchema`. When triggered via API (`POST /api/v2/workflows/{id}/instances`), pass values in `meta.payload`.

---

## 2. Monitor Trigger (monitorTrigger)

Fires when a Datadog monitor transitions to an alert state. To connect a monitor to a workflow, add the workflow's `@workflow-` mention handle to the monitor's notification message.

```json
{
  "triggers": [
    {
      "startStepNames": ["Remediate_alert"],
      "monitorTrigger": {
        "rateLimit": {
          "count": 1,
          "interval": "3600s"
        }
      }
    }
  ]
}
```

**Rate limit configuration:**
- `count` -- Maximum number of executions within the interval
- `interval` -- Time window as a duration string (e.g., `"60s"`, `"3600s"`, `"86400s"`)
- If omitted, no rate limiting is applied (every alert triggers the workflow)

**Monitor notification syntax:**
Add this to the monitor message body:
```
@workflow-My-Workflow-Name
```

To pass key-value parameters from the monitor:
```
@workflow-My-Workflow-Name(service_name="web-api",region="us-east-1")
```

**Available source variables in steps:**
- `{{ Source.monitor.id }}` -- Monitor ID
- `{{ Source.monitor.name }}` -- Monitor name
- `{{ Source.monitor.query }}` -- Monitor query
- `{{ Source.monitor.type }}` -- Monitor type
- `{{ Source.monitor.message }}` -- Monitor message body
- `{{ Source.monitor.tags }}` -- Monitor tags (array)
- `{{ Source.monitor.status }}` -- Alert status (e.g., `Alert`, `Warn`, `OK`)

---

## 3. Dashboard Trigger (Run Workflow Widget)

Dashboards can trigger workflows through the **Run Workflow** widget. This is not a trigger type in the workflow spec; instead, the workflow uses an `apiTrigger` and the dashboard widget is configured to call it.

**Setup:**
1. Create the workflow with an `apiTrigger` and `inputSchema`
2. In the dashboard, add a "Run Workflow" widget
3. Configure the widget to target the workflow by ID or name
4. Map dashboard template variables to workflow input parameters

The widget renders a button in the dashboard. When clicked, it opens the input form (from `inputSchema`) and executes the workflow.

**Template variable mapping in the widget:**
```json
{
  "workflow_id": "<workflow-uuid>",
  "inputs": {
    "service_name": "$service.value",
    "environment": "$env.value"
  }
}
```

---

## 4. Incident Trigger (incidentTrigger)

Fires when a Datadog Incident Management incident is created, updated, or resolved.

```json
{
  "triggers": [
    {
      "startStepNames": ["Handle_incident"],
      "incidentTrigger": {}
    }
  ]
}
```

**Available source variables:**
- `{{ Source.incident.id }}` -- Incident ID
- `{{ Source.incident.title }}` -- Incident title
- `{{ Source.incident.severity }}` -- Severity level (SEV-1 through SEV-5)
- `{{ Source.incident.status }}` -- Status (active, stable, resolved)
- `{{ Source.incident.commander }}` -- Incident commander
- `{{ Source.incident.created }}` -- Creation timestamp
- `{{ Source.incident.fields }}` -- Custom incident fields

---

## 5. Security Trigger (securityTrigger)

Fires when a Datadog Cloud SIEM signal is generated. This is the primary trigger for automated security remediation workflows.

```json
{
  "triggers": [
    {
      "startStepNames": ["Disable_compromised_user"],
      "securityTrigger": {}
    }
  ]
}
```

**Available source variables:**

| Variable | Description | Example |
|---|---|---|
| `{{ Source.securityFinding.resource }}` | Primary resource identifier | IAM username, EC2 instance ID |
| `{{ Source.securityFinding.resourceConfiguration.group_id }}` | Resource config field | Security group ID |
| `{{ Source.securityFinding.resourceConfiguration.* }}` | Any field from the resource config | Varies by finding type |
| `{{ Source.securityFinding.severity }}` | Signal severity | `critical`, `high`, `medium`, `low`, `info` |
| `{{ Source.securityFinding.title }}` | Signal rule name | "Impossible Travel detected" |
| `{{ Source.securityFinding.message }}` | Signal description | Rule-defined message |
| `{{ Source.securityFinding.tags }}` | Tags on the signal | Array of strings |
| `{{ Source.securityFinding.attributes }}` | Full attributes map | Raw signal attributes |

**Important:** The structure of `resourceConfiguration` varies depending on the SIEM rule and AWS resource type. Always verify the specific fields available for your finding type by examining a sample signal in the Datadog Security Signals explorer.

---

## 6. Software Catalog Trigger (catalogTrigger)

Fires on Software Catalog entity events such as scorecard rule evaluations or metadata changes.

```json
{
  "triggers": [
    {
      "startStepNames": ["Process_catalog_event"],
      "catalogTrigger": {}
    }
  ]
}
```

**Available source variables:**
- `{{ Source.catalog.entity.name }}` -- Entity name
- `{{ Source.catalog.entity.kind }}` -- Entity kind (service, datastore, queue, etc.)
- `{{ Source.catalog.entity.owner }}` -- Owning team
- `{{ Source.catalog.event.type }}` -- Event type

---

## 7. GitHub Trigger (Webhook)

Workflows can be triggered by GitHub events via webhooks. This requires configuring a GitHub webhook to send events to a Datadog-provided URL.

**Setup:**
1. In the Datadog Workflow Automation UI, create a workflow with a `webhookTrigger`
2. Copy the generated webhook URL from the trigger configuration
3. In your GitHub repository settings, add a webhook pointing to that URL
4. Select the events to trigger on (e.g., `push`, `pull_request`, `issues`)

```json
{
  "triggers": [
    {
      "startStepNames": ["Process_github_event"],
      "webhookTrigger": {
        "source": "github"
      }
    }
  ]
}
```

**Available source variables:**
- `{{ Source.webhook.body }}` -- Full webhook payload as JSON
- `{{ Source.webhook.headers }}` -- HTTP headers
- Parse specific fields using data transformation steps: `{{ Source.webhook.body.action }}`, `{{ Source.webhook.body.repository.full_name }}`

---

## 8. Slack Trigger

Workflows can be invoked from Slack using the `/datadog workflow` command in any channel where the Datadog Slack integration is installed.

**Slack command syntax:**
```
/datadog workflow run "My Workflow Name" --param1 value1 --param2 value2
```

The workflow must have an `apiTrigger` configured. Parameters passed via `--param` flags are matched to `inputSchema` parameter names.

**Setup requirements:**
1. Datadog Slack integration must be installed in the workspace
2. The workflow must be published and have an `apiTrigger`
3. The user must have `workflows_run` permissions in Datadog

---

## 9. API Trigger (Direct REST Invocation)

Any external system can trigger a workflow by calling the execution API endpoint directly. This uses the same `apiTrigger` configuration as the manual trigger.

**curl example:**

```bash
curl -X POST "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "meta": {
      "payload": {
        "service_name": "my-ecs-service",
        "image_tag": "v1.2.3"
      }
    }
  }'
```

**Response:**
```json
{
  "data": {
    "id": "instance-uuid-here"
  }
}
```

Use the returned instance ID to poll status at `GET /api/v2/workflows/{workflow_id}/instances/{instance_id}`.

**Common integrations:** CI/CD pipelines (GitHub Actions, Jenkins, GitLab CI), custom scripts, AWS Lambda, PagerDuty webhooks.

---

## 10. Scheduled Trigger (scheduleTrigger)

Runs a workflow on a recurring schedule using cron syntax.

```json
{
  "triggers": [
    {
      "startStepNames": ["Check_compliance"],
      "scheduleTrigger": {
        "cronExpression": "0 9 * * 1-5",
        "timezone": "America/New_York"
      }
    }
  ]
}
```

**Cron syntax:** Standard 5-field cron: `minute hour day-of-month month day-of-week`

| Schedule | Cron Expression |
|---|---|
| Every hour | `0 * * * *` |
| Daily at 9 AM UTC | `0 9 * * *` |
| Weekdays at 9 AM ET | `0 9 * * 1-5` (with `timezone: "America/New_York"`) |
| Every 15 minutes | `*/15 * * * *` |
| First Monday of month at midnight | `0 0 1-7 * 1` |

**Service account requirement:** Scheduled workflows execute under a service account context rather than a specific user's credentials. The service account must have the necessary app key scopes. When you publish a workflow with a `scheduleTrigger`, Datadog automatically configures the service account association.

**Important notes:**
- The `timezone` field defaults to UTC if omitted
- Minimum schedule interval is 1 minute
- Scheduled workflows still respect the workflow-level rate limits
- No `inputSchema` parameters are available since there is no caller; use hardcoded values or fetch configuration from external sources in the first step

---

## 11. Workflow-to-Workflow Trigger (workflowTrigger / Child Workflows)

A parent workflow can invoke a child workflow as a step, passing parameters and receiving outputs.

```json
{
  "triggers": [
    {
      "startStepNames": ["Process_input"],
      "workflowTrigger": {}
    }
  ]
}
```

**Calling a child workflow from a parent step:**

The parent workflow uses the `com.datadoghq.dd.workflow.execute` action to invoke the child:

```json
{
  "name": "Run_child_workflow",
  "actionId": "com.datadoghq.dd.workflow.execute",
  "parameters": [
    { "name": "workflowId", "value": "child-workflow-uuid" },
    { "name": "payload", "value": { "param1": "{{ Steps.Previous.output }}" } }
  ]
}
```

**Accessing child workflow outputs in the parent:**
- `{{ Steps.Run_child_workflow.outputs }}` -- Full outputs object
- `{{ Steps.Run_child_workflow.outputs.result_key }}` -- Specific output field
- `{{ Steps.Run_child_workflow.status }}` -- Execution status of the child

**Output parameters:** The child workflow defines output parameters to expose values back to the parent. Configure these in the workflow's Output Parameters section (see `references/flow-control-and-expressions.md`).

**Use cases:**
- Reusable remediation sub-workflows (e.g., a "disable IAM user" child called by multiple parent workflows)
- Fan-out patterns: a parent iterates over a list and calls a child workflow for each item
- Separation of concerns: keep complex workflows modular
