# Datadog Tags Actions
Bundle: `com.datadoghq.dd.tags` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Etags)

## com.datadoghq.dd.tags.createHostTags
**Create host tags** — Add new tags to a host and optionally specifying where these tags come from.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | host_name | string | yes | This endpoint allows you to add new tags to a host, optionally specifying where the tags came from. |
  | source | string | no | The source of the tags (for example chef, puppet). A complete list of sources [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
  | host | string | no | Your host name. |
  | tags | any | yes | A list of tags to apply to the host. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | host | string | Your host name. |
  | tags | any | A list of tags that were applied to the host. |
  | tag_value | object | A map  of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map  of tags where the keys are strings and the values are lists of strings. |


## com.datadoghq.dd.tags.deleteHostTags
**Delete host tags** — Remove all user-assigned tags for a single host.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | host_name | string | yes | This endpoint allows you to remove all user-assigned tags for a single host. |
  | source | string | no | The source of the tags (for example chef, puppet). A complete list of sources [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |


## com.datadoghq.dd.tags.getHostTags
**Get host tags** — Return all tags that apply to a given host.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | host_name | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | host | string |  |
  | tags | any | A list of raw tag strings for this host. |
  | tag_value | object | A map  of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map  of tags where the keys are strings and the values are lists of strings. |


## com.datadoghq.dd.tags.listHostTags
**List host tags** — Return a mapping of tags to hosts for your whole infrastructure.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | source | string | no | When specified, filters host list to those tags with the specified source. A complete list of sources [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tags | object | A list of tags to apply to the host. |
  | tag_value | any | A map  of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | any | A map  of tags where the keys are strings and the values are lists of strings. |


## com.datadoghq.dd.tags.updateHostTags
**Update host tags** — Update/replace all tags in an integration source with those supplied in the request.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | host_name | string | yes | This endpoint allows you to update/replace all in an integration source with those supplied in the request. |
  | source | string | no | The source of the tags (for example chef, puppet). A complete list of sources [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value). |
  | host | string | no | Your host name. |
  | tags | any | yes | A list of tags to apply to the host. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | host | string | Your host name. |
  | tags | any | A list of tags that were applied to the host. |
  | tag_value | object | A map  of tags where both the keys and the values are strings. If a key has multiple values, the last value wins. |
  | tag_value_list | object | A map  of tags where the keys are strings and the values are lists of strings. |

