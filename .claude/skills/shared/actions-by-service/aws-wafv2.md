# AWS WAFV2 Actions
Bundle: `com.datadoghq.aws.wafv2` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ewafv2)

## com.datadoghq.aws.wafv2.add_to_ip_set
**Add to IP set** — Add given IPs to an IP set if they don't already exist.
- Stability: stable
- Permissions: `wafv2:GetIPSet`, `wafv2:UpdateIPSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipSetId | string | yes | A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |
  | ipSetName | string | yes | The name of the IP set. You cannot change the name of an IPSet after you create it. |
  | addressesToAdd | array<string> | yes | A list of one or more IP addresses or blocks of IP addresses. WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSet | object | One or more IP addresses or blocks of IP addresses, specified in CIDR notation. |
  | addedAddresses | array<string> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.getRegexPatternSet
**Get regex pattern set** — Retrieves the specified RegexPatternSet.
- Stability: stable
- Permissions: `wafv2:GetRegexPatternSet`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the set. You cannot change the name after you create the set. |
  | scope | string | yes | Specifies whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an A... |
  | id | string | yes | A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegexPatternSet | object |  |
  | LockToken | string | A token used for optimistic locking. WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the... |


## com.datadoghq.aws.wafv2.get_ip_set
**Get IP set** — Retrieve an IP set.
- Stability: stable
- Permissions: `wafv2:GetIPSet`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipSetId | string | yes | A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |
  | ipSetName | string | yes | The name of the IP set. You cannot change the name of an `IPSet` after you create it. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSet | object | One or more IP addresses or blocks of IP addresses, specified in CIDR notation. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.get_web_acl
**Get web ACL** — Retrieve a WebACL.
- Stability: stable
- Permissions: `wafv2:GetWebACL`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | webAclId | string | yes | The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |
  | webAclName | string | yes | The name of the web ACL. You cannot change the name of a web ACL after you create it. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | webAcl | object | The web ACL specification. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.list_ip_sets
**List IP set** — Retrieve an array of `IPSetSummary` objects for your IP sets.
- Stability: stable
- Permissions: `wafv2:ListIPSets`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no |  |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSets | array<object> | One or more IP addresses or blocks of IP addresses, specified in CIDR notation. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.list_web_acls
**List web ACL** — Retrieve an array of `WebACLSummary` objects for your web ACLs.
- Stability: stable
- Permissions: `wafv2:ListWebACLs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no |  |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | webAcls | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.remove_from_ip_set
**Remove from IP set** — Remove given IPs from an IP set.
- Stability: stable
- Permissions: `wafv2:GetIPSet`, `wafv2:UpdateIPSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipSetId | string | yes | A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |
  | ipSetName | string | yes | The name of the IP set. You cannot change the name of an `IPSet` after you create it. |
  | addressesToRemove | array<string> | yes | A list of one or more IP addresses or blocks of IP addresses. WAF supports all IPv4 and IPv6 CIDR ranges except for `/0`. |
  | scope | string | no | Specify whether this is for an Amazon CloudFront distribution or for a regional application. A CloudFront application must use `us-east-1` as its region. A regional application can be an Applicatio... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | ipSet | object | One or more IP addresses or blocks of IP addresses, specified in CIDR notation. |
  | removedAddresses | array<string> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.wafv2.updateRegexPatternSet
**Update regex pattern set** — Updates the specified RegexPatternSet. This operation completely replaces the mutable specifications that you already have for the regex pattern set with the ones that you provide to this call.
- Stability: stable
- Permissions: `wafv2:UpdateRegexPatternSet`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the set. You cannot change the name after you create the set. |
  | scope | string | yes | Specifies whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an A... |
  | id | string | yes | A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete. |
  | description | string | no | A description of the set that helps with identification. |
  | regularExpressionList | array<object> | yes |  |
  | lockToken | string | yes | A token used for optimistic locking. WAF returns a token to your get and list requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | NextLockToken | string | A token used for optimistic locking. WAF returns this token to your update requests. You use NextLockToken in the same manner as you use LockToken. |

