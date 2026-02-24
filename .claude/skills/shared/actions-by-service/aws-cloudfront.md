# AWS CloudFront Actions
Bundle: `com.datadoghq.aws.cloudfront` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecloudfront)

## com.datadoghq.aws.cloudfront.create_invalidation
**Create invalidation** — Create a new invalidation.
- Stability: stable
- Permissions: `cloudfront:CreateInvalidation`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | distributionId | string | yes |  |
  | paths | array<string> | yes | A list of paths to invalidate. For more information, see [Specifying the Objects to Invalidate](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-spe... |
  | waitForCompletion | boolean | no | Wait for the creation request to complete before continuing the workflow. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | status | string |  |
  | createTime | string |  |
  | invalidationBatch | object |  |
  | location | string |  |


## com.datadoghq.aws.cloudfront.getAWSCloudFrontDistribution
**Describe distribution** — Get details about a distribution.
- Stability: stable
- Permissions: `cloudfront:GetDistribution*`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | distribution | object |  |


## com.datadoghq.aws.cloudfront.get_invalidation
**Describe invalidation** — Get information about an invalidation.
- Stability: stable
- Permissions: `cloudfront:GetInvalidation`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | distributionId | string | yes |  |
  | id | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | id | string |  |
  | status | string |  |
  | createTime | string |  |
  | invalidationBatch | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.cloudfront.list_distributions
**List distributions** — List CloudFront distributions. A distribution tells CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.
- Stability: stable
- Permissions: `cloudfront:ListDistributions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxItems | string | no | The maximum number of items returned by this action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | items | array<object> |  |
  | quantity | number |  |
  | isTruncated | boolean |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.cloudfront.list_distributions_by_web_acl
**List distributions by web ACL** — List the distributions that are associated with a WAF web ACL.
- Stability: stable
- Permissions: `cloudfront:ListDistributionsByWebACLId`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webAclId | string | yes | The ID of the WAF web ACL from which to list the associated distributions. If you specify `null` for the ID, the request returns a list of the distributions that aren't associated with a web ACL. |
  | maxItems | string | no | The maximum number of items returned by this action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | items | array<object> |  |
  | quantity | number |  |
  | isTruncated | boolean |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.cloudfront.list_invalidations
**List invalidations** — List invalidation batches.
- Stability: stable
- Permissions: `cloudfront:ListInvalidations`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | distributionId | string | yes |  |
  | maxItems | string | no | The maximum number of items returned by this action. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | items | array<object> |  |
  | quantity | number |  |
  | isTruncated | boolean |  |
  | amzRequestId | string | The unique identifier for the request. |

