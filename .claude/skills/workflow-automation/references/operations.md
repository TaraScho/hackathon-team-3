# Workflow Automation Operations

This reference covers publishing, versioning, rate limits, billing, monitoring, and operational best practices for Datadog Workflow Automation.

---

## Publishing and Versioning

### Draft vs Published

Workflows exist in two states:

- **Draft** (`published: false`) -- The workflow is saved but will not execute on triggers. Useful for iterating on spec changes without impacting production. Manual API execution is still possible for testing.
- **Published** (`published: true`) -- The workflow is active. All configured triggers (monitors, schedules, security signals) will invoke it.

Toggle publishing state via PATCH:

```json
{
  "data": {
    "type": "workflows",
    "attributes": {
      "published": true
    }
  }
}
```

### Versioning

Datadog Workflow Automation does not expose a built-in version history API. Each PATCH to a workflow overwrites the previous spec. To maintain version history:

1. **Terraform state** -- If managed via Terraform, the state file tracks changes and `terraform plan` shows diffs before applying
2. **Git-based spec files** -- Store workflow JSON specs in version control and deploy via CI/CD using the API
3. **Manual snapshots** -- Before updating, GET the current workflow and save the response as a backup

**Recommended pattern:** Store the canonical workflow spec as a JSON file in your repository, use CI/CD to deploy it via the API, and rely on Git for change tracking and rollback.

---

## Rate Limits and Throttling

### Account-Level Limits

| Resource | Limit | Notes |
|---|---|---|
| Workflow create/update requests | 500 per minute | `POST` and `PATCH /api/v2/workflows` combined |
| Workflow execution requests | 200 per minute | `POST /api/v2/workflows/{id}/instances` |
| Total active workflows | No hard cap | Subject to billing plan |

When limits are exceeded, the API returns `429 Too Many Requests` with a `Retry-After` header indicating how many seconds to wait.

### Workflow-Level Limits

| Resource | Limit |
|---|---|
| Maximum steps per workflow | 150 |
| Maximum workflow execution duration | 7 days |
| Step execution rate | 60 steps per minute per workflow instance |
| Total output size per execution | 150 MB |
| Loop iterations (For Loop, While Loop) | 2,000 per loop |

### Action-Level Limits

| Resource | Limit |
|---|---|
| Action input payload size | 15 MB |
| Action output payload size | 15 MB |
| JavaScript function script size | 10 KB |
| Python function script size | 10 KB |

### Trigger-Level Rate Limits

Monitor and security triggers support explicit rate limiting to prevent alert storms from overwhelming downstream systems:

```json
{
  "monitorTrigger": {
    "rateLimit": {
      "count": 1,
      "interval": "3600s"
    }
  }
}
```

This limits the workflow to 1 execution per 3,600 seconds (1 hour), regardless of how many monitor alerts fire. Without a rate limit, every alert transition triggers an execution.

---

## Billing Model

### SKU and Allotments

Workflow Automation billing is based on **workflow executions** (each time a workflow runs counts as one execution).

| Component | Description |
|---|---|
| **Committed executions** | Pre-purchased execution volume at a fixed rate per billing period |
| **On-demand executions** | Executions exceeding the committed volume, billed at a higher per-execution rate |

### Free Workflow Executions

Certain Datadog products include free workflow executions:

| Product | Free Executions |
|---|---|
| **Incident Management** | Workflows triggered by incidents (via `incidentTrigger`) |
| **On-Call** | Workflows triggered by on-call escalations |
| **App Builder** | Workflows invoked from App Builder applications |

These free executions apply only when the workflow is triggered through the qualifying product. The same workflow triggered via API or monitor does not qualify for free executions.

### Cost Optimization Tips

- Use `rateLimit` on monitor/security triggers to cap executions during alert storms
- Consolidate related steps into a single workflow rather than chaining multiple workflows
- Use If/Switch conditions early in the workflow to exit quickly when no action is needed
- Avoid scheduled workflows with very short intervals (e.g., every minute) unless necessary
- Monitor execution counts via the Workflow Automation dashboard (see Monitoring Metrics below)

---

## Notifications

Workflows can send notifications at any point during execution using built-in notification actions:

### Slack Notification Step

**Action ID:** `com.datadoghq.slack.send_simple_message`

```json
{
  "name": "Notify_team",
  "actionId": "com.datadoghq.slack.send_simple_message",
  "parameters": [
    { "name": "channel", "value": "#security-alerts" },
    { "name": "text", "value": "Remediation completed for {{ Source.securityFinding.resource }}" }
  ]
}
```

### Email Notification Step

**Action ID:** `com.datadoghq.notification.email`

```json
{
  "name": "Email_report",
  "actionId": "com.datadoghq.notification.email",
  "parameters": [
    { "name": "to", "value": "security-team@company.com" },
    { "name": "subject", "value": "Security Remediation Report" },
    { "name": "body", "value": "Workflow completed. Affected resource: {{ Steps.Remediate.result }}" }
  ]
}
```

### Datadog Event Step

**Action ID:** `com.datadoghq.dd.events.post`

Posts an event to the Datadog Events Explorer, useful for audit trails.

---

## Saved Actions

Saved actions are reusable, pre-configured action steps that can be shared across multiple workflows. They encapsulate an action with specific parameters, connection settings, and retry configuration.

**Creating a saved action (via UI):**
1. In the Workflow Automation editor, configure a step with all desired parameters
2. Click "Save as Saved Action" and give it a name
3. The saved action appears in the action palette for all workflow authors

**Using a saved action in a spec:**
Saved actions are referenced by their saved action ID rather than the raw `actionId`. The connection and default parameters come from the saved action definition, though they can be overridden per step.

**Use cases:**
- Standardized notification steps (same Slack channel, message format)
- Pre-configured AWS actions with correct connection labels
- Approved remediation actions with proper retry and error handling

---

## Audit Trail

All workflow operations are recorded in the Datadog Audit Trail:

| Event | What is Logged |
|---|---|
| Workflow created | Creator, workflow name, initial spec |
| Workflow updated | Updater, changed fields |
| Workflow deleted | Deleter, workflow name |
| Workflow published/unpublished | User, state change |
| Workflow executed | Trigger source, input parameters, instance ID |
| Workflow execution completed/failed | Status, duration, error details |

**Accessing audit logs:**
- Datadog UI: Organization Settings > Audit Trail
- API: `GET /api/v2/audit/events` with `source:workflow` filter

Audit events include the `@usr.email` attribute identifying who performed the action, and `@evt.name` for the event type.

---

## Monitoring Metrics

Datadog emits metrics about workflow execution that you can use in monitors and dashboards:

| Metric | Description |
|---|---|
| `datadog.workflow.executions.count` | Total executions by workflow, status, trigger type |
| `datadog.workflow.executions.duration` | Execution duration in seconds |
| `datadog.workflow.executions.errors` | Failed execution count |
| `datadog.workflow.steps.count` | Steps executed per workflow run |
| `datadog.workflow.steps.duration` | Per-step execution time |

**Recommended monitors:**
- Alert when a critical remediation workflow fails: `datadog.workflow.executions.errors` filtered by workflow name
- Track execution latency: `avg:datadog.workflow.executions.duration{workflow_name:ecs-rollback} > 300`
- Detect execution storms: `sum:datadog.workflow.executions.count{*} > 100` over 5 minutes

**Dashboard integration:** Use these metrics in the dashboards skill to create operational visibility panels alongside your infrastructure dashboards.

---

## Permissions and RBAC

### Workflow-Level Permissions

Workflows inherit Datadog's role-based access control (RBAC):

| Permission | Allows |
|---|---|
| `workflows_read` | View workflows and execution history |
| `workflows_write` | Create, edit, delete, publish workflows |
| `workflows_run` | Trigger workflow executions |

### Connection Permissions

Workflows access external services (AWS, Slack, etc.) through action connections. The connection's IAM role or API key defines what the workflow can do in the external service. See the `action-connections` skill for IAM role setup.

### Principle of Least Privilege

Each workflow should use a dedicated action connection with only the IAM permissions the workflow's steps actually need. This limits blast radius if a workflow is misconfigured or triggered unexpectedly.

---

## Operational Best Practices

1. **Always set rate limits on monitor/security triggers** to prevent alert storms from creating thousands of executions
2. **Use error branches on critical steps** to handle AWS API failures gracefully (e.g., notify the team instead of silently failing)
3. **Add retry configuration to AWS API steps** with exponential backoff to handle transient throttling
4. **Test workflows in draft mode** using manual API execution before publishing
5. **Store workflow specs in Git** and deploy via CI/CD for auditability and rollback capability
6. **Monitor workflow metrics** and set alerts on failure rates for critical remediation workflows
7. **Use meaningful step names** that describe the action (e.g., `Disable_compromised_user` not `Step_1`)
8. **Keep workflows under 20 steps** when possible; break complex flows into parent/child workflows
9. **Document inputSchema parameters** with clear labels and descriptions so other team members can use the workflow
10. **Review IAM permissions quarterly** to ensure connections are not over-provisioned
