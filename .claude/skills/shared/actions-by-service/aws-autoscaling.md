# AWS Autoscaling Actions
Bundle: `com.datadoghq.aws.autoscaling` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eautoscaling)

## com.datadoghq.aws.autoscaling.attachInstance
**Attach instance** — Attach one or more EC2 instances to the specified Auto Scaling group.
- Stability: stable
- Permissions: `autoscaling:AttachInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | instanceId | string | yes | The ID of the instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.deleteScheduledAction
**Delete scheduled action** — Deletes the specified scheduled action.
- Stability: stable
- Permissions: `autoscaling:DeleteScheduledAction`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | scheduledActionName | string | yes | The name of the action to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.describeInstanceRefreshes
**Describe instance refresh** — Get information about the instance refreshes for the specified auto scaling group.
- Stability: stable
- Permissions: `autoscaling:DescribeInstanceRefreshes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | instanceRefreshId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceRefresh | object |  |


## com.datadoghq.aws.autoscaling.describeScalingActivity
**Describe activity** — Get information about the scaling activity in the account and region.
- Stability: stable
- Permissions: `autoscaling:DescribeScalingActivities`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | activityId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | activityId | string |  |
  | statusCode | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.describeScheduledActions
**Describe scheduled actions** — Gets information about the scheduled actions that haven't run or that have not reached their end time.
- Stability: stable
- Permissions: `autoscaling:DescribeScheduledActions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | no | The name of the Auto Scaling group. |
  | scheduledActionNames | array<string> | no | The names of one or more scheduled actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error. |
  | startTime | string | no | The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored. |
  | endTime | string | no | The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored. |
  | maxRecords | number | no | The maximum number of items to return with this call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | scheduledUpdateGroupActions | array<object> | The scheduled actions. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.describe_auto_scaling_group
**Describe auto scaling group** — Get information about the auto scaling groups in an account and region.
- Stability: stable
- Permissions: `autoscaling:DescribeAutoScalingGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | autoScalingGroup | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.describe_auto_scaling_instance
**Describe auto scaling instance** — Get information about the auto scaling instances in an account and region.
- Stability: stable
- Permissions: `autoscaling:DescribeAutoScalingInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes | The ID of the instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | isInAutoScalingGroup | boolean |  |
  | autoScalingInstance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.detachInstance
**Detach instance** — Remove one or more instances from the specified auto scaling group.
- Stability: stable
- Permissions: `autoscaling:DetachInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | instanceId | string | yes | The ID of the instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | activityId | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.execute_policy
**Execute policy** — Execute the specified policy. This can be useful for testing the design of your scaling policy.
- Stability: stable
- Permissions: `autoscaling:ExecutePolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | policyName | string | yes | The name or ARN of the policy. |
  | autoScalingGroupName | string | no | The name of the Auto Scaling group. |
  | breachThreshold | number | no | The breach threshold for the alarm. |
  | honorCooldown | boolean | no | Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy. Valid only if the policy type is `SimpleScaling`. |
  | metricValue | number | no | The metric value to compare to `BreachThreshold`. This enables you to execute a policy of type `StepScaling` and determine which step adjustment to use. For example, if the breach threshold is 50 a... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.setDesiredCapacity
**Set desired capacity** — Set the size of the specified Auto Scaling group.
- Stability: stable
- Permissions: `autoscaling:SetDesiredCapacity`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | desiredCapacity | number | yes |  |
  | honorCooldown | boolean | no | Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 A... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.autoscaling.startInstanceRefresh
**Start instance refresh** — Start a new instance refresh operation. An instance refresh performs a rolling replacement of all or some instances in an auto scaling group. Each instance is terminated first and then replaced, which temporarily reduces the capacity available within your auto scaling group.
- Stability: stable
- Permissions: `autoscaling:StartInstanceRefresh`
- Access: update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | autoScalingGroupName | string | yes | The name of the Auto Scaling group. |
  | desiredConfiguration | object | no | The desired configuration. For example, the desired configuration can specify a new launch template or a new version of the current launch template. Once the instance refresh succeeds, Amazon EC2 a... |
  | preferences | object | no | Set of preferences associated with the instance refresh request. If not provided, the default values are used. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceRefreshId | string | A unique ID for tracking the progress of the instance refresh. |
  | amzRequestId | string | The unique identifier for the request. |

