# AWS EKS Actions
Bundle: `com.datadoghq.aws.eks` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eeks)

## com.datadoghq.aws.eks.deleteCluster
**Delete cluster** — Delete the Amazon EKS cluster control plane. If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first.
- Stability: stable
- Permissions: `eks:DeleteCluster`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the cluster to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | cluster | object | The full description of the cluster to delete. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.describeCluster
**Describe cluster** — Get details about a cluster.
- Stability: stable
- Permissions: `eks:DescribeCluster`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the cluster to describe. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | cluster | object | The full description of your specified cluster. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.describeNodegroup
**Describe node group** — Get details about a node group.
- Stability: stable
- Permissions: `eks:DescribeNodegroup`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the Amazon EKS cluster associated with the node group. |
  | nodegroupName | string | yes | The name of the node group to describe. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | nodegroup | object | The full description of your node group. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.describeUpdate
**Describe update** — Return information about an update of your Amazon EKS cluster, associated managed node group, or Amazon EKS add-on.
- Stability: stable
- Permissions: `eks:DescribeUpdate`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the Amazon EKS cluster associated with the update. |
  | updateId | string | yes | The ID of the update to describe. |
  | nodegroupName | string | no | The name of the Amazon EKS node group associated with the update. This parameter is required if the update is a node group update. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | update | object | The full description of the specified update. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.listClusters
**List clusters** — List clusters.
- Stability: stable
- Permissions: `eks:ListClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | clusters | array<string> | A list of all of the clusters for your account in the specified Amazon Web Services Region. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.listNodegroups
**List node groups** — List node groups.
- Stability: stable
- Permissions: `eks:ListNodegroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the Amazon EKS cluster from which to list node groups. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | nodegroups | array<string> | A list of all of the node groups associated with the specified cluster. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.listTagsForResource
**List tags for resource** — List the tags for an Amazon EKS resource.
- Stability: stable
- Permissions: `eks:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) that identifies the resource for which to list tags. Amazon EKS clusters and managed node groups are supported. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tags | object | The tags for the resource. |
  | tagValue | object |  |
  | tagValueList | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.listUpdates
**List updates** — List the updates associated with an Amazon EKS cluster or managed node group.
- Stability: stable
- Permissions: `eks:ListUpdates`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the cluster for which to list updates. |
  | nodegroupName | string | no | The name of the Amazon EKS managed node group for which to list updates. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | updateIds | array<string> | A list of all the updates for the specified cluster and Region. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.eks.tagResource
**Tag resource** — Associate tags to a resource with a given `resourceArn`. Existing tags not specified in the request parameters remain unchanged. When a resource is deleted, the tags associated with that resource are also deleted.
- Stability: stable
- Permissions: `eks:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource to which to add tags. Amazon EKS clusters and managed node groups are supported. |
  | tags | any | yes | The tags to add to the resource. |


## com.datadoghq.aws.eks.untagResource
**Untag resource** — Delete tags from a resource.
- Stability: stable
- Permissions: `eks:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource from which to delete tags. Amazon EKS clusters and managed node groups are supported. |
  | tagKeys | array<string> | yes | The keys of the tags to remove. |


## com.datadoghq.aws.eks.updateNodegroupConfig
**Update node group configuration** — Update an Amazon EKS managed node group configuration. Node groups continue to function during the update.
- Stability: stable
- Permissions: `eks:UpdateNodegroupConfig`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | yes | The name of the Amazon EKS cluster that contains the managed node group. |
  | nodegroupName | string | yes | The name of the managed node group to update. |
  | labels | object | no | The Kubernetes labels to be applied to the nodes in the node group after the update. |
  | taints | object | no | The Kubernetes taints to be applied to the nodes in the node group after the update. |
  | scalingConfig | object | no | The scaling configuration details for the Auto Scaling group after the update. |
  | updateConfig | object | no | The node group update configuration. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | update | object |  |
  | amzRequestId | string | The unique identifier for the request. |

