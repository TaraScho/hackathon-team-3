---
name: workflow-automation
description: >
  Creates Datadog Workflow Automation workflows — multi-step automated remediation
  triggered by security signals, monitors, or manual execution. Covers spec
  authoring (steps, triggers, connectionEnvs), Terraform, and common patterns:
  IAM disable user, ECS rollback, revoke insecure ingress, data transforms.
  Trigger phrases: "workflow automation", "automated remediation", "security trigger",
  "monitor trigger", "ECS rollback", "connectionEnvs", "workflow spec JSON".
  Do NOT use for IAM connections (use action-connections), app UIs
  (use app-builder), or dashboards (use dashboards).
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars
  (app key scopes: workflows_read, workflows_write, workflows_run).
metadata:
  author: hackathon-team-3
  version: 1.1.0
  tags: [workflow-automation, security, remediation, iam, ecs, ec2, terraform, aws]
  category: infrastructure
---

# Workflow Automation Skill

## Overview

Datadog Workflow Automation runs multi-step runbooks in response to security signals, monitor alerts, or manual triggers. Each workflow is a directed graph of `steps`, each calling an AWS action (or Datadog API) via an action connection.

### Core spec structure

```json
{
  "steps": [...],
  "triggers": [...],
  "connectionEnvs": [...],
  "inputSchema": {...}
}
```

- **`steps`** — ordered actions; each has a `name`, `actionId`, `connectionLabel`, `parameters`, and optional `outboundEdges`
- **`triggers`** — what starts the workflow: `securityTrigger`, `monitorTrigger`, `workflowTrigger`, or `apiTrigger`
- **`connectionEnvs`** — maps a label (e.g., `INTEGRATION_AWS`) to a real connection ID per environment
- **`inputSchema`** — parameters the caller supplies at runtime (for manual/API triggers)

### Variable interpolation syntax

| Context | Syntax | Example |
|---|---|---|
| Step output | `{{ Steps.StepName.fieldName }}` | `{{ Steps.Describe_task_definition.taskDefinition.cpu }}` |
| Security trigger source | `{{ Source.securityFinding.resource }}` | IAM username from a SIEM alert |
| Security trigger resource config | `{{ Source.securityFinding.resourceConfiguration.group_id }}` | EC2 security group ID |
| Manual/API trigger param | `{{ Trigger.param_name }}` | `{{ Trigger.service_name }}` |
| Current loop value | `{{ Current.Value }}` | Inside a `forLoop` step |

### Dependency Diagram

```
action-connections ──► workflow-automation
```

A working action connection is required before any workflow can execute AWS steps.

---

## When to Use

- You need automated incident response that acts on AWS resources when Datadog detects a security finding
- You want to automate operational runbooks (ECS rollbacks, tag enforcement, scorecard updates)
- You are building IaC-driven provisioning that chains multiple AWS API calls
- You want a monitor to trigger remediation automatically (monitorTrigger)
- You need to write a Terraform module that includes both the connection and the workflow

---

## Prerequisites

| Requirement | Details |
|---|---|
| Action connection | Created automatically via action-connections skill if not provided; or provide an existing UUID in `connectionEnvs` |
| App key scopes | `workflows_read`, `workflows_write`, `workflows_run`, `connections_read`, `connections_resolve` |
| IAM role permissions | Auto-scoped when using least-privilege setup; the role gets exactly the permissions needed by the workflow steps |

**Note:** The action-connections skill handles IAM role creation and permission scoping. You do not need to create IAM roles manually.

---

## Trigger Types

| Trigger key | When to use | Source variables available |
|---|---|---|
| `securityTrigger` | Datadog Cloud SIEM signal fires | `{{ Source.securityFinding.* }}` |
| `monitorTrigger` | Datadog monitor alert | `{{ Source.monitor.* }}` |
| `workflowTrigger` | Another workflow calls this one | `{{ Trigger.* }}` (caller params) |
| `apiTrigger` | Manual execution or API call | `{{ Trigger.* }}` (inputSchema params) |

A workflow spec can include multiple trigger blocks (e.g., both `apiTrigger` and `monitorTrigger`). For all 11 trigger types with full configuration, see `references/triggers.md`.

---

## Top 10 Action IDs

| Action ID | Service | Operation |
|---|---|---|
| `com.datadoghq.aws.iam.disable_user` | IAM | Disable IAM user login |
| `com.datadoghq.aws.ec2.revoke_security_group_ingress` | EC2 | Remove security group ingress rules |
| `com.datadoghq.aws.ec2.modify_instance_metadata_options` | EC2 | Enforce IMDSv2 |
| `com.datadoghq.aws.ecs.describeTaskDefinition` | ECS | Get task definition details |
| `com.datadoghq.aws.ecs.registerTaskDefinition` | ECS | Register new task definition revision |
| `com.datadoghq.aws.ecs.updateEcsService` | ECS | Update service to new task definition |
| `com.datadoghq.datatransformation.func` | Transform | Run a JavaScript function on step outputs |
| `com.datadoghq.core.forLoop` | Core | Iterate over a list |
| `com.datadoghq.core.if` | Core | Conditional branch |
| `com.datadoghq.dd.cases.createCase` | Datadog | Create a Datadog case/incident |

---

## Workflow Spec JSON Skeleton

```json
{
  "handle": "my-workflow-handle",
  "triggers": [
    {
      "securityTrigger": {},
      "startStepNames": ["First_step"]
    }
  ],
  "connectionEnvs": [
    {
      "env": "default",
      "connections": [
        {
          "connectionId": "<uuid>",
          "label": "INTEGRATION_AWS"
        }
      ]
    }
  ],
  "inputSchema": {
    "parameters": [
      { "name": "service_name", "type": "STRING" }
    ]
  },
  "steps": [
    {
      "name": "First_step",
      "actionId": "com.datadoghq.aws.iam.disable_user",
      "connectionLabel": "INTEGRATION_AWS",
      "parameters": [
        {"name": "userName", "value": "{{ Source.securityFinding.resource }}"}
      ],
      "outboundEdges": [
        {"nextStepName": "Second_step", "branchName": "main"}
      ]
    }
  ]
}
```

Key rules: `connectionLabel` in each step must exactly match (case-sensitive) a `label` in `connectionEnvs`. Step names must be unique within the workflow.

---

## ECS Rollback Walk-Through

The 4-step chain in `examples/ECS-Rollback-Leaderboard.json` illustrates step chaining and data transformation:

1. **Describe_task_definition** — `describeTaskDefinition` with `{{ Trigger.service_name }}`
2. **Transform_image_tag** — JavaScript `datatransformation.func` replaces the image tag with `{{ Trigger.image_tag }}`
3. **Register_task_definition** — `registerTaskDefinition` using transformed containerDefinitions from Step 2 and metadata from Step 1
4. **Update_ECS_service** — `updateEcsService` with the new task definition ARN and `forceNewDeployment = true`

The `outboundEdges` field chains steps: Describe -> Transform -> Register -> Update.

---

## Terraform Pattern

```hcl
resource "datadog_workflow_automation" "remove_insecure_ingress" {
  name        = "Remove insecure ingress rules"
  description = "Removes security group rules exposing ports to the internet"
  tags        = ["security", "remediation", "ec2"]
  published   = true
  depends_on  = [datadog_action_connection.aws_ec2_workflow]

  spec_json = jsonencode({
    triggers = [{
      startStepNames = ["Revoke_security_group_ingress"]
      securityTrigger = {}
    }]
    steps = [{
      name            = "Revoke_security_group_ingress"
      actionId        = "com.datadoghq.aws.ec2.revoke_security_group_ingress"
      connectionLabel = "WORKFLOW_EC2"
      parameters = [
        {name = "region",   value = var.aws_region},
        {name = "groupId",  value = "{{ Source.securityFinding.resourceConfiguration.group_id }}"}
      ]
    }]
    connectionEnvs = [{
      env = "default"
      connections = [{
        connectionId = datadog_action_connection.aws_ec2_workflow[0].id
        label        = "WORKFLOW_EC2"
      }]
    }]
  })
}
```

For workflows with many steps, store the spec as a separate JSON file and use `templatefile()`:

```hcl
spec_json = templatefile("${path.module}/my-workflow-spec.json", {
  connection_id = datadog_action_connection.aws_workflow.id
  aws_region    = var.aws_region
})
```

Always add `depends_on` for the action connection to ensure ordering. See `examples/terraform/automating-meaningful-actions-workflows.tf` for forLoop, if-step, and scorecard update patterns.

---

## Connection Setup with Least-Privilege Role

This skill delegates IAM role + connection creation to the action-connections skill.
Extract action FQNs → resolve IAM permissions via `iam_permissions.py` → call
`setup_datadog_action_connection(permissions=...)`. See the action-connections
skill for the full 6-step flow and code examples.

---

## Cross-Skill Notes

- **Delegates to action-connections**: The action-connections skill is the single IAM authority. This skill extracts the needed permissions and delegates role + connection creation. You can also provide a pre-existing `connection_id` to skip auto-provisioning.
- **Monitor IDs from dashboards**: To use a `monitorTrigger`, you need the monitor ID. Create monitors in the dashboards step and pass the ID here.
- **Workflow outputs can update service catalog**: Use `com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome` to mark pass/fail on scorecard rules after remediation completes — closing the IaC -> detect -> remediate -> score loop.

---

## Additional Resources

| Reference | Contents |
|---|---|
| `references/api-reference.md` | Full Workflow REST API contracts: all 8 endpoints, request/response schemas, curl examples, error shapes, idempotent create-or-update pattern |
| `references/triggers.md` | All 11 trigger types with full configuration: manual, monitor, dashboard, incident, security, catalog, GitHub, Slack, API, scheduled, workflow-to-workflow |
| `references/flow-control-and-expressions.md` | Flow actions (If, Switch, Sleep, For Loop, While Loop), error handling (retries, error paths, wait-until), expressions (JavaScript with Lodash, Python 3.12.8), custom variables, output parameters |
| `references/operations.md` | Publishing/versioning, rate limits and throttling, billing model, notifications, saved actions, audit trail, monitoring metrics, RBAC, operational best practices |

---

## Level 3 References

- `examples/create_workflows.py` — ECS rollback (4-step + data transform), IAM attach policy, connection lookup by name, idempotent create-or-update
- `examples/terraform/automating-meaningful-actions-workflows.tf` — `datadog_workflow_automation` with forLoop, if-step, data transform, and scorecard update steps
- `examples/AWS-IAM-Disable-User.json` — minimal single-step `securityTrigger` workflow (simplest possible reference)
- `examples/json/workflow-remove-insecure-ingress.json` — multi-step workflow with conditional branch and EC2 security group remediation
- `examples/AWS_ACTION_CONNECTION_SETUP.md` — connection-to-workflow dependency architecture and setup sequence
