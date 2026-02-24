---
name: action-connections
description: >
  Creates and manages Datadog Action Connections that authorize Datadog Workflow
  Automation and App Builder to perform actions in AWS via IAM role assumption.
  Use this skill when you need to: set up cross-account AWS access for Datadog,
  create an AWS action connection via the Datadog API, configure IAM trust policies
  with Datadog external IDs, automate connection setup in Lambda or Python scripts,
  manage app key scopes for connections_read/connections_write/workflows_run,
  handle the 7-step connection setup workflow (including auto-creating IAM roles
  with least-privilege permissions), or troubleshoot 403 errors on the
  actions API. Trigger phrases: "set up action connection", "Datadog assume role",
  "external ID trust policy", "IAM role for Datadog", "connection for workflows",
  "scoped app key", "DatadogActionRole", "464622532012", "awsassumerole".
  Do NOT use for creating workflow logic (use workflow-automation), building app
  UIs (use app-builder), or registering catalog entities (use software-catalog).
compatibility: >
  Requires Python 3.8+, requests, boto3, DD_API_KEY and DD_APP_KEY env vars,
  and valid AWS credentials with iam:CreateRole, iam:GetRole, iam:PutRolePolicy,
  iam:UpdateAssumeRolePolicy permissions.
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
| IAM role | Auto-created if missing (path `/datadog/`); Datadog account `464622532012` is set as the trust policy principal |
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Initial Datadog app key — used only to create the scoped key in Step 1 |
| Python dependencies | `boto3`, `requests` |
| AWS permissions (Lambda/execution role) | `iam:CreateRole`, `iam:GetRole`, `iam:PutRolePolicy`, `iam:UpdateAssumeRolePolicy`, `sts:GetCallerIdentity` |

### Required App Key Scopes

The scoped key created in Step 1 needs these scopes to operate connections, workflows, and apps:

```
connections_read, connections_write, connections_resolve
workflows_read, workflows_write, workflows_run
apps_run, apps_write
```

---

## 7-Step Setup Workflow

The reference implementation is `setup_datadog_action_connection()` in `examples/python/setup_action_connection.py`.

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

### Step 0 — Ensure IAM role exists

The `ensure_iam_role()` function checks if the role exists via `iam:GetRole`. If not, it creates the role with:
- Path: `/datadog/` (enables discovery via `iam.list_roles(PathPrefix="/datadog/")`)
- Trust policy: allows `sts:AssumeRole` from Datadog's account `464622532012` with a placeholder external ID
- The placeholder external ID is updated in Step 4 after the connection is created

```python
from setup_action_connection import ensure_iam_role

response = ensure_iam_role("DatadogAction-MyApp-abc123", aws_session=session)
# response.data = {"role_name": "...", "role_arn": "arn:aws:iam::...:role/datadog/...", "created": True}
```

### Step 0.5 — Scope role permissions (optional, for least privilege)

If a `permissions` list is provided, `update_role_permissions()` applies an inline policy with exactly those IAM actions. Each role is dedicated to one app/workflow, so the policy is replaced entirely (no merge).

```python
from setup_action_connection import update_role_permissions

permissions = ["ec2:DescribeInstances", "ec2:DescribeTags", "s3:ListBuckets"]
response = update_role_permissions("DatadogAction-MyApp-abc123", permissions, aws_session=session)
# response.data = {"role_name": "...", "policy_name": "DatadogActionPermissions", "permissions_count": 3}
```

Downstream skills (app-builder, workflow-automation) compute the permissions they need using the shared `iam_permissions.py` utility:

```python
import sys
sys.path.insert(0, ".claude/skills/shared")
from iam_permissions import load_action_catalog, extract_actions_from_app_json, resolve_permissions

catalog = load_action_catalog(".claude/skills/shared/actions-by-service")
actions = extract_actions_from_app_json("path/to/app.json")
permissions = resolve_permissions(actions, catalog)
# Pass permissions to setup_datadog_action_connection(permissions=permissions)
```

### Step 1 — Create scoped application key

**`POST https://api.datadoghq.com/api/v2/current_user/application_keys`**

Create a new app key with only the scopes required for action connections and workflow automation. Use this new key for all subsequent API calls (not your root app key).

**Request body:**
```json
{
  "data": {
    "type": "application_keys",
    "attributes": {
      "name": "DatadogActionsKey_1234",
      "scopes": [
        "connections_read", "connections_write", "connections_resolve",
        "workflows_read", "workflows_write", "workflows_run",
        "apps_run", "apps_write"
      ]
    }
  }
}
```

**Response (201):**
```json
{
  "data": {
    "id": "abcdef12-3456-7890-abcd-ef1234567890",
    "type": "application_keys",
    "attributes": {
      "name": "DatadogActionsKey_1234",
      "key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "scopes": ["connections_read", "connections_write", "..."]
    }
  }
}
```

Key field: `data.attributes.key` — save this, it is shown only once.

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/current_user/application_keys" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "application_keys",
      "attributes": {
        "name": "DatadogActionsKey_1234",
        "scopes": ["connections_read","connections_write","connections_resolve",
                    "workflows_read","workflows_write","workflows_run",
                    "apps_run","apps_write"]
      }
    }
  }'
```

### Step 2 — Create the AWS action connection

**`POST https://api.datadoghq.com/api/v2/actions/connections`**

**Request body:**
```json
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "DatadogAWSConnection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "DatadogActionRole",
          "account_id": "123456789012"
        }
      }
    }
  }
}
```

Field notes:
- `integration.type`: enum `"AWS"` (uppercase)
- `credentials.type`: enum `"AWSAssumeRole"` (PascalCase)
- `credentials.role`: IAM role **name** (not ARN)
- `credentials.account_id`: 12-digit AWS account ID (string, must match `^\d{12}$`)

**Response (201):**
```json
{
  "data": {
    "id": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
    "type": "action_connection",
    "attributes": {
      "name": "DatadogAWSConnection",
      "integration": {
        "type": "AWS",
        "credentials": {
          "type": "AWSAssumeRole",
          "role": "DatadogActionRole",
          "account_id": "123456789012",
          "principal_id": "464622532012",
          "external_id": "33a1011635c44b38a064cf14e82e1d8f"
        }
      }
    }
  }
}
```

Key fields: `data.id` (connection UUID), `credentials.external_id` (read-only), `credentials.principal_id` (read-only, always `464622532012`).

**Errors:** `400` (invalid payload), `403` (missing `connections_write` scope), `429` (rate limited).

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/actions/connections" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "action_connection",
      "attributes": {
        "name": "DatadogAWSConnection",
        "integration": {
          "type": "AWS",
          "credentials": {
            "type": "AWSAssumeRole",
            "role": "DatadogActionRole",
            "account_id": "123456789012"
          }
        }
      }
    }
  }'
```

### Step 3 — Retrieve the external ID

**Critical:** The `/api/v2/actions/connections` endpoint does NOT return the external ID in all cases. Use the separate `custom_connections` endpoint:

**`GET https://api.datadoghq.com/api/v2/connection/custom_connections/{connection_id}`**

**Response (200):**
```json
{
  "data": {
    "id": "aaaabbbb-cccc-dddd-eeee-ffffffffffff",
    "attributes": {
      "data": {
        "aws": {
          "assumeRole": {
            "externalId": "33a1011635c44b38a064cf14e82e1d8f"
          }
        }
      }
    }
  }
}
```

External ID path: `data.attributes.data.aws.assumeRole.externalId`

If this returns an empty string, you called the wrong endpoint.

**curl:**
```bash
curl -X GET "https://api.datadoghq.com/api/v2/connection/custom_connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Step 4 — Update IAM role trust policy

Use the AWS CLI or SDK to patch the trust policy with the external ID from Step 3:

```bash
# AWS CLI
aws iam update-assume-role-policy \
  --role-name DatadogActionRole \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::464622532012:root"},
      "Action": "sts:AssumeRole",
      "Condition": {"StringEquals": {"sts:ExternalId": "'"${EXTERNAL_ID}"'"}}
    }]
  }'
```

### Step 5 — Set restriction policy and verify readiness

Make the connection org-wide accessible (otherwise only the creator can use it).

**`POST https://api.datadoghq.com/api/v2/restriction_policy/connection:{connection_id}`**

**Request body:**
```json
{
  "data": {
    "id": "connection:aaaabbbb-cccc-dddd-eeee-ffffffffffff",
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {
          "relation": "editor",
          "principals": ["org:your-org-id"]
        }
      ]
    }
  }
}
```

Field notes:
- `id`: Must be `connection:{connection_id}` (resource type prefix)
- `relation`: For connections, valid values are `viewer`, `resolver`, `editor`
- `principals`: Format `type:id` — supported types: `role`, `team`, `user`, `org`
- Get your org ID from `GET /api/v2/current_user` → `data.attributes.org.public_id`

**Response (200):** Returns the created restriction policy object.

**curl:**
```bash
curl -X POST "https://api.datadoghq.com/api/v2/restriction_policy/connection:${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "id": "connection:'"${CONNECTION_ID}"'",
      "type": "restriction_policy",
      "attributes": {
        "bindings": [{"relation": "editor", "principals": ["org:'"${ORG_ID}"'"]}]
      }
    }
  }'
```

Then poll `GET /api/v2/actions/connections/{connection_id}` until it returns 200 (up to 30 seconds with exponential backoff). This prevents race conditions in downstream app/workflow creation.

**Verify curl:**
```bash
curl -s -o /dev/null -w "%{http_code}" \
  "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## API Endpoints Reference

| Method | Endpoint | Status Codes | Purpose |
|---|---|---|---|
| `POST` | `/api/v2/current_user/application_keys` | 201, 400, 403 | Create scoped app key |
| `POST` | `/api/v2/actions/connections` | 201, 400, 403, 429 | Create action connection |
| `GET` | `/api/v2/actions/connections/{id}` | 200, 400, 403, 404, 429 | Get connection / verify readiness |
| `PATCH` | `/api/v2/actions/connections/{id}` | 200, 400, 403, 404, 429 | Update connection |
| `DELETE` | `/api/v2/actions/connections/{id}` | 204, 403, 404, 429 | Delete connection |
| `GET` | `/api/v2/connection/custom_connections/{id}` | 200 | **Get external ID** (different endpoint!) |
| `POST` | `/api/v2/restriction_policy/{resource_id}` | 200, 400, 403, 429 | Set org-wide access |
| `GET` | `/api/v2/restriction_policy/{resource_id}` | 200, 400, 403, 429 | Read restriction policy |
| `GET` | `/api/v2/current_user` | 200, 403 | Get org ID for restriction policy |

### PATCH /api/v2/actions/connections/{id}

Update an existing connection (e.g., change role name or account ID):

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "action_connection",
      "attributes": {
        "name": "UpdatedConnectionName",
        "integration": {
          "type": "AWS",
          "credentials": {
            "type": "AWSAssumeRole",
            "role": "NewRoleName",
            "account_id": "123456789012"
          }
        }
      }
    }
  }'
```

### DELETE /api/v2/actions/connections/{id}

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

Returns `204 No Content` on success.

### Error response shape

All error responses follow the JSON:API format:
```json
{
  "errors": [
    {
      "status": "403",
      "title": "Forbidden",
      "detail": "Missing required scope: connections_write"
    }
  ]
}
```

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

- **This skill is the single IAM authority.** App-builder and workflow-automation delegate IAM role creation and permission scoping to this skill. They do not create roles themselves.
- **workflow-automation**: Extracts action FQNs from workflow spec → resolves to IAM permissions via `iam_permissions.py` → calls `setup_datadog_action_connection(permissions=...)` to get a dedicated role + connection. Pass the connection ID in `connectionEnvs[].connections[].connectionId`.
- **app-builder**: Extracts action FQNs from app JSON → resolves to IAM permissions via `iam_permissions.py` → calls `setup_datadog_action_connection(permissions=...)` to get a dedicated role + connection. Pass the connection ID via `action_query_names_to_connection_ids` or replace `connectionId` in app JSON.
- **Shared utility**: `.claude/skills/shared/iam_permissions.py` provides `load_action_catalog()`, `extract_actions_from_app_json()`, `extract_actions_from_workflow_json()`, and `resolve_permissions()`.
- Best practice: create **separate connections per app/workflow** — each gets its own IAM role scoped to exactly the AWS actions it needs (true least privilege).

---

## Level 3 References

- `examples/python/setup_action_connection.py` — Full 7-step orchestration with `ensure_iam_role()`, `update_role_permissions()`, and `setup_datadog_action_connection(permissions=...)`; `DatadogResponse` wrapper pattern; exponential backoff; XA_Session pattern for cross-account Lambda usage
- `../shared/iam_permissions.py` — Shared utility for parsing action catalogs, extracting FQNs from app/workflow JSON, and resolving IAM permissions
- `../workflow-automation/examples/datadog_action_role_cfn_snippet.yaml` — CloudFormation IAM role with placeholder external ID; Lambda role permissions
- `../app-builder/examples/terraform/connections.tf` — Terraform `datadog_action_connection` resources (separate workflow vs. app-builder connections)
