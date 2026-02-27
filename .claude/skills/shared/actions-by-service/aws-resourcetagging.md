# AWS Resources Tagging Actions
Bundle: `com.datadoghq.aws.resourcetagging` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eresourcetagging)

## com.datadoghq.aws.resourcetagging.getResourceTags
**Get resource tags** — Return all tags associated with a resource.
- Stability: stable
- Permissions: `tag:GetResources`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tags | object |  |
  | tagValueList | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.resourcetagging.getResourcesByTags
**Get resources by tags** — Get all resources with the tags specified in the filters. If the filter list is empty, the response includes all resources that are currently tagged or have ever had a tag.
- Stability: stable
- Permissions: `tag:GetResources`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceTypes | array<string> | yes | The list of resource types to be included in the response. For the list of services whose resources can be used in this parameter, see [Services that support the Resource Groups Tagging API](https:... |
  | filters | array<object> | yes | List of tag filters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. The tags filters can be one of th... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | resources | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.resourcetagging.tagResources
**Tag resources** — Add tags to multiple AWS resources.
- Stability: stable
- Permissions: `tag:TagResources`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArns | array<string> | yes | ARNs of the resources to tag. |
  | tags | any | yes | A list of tags to add to the specified resource. Each tag consists of a `key` and a `value`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | failures | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.resourcetagging.untagResources
**Untag resources** — Remove tags from multiple AWS resources.
- Stability: stable
- Permissions: `tag:UntagResources`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArns | array<string> | yes | The ARNs of the resources from which to remove tags. |
  | tagKeys | array<string> | yes | The list of tag keys to remove from the specified resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | failures | object |  |
  | amzRequestId | string | The unique identifier for the request. |

