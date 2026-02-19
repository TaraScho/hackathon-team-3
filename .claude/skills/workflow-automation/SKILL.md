---
name: workflow-automation
description: >
  Creates Datadog Workflow Automation workflows that perform automated remediation
  and response actions in AWS — triggered by security signals, monitors, or manual
  execution. Use this skill when you need to: write a workflow spec in JSON or
  Terraform, automate IAM user disabling on security alerts, roll back an ECS
  service to a previous image tag, revoke insecure EC2 security group ingress rules,
  create a case for an AWS SIEM signal, attach IAM policies programmatically, use
  data transformation steps between AWS actions, or chain multiple AWS API calls in
  a workflow. Trigger phrases: "workflow automation", "automated remediation",
  "security trigger workflow", "monitor trigger", "ECS rollback workflow",
  "IAM disable user", "revoke ingress", "datadog_workflow_automation terraform",
  "connectionEnvs", "workflow spec JSON", "drift remediation", "auto-remediate".
metadata:
  author: hackathon-team-3
  version: 1.0.0
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
| Action connection | Must exist; provide its UUID in `connectionEnvs` |
| App key scopes | `workflows_read`, `workflows_write`, `workflows_run`, `connections_read`, `connections_resolve` |
| IAM role permissions | The role assumed by the connection must allow all AWS actions called in workflow steps |

---

## Trigger Types

| Trigger key | When to use | Source variables available |
|---|---|---|
| `securityTrigger` | Datadog Cloud SIEM signal fires | `{{ Source.securityFinding.* }}` |
| `monitorTrigger` | Datadog monitor alert | `{{ Trigger.* }}` (monitor context) |
| `workflowTrigger` | Another workflow calls this one | `{{ Trigger.* }}` (caller params) |
| `apiTrigger` | Manual execution or API call | `{{ Trigger.* }}` (inputSchema params) |

A workflow spec can include multiple trigger blocks (e.g., both `apiTrigger` and `monitorTrigger`).

---

## Action IDs Reference

| Action ID | Service | Operation |
|---|---|---|
| `com.datadoghq.aws.iam.disable_user` | IAM | Disable IAM user login |
| `com.datadoghq.aws.iam.attach_role_policy` | IAM | Attach managed policy to role |
| `com.datadoghq.aws.iam.list_roles` | IAM | List all IAM roles |
| `com.datadoghq.aws.ec2.describe_ec2_instances` | EC2 | Describe instances with filters |
| `com.datadoghq.aws.ec2.revoke_security_group_ingress` | EC2 | Remove security group ingress rules |
| `com.datadoghq.aws.ec2.modify_instance_metadata_options` | EC2 | Enforce IMDSv2 |
| `com.datadoghq.aws.ecs.describeTaskDefinition` | ECS | Get task definition details |
| `com.datadoghq.aws.ecs.registerTaskDefinition` | ECS | Register new task definition revision |
| `com.datadoghq.aws.ecs.updateEcsService` | ECS | Update service to new task definition |
| `com.datadoghq.datatransformation.func` | Transform | Run a JavaScript function on step outputs |
| `com.datadoghq.core.forLoop` | Core | Iterate over a list |
| `com.datadoghq.core.if` | Core | Conditional branch |
| `com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome` | Datadog | Update service scorecard |
| `com.datadoghq.dd.cases.createCase` | Datadog | Create a Datadog case/incident |

---

## Workflow Spec JSON Structure

Annotated skeleton:

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
          "connectionId": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
          "label": "INTEGRATION_AWS"
        }
      ]
    }
  ],
  "inputSchema": {
    "parameters": [
      {
        "name": "service_name",
        "label": "Service Name",
        "description": "ECS service to roll back",
        "type": "STRING"
      }
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
      ],
      "display": {"bounds": {"x": 0, "y": 0}}
    }
  ]
}
```

---

## ECS Rollback Walk-Through

The 4-step chain in `examples/ECS-Rollback-Leaderboard.json` illustrates step chaining and data transformation:

**Step 1 — Describe_task_definition**
```
actionId: com.datadoghq.aws.ecs.describeTaskDefinition
input:    taskDefinition = "{{ Trigger.service_name }}"
output:   taskDefinition object (full ECS task def)
```

**Step 2 — Transform_image_tag** (data transformation step)
```
actionId: com.datadoghq.datatransformation.func
script:   JavaScript that reads containerDefinitions from Step 1,
          replaces the image tag with {{ Trigger.image_tag }},
          returns updated containerDefinitions array
output:   data (the return value of the script)
```

**Step 3 — Register_task_definition**
```
actionId: com.datadoghq.aws.ecs.registerTaskDefinition
input:    containerDefinitions = "{{ Steps.Transform_image_tag.data }}"
          cpu, memory, family, etc. = "{{ Steps.Describe_task_definition.taskDefinition.* }}"
output:   taskDefinition.taskDefinitionArn
```

**Step 4 — Update_ECS_service**
```
actionId: com.datadoghq.aws.ecs.updateEcsService
input:    taskDefinition = "{{ Steps.Register_task_definition.taskDefinition.taskDefinitionArn }}"
          forceNewDeployment = true
```

The `outboundEdges` field chains steps: `Describe → Transform → Register → Update`.

---

## API: Create and Manage

### Create a workflow

```
POST /api/v2/workflows
```

```python
payload = {
    "data": {
        "type": "workflow",
        "attributes": {
            "name": "ECS Rollback",
            "description": "Rolls back an ECS service to a specified image tag",
            "tags": ["ecs", "rollback", "automated"],
            "published": True,
            "spec": workflow_spec_dict  # the spec JSON as a Python dict
        }
    }
}
```

- Returns `data.id` — the workflow UUID
- **409 conflict**: A workflow with this handle already exists. List workflows, find by name, then PUT to update.

### List workflows

```
GET /api/v2/workflows
```

Filter by name client-side. Use this for idempotent create-or-update logic.

---

## Terraform Pattern

### Inline spec with `jsonencode`

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

### Long specs with `templatefile()`

For workflows with many steps, store the spec as a separate JSON file and use `templatefile()` to inject Terraform values:

```hcl
spec_json = templatefile("${path.module}/my-workflow-spec.json", {
  connection_id = datadog_action_connection.aws_workflow.id
  aws_region    = var.aws_region
})
```

Always add `depends_on` for the action connection to ensure ordering.

See `examples/terraform/automating-meaningful-actions-workflows.tf` for forLoop, if-step, and scorecard update patterns.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Workflow fails with "permission denied" on AWS action | IAM role missing required permissions | Add the specific AWS action (e.g., `iam:DisableUser`) to the role policy |
| 403 on `POST /api/v2/workflows` | App key missing `workflows_write` scope | Re-create app key with required scopes |
| Step output field not found | Wrong field name in `{{ Steps.Name.field }}` | Check the action's return schema; field names are camelCase (e.g., `taskDefinition`, not `task_definition`) |
| Connection not found in workflow | `connectionLabel` in step doesn't match label in `connectionEnvs` | Labels are case-sensitive; verify exact match |
| 409 on workflow creation | Workflow handle already exists | List workflows, find existing ID, use PUT to update |
| `Source.securityFinding.resource` is empty | Trigger is not a security trigger or resource field has different path | Check the specific SIEM signal schema for your finding type |

---

## Cross-Skill Notes

- **Requires action-connections**: The connection UUID goes into `connectionEnvs[].connections[].connectionId`. Set `connectionLabel` consistently in both `connectionEnvs` and step `connectionLabel` fields.
- **Monitor IDs from dashboards**: To use a `monitorTrigger`, you need the monitor ID. Create monitors in the dashboards step and pass the ID here.
- **Workflow outputs can update service catalog**: Use `com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome` to mark pass/fail on scorecard rules after remediation completes — closing the IaC → detect → remediate → score loop.

---

## Level 3 References

- `examples/create_workflows.py` — ECS rollback (4-step + data transform), IAM attach policy, connection lookup by name, idempotent create-or-update
- `examples/terraform/automating-meaningful-actions-workflows.tf` — `datadog_workflow_automation` with forLoop, if-step, data transform, and scorecard update steps
- `examples/AWS-IAM-Disable-User.json` — minimal single-step `securityTrigger` workflow (simplest possible reference)
- `examples/json/workflow-remove-insecure-ingress.json` — multi-step workflow with conditional branch and EC2 security group remediation
- `examples/AWS_ACTION_CONNECTION_SETUP.md` — connection-to-workflow dependency architecture and setup sequence
