# AWS ELB Actions
Bundle: `com.datadoghq.aws.elb` | 16 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eelb)

## com.datadoghq.aws.elb.deregister_instances_from_classic_load_balancer
**Deregister instances from classic load balancer** — Deregister instances from a classic load balancer. After an instance is deregistered, it no longer receives traffic from the load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:DeregisterInstancesWithLoadBalancer`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes |  |
  | instanceIds | array<string> | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceIds | array<string> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.deregister_targets
**Deregister targets** — Deregister targets from a target group. After the targets are deregistered, they no longer receive traffic from the load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:DeregisterTargets`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |
  | targetIds | array<string> | yes | An array of target (instance) IDs to deregister. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_classic_load_balancer_attributes
**Describe classic load balancer attributes** — Describe the attributes of a classic load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeLoadBalancerAttributes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | clbAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_classic_load_balancers
**List classic load balancers** — Describe the specified classic load balancers. If no load balancers are specified, the call describes all of your load balancers.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeLoadBalancers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | loadBalancerNames | array<string> | no |  |
  | pageSize | number | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | classicLoadBalancers | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_instance_health
**Describe classic load balancer instance health** — Describe the health of instances registered with a classic load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeInstanceHealth`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes |  |
  | instanceIds | array<string> | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceStates | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_load_balancer_attributes
**Describe load balancer attributes** — Describe the attributes of a load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeLoadBalancerAttributes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | loadBalancerARN | string | yes | The Amazon Resource Name (ARN) of the load balancer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | loadBalancerAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_load_balancers
**List load balancers** — Describe the specified Load Balancers.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeLoadBalancers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | loadBalancerARNs | array<string> | no | The Amazon Resource Names (ARN) of the load balancers. |
  | pageSize | number | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | loadBalancers | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_target_group_attributes
**Describe target group attributes** — Describe the attributes of a target group.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeTargetGroupAttributes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | targetGroupAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_target_groups
**List target groups** — Describe the specified target groups. You can specify either their ARNs or their names.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeTargetGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | loadBalancerARN | string | no | The Amazon Resource Name (ARN) of the load balancer. |
  | targetGroupARNs | array<string> | no | The Amazon Resource Names (ARN) of the target groups. |
  | pageSize | number | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | targetGroups | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.describe_target_health
**Describe target health** — Describe the health of specific targets or all targets.
- Stability: stable
- Permissions: `elasticloadbalancing:DescribeTargetHealth`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |
  | targetIds | array<string> | no | An array of target (instance) IDs to describe. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | targetsHealth | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.modify_alb_target_group_attributes
**Modify ALB target group attributes** — Modify attributes of a target group.
- Stability: stable
- Permissions: `elasticloadbalancing:ModifyTargetGroupAttributes`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |
  | albAttributes | object | yes | The target group attributes to modify. For more information see the [`TargetGroupAttribute` type documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupA... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | albAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.modify_classic_load_balancer_attributes
**Modify classic load balancer attributes** — Modify the attributes of a classic load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:ModifyLoadBalancerAttributes`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes |  |
  | accessLog | object | no | Enable the load balancer to capture detailed information of all requests and deliver the information to an Amazon S3 bucket. |
  | idleTimeout | number | no | The time that the connection is allowed to be idle (no data sent over the connection) before it is closed by the load balancer. |
  | crossZoneLoadBalancingEnabled | boolean | no |  |
  | connectionDrainingEnabled | boolean | no |  |
  | connectionDrainingTimeout | number | no | The maximum time to keep existing connections open before deregistering the instances. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | name | string |  |
  | clbAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.modify_nlb_target_group_attributes
**Modify NLB target group attributes** — Modify attributes of a target group.
- Stability: stable
- Permissions: `elasticloadbalancing:ModifyTargetGroupAttributes`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |
  | nlbAttributes | object | yes | Target group attributes to modify. For more information see the [`TargetGroupAttribute` type documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupAttri... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | nlbAttributes | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.register_instances_with_classic_load_balancer
**Register instances with classic load balancer** — Add instances to a classic load balancer.
- Stability: stable
- Permissions: `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes |  |
  | instanceIds | array<string> | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceIds | array<string> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.register_targets
**Register targets** — Register targets with a target group.
- Stability: stable
- Permissions: `elasticloadbalancing:RegisterTargets`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | targetGroupARN | string | yes | The Amazon Resource Name (ARN) of the target group. |
  | targetIds | array<string> | yes | An array of target (instance) IDs to register. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elb.set_blue_green_strategy
**Set blue-green deployment strategy** — Configure a blue-green deployment for the application load balancer using the given strategy. This modifies the default actions of the given listener. When stickiness is enabled, requests routed to a target group remain in the same group for the duration you specify.
- Stability: stable
- Permissions: `elasticloadbalancing:ModifyListener`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | listenerARN | string | yes | The Amazon Resource Name (ARN) of the load balancer listener. |
  | blueTargetARN | string | yes | The Amazon Resource Name (ARN) of the blue target environment. |
  | greenTargetARN | string | yes | The Amazon Resource Name (ARN) of the green target environment. |
  | greenWeight | number | no | The percentage of traffic routed to the green environment. The default value is `0`, meaning that the blue environment carries the full production traffic by default. The blue target weight is impl... |
  | enableStickiness | boolean | no | Enable target group stickiness. Defaults to `False`. For more information see the [`TargetGroupStickinessConfig` type documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIRefer... |
  | stickinessDuration | number | no | The time period during which requests from a client are routed to the same target group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | listener | object |  |
  | amzRequestId | string | The unique identifier for the request. |

