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

Datadog Action Connections authorize Workflow Automation and App Builder to perform actions in external systems — AWS, HTTP APIs, and other integrations. Each connection encapsulates credentials so workflows and apps can execute actions without embedding secrets.

Each app or workflow gets its **own dedicated** connection (1:1 model — never shared).

### Dependency Diagram

```
action-connections (×1 per app)    ──► app-builder    ──► dashboards (composite)
action-connections (×1 per workflow) ──► workflow-automation
```

---

## Doc Fetch URLs

Before executing, fetch current API documentation:

| Source | URL / Resource |
|---|---|
| Datadog API docs | `https://docs.datadoghq.com/api/latest/action-connection.md` |
| Terraform provider | TF MCP → `datadog_action_connection` |

---

## Output Format Selection

Read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` |
| `shell` | Claude executes `curl` + `aws cli` commands directly via Bash tool |

---

## When to Use

- You need to create a new action connection for Workflow Automation or App Builder
- You are debugging 403 errors on the `/api/v2/actions/connections` endpoint
- You need to set restriction policies on connections

---

## Prerequisites

| Requirement | Details |
|---|---|
| `DD_API_KEY` | Datadog API key with org-level write access |
| `DD_APP_KEY` | Datadog app key with scopes: `connections_read`, `connections_write`, `connections_resolve`, `workflows_read`, `workflows_write`, `workflows_run`, `apps_run`, `apps_write` |
| AWS CLI | Configured with permissions: `iam:CreateRole`, `iam:GetRole`, `iam:PutRolePolicy`, `iam:UpdateAssumeRolePolicy`, `sts:GetCallerIdentity` |

---

## Supported Integration Types

| Type | `integration.type` | `credentials.type` | Use Case |
|---|---|---|---|
| **AWS** | `"AWS"` | `"AWSAssumeRole"` | Cross-account IAM role assumption |
| **HTTP Token** | `"HTTP"` | `"TokenAuth"` | APIs using bearer tokens or API keys |
| **HTTP Basic** | `"HTTP"` | `"HTTPBasic"` | APIs using HTTP Basic Auth |
| **HTTP OAuth** | `"HTTP"` | `"HTTPOAuth"` | APIs requiring OAuth2 token exchange |
| **HTTP mTLS** | `"HTTP"` | `"HTTPmTLS"` | APIs requiring mutual TLS client certificates |

---

## Core Workflow: AWS Connection Setup (6 Steps)

All API calls require headers: `DD-API-KEY: ${DD_API_KEY}`, `DD-APPLICATION-KEY: ${DD_APP_KEY}`, `Content-Type: application/json`.

### Step 0 — Ensure IAM role exists

Check if role exists (`aws iam get-role`). If not, create with `aws iam create-role` using path `/datadog/`, trust policy allowing `sts:AssumeRole` from Datadog's account, and a placeholder external ID.

### Step 0.5 — Scope role permissions (optional)

If specific IAM permissions are needed, apply an inline policy with `aws iam put-role-policy`. Each role is dedicated to one app/workflow, so the policy is replaced entirely.

### Step 1 — Create the action connection

`POST /api/v2/actions/connections` with `integration.type: "AWS"`, `credentials.type: "AWSAssumeRole"`, the role name, and 12-digit account ID.

Response: `data.id` (connection UUID).

### Step 2 — Retrieve the external ID

**Use the separate endpoint** — the actions/connections endpoint does NOT reliably return the external ID:

`GET /api/v2/connection/custom_connections/{connection_id}`

External ID is at: `data.attributes.data.aws.assumeRole.externalId`

### Step 3 — Update IAM role trust policy

Patch the trust policy with the real external ID using `aws iam update-assume-role-policy`.

### Step 4 — Set restriction policy

`POST /api/v2/restriction_policy/connection:{connection_id}` with an `editor` binding for your org.

Get org ID from `GET /api/v2/current_user` → `data.attributes.org.public_id`.

### Step 5 — Verify readiness

Poll `GET /api/v2/actions/connections/{connection_id}` until 200 (up to 30 seconds with exponential backoff).

---

## Gotchas & Patterns

| Gotcha | Details |
|---|---|
| **External ID wrong endpoint** | `/api/v2/actions/connections/{id}` returns empty `externalId`. Must use `/api/v2/connection/custom_connections/{id}` — path: `data.attributes.data.aws.assumeRole.externalId` |
| **Fixed AWS account ID** | Datadog's account: `464622532012` (US1/US3/US5/EU1). AP1: `417141415827`, AP2: `412381753143`, GovCloud: `065115117704` or `392588925713` |
| **PascalCase required** | `credentials.type` must be `"AWSAssumeRole"` (not lowercase). `integration.type` must be `"AWS"` (uppercase) |
| **Role name, not ARN** | `credentials.role` takes the role name only (e.g., `"DatadogAction-MyApp"`), not the full ARN |
| **Restriction policy ID format** | Must be `"connection:{connection_id}"` — the resource type prefix is required |
| **IAM propagation delay** | Wait 5-10 seconds after `update-assume-role-policy` before testing the connection |
| **409 = already exists** | Connection name already exists — list connections, retrieve existing ID, skip creation |
| **External ID rotation** | Regenerating external ID causes all workflows/apps using that connection to fail during rotation window |
| **Permission levels** | `viewer` < `resolver` < `editor`. `resolver` can only execute existing steps, not create new ones using the connection |

---

## Cross-Skill Notes

- **This skill is the single connection authority.** App-builder and workflow-automation delegate all connection creation here.
- **workflow-automation**: Pass connection ID in `connectionEnvs[].connections[].connectionId`.
- **app-builder**: Pass connection ID to replace `__CONNECTION_ID__` in app JSON.
- Best practice: create **separate connections per app/workflow** — each gets its own IAM role scoped to exactly the AWS actions it needs.

---

## JSON Examples

This skill has no JSON examples (procedural, not template-based).
