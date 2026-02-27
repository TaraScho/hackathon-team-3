# AWS CloudControl Actions
Bundle: `com.datadoghq.aws.cloudcontrol` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecloudcontrol)

## com.datadoghq.aws.cloudcontrol.cancelResourceRequest
**Cancel resource request** — Cancels the specified resource operation request. For more information, see Canceling resource operation requests in the Amazon Web Services Cloud Control API User Guide. Only resource operations requests with a status of PENDING or IN_PROGRESS can be canceled.
- Stability: stable
- Permissions: `cloudcontrol:CancelResourceRequest`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | requestToken | string | yes | The RequestToken of the ProgressEvent object returned by the resource operation request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProgressEvent | object |  |


## com.datadoghq.aws.cloudcontrol.createResource
**Create resource** — Creates the specified resource. For more information, see Creating a resource in the Amazon Web Services Cloud Control API User Guide. After you have initiated a resource creation request, you can monitor the progress of your request by calling GetResourceRequestStatus using the RequestToken of the ProgressEvent type returned by CreateResource.
- Stability: stable
- Permissions: `cloudcontrol:CreateResource`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the resource type. |
  | typeVersionId | string | no | For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version. |
  | roleArn | string | no | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions re... |
  | clientToken | string | no | A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately dis... |
  | desiredState | string | yes | Structured data format representing the desired state of the resource, consisting of that resource's properties and their desired values.  Cloud Control API currently supports JSON as a structured ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProgressEvent | object | Represents the current status of the resource creation request. After you have initiated a resource creation request, you can monitor the progress of your request by calling GetResourceRequestStatu... |


## com.datadoghq.aws.cloudcontrol.deleteResource
**Delete resource** — Deletes the specified resource. For details, see Deleting a resource in the Amazon Web Services Cloud Control API User Guide. After you have initiated a resource deletion request, you can monitor the progress of your request by calling GetResourceRequestStatus using the RequestToken of the ProgressEvent returned by DeleteResource.
- Stability: stable
- Permissions: `cloudcontrol:DeleteResource`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the resource type. |
  | typeVersionId | string | no | For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version. |
  | roleArn | string | no | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions re... |
  | clientToken | string | no | A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately dis... |
  | identifier | string | yes | The identifier for the resource. You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Prima... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProgressEvent | object | Represents the current status of the resource deletion request. After you have initiated a resource deletion request, you can monitor the progress of your request by calling GetResourceRequestStatu... |


## com.datadoghq.aws.cloudcontrol.getResource
**Get resource** — Returns information about the current state of the specified resource. For details, see Reading a resource&#x27;s current state. You can use this action to return information about an existing resource in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.
- Stability: stable
- Permissions: `cloudcontrol:GetResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the resource type. |
  | typeVersionId | string | no | For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version. |
  | roleArn | string | no | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions re... |
  | identifier | string | yes | The identifier for the resource. You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Prima... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TypeName | string | The name of the resource type. |
  | ResourceDescription | object |  |


## com.datadoghq.aws.cloudcontrol.getResourceRequestStatus
**Get resource request status** — Returns the current status of a resource operation request. For more information, see Tracking the progress of resource operation requests in the Amazon Web Services Cloud Control API User Guide.
- Stability: stable
- Permissions: `cloudcontrol:GetResourceRequestStatus`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | requestToken | string | yes | A unique token used to track the progress of the resource operation request. Request tokens are included in the ProgressEvent type returned by a resource operation request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProgressEvent | object | Represents the current status of the resource operation request. |


## com.datadoghq.aws.cloudcontrol.listResourceRequests
**List resource requests** — Returns existing resource operation requests. This includes requests of all status types. For more information, see Listing active resource operation requests in the Amazon Web Services Cloud Control API User Guide.  Resource operation requests expire after 7 days.
- Stability: stable
- Permissions: `cloudcontrol:ListResourceRequests`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a NextToken value that you can assign to the NextToke... |
  | nextToken | string | no | If the previous paginated request didn't return all of the remaining results, the response object's NextToken parameter value is set to a token. To retrieve the next set of results, call this actio... |
  | resourceRequestStatusFilter | object | no | The filter criteria to apply to the requests returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ResourceRequestStatusSummaries | array<object> | The requests that match the specified filter criteria. |
  | NextToken | string | If the request doesn't return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call ListResources again and assign that token to the request object's ... |


## com.datadoghq.aws.cloudcontrol.listResources
**List resources** — Returns information about the specified resources. For more information, see Discovering resources in the Amazon Web Services Cloud Control API User Guide. You can use this action to return information about existing resources in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.
- Stability: stable
- Permissions: `cloudcontrol:ListResources`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the resource type. |
  | typeVersionId | string | no | For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version. |
  | roleArn | string | no | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions re... |
  | nextToken | string | no | If the previous paginated request didn't return all of the remaining results, the response object's NextToken parameter value is set to a token. To retrieve the next set of results, call this actio... |
  | maxResults | number | no | Reserved. |
  | resourceModel | string | no | The resource model to use to select the resources to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TypeName | string | The name of the resource type. |
  | ResourceDescriptions | array<object> | Information about the specified resources, including primary identifier and resource model. |
  | NextToken | string | If the request doesn't return all of the remaining results, NextToken is set to a token. To retrieve the next set of results, call ListResources again and assign that token to the request object's ... |


## com.datadoghq.aws.cloudcontrol.updateResource
**Update resource** — Updates the specified property values in the resource. You specify your resource property updates as a list of patch operations contained in a JSON patch document that adheres to the  RFC 6902 - JavaScript Object Notation (JSON) Patch  standard. For details on how Cloud Control API performs resource update operations, see Updating a resource in the Amazon Web Services Cloud Control API User Guide. After you have initiated a resource update request, you can monitor the progress of your request by calling GetResourceRequestStatus using the RequestToken of the ProgressEvent returned by UpdateResource. For more information about the properties of a specific resource, refer to the related topic for the resource in the Resource and property types reference in the CloudFormation Users Guide.
- Stability: stable
- Permissions: `cloudcontrol:UpdateResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | typeName | string | yes | The name of the resource type. |
  | typeVersionId | string | no | For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version. |
  | roleArn | string | no | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions re... |
  | clientToken | string | no | A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately dis... |
  | identifier | string | yes | The identifier for the resource. You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Prima... |
  | patchDocument | string | yes | A JavaScript Object Notation (JSON) document listing the patch operations that represent the updates to apply to the current resource properties. For details, see Composing the patch document in th... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ProgressEvent | object | Represents the current status of the resource update request. Use the RequestToken of the ProgressEvent with GetResourceRequestStatus to return the current status of a resource operation request. |

