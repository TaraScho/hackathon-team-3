---
name: action-connections
description: >
  Creates Datadog Action Connections and configures required integration authentication for Workflow
  Automation and App Builder. Use when user asks to set up new Datadog Action Connections.
metadata:
  author: hackathon-team-3
  tags: [actions, action-connections, workflow-automation, app-builder]
---

# Action Connections Skill

## Overview

Datadog Action Connections authorize Workflow Automation and App Builder to perform actions in external systems — AWS, HTTP APIs, and other integrations. Each connection encapsulates the credentials and configuration needed for a specific integration, so workflows and apps can execute actions without embedding secrets.

### Supported Integration Types

| Type | `integration.type` | `credentials.type` | Use Case |
|---|---|---|---|
| **AWS** | `"AWS"` | `"AWSAssumeRole"` | Cross-account IAM role assumption for AWS actions (EC2, ECS, IAM, S3, etc.) |
| **HTTP Token** | `"HTTP"` | `"TokenAuth"` | APIs using bearer tokens or API keys |
| **HTTP Basic** | `"HTTP"` | `"HTTPBasic"` | APIs using HTTP Basic Auth |
| **HTTP OAuth** | `"HTTP"` | `"HTTPOAuth"` | APIs requiring OAuth2 token exchange |
| **HTTP mTLS** | `"HTTP"` | `"HTTPmTLS"` | APIs requiring mutual TLS client certificates |

See `references/advanced-patterns.md` for HTTP connection payloads, Private Action Runners, and security best practices.

### AWS Connections (Primary Use Case)

AWS connections use cross-account IAM role assumption with an external ID to prevent confused-deputy attacks:
- Datadog's fixed AWS account ID is **`464622532012`** (US1 site; see `references/advanced-patterns.md` for other regions)
- Datadog generates a unique **external ID** per connection — you must embed this in the IAM role trust policy
- The connection ID (UUID) is referenced in workflow `connectionEnvs` and app-builder `action_query_names_to_connection_ids`

### Dependency Diagram

```
action-connections ──► workflow-automation
        │
        └──────────► app-builder ──► dashboards
```

**This skill is the foundational prerequisite.** Workflows and apps cannot perform external actions until a working connection exists.

---

## When to Use

**Any integration type:**
- You need to create a new action connection for Workflow Automation or App Builder
- You are debugging 403 errors on the `/api/v2/actions/connections` endpoint
- You need to set restriction policies on connections

**AWS connections:**
- You need Datadog Workflow Automation to perform AWS actions (IAM, EC2, ECS, S3, etc.)
- You need App Builder apps to read/write AWS resources
- You are setting up a new Datadog org and need to wire up AWS access
- You want to automate connection setup inside a Lambda
- You want to write Terraform that manages the connection as code
- You need to understand the external ID and why it must be fetched from a different API endpoint

**HTTP connections:**
- You need to connect Datadog workflows to a third-party API (GitHub, Slack, PagerDuty, internal services)
- See `references/advanced-patterns.md` for HTTP connection payloads and auth patterns

---

## Prerequisites

**All connection types:**

| Requirement | Details |
|---|---|
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Datadog app key scoped for actions (see Required App Key Scopes below) |

**AWS connections additionally require:**

| Requirement | Details |
|---|---|
| IAM role | Auto-created if missing (path `/datadog/`); Datadog account `464622532012` is trust principal |
| Python dependencies | `boto3`, `requests` |
| AWS permissions | `iam:CreateRole`, `iam:GetRole`, `iam:PutRolePolicy`, `iam:UpdateAssumeRolePolicy`, `sts:GetCallerIdentity` |

### Required App Key Scopes

Your `DD_APP_KEY` must have these scopes:

```
connections_read, connections_write, connections_resolve
workflows_read, workflows_write, workflows_run
apps_run, apps_write
```

---

## API Endpoints Quick Reference

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/v2/actions/connections` | Create action connection |
| `GET` | `/api/v2/actions/connections/{id}` | Get connection / verify readiness |
| `PATCH` | `/api/v2/actions/connections/{id}` | Update connection |
| `DELETE` | `/api/v2/actions/connections/{id}` | Delete connection |
| `GET` | `/api/v2/connection/custom_connections/{id}` | **Get external ID** (different endpoint!) |
| `POST` | `/api/v2/restriction_policy/{resource_id}` | Set org-wide access |
| `GET` | `/api/v2/current_user` | Get org ID for restriction policy |

Full request/response schemas, curl examples, and status codes are in `references/api-reference.md`.

---

## AWS Connection Setup (6-Step Workflow)

The reference implementation is `setup_datadog_action_connection()` in `examples/python/setup_action_connection.py`.

All endpoints require these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

### Step 0 -- Ensure IAM role exists

The `ensure_iam_role()` function checks if the role exists via `iam:GetRole`. If not, it creates the role with path `/datadog/`, a trust policy allowing `sts:AssumeRole` from `464622532012`, and a placeholder external ID (updated in Step 4).

```python
from setup_action_connection import ensure_iam_role

response = ensure_iam_role("DatadogAction-MyApp-abc123", aws_session=session)
```

### Step 0.5 -- Scope role permissions (optional)

If a `permissions` list is provided, `update_role_permissions()` applies an inline policy with exactly those IAM actions. Each role is dedicated to one app/workflow, so the policy is replaced entirely.

```python
from setup_action_connection import update_role_permissions

permissions = ["ec2:DescribeInstances", "ec2:DescribeTags", "s3:ListBuckets"]
update_role_permissions("DatadogAction-MyApp-abc123", permissions, aws_session=session)
```

Downstream skills compute permissions using the shared `iam_permissions.py` utility:

```python
import sys
sys.path.insert(0, ".claude/skills/shared")
from iam_permissions import load_action_catalog, extract_actions_from_app_json, resolve_permissions

catalog = load_action_catalog(".claude/skills/shared/actions-by-service")
actions = extract_actions_from_app_json("path/to/app.json")
permissions = resolve_permissions(actions, catalog)
```

### Step 1 -- Create the AWS action connection

**`POST /api/v2/actions/connections`** -- Submit the connection with `integration.type: "AWS"`, `credentials.type: "AWSAssumeRole"` (PascalCase), the role name, and 12-digit account ID.

Key fields in response: `data.id` (connection UUID), `credentials.external_id` (read-only).

### Step 2 -- Retrieve the external ID

**Critical:** The `/api/v2/actions/connections` endpoint does NOT reliably return the external ID. Use the separate endpoint:

**`GET /api/v2/connection/custom_connections/{connection_id}`**

External ID path: `data.attributes.data.aws.assumeRole.externalId`

If this returns an empty string, you called the wrong endpoint.

### Step 3 -- Update IAM role trust policy

Patch the trust policy with the external ID from Step 2:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::464622532012:root"},
    "Action": "sts:AssumeRole",
    "Condition": {"StringEquals": {"sts:ExternalId": "<external-id-from-step-3>"}}
  }]
}
```

### Step 4 -- Set restriction policy

Make the connection org-wide accessible (by default, only the creator can use it):

**`POST /api/v2/restriction_policy/connection:{connection_id}`** with an `editor` binding for your org principal.

Get your org ID from `GET /api/v2/current_user` at `data.attributes.org.public_id`.

### Step 5 -- Verify readiness

Poll `GET /api/v2/actions/connections/{connection_id}` until it returns 200 (up to 30 seconds with exponential backoff). This prevents race conditions in downstream app/workflow creation.

---

## HTTP Connection Setup

For HTTP-based connections (TokenAuth, HTTPBasic, HTTPOAuth, HTTPmTLS):

1. **POST the connection** with `integration.type: "HTTP"` and the appropriate `credentials.type`
2. **Set restriction policy** (same as AWS Step 4)
3. **Verify readiness** (same as AWS Step 5)

No IAM role, external ID, or trust policy steps needed. See `references/advanced-patterns.md` for full payload examples per auth type.

---

## Terraform Pattern (AWS)

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

locals {
  connection_id = datadog_action_connection.aws_workflow.id
}
```

See `../app-builder/examples/terraform/connections.tf` for the full pattern including separate workflow vs. app-builder connections.

---

## CloudFormation Pattern (AWS)

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

After the Lambda runs `setup_datadog_action_connection()`, the trust policy is patched with the real external ID.

---

## Common Pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| 403 on `POST /api/v2/actions/connections` | App key missing `connections_write` scope | Ensure `DD_APP_KEY` has all required scopes (see Required App Key Scopes) |
| 409 on `POST /api/v2/actions/connections` | Connection name already exists | List connections, retrieve existing ID, skip creation |
| `externalId` is empty string | Called `/api/v2/actions/connections/{id}` instead of `/api/v2/connection/custom_connections/{id}` | Use the `custom_connections` endpoint for external ID |
| Connection works for creator but not others | Restriction policy not set | POST to `/api/v2/restriction_policy/connection:{id}` with org binding |
| Trust fails after external ID update | IAM propagation delay | Wait 5-10 seconds after `update_assume_role_policy` before testing |

---

## Cross-Skill Notes

- **This skill is the single connection authority.** App-builder and workflow-automation delegate all connection creation to this skill. For AWS connections, this includes IAM role creation and permission scoping. They do not create connections themselves.
- **workflow-automation**: Extracts action FQNs from workflow spec, resolves to IAM permissions via `iam_permissions.py`, calls `setup_datadog_action_connection(permissions=...)`. Pass the connection ID in `connectionEnvs[].connections[].connectionId`.
- **app-builder**: Extracts action FQNs from app JSON, resolves to IAM permissions via `iam_permissions.py`, calls `setup_datadog_action_connection(permissions=...)`. Pass the connection ID via `action_query_names_to_connection_ids`.
- **Shared utility**: `.claude/skills/shared/iam_permissions.py` provides `load_action_catalog()`, `extract_actions_from_app_json()`, `extract_actions_from_workflow_json()`, and `resolve_permissions()`.
- Best practice: create **separate connections per app/workflow** -- each gets its own IAM role scoped to exactly the AWS actions it needs.

---

## Level 3 References

- `examples/python/setup_action_connection.py` -- Full 6-step orchestration with `ensure_iam_role()`, `update_role_permissions()`, and `setup_datadog_action_connection(permissions=...)`; `DatadogResponse` wrapper pattern; exponential backoff; XA_Session pattern for cross-account Lambda usage
- `../shared/iam_permissions.py` -- Shared utility for parsing action catalogs, extracting FQNs from app/workflow JSON, and resolving IAM permissions
- `../workflow-automation/examples/datadog_action_role_cfn_snippet.yaml` -- CloudFormation IAM role with placeholder external ID; Lambda role permissions
- `../app-builder/examples/terraform/connections.tf` -- Terraform `datadog_action_connection` resources (separate workflow vs. app-builder connections)

---

## Additional Resources

- **`references/api-reference.md`** -- Complete HTTP API contracts for all endpoints: POST/GET/PATCH/DELETE connections, GET custom_connections (external ID retrieval), POST/GET restriction policies. Includes full request/response JSON schemas, curl examples, status codes, and error response format.
- **`references/advanced-patterns.md`** -- Region-specific Datadog AWS account IDs (AP1, AP2, GovCloud), connection groups with identifier tags, `generate_new_external_id` flag for external ID rotation, connection permission levels (viewer/resolver/editor), HTTP connection types (Token/Basic/OAuth/mTLS), Private Action Runner setup, and security best practices.
