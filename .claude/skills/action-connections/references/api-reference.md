# Action Connections API Reference

Complete HTTP API contracts for creating and managing Datadog Action Connections. All endpoints use the `https://api.datadoghq.com` base URL (adjust for your Datadog site).

## Common Headers

Every request requires these headers:

```
DD-API-KEY: ${DD_API_KEY}
DD-APPLICATION-KEY: ${DD_APP_KEY}
Content-Type: application/json
```

## Error Response Shape

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

Multiple errors may be returned in the array when validation fails on several fields simultaneously.

---

## POST /api/v2/actions/connections

Create a new AWS action connection.

**Request:**

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

**Response (201 Created):**

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

**Status codes:** `201` (created), `400` (invalid payload), `403` (missing `connections_write` scope), `409` (name already exists), `429` (rate limited).

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

---

## GET /api/v2/actions/connections/{id}

Retrieve a connection by ID. Used to verify connection readiness after creation.

**Response (200 OK):**

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
          "principal_id": "464622532012"
        }
      }
    }
  }
}
```

Note: This endpoint does NOT reliably return the `external_id`. Use the `custom_connections` endpoint instead (see below).

**Status codes:** `200` (success), `400` (invalid ID format), `403` (missing scope), `404` (not found), `429` (rate limited).

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## PATCH /api/v2/actions/connections/{id}

Update an existing connection (change role name, account ID, or connection name).

**Request:**

```json
{
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
}
```

**Response (200 OK):** Returns the full updated connection object in the same shape as the POST response.

**Status codes:** `200` (updated), `400` (invalid payload), `403` (missing scope), `404` (connection not found), `429` (rate limited).

**curl:**

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

---

## DELETE /api/v2/actions/connections/{id}

Delete a connection. Any workflows or apps referencing this connection will fail until reassigned.

**Response:** `204 No Content` on success (empty body).

**Status codes:** `204` (deleted), `403` (missing scope), `404` (not found), `429` (rate limited).

**curl:**

```bash
curl -X DELETE "https://api.datadoghq.com/api/v2/actions/connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## GET /api/v2/connection/custom_connections/{id}

Retrieve the external ID for a connection. This is a **different API path** from the actions/connections endpoint -- using the wrong endpoint is the most common mistake.

**Response (200 OK):**

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

If this returns an empty string, you called the wrong endpoint (`/api/v2/actions/connections/` instead of `/api/v2/connection/custom_connections/`).

**Status codes:** `200` (success).

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/connection/custom_connections/${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## POST /api/v2/restriction_policy/connection:{connection_id}

Set access policy to make a connection available org-wide (by default, only the creator can use it).

**Request:**

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
- `id`: Must be `connection:{connection_id}` (resource type prefix required)
- `relation`: Valid values for connections: `viewer`, `resolver`, `editor`
- `principals`: Format `type:id` -- supported types: `role`, `team`, `user`, `org`
- Get your org ID from `GET /api/v2/current_user` at `data.attributes.org.public_id`

**Response (200 OK):** Returns the created restriction policy object.

**Status codes:** `200` (created/updated), `400` (invalid payload), `403` (missing scope), `429` (rate limited).

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

---

## GET /api/v2/restriction_policy/connection:{connection_id}

Read the current restriction policy for a connection.

**Response (200 OK):**

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

**Status codes:** `200` (success), `400` (invalid resource ID format), `403` (missing scope), `429` (rate limited).

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/restriction_policy/connection:${CONNECTION_ID}" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

---

## GET /api/v2/current_user

Retrieve the current user's profile, including the org public ID needed for restriction policies.

**Response (200 OK):** (abbreviated)

```json
{
  "data": {
    "id": "user-uuid",
    "type": "users",
    "attributes": {
      "name": "User Name",
      "email": "user@example.com",
      "org": {
        "public_id": "abc123def456"
      }
    }
  }
}
```

Key field: `data.attributes.org.public_id` -- used as the principal in restriction policies (format: `org:{public_id}`).

**Status codes:** `200` (success), `403` (invalid API/app key).

**curl:**

```bash
curl -X GET "https://api.datadoghq.com/api/v2/current_user" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```
