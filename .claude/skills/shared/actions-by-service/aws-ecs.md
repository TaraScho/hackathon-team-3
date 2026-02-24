# AWS ECS Actions
Bundle: `com.datadoghq.aws.ecs` | 26 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eecs)

## com.datadoghq.aws.ecs.createCluster
**Create cluster** — Creates a new Amazon ECS cluster. By default, your account receives a default cluster when you launch your first container instance. However, you can create your own cluster with a unique name.  When you call the CreateCluster API operation, Amazon ECS attempts to create the Amazon ECS service-linked role for your account. This is so that it can manage required resources in other Amazon Web Services services on your behalf. However, if the user that makes the call doesn&#x27;t have permissions to create the service-linked role, it isn&#x27;t created. For more information, see Using service-linked roles for Amazon ECS in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:CreateCluster`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusterName | string | no | The name of your cluster. If you don't specify a name for your cluster, you create a cluster that's named default. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are... |
  | tags | any | no | The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. The following basic restrictions apply to tag... |
  | settings | array<object> | no | The setting to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the containerInsights value set w... |
  | configuration | object | no | The execute command configuration for the cluster. |
  | capacityProviders | array<string> | no | The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provi... |
  | defaultCapacityProviderStrategy | array<object> | no | The capacity provider strategy to set as the default for the cluster. After a default capacity provider strategy is set for a cluster, when you call the CreateService or RunTask APIs with no capaci... |
  | serviceConnectDefaults | object | no | Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | cluster | object | The full description of your new cluster. |


## com.datadoghq.aws.ecs.createService
**Create service** — Runs and maintains your desired number of tasks from a specified task definition.
- Stability: stable
- Permissions: `ecs:CreateService`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed. |
  | serviceName | string | yes | The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named... |
  | taskDefinition | string | no | The family and revision (family:revision) or full ARN of the task definition to run in your service. If a revision isn't specified, the latest ACTIVE revision is used. A task definition must be spe... |
  | loadBalancers | array<object> | no | A load balancer object representing the load balancers to use with your service. For more information, see Service load balancing in the Amazon Elastic Container Service Developer Guide. If the ser... |
  | serviceRegistries | array<object> | no | The details of the service discovery registry to associate with this service. For more information, see Service discovery.  Each service may be associated with one service registry. Multiple servic... |
  | desiredCount | number | no | The number of instantiations of the specified task definition to place and keep running in your service. This is required if schedulingStrategy is REPLICA or isn't specified. If schedulingStrategy ... |
  | clientToken | string | no | An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed. |
  | launchType | string | no | The infrastructure that you run your service on. For more information, see Amazon ECS launch types in the Amazon Elastic Container Service Developer Guide. The FARGATE launch type runs your tasks o... |
  | capacityProviderStrategy | array<object> | no | The capacity provider strategy to use for the service. If a capacityProviderStrategy is specified, the launchType parameter must be omitted. If no capacityProviderStrategy or launchType is specifie... |
  | platformVersion | string | no | The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the LATEST platform version... |
  | role | string | no | The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balan... |
  | deploymentConfiguration | object | no | Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks. |
  | placementConstraints | array<object> | no | An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and thos... |
  | placementStrategy | array<object> | no | The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service. |
  | networkConfiguration | object | no | The network configuration for the service. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it isn't supported fo... |
  | healthCheckGracePeriodSeconds | number | no | The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. This is only used when your servi... |
  | schedulingStrategy | string | no | The scheduling strategy to use for the service. For more information, see Services. There are two service scheduler strategies available:    REPLICA-The replica scheduling strategy places and maint... |
  | deploymentController | object | no | The deployment controller to use for the service. If no deployment controller is specified, the default value of ECS is used. |
  | tags | any | no | The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags ... |
  | enableECSManagedTags | boolean | no | Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see Tagging your Amazon ECS resources in the Amazon Elastic Container Service Developer ... |
  | propagateTags | string | no | Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To ... |
  | enableExecuteCommand | boolean | no | Determines whether the execute command functionality is turned on for the service. If true, this enables execute command functionality on all containers in the service tasks. |
  | serviceConnectConfiguration | object | no | The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace. Tasks that run in a namespace can use short name... |
  | volumeConfigurations | array<object> | no | The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | service | object | The full description of your service following the create call. A service will return either a capacityProviderStrategy or launchType parameter, but not both, depending where one was specified when... |


## com.datadoghq.aws.ecs.createTaskSet
**Create task set** — Create a task set in the specified cluster and service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see Amazon ECS deployment types in the Amazon Elastic Container Service Developer Guide.  On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.  For information about the maximum number of task sets and other quotas, see Amazon ECS service quotas in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:CreateTaskSet`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | service | string | yes | The short name or full Amazon Resource Name (ARN) of the service to create the task set in. |
  | cluster | string | yes | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in. |
  | externalId | string | no | An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the ECS_TASK_SET_... |
  | taskDefinition | string | yes | The task definition for the tasks in the task set to use. If a revision isn't specified, the latest ACTIVE revision is used. |
  | networkConfiguration | object | no | An object representing the network configuration for a task set. |
  | loadBalancers | array<object> | no | A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer. |
  | serviceRegistries | array<object> | no | The details of the service discovery registries to assign to this task set. For more information, see Service discovery. |
  | launchType | string | no | The launch type that new tasks in the task set uses. For more information, see Amazon ECS launch types in the Amazon Elastic Container Service Developer Guide. If a launchType is specified, the cap... |
  | capacityProviderStrategy | array<object> | no | The capacity provider strategy to use for the task set. A capacity provider strategy consists of one or more capacity providers along with the base and weight to assign to them. A capacity provider... |
  | platformVersion | string | no | The platform version that the tasks in the task set uses. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the LATEST platform version is used. |
  | scale | object | no | A floating-point percentage of the desired number of tasks to place and keep running in the task set. |
  | clientToken | string | no | An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed. |
  | tags | any | no | The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. When a service is deleted, the tags are dele... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskSet | object | Information about a set of Amazon ECS tasks in either an CodeDeploy or an EXTERNAL deployment. A task set includes details such as the desired number of tasks, how many tasks are running, and wheth... |


## com.datadoghq.aws.ecs.deleteCluster
**Delete cluster** — Deletes the specified cluster. The cluster transitions to the INACTIVE state. Clusters with an INACTIVE status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don&#x27;t recommend that you rely on INACTIVE clusters persisting. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with ListContainerInstances and deregister them with DeregisterContainerInstance.
- Stability: stable
- Permissions: `ecs:DeleteCluster`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | yes | The short name or full Amazon Resource Name (ARN) of the cluster to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | cluster | object | The full description of the deleted cluster. |


## com.datadoghq.aws.ecs.deleteService
**Delete service** — Deletes a specified service within a cluster.
- Stability: stable
- Permissions: `ecs:DeleteService`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed. |
  | service | string | yes | The name of the service to delete. |
  | force | boolean | no | If true, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the REPLICA scheduling strategy. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | service | object | The full description of the deleted service. |


## com.datadoghq.aws.ecs.deleteTaskSet
**Delete task set** — Deletes a specified task set within a service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see Amazon ECS deployment types in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:DeleteTaskSet`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | yes | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete. |
  | service | string | yes | The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete. |
  | taskSet | string | yes | The task set ID or full Amazon Resource Name (ARN) of the task set to delete. |
  | force | boolean | no | If true, you can delete a task set even if it hasn't been scaled down to zero. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskSet | object | Details about the task set. |


## com.datadoghq.aws.ecs.deregisterTaskDefinition
**Deregister task definition** — Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as INACTIVE. Existing tasks and services that reference an INACTIVE task definition continue to run without disruption. Existing services that reference an INACTIVE task definition can still scale up or down by modifying the service&#x27;s desired count. If you want to delete a task definition revision, you must first deregister the task definition revision. You can&#x27;t use an INACTIVE task definition to run new tasks or create new services, and you can&#x27;t update an existing service to reference an INACTIVE task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.  At this time, INACTIVE task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future. We don&#x27;t recommend that you rely on INACTIVE task definitions persisting beyond the lifecycle of any associated tasks and services.  You must deregister a task definition revision before you delete it. For more information, see DeleteTaskDefinitions.
- Stability: stable
- Permissions: `ecs:DeregisterTaskDefinition`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | taskDefinition | string | yes | The family and revision (family:revision) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a revision. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskDefinition | object | The full description of the deregistered task. |


## com.datadoghq.aws.ecs.describeClusters
**Describe clusters** — Describes one or more of your clusters.
- Stability: stable
- Permissions: `ecs:DescribeClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clusters | array<string> | no | A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed. |
  | include | array<string> | no | Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included. If ATTACHMENTS is specified, the attachments for ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clusters | array<object> | The list of clusters. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecs.describeEcsService
**Describe ECS service** — Get the full description of your ECS service.
- Stability: stable
- Permissions: `ecs:DescribeServices`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceName | string | yes | The name of the service to use when filtering the ListTasks results. Specifying a serviceName limits the results to tasks that belong to that service. |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the ListServices results. If you do not specify a cluster, the default cluster is assumed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | service | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.describeEcsTask
**Describe ECS task** — Get the full description of your ECS task.
- Stability: stable
- Permissions: `ecs:DescribeTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | taskID | string | yes | The ID of the task to use when filtering the results. |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the ListTasks results. If you do not specify a cluster, the default cluster is assumed. This parameter is requ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | task | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.describeEcsTasks
**Describe ECS tasks** — Get the full description of your ECS tasks.
- Stability: stable
- Permissions: `ecs:DescribeTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is require... |
  | tasks | array<string> | yes | A list of up to 100 task IDs or full ARN entries. |
  | includeTags | boolean | no | Specifies whether you want to see the resource tags for the task. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | tasks | array<object> |  |
  | failures | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.describeServices
**Describe services** — Describes the specified services running in a specified cluster.
- Stability: stable
- Permissions: `ecs:DescribeServices`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the s... |
  | services | array<string> | yes | A list of services to describe. You may specify up to 10 services to describe in a single operation. |
  | include | array<string> | no | Determines whether you want to see the resource tags for the service. If TAGS is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | services | array<object> | The list of services described. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecs.describeTaskDefinition
**Describe task definition** — Describes a task definition.
- Stability: stable
- Permissions: `ecs:DescribeTaskDefinition`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | taskDefinition | string | yes | The family for the latest ACTIVE revision, family and revision (family:revision) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe. |
  | include | array<string> | no | Determines whether to see the resource tags for the task definition. If TAGS is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskDefinition | object | The full task definition description. |
  | tags | array<object> | The metadata that's applied to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both. The following basic restrictions appl... |


## com.datadoghq.aws.ecs.describeTaskSets
**Describe task sets** — Describes the task sets in the specified cluster and service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see Amazon ECS Deployment Types in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:DescribeTaskSets`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | yes | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in. |
  | service | string | yes | The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in. |
  | taskSets | array<string> | no | The ID or full Amazon Resource Name (ARN) of task sets to describe. |
  | include | array<string> | no | Specifies whether to see the resource tags for the task set. If TAGS is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskSets | array<object> | The list of task sets described. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecs.executeCommand
**Execute command** — Runs a command remotely on a container within a task. If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an AccessDeniedException when there is a mismatch between the condition key value and the corresponding parameter value. For information about required permissions and considerations, see Using Amazon ECS Exec for debugging in the Amazon ECS Developer Guide.
- Stability: stable
- Permissions: `ecs:ExecuteCommand`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed. |
  | container | string | no | The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers. |
  | command | string | yes | The command to run on the container. |
  | interactive | boolean | yes | Use this flag to run your command in interactive mode. |
  | task | string | yes | The Amazon Resource Name (ARN) or ID of the task the container is part of. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clusterArn | string | The Amazon Resource Name (ARN) of the cluster. |
  | containerArn | string | The Amazon Resource Name (ARN) of the container. |
  | containerName | string | The name of the container. |
  | interactive | boolean | Determines whether the execute command session is running in interactive mode. Amazon ECS only supports initiating interactive sessions, so you must specify true for this value. |
  | session | object | The details of the SSM session that was created for this instance of execute-command. |
  | taskArn | string | The Amazon Resource Name (ARN) of the task. |


## com.datadoghq.aws.ecs.listEcsClusters
**List ECS clusters** — List ECS clusters in a particular region.
- Stability: stable
- Permissions: `ecs:ListClusters`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | limit | number | no | Number of items to return. |
  | nextToken | any | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | clusterARNs | array<string> | A list of the full Amazon Resource Name (ARN) entries for each cluster that's associated with your account. |
  | nextToken | any | The nextToken value to include in a future ListClusters request. When the results of a ListClusters request exceed maxResults, this value can be used to retrieve the next page of results. This valu... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.listEcsServices
**List ECS services** — List ECS services in a particular cluster.
- Stability: stable
- Permissions: `ecs:ListServices`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the ListServices results. If you do not specify a cluster, the default cluster is assumed. |
  | limit | number | no | Number of items to return. |
  | nextToken | string | no | The nextToken value returned from a ListServices request indicating that more results are available to fulfill the request and further calls will be needed. If maxResults was provided, it is possib... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | serviceARNs | array<string> | A list of the full Amazon Resource Name (ARN) entries for each service that's associated with your account. |
  | nextToken | string | The nextToken value to include in a future ListServices request. When the results of a ListServices request exceed maxResults, this value can be used to retrieve the next page of results. This valu... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.listEcsTasks
**List ECS tasks** — List ECS tasks for a particular cluster and service.
- Stability: stable
- Permissions: `ecs:ListTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the ListServices results. If you do not specify a cluster, the default cluster is assumed. |
  | serviceName | string | no | The name of the service to use when filtering the ListTasks results. Specifying a serviceName limits the results to tasks that belong to that service. |
  | limit | number | no | Number of items to return. |
  | nextToken | any | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | taskARNs | array<string> | The list of task ARN entries for the tasks that are running on the specified cluster. |
  | nextToken | any | The nextToken value to include in a future ListTasks request. When the results of a ListTasks request exceed maxResults, this value can be used to retrieve the next page of results. This value is n... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.listTaskDefinitions
**List task definitions** — Returns a list of task definitions that are registered to your account. You can filter the results by family name with the familyPrefix parameter or by status with the status parameter.
- Stability: stable
- Permissions: `ecs:ListTaskDefinitions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | familyPrefix | string | no | The full family name to filter the ListTaskDefinitions results with. Specifying a familyPrefix limits the listed task definitions to task definition revisions that belong to that family. |
  | status | string | no | The task definition status to filter the ListTaskDefinitions results with. By default, only ACTIVE task definitions are listed. By setting this parameter to INACTIVE, you can view task definitions ... |
  | sort | string | no | The order to sort the results in. Valid values are ASC and DESC. By default, (ASC) task definitions are listed lexicographically by family name and in ascending numerical order by revision so that ... |
  | nextToken | string | no | The nextToken value returned from a ListTaskDefinitions request indicating that more results are available to fulfill the request and further calls will be needed. If maxResults was provided, it is... |
  | maxResults | number | no | The maximum number of task definition results that ListTaskDefinitions returned in paginated output. When this parameter is used, ListTaskDefinitions only returns maxResults results in a single pag... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskDefinitionArns | array<string> | The list of task definition Amazon Resource Name (ARN) entries for the ListTaskDefinitions request. |
  | nextToken | string | The nextToken value to include in a future ListTaskDefinitions request. When the results of a ListTaskDefinitions request exceed maxResults, this value can be used to retrieve the next page of resu... |


## com.datadoghq.aws.ecs.putAccountSetting
**Put account setting** — Modifies an account setting. Account settings are set on a per-Region basis. If you change the root user account setting, the default settings are reset for users and roles that do not have specified individual account settings. For more information, see Account Settings in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:PutAccountSetting`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The Amazon ECS account setting name to modify. The following are the valid values for the account setting name.    serviceLongArnFormat - When modified, the Amazon Resource Name (ARN) and resource ... |
  | value | string | yes | The account setting value for the specified principal ARN. Accepted values are enabled, disabled, on, and off. When you specify fargateTaskRetirementWaitPeriod for the name, the following are the v... |
  | principalArn | string | no | The ARN of the principal, which can be a user, role, or the root user. If you specify the root user, it modifies the account setting for all users, roles, and the root user of the account unless a ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | setting | object | The current account setting for a resource. |


## com.datadoghq.aws.ecs.putAccountSettingDefault
**Put account setting default** — Modifies an account setting for all users on an account for whom no individual account setting has been specified. Account settings are set on a per-Region basis.
- Stability: stable
- Permissions: `ecs:PutAccountSettingDefault`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The resource name for which to modify the account setting. The following are the valid values for the account setting name.    serviceLongArnFormat - When modified, the Amazon Resource Name (ARN) a... |
  | value | string | yes | The account setting value for the specified principal ARN. Accepted values are enabled, disabled, on, and off. When you specify fargateTaskRetirementWaitPeriod for the name, the following are the v... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | setting | object | The current setting for a resource. |


## com.datadoghq.aws.ecs.registerTaskDefinition
**Register task definition** — Registers a new task definition with a specified family and container definitions.
- Stability: stable
- Permissions: `ecs:RegisterTaskDefinition`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | family | string | yes | You must specify a family for a task definition. You can use it track multiple versions of the same task definition. The family is used as a name for your task definition. Up to 255 letters (upperc... |
  | taskRoleArn | any | no | The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. F... |
  | executionRoleArn | any | no | The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the requir... |
  | networkMode | any | no | The Docker networking mode to use for the containers in the task. The valid values are none, bridge, awsvpc, and host. If no network mode is specified, the default is bridge. For Amazon ECS tasks o... |
  | containerDefinitions | array<object> | yes | A list of container definitions in JSON format that describe the different containers that make up your task. |
  | volumes | any | no | A list of volume definitions in JSON format that containers in your task might use. |
  | placementConstraints | any | no | An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified a... |
  | requiresCompatibilities | any | no | The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value... |
  | cpu | any | no | The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, 1024) or as a string using vCPUs (for example, 1 vCPU or 1 vcpu) in a task definition. Stri... |
  | memory | any | no | The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,1024) or as a string using GB (for example, 1GB or 1 GB) in a task definition. String value... |
  | tags | any | no | The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them. The following basic restricti... |
  | pidMode | any | no | The process namespace to use for the containers in the task. The valid values are host or task. On Fargate for Linux containers, the only valid value is task. For example, monitoring sidecars might... |
  | ipcMode | any | no | The IPC resource namespace to use for the containers in the task. The valid values are host, task, or none. If host is specified, then all containers within the tasks that specified the host IPC mo... |
  | proxyConfiguration | any | no | The configuration details for the App Mesh proxy. For tasks hosted on Amazon EC2 instances, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.... |
  | inferenceAccelerators | any | no | The Elastic Inference accelerators to use for the containers in the task. |
  | ephemeralStorage | any | no | The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. F... |
  | runtimePlatform | any | no | The operating system that your tasks definitions run on. A platform family is specified only for tasks using the Fargate launch type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | taskDefinition | object | The full description of the registered task definition. |
  | tags | array<object> | The list of tags associated with the task definition. |


## com.datadoghq.aws.ecs.runTask
**Run task** — Starts a new task using the specified task definition.  On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.  You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide. Alternatively, you can use StartTask to use your own scheduler or place tasks manually on specific container instances. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.  You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more infomation, see Amazon EBS volumes in the Amazon Elastic Container Service Developer Guide. The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command. To manage eventual consistency, you can do the following:   Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.   Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.
- Stability: stable
- Permissions: `ecs:RunTask`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | capacityProviderStrategy | array<object> | no | The capacity provider strategy to use for the task. If a capacityProviderStrategy is specified, the launchType parameter must be omitted. If no capacityProviderStrategy or launchType is specified, ... |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed. |
  | count | number | no | The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call. |
  | enableECSManagedTags | boolean | no | Specifies whether to use Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide. |
  | enableExecuteCommand | boolean | no | Determines whether to use the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. If true, then the tas... |
  | group | string | no | The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name). |
  | launchType | string | no | The infrastructure to run your standalone task on. For more information, see Amazon ECS launch types in the Amazon Elastic Container Service Developer Guide. The FARGATE launch type runs your tasks... |
  | networkConfiguration | object | no | The network configuration for the task. This parameter is required for task definitions that use the awsvpc network mode to receive their own elastic network interface, and it isn't supported for o... |
  | overrides | object | no | A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a co... |
  | placementConstraints | array<object> | no | An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime). |
  | placementStrategy | array<object> | no | The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task. |
  | platformVersion | string | no | The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the LATEST platform version is used. For more information, see Fargate ... |
  | propagateTags | string | no | Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To ... |
  | referenceId | string | no | The reference ID to use for the task. The reference ID can have a maximum length of 1024 characters. |
  | startedBy | string | no | An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the... |
  | tags | any | no | The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply ... |
  | taskDefinition | string | yes | The family and revision (family:revision) or full ARN of the task definition to run. If a revision isn't specified, the latest ACTIVE revision is used. The full ARN value must match the value that ... |
  | clientToken | string | no | An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range o... |
  | volumeConfigurations | array<object> | no | The details of the volume that was configuredAtLaunch. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in in TaskManagedEBSVolumeConfiguration. The name of the vol... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tasks | array<object> | A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here. |
  | failures | array<object> | Any failures associated with the call. For information about how to address failures, see Service event messages and API failure reasons in the Amazon Elastic Container Service Developer Guide. |


## com.datadoghq.aws.ecs.startTask
**Start task** — Starts a new task from the specified task definition on the specified container instance or instances.  On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.  Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.  Alternatively, you can useRunTask to place tasks for you. For more information, see Scheduling Tasks in the Amazon Elastic Container Service Developer Guide. You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more infomation, see Amazon EBS volumes in the Amazon Elastic Container Service Developer Guide.
- Stability: stable
- Permissions: `ecs:StartTask`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed. |
  | containerInstances | array<string> | yes | The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances. |
  | enableECSManagedTags | boolean | no | Specifies whether to use Amazon ECS managed tags for the task. For more information, see Tagging Your Amazon ECS Resources in the Amazon Elastic Container Service Developer Guide. |
  | enableExecuteCommand | boolean | no | Whether or not the execute command functionality is turned on for the task. If true, this turns on the execute command functionality on all containers in the task. |
  | group | string | no | The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name). |
  | networkConfiguration | object | no | The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the awsvpc networking mode. |
  | overrides | object | no | A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a containe... |
  | propagateTags | string | no | Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated. |
  | referenceId | string | no | The reference ID to use for the task. |
  | startedBy | string | no | An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the... |
  | tags | any | no | The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply ... |
  | taskDefinition | string | yes | The family and revision (family:revision) or full ARN of the task definition to start. If a revision isn't specified, the latest ACTIVE revision is used. |
  | volumeConfigurations | array<object> | no | The details of the volume that was configuredAtLaunch. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in TaskManagedEBSVolumeConfiguration. The name of the volume... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tasks | array<object> | A full description of the tasks that were started. Each task that was successfully placed on your container instances is described. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecs.stopEcsTask
**Stop ECS task** — Stop an ECS task.
- Stability: stable
- Permissions: `ecs:StopTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | taskId | string | yes |  |
  | cluster | string | no | The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the task... |
  | reason | string | no | An optional message specified when a task is stopped. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | task | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecs.updateEcsService
**Update ECS service** — Update an Amazon ECS service.
- Stability: stable
- Permissions: `ecs:UpdateService`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | serviceName | string | yes | The name of the service to update. |
  | desiredCount | ['number', 'null'] | no | The number of instantiations of the task to place and keep running in your service. |
  | cluster | ['string', 'null'] | no | The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed. |
  | taskDefinition | ['string', 'null'] | no | The family and revision (family:revision) or full ARN of the task definition to run in your service. If a revision is not specified, the latest ACTIVE revision is used. If you modify the task defin... |
  | capacityProviderStrategy | any | no | The capacity provider strategy to update the service to use. |
  | deploymentConfiguration | any | no | Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks. |
  | networkConfiguration | any | no | An object representing the network configuration for the service. |
  | placementConstraints | any | no | An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. |
  | placementStrategy | any | no | The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. |
  | platformVersion | ['string', 'null'] | no | The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the LATEST platform... |
  | forceNewDeployment | ['boolean', 'null'] | no | Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. |
  | healthCheckGracePeriodSeconds | ['number', 'null'] | no | The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your servic... |
  | enableExecuteCommand | ['boolean', 'null'] | no | If true, this enables execute command functionality on all task containers. |
  | enableECSManagedTags | ['boolean', 'null'] | no | Determines whether to turn on Amazon ECS managed tags for the tasks in the service. |
  | loadBalancers | any | no | A list of Elastic Load Balancing load balancer objects. |
  | propagateTags | any | no | Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated. |
  | serviceRegistries | any | no | The details for the service discovery registries to assign to this service. |
  | serviceConnectConfiguration | any | no | The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace. |
  | volumeConfigurations | any | no | The details of the volume that was configured at launch. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | service | object |  |
  | amzRequestId | string | The unique identifier for the request. |

