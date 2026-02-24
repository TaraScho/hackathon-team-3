# Datadog Restriction Policies Actions
Bundle: `com.datadoghq.dd.restrictionpolicies` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Erestrictionpolicies)

## com.datadoghq.dd.restrictionpolicies.deleteRestrictionPolicy
**Delete restriction policy** — Deletes the restriction policy associated with a specified resource.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | resource_id | string | yes | Identifier, formatted as `type:id`. |


## com.datadoghq.dd.restrictionpolicies.getRestrictionPolicy
**Get restriction policy** — Retrieves the restriction policy associated with a specified resource.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | resource_id | string | yes | Identifier, formatted as `type:id`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Restriction policy object. |


## com.datadoghq.dd.restrictionpolicies.updateRestrictionPolicy
**Update restriction policy** — Updates the restriction policy associated with a resource.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | resource_id | string | yes | Identifier, formatted as `type:id`. |
  | allow_self_lockout | boolean | no | Allows admins (users with the `user_access_manage` permission) to remove their own access from the resource if set to `true`. |
  | bindings | array<object> | yes | An array of bindings. |
  | id | string | yes | The identifier, always equivalent to the value specified in the `resource_id` path parameter. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Restriction policy object. |

