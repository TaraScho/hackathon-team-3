---
name: workflow-automation
description: >
  Creates Datadog Workflow Automation workflows — multi-step automated remediation
  triggered by security signals, monitors, or manual execution. Covers spec
  authoring (steps, triggers, connectionEnvs) and common patterns:
  IAM disable user, ECS rollback, revoke insecure ingress, data transforms.
  Trigger phrases: "workflow automation", "automated remediation", "security trigger",
  "monitor trigger", "ECS rollback", "connectionEnvs", "workflow spec JSON".
  Do NOT use for IAM connections (use action-connections), app UIs
  (use app-builder), or dashboards (use dashboards).
metadata:
  author: hackathon-team-3
  tags: [workflow-automation, security, remediation, iam, ecs, ec2, aws]
  category: infrastructure
---

# Workflow Automation Skill

## Overview

Datadog Workflow Automation runs multi-step runbooks in response to security signals, monitor alerts, or manual triggers. Each workflow is a directed graph of `steps`, each calling an AWS action (or Datadog API) via an action connection.

### Dependency Diagram

```
(action-connections → workflow-automation) × M workflows
```

Each workflow gets its own dedicated action connection (1:1 — never shared).

---

## Doc Fetch URLs

Before executing, fetch current API and product documentation:

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/workflow-automation.md` |
| Triggers reference | `https://docs.datadoghq.com/actions/workflows/triggers.md` |
| Build workflows | `https://docs.datadoghq.com/actions/workflows/build.md` |
| Actions reference | `https://docs.datadoghq.com/actions/workflows/actions.md` |
| Expressions | `https://docs.datadoghq.com/actions/workflows/expressions.md` |
| Terraform provider | TF MCP → `datadog_workflow_automation` |

---

## Output Format Selection

Read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` |
| `shell` | Claude executes `curl` commands directly via Bash tool |

---

## When to Use

- You need automated incident response for AWS resources triggered by Datadog findings
- You want to automate operational runbooks (ECS rollbacks, tag enforcement, scorecard updates)
- You need a monitor to trigger remediation automatically
- You want to chain multiple AWS API calls in a workflow

---

## Prerequisites

| Requirement | Details |
|---|---|
| Action connection | Created via action-connections skill; UUID goes in `connectionEnvs` |
| App key scopes | `workflows_read`, `workflows_write`, `workflows_run`, `connections_read`, `connections_resolve` |

---

## Core Workflow: Submit a Workflow Spec

All API calls require headers: `DD-API-KEY`, `DD-APPLICATION-KEY`, `Content-Type: application/json`.

### Workflow spec structure

```json
{
  "name": "Workflow Name",
  "spec": {
    "triggers": [...],
    "steps": [...],
    "connectionEnvs": [...],
    "inputSchema": {...}
  }
}
```

- **`steps`** — ordered actions; each has `name`, `actionId`, `connectionLabel`, `parameters`, optional `outboundEdges`
- **`triggers`** — what starts the workflow: `securityTrigger`, `monitorTrigger`, `workflowTrigger`, `apiTrigger`, etc.
- **`connectionEnvs`** — maps a label to a real connection ID per environment
- **`inputSchema`** — parameters the caller supplies at runtime

### Step 1 — Prepare the spec

Load a template from `examples/json/`, replace `__CONNECTION_ID__` with the real UUID in `connectionEnvs[].connections[].connectionId`.

### Step 2 — Create the workflow

`POST /api/v2/workflows` with the spec wrapped in API envelope:

```json
{
  "data": {
    "type": "workflows",
    "attributes": {
      "name": "Workflow Name",
      "description": "...",
      "published": true,
      "spec": { ...spec from template... }
    }
  }
}
```

Note: `data.type` must be `"workflows"` (plural).

### Step 3 — Verify

Check response for `data.id` (workflow UUID). Save for dashboard embedding.

---

## Variable Interpolation

| Context | Syntax | Example |
|---|---|---|
| Step output | `{{ Steps.StepName.fieldName }}` | `{{ Steps.Describe_task_definition.taskDefinition.cpu }}` |
| Security trigger | `{{ Source.securityFinding.resource }}` | IAM username from SIEM alert |
| Monitor trigger | `{{ Source.monitor.* }}` | Monitor alert data |
| Manual/API trigger | `{{ Trigger.param_name }}` | `{{ Trigger.service_name }}` |
| Loop value | `{{ Current.Value }}` | Inside a `forLoop` step |

---

## Trigger Types

| Trigger key | When to use |
|---|---|
| `securityTrigger` | Cloud SIEM signal fires |
| `monitorTrigger` | Monitor alert |
| `apiTrigger` | Manual execution or API call |
| `workflowTrigger` | Another workflow calls this one |

A workflow spec can include multiple trigger blocks. Workflows with `apiTrigger` can be triggered from dashboard `run_workflow` widgets.

---

## Top 10 Action IDs

| Action ID | Service | Operation |
|---|---|---|
| `com.datadoghq.aws.iam.disable_user` | IAM | Disable IAM user login |
| `com.datadoghq.aws.ec2.revoke_security_group_ingress` | EC2 | Remove SG ingress rules |
| `com.datadoghq.aws.ec2.modify_instance_metadata_options` | EC2 | Enforce IMDSv2 |
| `com.datadoghq.aws.ecs.describeTaskDefinition` | ECS | Get task definition details |
| `com.datadoghq.aws.ecs.registerTaskDefinition` | ECS | Register new revision |
| `com.datadoghq.aws.ecs.updateEcsService` | ECS | Update service |
| `com.datadoghq.datatransformation.func` | Transform | Run JavaScript function |
| `com.datadoghq.core.forLoop` | Core | Iterate over a list |
| `com.datadoghq.core.if` | Core | Conditional branch |
| `com.datadoghq.dd.cases.createCase` | Datadog | Create a case/incident |

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **`connectionLabel` case-sensitivity** | Must **exactly match** (case-sensitive) the `label` in `connectionEnvs[].connections[].label` |
| **`data.type` is plural** | Must be `"workflows"` not `"workflow"` |
| **If branch names** | Must be exactly `"true"` and `"false"` (strings, lowercase), NOT boolean values |
| **Loop branch names** | Must be exactly `"loop"` and `"after_loop"` |
| **Error branch name** | Must be exactly `"error"` (lowercase) |
| **No list API by name** | Cannot query workflows by name or handle — must track ID externally |
| **409 = handle exists** | Workflow handle already exists; requires external ID lookup to update |
| **Monitor trigger syntax** | `@workflow-My-Workflow-Name` in monitor message body; params: `@workflow-Name(param="value")` |
| **Rate limits** | Without rate limiting on triggers, every alert fires the workflow — set `{ "count": 1, "interval": "3600s" }` |
| **JavaScript steps** | Must define `function main(args)` and return value; max 10 KB script size |
| **Python steps** | Must define `def main(ctx)` and return serializable value; Python 3.12.8 runtime |
| **Loop iteration limit** | 2,000 per loop; automatic silent exit if exceeded |
| **Max steps per workflow** | 150 |
| **Workflow execution timeout** | 7 days maximum |
| **Security trigger resources** | `resourceConfiguration.*` fields vary by AWS resource type — verify field availability |
| **Scheduled trigger** | Executes under service account context; no `inputSchema` parameters available |

---

## Cross-Skill Notes

- **Delegates to action-connections**: Connection creation is handled by the action-connections skill.
- **Monitor IDs from dashboards**: Monitors created by the dashboards skill can be used as `monitorTrigger` sources.
- **Dashboard embedding**: Include `apiTrigger` alongside primary trigger to enable dashboard `run_workflow` widgets.
- **Scorecard updates**: Use `com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome` to mark pass/fail after remediation.

---

## JSON Examples

Seven workflow spec templates in `examples/json/`:

| File | Pattern |
|---|---|
| `AWS-IAM-Disable-User.json` | Single-step security trigger — disable IAM user |
| `AWS-IAM-Revoke-Permissions.json` | Revoke IAM permissions on security finding |
| `AWS-EC2-Require-IMDS-v2_spec.json` | Enforce IMDSv2 on EC2 instances |
| `ECS-Rollback-Leaderboard.json` | 4-step ECS rollback with data transform |
| `workflow-remove-insecure-ingress.json` | Multi-step EC2 security group remediation |
| `workflow-remove-insecure-ingress-simple.json` | Simplified ingress revocation |
| `cloud-siem-waf-workflow-spec.json` | Cloud SIEM WAF workflow |

All templates use `__CONNECTION_ID__` as the connection placeholder (except `cloud-siem-waf-workflow-spec.json` which uses `${connection_id}` for Terraform templatefile compatibility). All bare specs have been wrapped in `{ "name": "...", "spec": { ... } }` format.
