# AWS WAF classic Actions
Bundle: `com.datadoghq.aws.waf.classic` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ewaf%2Eclassic)

## com.datadoghq.aws.waf.classic.add_ip
**Add to IP set** — Add given IPs to an IP set if they don't already exist.
- Stability: stable
- Permissions: `waf:CreateIPSet`, `waf:GetChangeToken`, `waf:UpdateIPSet`, `waf:GetIPSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipSetId | string | yes | The `IPSetId` of the `IPSet` that you want to update. `IPSetId` is returned by `CreateIPSet` and by `ListIPSets`. |
  | ipType | string | yes | The type of IPs: `IPV4` or `IPV6`. |
  | ipAddresses | array<string> | yes | A list of one or more IP addresses or blocks of IP addresses. WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, or an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSet | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.waf.classic.delete_ip
**Remove from IP set** — Remove given IPs from an IP set.
- Stability: stable
- Permissions: `waf:CreateIPSet`, `waf:GetChangeToken`, `waf:UpdateIPSet`, `waf:DeleteIPSet`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipSetId | string | yes | The `IPSetId` of the `IPSet` that you want to update. `IPSetId` is returned by `CreateIPSet` and by `ListIPSets`. |
  | ipType | string | yes | The type of IPs: `IPV4` or `IPV6`. |
  | ipAddresses | array<string> | yes | A list of one or more IP addresses or blocks of IP addresses. WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, or an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSet | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.waf.classic.get_rule
**Get rule** — Return the rule associated with the `RuleId` included in the `GetRule` request.
- Stability: stable
- Permissions: `waf:GetRule`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ruleId | string | yes | The `RuleId` of the [Rule](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_Rule.html "{isExternal}") that you want to get. `RuleId` is returned by [CreateRule](https://docs.aws.amazon.c... |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, or an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | rule | object | Information about the rule specified in the request. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.waf.classic.get_web_acl
**Get web ACL** — Return the WebACL specified by `WebACLId`.
- Stability: stable
- Permissions: `waf:GetWebACL`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webAclId | string | yes | The `WebACLId` of the WebACL that you want to get. `WebACLId` is returned by [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_CreateWebACL.html "{isExternal}") and by [Lis... |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, or an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | webAcl | object |  |


## com.datadoghq.aws.waf.classic.list_web_acls
**List web ACL** — Return an array of `WebACLSummary` objects in the response.
- Stability: stable
- Permissions: `waf:ListWebACLs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no | Specify the number of WebACL objects for AWS WAF to return from this request. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, or an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | webAcls | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |

