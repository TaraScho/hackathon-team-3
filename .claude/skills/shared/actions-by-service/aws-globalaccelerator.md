# AWS Global Accelerator Actions
Bundle: `com.datadoghq.aws.globalaccelerator` | 2 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eglobalaccelerator)

## com.datadoghq.aws.globalaccelerator.listEndpointGroups
**List endpoint groups** — List the endpoint groups that are associated with a listener.
- Stability: stable
- Permissions: `globalaccelerator:ListEndpointGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | listenerArn | string | yes | The Amazon Resource Name (ARN) of the listener. |
  | maxResults | number | no | The number of endpoint group objects that you want to return with this call. The default value is 10. |
  | nextToken | string | no | The token for the next set of results. You receive this token from a previous call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | EndpointGroups | array<object> | The list of the endpoint groups associated with a listener. |
  | NextToken | string | The token for the next set of results. You receive this token from a previous call. |


## com.datadoghq.aws.globalaccelerator.updateEndpointGroup
**Update endpoint group** — Update an endpoint group. A resource must be valid and active when you add it as an endpoint.
- Stability: stable
- Permissions: `globalaccelerator:UpdateEndpointGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | endpointGroupArn | string | yes | The Amazon Resource Name (ARN) of the endpoint group. |
  | endpointConfigurations | array<object> | no | The list of endpoint objects. A resource must be valid and active when you add it as an endpoint. |
  | trafficDialPercentage | number | no | The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener.  Use this action to increase (dial up) or decrease ... |
  | healthCheckPort | number | no | The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If th... |
  | healthCheckProtocol | string | no | The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP. |
  | healthCheckPath | string | no | If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/). |
  | healthCheckIntervalSeconds | number | no | The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30. |
  | thresholdCount | number | no | The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3. |
  | portOverrides | array<object> | no | Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | EndpointGroup | object | The information about the endpoint group that was updated. |

