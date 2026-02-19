---
name: action-connections
description: >
  Creates and manages Datadog Action Connections that authorize Datadog Workflow
  Automation and App Builder to perform actions in AWS via IAM role assumption.
  Use this skill when you need to: set up cross-account AWS access for Datadog,
  create an AWS action connection via the Datadog API, configure IAM trust policies
  with Datadog external IDs, automate connection setup in Lambda or Python scripts,
  manage app key scopes for connections_read/connections_write/workflows_run,
  handle the 5-step connection setup workflow, or troubleshoot 403 errors on the
  actions API. Trigger phrases: "set up action connection", "Datadog assume role",
  "external ID trust policy", "IAM role for Datadog", "connection for workflows",
  "scoped app key", "DatadogActionRole", "464622532012", "awsassumerole".
metadata:
  author: hackathon-team-3
  version: 1.0.0
  tags: [aws, iam, action-connections, workflow-automation, terraform, security]
  category: infrastructure
---

# Action Connections Skill

## Overview

Datadog Action Connections solve the **confused-deputy problem**: they give Datadog Workflow Automation and App Builder a secure, audited path to assume an IAM role in your AWS account without embedding long-lived credentials anywhere.

The mechanism is standard AWS cross-account role assumption with an external ID condition:

- Datadog's fixed AWS account ID is **`464622532012`** — this is the principal you trust in every `sts:AssumeRole` statement.
- Datadog generates a unique **external ID** per connection to prevent confused-deputy attacks. You must embed this value in the IAM role trust policy before the connection becomes usable.
- The connection ID (a UUID) is used as a reference in workflow `connectionEnvs` and app-builder `action_query_names_to_connection_ids`.

### Dependency Diagram

```
action-connections ──► workflow-automation
        │
        └──────────► app-builder ──► dashboards
```

**This skill is the foundational prerequisite.** Workflows and apps cannot perform AWS actions until a working connection exists.

---

## When to Use

- You need Datadog Workflow Automation to perform AWS actions (IAM, EC2, ECS, S3, etc.)
- You need App Builder apps to read/write AWS resources
- You are setting up a new Datadog org and need to wire up AWS access for the first time
- You want to automate connection setup inside a Lambda (e.g., a CloudFormation custom resource)
- You want to write Terraform that manages the connection as code
- You are debugging 403 errors on the `/api/v2/actions/connections` endpoint
- You need to understand the external ID and why it must be fetched from a different API endpoint

---

## Prerequisites

| Requirement | Details |
|---|---|
| IAM role | Must exist in your AWS account before running setup; Datadog account `464622532012` must be in the trust policy principal |
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Initial Datadog app key — used only to create the scoped key in Step 1 |
| Python dependencies | `boto3`, `requests` |
| AWS permissions (Lambda/execution role) | `iam:UpdateAssumeRolePolicy`, `iam:GetRole`, `sts:GetCallerIdentity` |

### Required App Key Scopes

The scoped key created in Step 1 needs these scopes to operate connections, workflows, and apps:

```
connections_read, connections_write, connections_resolve
workflows_read, workflows_write, workflows_run
apps_run, apps_write
```

---

## 5-Step Setup Workflow

The reference implementation is `setup_datadog_action_connection()` in `examples/python/setup_action_connection.py`.

### Step 1 — Create scoped application key

```
POST /api/v2/current_user/application_keys
```

Create a new app key that has only the scopes required for action connections and workflow automation. Use this new key for all subsequent API calls (not your root app key).

```python
payload = {
    "data": {
        "type": "application_keys",
        "attributes": {
            "name": "DatadogActionsKey_1234",
            "scopes": ["connections_read", "connections_write", "connections_resolve",
                       "workflows_read", "workflows_write", "workflows_run",
                       "apps_run", "apps_write"]
        }
    }
}
```

Returns: `data.attributes.key` (the new app key value).

### Step 2 — Create the AWS action connection

```
POST /api/v2/actions/connections
```

```python
payload = {
    "data": {
        "type": "action_connection",
        "attributes": {
            "name": "DatadogAWSConnection",
            "integration": {
                "type": "aws",
                "credentials": {
                    "type": "awsassumerole",
                    "role": "DatadogActionRole",   # role name, not ARN
                    "account_id": "123456789012"   # your AWS account ID
                }
            }
        }
    }
}
```

Returns: `data.id` — the connection UUID. Save this.

### Step 3 — Retrieve the external ID

**Critical:** The `/api/v2/actions/connections` endpoint does NOT return the external ID. You must use the separate `custom_connections` endpoint:

```
GET /api/v2/connection/custom_connections/{connection_id}
```

External ID path in response:
```
data.attributes.data.aws.assumeRole.externalId
```

If this returns an empty string, you called the wrong endpoint.

### Step 4 — Update IAM role trust policy

Call `iam:UpdateAssumeRolePolicy` with the external ID from Step 3:

```python
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {"AWS": "arn:aws:iam::464622532012:root"},
        "Action": "sts:AssumeRole",
        "Condition": {"StringEquals": {"sts:ExternalId": external_id}}
    }]
}
iam_client.update_assume_role_policy(RoleName="DatadogActionRole",
                                     PolicyDocument=json.dumps(trust_policy))
```

### Step 5 — Set restriction policy and verify readiness

Make the connection org-wide accessible (otherwise only the creator can use it):

```
POST /api/v2/restriction_policy/connection:{connection_id}
```

```python
payload = {
    "data": {
        "id": f"connection:{connection_id}",
        "type": "restriction_policy",
        "attributes": {
            "bindings": [{"relation": "editor", "principals": [f"org:{org_id}"]}]
        }
    }
}
```

Then poll `GET /api/v2/actions/connections/{connection_id}` until it returns 200 (up to 30 seconds with exponential backoff). This prevents race conditions in downstream app/workflow creation.

---

## API Endpoints Reference

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/v2/current_user/application_keys` | Create scoped app key |
| `POST` | `/api/v2/actions/connections` | Create action connection |
| `GET` | `/api/v2/actions/connections` | List all connections |
| `GET` | `/api/v2/actions/connections/{id}` | Get connection / verify readiness |
| `GET` | `/api/v2/connection/custom_connections/{id}` | **Get external ID** (different endpoint!) |
| `POST` | `/api/v2/restriction_policy/connection:{id}` | Set org-wide access |
| `GET` | `/api/v2/current_user` | Get org ID for restriction policy |

---

## Terraform Pattern

Use the `datadog_action_connection` resource from the Datadog Terraform provider:

```hcl
resource "datadog_action_connection" "aws_workflow" {
  name = "workflow-ec2"

  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = "DatadogActionRole"
    }
  }
}

# Separate connection for App Builder (principle of least privilege)
resource "datadog_action_connection" "aws_appbuilder" {
  name = "appbuilder-ec2"

  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = "datadog-appbuilder-ec2"
    }
  }
}
```

Reference the connection ID downstream:

```hcl
locals {
  connection_id = datadog_action_connection.aws_workflow.id
}
```

See `../app-builder/examples/terraform/connections.tf` for the full pattern including separate workflow vs. app-builder connections.

---

## CloudFormation Pattern

The IAM role must exist before the Python setup runs. Use a placeholder external ID initially; the Lambda will update it:

```yaml
DatadogActionRole:
  Type: AWS::IAM::Role
  Properties:
    RoleName: DatadogActionRole
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/PowerUserAccess
    Policies:
      - PolicyName: DatadogIAMManagementPolicy
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action: [iam:ListRoles, iam:CreateRole, iam:AttachRolePolicy,
                       iam:DetachRolePolicy, iam:DeleteRole, iam:ListPolicies,
                       iam:CreatePolicy, iam:DeletePolicy]
              Resource: '*'
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            AWS: !Sub 'arn:aws:iam::${AWS::AccountId}:root'
          Action: sts:AssumeRole
          Condition:
            StringEquals:
              sts:ExternalId: 'placeholder-will-be-updated'
```

After the Lambda runs `setup_datadog_action_connection()`, the trust policy is patched with the real external ID. The Lambda execution role needs `iam:UpdateAssumeRolePolicy` and `iam:GetRole` on the DatadogActionRole ARN.

See `../workflow-automation/examples/datadog_action_role_cfn_snippet.yaml` for the full snippet including Lambda role permissions.

---

## Common Pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| 403 on `POST /api/v2/actions/connections` | App key missing `connections_write` scope | Re-create app key with all required scopes in Step 1 |
| 409 on `POST /api/v2/actions/connections` | Connection name already exists | List connections, retrieve existing ID, skip creation |
| `externalId` is empty string | Called `/api/v2/actions/connections/{id}` instead of `/api/v2/connection/custom_connections/{id}` | Use the `custom_connections` endpoint for external ID |
| Connection works for creator but not others | Restriction policy not set | POST to `/api/v2/restriction_policy/connection:{id}` with org binding |
| Trust fails after external ID update | IAM propagation delay | Wait 5-10 seconds after `update_assume_role_policy` before testing |

---

## Cross-Skill Notes

- **workflow-automation**: Pass the connection ID in `connectionEnvs[].connections[].connectionId`. The label (e.g., `INTEGRATION_AWS`) is referenced in each step's `connectionLabel` field.
- **app-builder**: Pass the connection ID in `action_query_names_to_connection_ids` when creating apps via Terraform, or replace `connectionId` in app JSON during the `transform_app_json_for_api()` step.
- Best practice: create **two separate connections** — one for Workflow Automation, one for App Builder — so each can have an IAM role scoped to only the AWS actions it needs.

---

## Level 3 References

- `examples/python/setup_action_connection.py` — Full 5-step orchestration; `DatadogResponse` wrapper pattern; exponential backoff; XA_Session pattern for cross-account Lambda usage
- `../workflow-automation/examples/datadog_action_role_cfn_snippet.yaml` — CloudFormation IAM role with placeholder external ID; Lambda role permissions
- `../app-builder/examples/terraform/connections.tf` — Terraform `datadog_action_connection` resources (separate workflow vs. app-builder connections)
