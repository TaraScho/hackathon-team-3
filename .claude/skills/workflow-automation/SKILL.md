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
  Do NOT use for setting up IAM connections (use action-connections), building
  App Builder UIs (use app-builder), or creating dashboards (use dashboards).
compatibility: >
  Requires Python 3.8+, requests, DD_API_KEY and DD_APP_KEY env vars
  (app key scopes: workflows_read, workflows_write, workflows_run).
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
| Action connection | Created automatically via action-connections skill if not provided; or provide an existing UUID in `connectionEnvs` |
| App key scopes | `workflows_read`, `workflows_write`, `workflows_run`, `connections_read`, `connections_resolve` |
| IAM role permissions | Auto-scoped when using least-privilege setup; the role gets exactly the permissions needed by the workflow steps |

**Note:** The action-connections skill handles IAM role creation and permission scoping. You do not need to create IAM roles manually.

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

## API: Create and Manage Workflows

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

Required app key scopes: `workflows_write` (create/update/delete), `workflows_read` (get/list), `workflows_run` (execute).

### POST /api/v2/workflows — Create a workflow

**Request body:**
```json
{
  "data": {
    "type": "workflows",
    "attributes": {
      "name": "ECS Rollback",
      "description": "Rolls back an ECS service to a specified image tag",
      "tags": ["ecs", "rollback", "automated"],
      "published": true,
      "spec": {
        "handle": "ecs-rollback",
        "triggers": [
          {
            "startStepNames": ["Describe_task_definition"],
            "monitorTrigger": {
              "rateLimit": { "count": 1, "interval": "3600s" }
            }
          }
        ],
        "steps": [
          {
            "name": "Describe_task_definition",
            "actionId": "com.datadoghq.aws.ecs.describeTaskDefinition",
            "connectionLabel": "INTEGRATION_AWS",
            "parameters": [
              { "name": "taskDefinition", "value": "{{ Trigger.service_name }}" }
            ],
            "outboundEdges": [
              { "nextStepName": "Next_step", "branchName": "main" }
            ]
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
        }
      }
    }
  }
}
```

**Response (201):**
```json
{
  "data": {
    "id": "workflow-uuid-here",
    "type": "workflows",
    "attributes": {
      "name": "ECS Rollback",
      "description": "Rolls back an ECS service to a specified image tag",
      "published": true,
      "createdAt": "2024-01-15T10:30:00.000Z",
      "spec": { "..." }
    }
  }
}
```

Key field: `data.id` — the workflow UUID.

**Errors:** `400` (invalid spec), `403` (missing `workflows_write`), `429` (rate limited).

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/workflows" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @workflow-spec.json
```

### GET /api/v2/workflows/{workflow_id} — Get a workflow

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

**Status codes:** `200`, `400`, `403`, `404`, `429`.

### PATCH /api/v2/workflows/{workflow_id} — Update a workflow

Same body structure as create. Partial updates to attributes.

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d @updated-workflow.json
```

### DELETE /api/v2/workflows/{workflow_id} — Delete a workflow

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Returns `204 No Content` on success.

### POST /api/v2/workflows/{workflow_id}/instances — Execute a workflow

Manually trigger a workflow execution with input parameters.

**Request body:**
```json
{
  "meta": {
    "payload": {
      "service_name": "my-ecs-service",
      "image_tag": "v1.2.3"
    }
  }
}
```

**Response (200):**
```json
{
  "data": {
    "id": "instance-uuid-here"
  }
}
```

Key field: `data.id` — the execution instance ID. Use to poll status.

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"meta": {"payload": {"service_name": "my-ecs-service"}}}'
```

### GET /api/v2/workflows/{workflow_id}/instances — List executions

**Query parameters:**
| Param | Type | Description |
|---|---|---|
| `page[size]` | int | Results per page |
| `page[number]` | int | Page number |

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances?page[size]=10" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### GET /api/v2/workflows/{workflow_id}/instances/{instance_id} — Get execution status

```bash
curl -X GET "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances/${INSTANCE_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### PUT /api/v2/workflows/{workflow_id}/instances/{instance_id}/cancel — Cancel execution

```bash
curl -X PUT "https://api.datadoghq.com/api/v2/workflows/${WORKFLOW_ID}/instances/${INSTANCE_ID}/cancel" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Error response shape

All errors follow the JSON:API format:
```json
{
  "errors": [
    {
      "status": "403",
      "title": "Forbidden",
      "detail": "Missing required scope: workflows_write"
    }
  ]
}
```

### Idempotent create-or-update pattern

The API does not support listing workflows by name. To create-or-update:
1. Attempt `POST /api/v2/workflows` to create
2. If you get a conflict (handle already exists), use `GET` to find by ID, then `PATCH` to update

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

## Action Catalog Reference

When you need to look up available actions, their FQNs, required inputs, or output schemas:

1. Read the master index at `.claude/skills/shared/action-catalog-index.md` to find which service file you need
2. Read the per-service file at `.claude/skills/shared/actions-by-service/{service}.md` for full action details
3. Use the exact FQN from the reference (e.g., `com.datadoghq.aws.iam.disable_user`) in step `actionId` fields

Common service files for this skill:
- `aws-ec2.md` — EC2 instance/security group management
- `aws-ecs.md` — ECS service/task management
- `aws-iam.md` — IAM user/role/policy management
- `aws-s3.md` — S3 bucket/object operations
- `aws-lambda.md` — Lambda function management
- `aws-guardduty.md` — GuardDuty finding management
- `aws-cloudtrail.md` — CloudTrail log management
- `dd-casem.md` — Datadog Case Management
- `dd-service_catalog.md` — Datadog Service Catalog (scorecard updates)
- `dd-securitymonitoring.md` — Datadog Security Monitoring rules/signals
- `core-workflow.md` — Loop, condition, JS transform actions
- `core-datatransformation.md` — JavaScript/Python data transformation

---

## Connection Setup with Least-Privilege Role

When creating a workflow, you can automatically provision a dedicated IAM role + connection scoped to exactly the AWS actions the workflow needs. This uses the shared `iam_permissions.py` utility to extract actions from the workflow spec and resolve them to IAM permissions.

**Step-by-step:**
1. Extract action FQNs from the workflow spec using the shared utility
2. Resolve FQNs to IAM permissions via the action catalog
3. Call `setup_datadog_action_connection(permissions=...)` from the action-connections skill to create a dedicated role + connection
4. Use the returned `connection_id` in the workflow's `connectionEnvs`

```python
import sys
sys.path.insert(0, ".claude/skills/shared")
from iam_permissions import load_action_catalog, extract_actions_from_workflow_json, resolve_permissions

# Step 1-2: Extract actions and resolve permissions
catalog = load_action_catalog(".claude/skills/shared/actions-by-service")
actions = extract_actions_from_workflow_json("path/to/workflow.json")
permissions = resolve_permissions(actions, catalog)

# Step 3: Create dedicated role + connection
sys.path.insert(0, ".claude/skills/action-connections/examples/python")
from setup_action_connection import setup_datadog_action_connection

response = setup_datadog_action_connection(
    api_key=os.environ["DD_API_KEY"],
    app_key=os.environ["DD_APP_KEY"],
    role_name="DatadogAction-MyWorkflow",
    connection_name="MyWorkflow-Connection",
    permissions=permissions,  # Scopes the role to only these permissions
)
connection_id = response.data["connection_id"]

# Step 4: Use connection_id in connectionEnvs when creating the workflow
```

This gives each workflow its own IAM role with only the permissions it actually uses.

---

## Cross-Skill Notes

- **Delegates to action-connections**: The action-connections skill is the single IAM authority. This skill extracts the needed permissions and delegates role + connection creation. You can also provide a pre-existing `connection_id` to skip auto-provisioning.
- **Monitor IDs from dashboards**: To use a `monitorTrigger`, you need the monitor ID. Create monitors in the dashboards step and pass the ID here.
- **Workflow outputs can update service catalog**: Use `com.datadoghq.dd.service_catalog.updateScorecardRuleOutcome` to mark pass/fail on scorecard rules after remediation completes — closing the IaC → detect → remediate → score loop.

---

## Level 3 References

- `examples/create_workflows.py` — ECS rollback (4-step + data transform), IAM attach policy, connection lookup by name, idempotent create-or-update
- `examples/terraform/automating-meaningful-actions-workflows.tf` — `datadog_workflow_automation` with forLoop, if-step, data transform, and scorecard update steps
- `examples/AWS-IAM-Disable-User.json` — minimal single-step `securityTrigger` workflow (simplest possible reference)
- `examples/json/workflow-remove-insecure-ingress.json` — multi-step workflow with conditional branch and EC2 security group remediation
- `examples/AWS_ACTION_CONNECTION_SETUP.md` — connection-to-workflow dependency architecture and setup sequence
