# Datadog AuthN Mappings Actions
Bundle: `com.datadoghq.dd.authnmappings` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eauthnmappings)

## com.datadoghq.dd.authnmappings.createAuthNMapping
**Create AuthN mapping** — Create an AuthN Mapping.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | attribute_key | string | no | Key portion of a key/value pair of the attribute sent from the Identity Provider. |
  | attribute_value | string | no | Value portion of a key/value pair of the attribute sent from the Identity Provider. |
  | relationships | any | no | Relationship of AuthN Mapping create object to a Role or Team. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The AuthN Mapping object returned by API. |
  | included | array<object> | Included data in the AuthN Mapping response. |


## com.datadoghq.dd.authnmappings.deleteAuthNMapping
**Delete AuthN mapping** — Delete an AuthN Mapping specified by AuthN Mapping UUID.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | authn_mapping_id | string | yes | The UUID of the AuthN Mapping. |


## com.datadoghq.dd.authnmappings.getAuthNMapping
**Get AuthN mapping** — Get an AuthN Mapping specified by the AuthN Mapping UUID.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | authn_mapping_id | string | yes | The UUID of the AuthN Mapping. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The AuthN Mapping object returned by API. |
  | included | array<object> | Included data in the AuthN Mapping response. |


## com.datadoghq.dd.authnmappings.listAuthNMappings
**List AuthN mappings** — List all AuthN Mappings in the org.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_size | number | no | Size for a given page. |
  | page_number | number | no | Specific page number to return. |
  | sort | string | no | Sort AuthN Mappings depending on the given field. |
  | filter | string | no | Filter all mappings by the given string. |
  | resource_type | string | no | Filter by mapping resource type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of returned AuthN Mappings. |
  | included | array<object> | Included data in the AuthN Mapping response. |
  | meta | object | Object describing meta attributes of response. |


## com.datadoghq.dd.authnmappings.updateAuthNMapping
**Update AuthN mapping** — Edit an AuthN Mapping.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | authn_mapping_id | string | yes | The UUID of the AuthN Mapping. |
  | attribute_key | string | no | Key portion of a key/value pair of the attribute sent from the Identity Provider. |
  | attribute_value | string | no | Value portion of a key/value pair of the attribute sent from the Identity Provider. |
  | id | string | yes | ID of the AuthN Mapping. |
  | relationships | any | no | Relationship of AuthN Mapping update object to a Role or Team. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The AuthN Mapping object returned by API. |
  | included | array<object> | Included data in the AuthN Mapping response. |

