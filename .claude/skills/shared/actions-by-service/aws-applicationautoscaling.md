# AWS Application Auto Scaling Actions
Bundle: `com.datadoghq.aws.applicationautoscaling` | 3 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eapplicationautoscaling)

## com.datadoghq.aws.applicationautoscaling.deleteScheduledAction
**Delete scheduled actions** — Deletes the specified scheduled action for an Application Auto Scaling scalable target. For more information, see Delete a scheduled action in the Application Auto Scaling User Guide.
- Stability: stable
- Permissions: `application-autoscaling:DeleteScheduledAction`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceNamespace | string | yes | The namespace of the AWS service that provides the resource. |
  | scheduledActionName | string | yes | The name of the scheduled action. |
  | resourceId | string | yes | The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier. See [documentation](https://docs.aws.amazon.com/autoscaling/app... |
  | scalableDimension | string | yes | The scalable dimension. This string consists of the service namespace, resource type, and scaling property. See [documentation](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.applicationautoscaling.describeScalableTargets
**Describe scalable targets** — Gets information about the scalable targets in the specified namespace.
- Stability: stable
- Permissions: `application-autoscaling:DescribeScalableTargets`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceNamespace | string | yes | The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead. |
  | resourceIds | array<string> | no | The identifiers of the resources associated with the scalable target. This string consists of the resource type and unique identifier. See [documentation](https://docs.aws.amazon.com/autoscaling/ap... |
  | scalableDimension | string | no | The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property. See [documentation](https://docs.aws.amazon.com/autos... |
  | maxResults | number | no | The maximum number of scalable targets. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | scalableTargets | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.applicationautoscaling.describeScheduledActions
**Describe scheduled actions** — Describes the Application Auto Scaling scheduled actions for the specified service namespace.
- Stability: stable
- Permissions: `application-autoscaling:DescribeScheduledActions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | scheduledActionNames | array<string> | no | The names of the scheduled actions to describe. |
  | serviceNamespace | string | yes | The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead. |
  | resourceId | string | no | The identifier of the resource associated with the scheduled action. This string consists of the resource type and unique identifier. See [documentation](https://docs.aws.amazon.com/autoscaling/app... |
  | scalableDimension | string | no | The scalable dimension. This string consists of the service namespace, resource type, and scaling property. See [documentation](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_... |
  | maxResults | number | no | The maximum number of scheduled action results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | scheduledActions | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |

