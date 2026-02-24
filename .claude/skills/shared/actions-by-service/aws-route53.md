# AWS Route53 Actions
Bundle: `com.datadoghq.aws.route53` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eroute53)

## com.datadoghq.aws.route53.associateFirewallRuleGroup
**Associate firewall rule group** — Associate a firewall rule group with a VPC, to provide DNS filtering for the VPC.
- Stability: stable
- Permissions: `route53resolver:AssociateFirewallRuleGroup`, `route53resolver:ListFirewallRuleGroupAssociations`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | firewallRuleGroupId | string | yes |  |
  | name | string | yes |  |
  | priority | number | yes | The processing order of the rule group among the rule groups that you associate with a VPC. DNS firewall filters are applied to VPC traffic starting from the rule group with the lowest numeric prio... |
  | vpcId | string | yes | The unique identifier of the VPC to associate with the rule group. |
  | creatorRequestId | string | no | A unique string to identify the request and allow failed requests to be retried, without risk of running the operation twice. Can be any unique string, for example, a date or time stamp. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | association | object |  |
  | associationAlreadyExists | boolean |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.route53.disassociateFirewallRuleGroup
**Disassociate firewall rule group** — Disassociate a firewall rule group from a VPC, to remove DNS filtering from the VPC.
- Stability: stable
- Permissions: `route53resolver:DisassociateFirewallRuleGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | associationId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | removedAssociation | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.route53.getAWSRoute53HealthCheck
**Describe health check** — Get details about a health check.
- Stability: stable
- Permissions: `route53:GetHealthCheck`, `route53:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | healthCheck | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.route53.getHealthCheckStatus
**Get health check status** — Get the status of a health check.
- Stability: stable
- Permissions: `route53:GetHealthCheckStatus`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | healthCheckId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | healthCheckObservations | array<object> | A list that contains one `HealthCheckObservation` element for each Amazon Route 53 health checker that is reporting a status about the health check endpoint. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.route53.listAWSRoute53HealthCheck
**List health checks** — List health checks.
- Stability: stable
- Permissions: `route53:ListHealthChecks`, `route53:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | healthChecks | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.route53.listFirewallRuleGroupAssociations
**List firewall rule group associations** — Retrieve any defined firewall rule group associations. Each association enables DNS filtering for a VPC with one rule group.
- Stability: stable
- Permissions: `route53resolver:ListFirewallRuleGroupAssociations`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | firewallRuleGroupId | string | yes |  |
  | vpcId | string | yes | The unique identifier of the VPC to associate with the rule group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | associations | array<object> | A list of firewall rule group associations. |

