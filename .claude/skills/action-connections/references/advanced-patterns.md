# Action Connections Advanced Patterns

Advanced configuration patterns for Datadog Action Connections beyond the standard 6-step setup workflow. This document covers multi-region deployments, connection grouping, security hardening, HTTP connection types, and Private Action Runners.

---

## Region-Specific Datadog Account IDs

The standard Datadog principal account ID (`464622532012`) applies only to the US1 site (`datadoghq.com`). Other Datadog sites use different AWS account IDs as the trust principal. Using the wrong account ID causes `AssumeRole` to fail silently.

| Datadog Site | Site URL | AWS Account ID |
|---|---|---|
| US1 (default) | `datadoghq.com` | `464622532012` |
| US3 | `us3.datadoghq.com` | `464622532012` |
| US5 | `us5.datadoghq.com` | `464622532012` |
| AP1 (Tokyo) | `ap1.datadoghq.com` | `417141415827` |
| AP2 (Sydney) | `ap2.datadoghq.com` | `412381753143` |
| EU1 | `datadoghq.eu` | `464622532012` |
| GovCloud (US1-FED) | `ddog-gov.com` | `065115117704` |
| GovCloud (alternate) | `ddog-gov.com` | `392588925713` |

When building multi-region connection automation, determine the correct account ID from the Datadog site URL:

```python
DD_ACCOUNT_IDS = {
    "datadoghq.com": "464622532012",
    "us3.datadoghq.com": "464622532012",
    "us5.datadoghq.com": "464622532012",
    "ap1.datadoghq.com": "417141415827",
    "ap2.datadoghq.com": "412381753143",
    "datadoghq.eu": "464622532012",
    "ddog-gov.com": "065115117704",
}

def get_dd_account_id(site: str) -> str:
    """Return the Datadog AWS account ID for the given site."""
    return DD_ACCOUNT_IDS.get(site, "464622532012")
```

For GovCloud deployments, the IAM role trust principal must reference the GovCloud partition:

```json
{
  "Principal": {
    "AWS": "arn:aws-us-gov:iam::065115117704:root"
  }
}
```

---

## Connection Groups with Identifier Tags

When managing many connections across multiple AWS accounts or environments, use a naming convention and identifier tags to organize them into logical groups.

### Naming Convention

```
{purpose}-{environment}-{region}-{account-suffix}
```

Examples:
- `workflow-prod-us-east-1-7890` -- production workflow connection in us-east-1
- `appbuilder-staging-eu-west-1-3456` -- staging App Builder connection in eu-west-1

### Identifier Tags in Restriction Policies

Group connections using teams in restriction policies:

```json
{
  "data": {
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {
          "relation": "editor",
          "principals": ["team:platform-eng-team-id"]
        },
        {
          "relation": "viewer",
          "principals": ["org:your-org-id"]
        }
      ]
    }
  }
}
```

This pattern gives full edit access to the platform engineering team while allowing the rest of the org to view (and use) the connection in their workflows.

---

## External ID Regeneration

If an external ID is compromised or you need to rotate it for compliance, use the `generate_new_external_id` flag when updating the connection:

```bash
curl -X PATCH "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "type": "action_connection",
      "attributes": {
        "name": "ExistingConnectionName",
        "integration": {
          "type": "AWS",
          "credentials": {
            "type": "AWSAssumeRole",
            "role": "DatadogActionRole",
            "account_id": "123456789012",
            "generate_new_external_id": true
          }
        }
      }
    }
  }'
```

After regeneration, you must:
1. Fetch the new external ID from `GET /api/v2/connection/custom_connections/{id}`
2. Update the IAM role trust policy with the new value
3. Wait for IAM propagation (5-10 seconds) before testing

All workflows and apps using this connection will fail during the window between external ID regeneration and IAM policy update. Schedule rotations during maintenance windows.

---

## Connection Permission Levels

Restriction policies support three relation levels for connections. Choose the minimum level required for each principal.

| Relation | Capabilities |
|---|---|
| `viewer` | Can see the connection in the UI and use it in workflows/apps they run |
| `resolver` | Viewer permissions plus can resolve the connection (execute the assume-role) in workflow steps they author |
| `editor` | Full access: create, update, delete the connection and its restriction policy |

### Recommended Principal Assignments

- **Platform/DevOps team**: `editor` -- manages connection lifecycle
- **Application developers**: `resolver` -- can author workflows that use the connection
- **Everyone else (org-wide)**: `viewer` -- can run workflows that reference the connection but cannot modify it or create new workflow steps using it

Example with multiple bindings:

```json
{
  "data": {
    "type": "restriction_policy",
    "attributes": {
      "bindings": [
        {"relation": "editor", "principals": ["team:platform-eng-id"]},
        {"relation": "resolver", "principals": ["team:app-dev-id", "team:sre-id"]},
        {"relation": "viewer", "principals": ["org:org-public-id"]}
      ]
    }
  }
}
```

---

## HTTP Connection Types

Action connections are not limited to AWS. Datadog supports several HTTP-based connection types for integrating with arbitrary APIs and services.

### Token Authentication

For APIs that use bearer tokens or API keys in headers:

```json
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "my-api-token",
      "integration": {
        "type": "HTTP",
        "credentials": {
          "type": "TokenAuth",
          "tokens": [
            {
              "name": "Authorization",
              "type": "header",
              "value": "Bearer your-token-here"
            }
          ]
        }
      }
    }
  }
}
```

Token placement options: `header`, `query_param`, `body`.

### Basic Authentication

For APIs that use HTTP Basic Auth:

```json
{
  "credentials": {
    "type": "HTTPBasic",
    "username": "api-user",
    "password": "api-password"
  }
}
```

### 2-Step (OAuth) Authentication

For APIs that require an OAuth token exchange before making requests:

```json
{
  "credentials": {
    "type": "HTTPOAuth",
    "token_url": "https://auth.example.com/oauth2/token",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret",
    "scope": "read write",
    "grant_type": "client_credentials"
  }
}
```

The access token is automatically refreshed when it expires.

### mTLS (Mutual TLS) Authentication

For APIs that require client certificate authentication:

```json
{
  "credentials": {
    "type": "HTTPmTLS",
    "cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
    "key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----",
    "ca_cert": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
  }
}
```

The `ca_cert` field is optional -- include it only if the server uses a private CA.

---

## Private Action Runner

For environments where Datadog cannot directly reach your AWS APIs (VPC-isolated resources, on-premises infrastructure, air-gapped networks), deploy a Private Action Runner.

### How It Works

1. A lightweight container runs inside your network (ECS, Kubernetes, EC2)
2. The runner polls Datadog for pending action executions via HTTPS outbound
3. When a workflow or app triggers an action, the runner executes it locally and returns the result
4. No inbound firewall rules required -- communication is outbound-only

### Runner Setup

```bash
# Pull the runner image
docker pull datadog/private-action-runner:latest

# Run with required environment variables
docker run -d \
  --name dd-action-runner \
  -e DD_API_KEY="${DD_API_KEY}" \
  -e DD_APP_KEY="${DD_APP_KEY}" \
  -e DD_ACTION_RUNNER_ID="${RUNNER_ID}" \
  -e DD_ACTION_RUNNER_PRIVATE_KEY="${RUNNER_PRIVATE_KEY}" \
  datadog/private-action-runner:latest
```

The `RUNNER_ID` and `RUNNER_PRIVATE_KEY` are obtained when you register the runner via the Datadog UI (Workflow Automation > Settings > Private Action Runners).

### Linking a Connection to a Runner

When creating or updating a connection, specify the runner:

```json
{
  "data": {
    "type": "action_connection",
    "attributes": {
      "name": "vpc-internal-api",
      "integration": {
        "type": "HTTP",
        "credentials": {
          "type": "TokenAuth",
          "tokens": [{"name": "X-Api-Key", "type": "header", "value": "key"}]
        }
      },
      "runner_id": "runner-uuid-here"
    }
  }
}
```

### Runner Considerations

- The runner must have network access to the target resources
- If using AWS connections, the runner's host needs an IAM role or credentials that can assume the target role
- Runner health is visible in the Datadog UI; set up a monitor on `datadog.private_action_runner.heartbeat`
- For high availability, deploy multiple runners in the same group -- Datadog round-robins between healthy runners

---

## Security Best Practices

### Least-Privilege IAM Roles

Create one connection per workflow or app. Each connection should reference a dedicated IAM role scoped to the minimum permissions needed:

```python
# Per-app connection with scoped permissions
setup_datadog_action_connection(
    connection_name="appbuilder-ec2-viewer",
    role_name="DatadogAction-EC2Viewer-abc123",
    permissions=["ec2:DescribeInstances", "ec2:DescribeTags"],
    aws_account_id="123456789012"
)
```

Avoid sharing a single PowerUserAccess connection across all workflows.

### External ID Handling

- Never log or expose the external ID in application outputs
- Store external IDs in AWS Secrets Manager or SSM Parameter Store if your automation needs to reference them
- Rotate external IDs on a schedule (quarterly recommended) using `generate_new_external_id`

### App Key Scope Minimization

Ensure your app key has the appropriate scopes for your use case:

| Use Case | Required Scopes |
|---|---|
| Connection management only | `connections_read`, `connections_write` |
| Running existing workflows | `workflows_run`, `connections_resolve` |
| Full automation setup | `connections_read`, `connections_write`, `connections_resolve`, `workflows_read`, `workflows_write`, `workflows_run`, `apps_run`, `apps_write` |

### Audit and Monitoring

- Enable Datadog Audit Trail to track connection creation, modification, and deletion events
- Monitor `aws.iam.assume_role` CloudTrail events filtered to Datadog's account ID to detect unexpected role assumptions
- Set up alerts on `403` errors from the actions API to catch permission drift early

### Network Controls

- Use VPC endpoints for AWS API calls when the Private Action Runner is deployed in a VPC
- Apply SCP (Service Control Policy) guardrails to limit which IAM actions Datadog-assumed roles can perform, as a defense-in-depth layer beyond the inline policy
- For GovCloud deployments, ensure all Datadog API traffic routes through approved network paths
