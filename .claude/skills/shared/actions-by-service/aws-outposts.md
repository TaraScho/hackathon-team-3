# AWS Outposts Actions
Bundle: `com.datadoghq.aws.outposts` | 34 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eoutposts)

## com.datadoghq.aws.outposts.cancelCapacityTask
**Cancel capacity task** — Cancels the capacity task.
- Stability: stable
- Permissions: `outposts:CancelCapacityTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | capacityTaskId | string | yes | ID of the capacity task that you want to cancel. |
  | outpostIdentifier | string | yes | ID or ARN of the Outpost associated with the capacity task that you want to cancel. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.cancelOrder
**Cancel order** — Cancels the specified order for an Outpost.
- Stability: stable
- Permissions: `outposts:CancelOrder`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | orderId | string | yes | The ID of the order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.createOrder
**Create order** — Creates an order for an Outpost.
- Stability: stable
- Permissions: `outposts:CreateOrder`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID or the Amazon Resource Name (ARN) of the Outpost. |
  | lineItems | array<object> | yes | The line items that make up the order. |
  | paymentOption | string | yes | The payment option. |
  | paymentTerm | string | no | The payment terms. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Order | object | Information about this order. |


## com.datadoghq.aws.outposts.createOutpost
**Create outpost** — Creates an Outpost. You can specify either an Availability zone or an AZ ID.
- Stability: stable
- Permissions: `outposts:CreateOutpost`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the Outpost. |
  | description | string | no | The description of the Outpost. |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |
  | availabilityZone | string | no | The Availability Zone. |
  | availabilityZoneId | string | no | The ID of the Availability Zone. |
  | tags | any | no | The tags to apply to the Outpost. |
  | supportedHardwareType | string | no | The type of hardware for this Outpost. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Outpost | object | Information about an Outpost. |


## com.datadoghq.aws.outposts.createSite
**Create site** — Creates a site for an Outpost.
- Stability: stable
- Permissions: `outposts:CreateSite`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the site. |
  | description | string | no | The description of the site. |
  | notes | string | no | Additional information that you provide about site access requirements, electrician scheduling, personal protective equipment, or regulation of equipment materials that could affect your installati... |
  | tags | any | no | The tags to apply to a site. |
  | operatingAddress | object | no | The location to install and power on the hardware. This address might be different from the shipping address. |
  | shippingAddress | object | no | The location to ship the hardware. This address might be different from the operating address. |
  | rackPhysicalProperties | object | no | Information about the physical and logistical details for the rack at this site. For more information about hardware requirements for racks, see Network readiness checklist in the Amazon Web Servic... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Site | object | Information about a site. |


## com.datadoghq.aws.outposts.deleteOutpost
**Delete outpost** — Deletes the specified Outpost.
- Stability: stable
- Permissions: `outposts:DeleteOutpost`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostId | string | yes | The ID or ARN of the Outpost. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.deleteSite
**Delete site** — Deletes the specified site.
- Stability: stable
- Permissions: `outposts:DeleteSite`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.getCapacityTask
**Get capacity task** — Gets details of the specified capacity task.
- Stability: stable
- Permissions: `outposts:GetCapacityTask`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | capacityTaskId | string | yes | ID of the capacity task. |
  | outpostIdentifier | string | yes | ID or ARN of the Outpost associated with the specified capacity task. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CapacityTaskId | string | ID of the capacity task. |
  | OutpostId | string | ID of the Outpost associated with the specified capacity task. |
  | OrderId | string | ID of the Amazon Web Services Outposts order associated with the specified capacity task. |
  | AssetId | string | The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts       rack or an Outposts server configuration. |
  | RequestedInstancePools | array<object> | List of instance pools requested in the capacity task. |
  | InstancesToExclude | object | Instances that the user specified they cannot stop in order to free up the capacity needed       to run the capacity task. |
  | DryRun | boolean | Performs a dry run to determine if you are above or below instance capacity. |
  | CapacityTaskStatus | string | Status of the capacity task.          A capacity task can have one of the following statuses:                                                          REQUESTED - The capacity task was created and ... |
  | Failed | object | Reason why the capacity task failed. |
  | CreationDate | string | The date the capacity task was created. |
  | CompletionDate | string | The date the capacity task ran successfully. |
  | LastModifiedDate | string | The date the capacity task was last modified. |
  | TaskActionOnBlockingInstances | string | User-specified option in case an instance is blocking the capacity task from running.       Shows one of the following options:                                                          WAIT_FOR_EVA... |


## com.datadoghq.aws.outposts.getCatalogItem
**Get catalog item** — Gets information about the specified catalog item.
- Stability: stable
- Permissions: `outposts:GetCatalogItem`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogItemId | string | yes | The ID of the catalog item. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CatalogItem | object | Information about this catalog item. |


## com.datadoghq.aws.outposts.getConnection
**Get connection** — Amazon Web Services uses this action to install Outpost servers. Gets information about the specified connection. Use CloudTrail to monitor this action or Amazon Web Services managed policy for Amazon Web Services Outposts to secure it. For more information, see Amazon Web Services managed policies for Amazon Web Services Outposts and Logging Amazon Web Services Outposts API calls with Amazon Web Services CloudTrail in the Amazon Web Services Outposts User Guide.
- Stability: stable
- Permissions: `outposts:GetConnection`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | connectionId | string | yes | The ID of the connection. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ConnectionId | string | The ID of the connection. |
  | ConnectionDetails | object | Information about the connection. |


## com.datadoghq.aws.outposts.getOrder
**Get order** — Gets information about the specified order.
- Stability: stable
- Permissions: `outposts:GetOrder`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | orderId | string | yes | The ID of the order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Order | object | Information about an order. |


## com.datadoghq.aws.outposts.getOutpost
**Get outpost** — Gets information about the specified Outpost.
- Stability: stable
- Permissions: `outposts:GetOutpost`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostId | string | yes | The ID or ARN of the Outpost. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Outpost | object | Information about an Outpost. |


## com.datadoghq.aws.outposts.getOutpostBillingInformation
**Get outpost billing information** — Gets current and historical billing information about the specified Outpost.
- Stability: stable
- Permissions: `outposts:GetOutpostBillingInformation`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |
  | outpostIdentifier | string | yes | The ID or ARN of the Outpost. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | NextToken | string | The pagination token. |
  | Subscriptions | array<object> | The subscription details for the specified Outpost. |
  | ContractEndDate | string | The date the current contract term ends for the specified Outpost. You must start the renewal or       decommission process at least 5 business days before the current term for your       Amazon We... |


## com.datadoghq.aws.outposts.getOutpostInstanceTypes
**Get outpost instance types** — Gets the instance types for the specified Outpost.
- Stability: stable
- Permissions: `outposts:GetOutpostInstanceTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostId | string | yes | The ID or ARN of the Outpost. |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | InstanceTypes | array<object> | Information about the instance types. |
  | NextToken | string | The pagination token. |
  | OutpostId | string | The ID of the Outpost. |
  | OutpostArn | string | The Amazon Resource Name (ARN) of the Outpost. |


## com.datadoghq.aws.outposts.getOutpostSupportedInstanceTypes
**Get outpost supported instance types** — Gets the instance types that an Outpost can support in InstanceTypeCapacity. This will generally include instance types that are not currently configured and therefore cannot be launched with the current Outpost capacity configuration.
- Stability: stable
- Permissions: `outposts:GetOutpostSupportedInstanceTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID or ARN of the Outpost. |
  | orderId | string | no | The ID for the Amazon Web Services Outposts order. |
  | assetId | string | no | The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration. |
  | maxResults | number | no | The maximum page size. |
  | nextToken | string | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | InstanceTypes | array<object> | Information about the instance types. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.getSite
**Get site** — Gets information about the specified Outpost site.
- Stability: stable
- Permissions: `outposts:GetSite`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Site | object | Information about a site. |


## com.datadoghq.aws.outposts.getSiteAddress
**Get site address** — Gets the site address of the specified site.
- Stability: stable
- Permissions: `outposts:GetSiteAddress`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |
  | addressType | string | yes | The type of the address you request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SiteId | string | The ID of the site. |
  | AddressType | string | The type of the address you receive. |
  | Address | object | Information about the address. |


## com.datadoghq.aws.outposts.listAssetInstances
**List asset instances** — A list of Amazon EC2 instances, belonging to all accounts, running on the specified Outpost. Does not include Amazon EBS or Amazon S3 instances.
- Stability: stable
- Permissions: `outposts:ListAssetInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID of the Outpost. |
  | assetIdFilter | array<string> | no | Filters the results by asset ID. |
  | instanceTypeFilter | array<string> | no | Filters the results by instance ID. |
  | accountIdFilter | array<string> | no | Filters the results by account ID. |
  | awsServiceFilter | array<string> | no | Filters the results by Amazon Web Services service. |
  | maxResults | number | no | The maximum page size. |
  | nextToken | string | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | AssetInstances | array<object> | List of instances owned by all accounts on the Outpost. Does not include Amazon EBS or Amazon S3       instances. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listAssets
**List assets** — Lists the hardware assets for the specified Outpost. Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.
- Stability: stable
- Permissions: `outposts:ListAssets`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID or the Amazon Resource Name (ARN) of the Outpost. |
  | hostIdFilter | array<string> | no | Filters the results by the host ID of a Dedicated Host. |
  | maxResults | number | no | The maximum page size. |
  | nextToken | string | no | The pagination token. |
  | statusFilter | array<string> | no | Filters the results by state. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Assets | array<object> | Information about the hardware assets. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listBlockingInstancesForCapacityTask
**List blocking instances for capacity task** — A list of Amazon EC2 instances running on the Outpost and belonging to the account that initiated the capacity task. Use this list to specify the instances you cannot stop to free up capacity to run the capacity task.
- Stability: stable
- Permissions: `outposts:ListBlockingInstancesForCapacityTask`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID or ARN of the Outpost associated with the specified capacity task. |
  | capacityTaskId | string | yes | The ID of the capacity task. |
  | maxResults | number | no | The maximum page size. |
  | nextToken | string | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | BlockingInstances | array<object> | A list of all running Amazon EC2 instances on the Outpost. Stopping one or more of these       instances can free up the capacity needed to run the capacity task. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listCapacityTasks
**List capacity tasks** — Lists the capacity tasks for your Amazon Web Services account. Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.
- Stability: stable
- Permissions: `outposts:ListCapacityTasks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifierFilter | string | no | Filters the results by an Outpost ID or an Outpost ARN. |
  | maxResults | number | no | The maximum page size. |
  | nextToken | string | no | The pagination token. |
  | capacityTaskStatusFilter | array<string> | no | A list of statuses. For example, REQUESTED or WAITING_FOR_EVACUATION. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CapacityTasks | array<object> | Lists all the capacity tasks. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listCatalogItems
**List catalog items** — Lists the items in the catalog. Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.
- Stability: stable
- Permissions: `outposts:ListCatalogItems`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |
  | itemClassFilter | array<string> | no | Filters the results by item class. |
  | supportedStorageFilter | array<string> | no | Filters the results by storage option. |
  | eC2FamilyFilter | array<string> | no | Filters the results by EC2 family (for example, M5). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CatalogItems | array<object> | Information about the catalog items. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listOrders
**List orders** — Lists the Outpost orders for your Amazon Web Services account.
- Stability: stable
- Permissions: `outposts:ListOrders`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifierFilter | string | no | The ID or the Amazon Resource Name (ARN) of the Outpost. |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Orders | array<object> | Information about the orders. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listOutposts
**List outposts** — Lists the Outposts for your Amazon Web Services account. Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.
- Stability: stable
- Permissions: `outposts:ListOutposts`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |
  | lifeCycleStatusFilter | array<string> | no | Filters the results by the lifecycle status. |
  | availabilityZoneFilter | array<string> | no | Filters the results by Availability Zone (for example, us-east-1a). |
  | availabilityZoneIdFilter | array<string> | no | Filters the results by AZ ID (for example, use1-az1). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Outposts | array<object> | Information about the Outposts. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listSites
**List sites** — Lists the Outpost sites for your Amazon Web Services account. Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.
- Stability: stable
- Permissions: `outposts:ListSites`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The pagination token. |
  | maxResults | number | no | The maximum page size. |
  | operatingAddressCountryCodeFilter | array<string> | no | Filters the results by country code. |
  | operatingAddressStateOrRegionFilter | array<string> | no | Filters the results by state or region. |
  | operatingAddressCityFilter | array<string> | no | Filters the results by city. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Sites | array<object> | Information about the sites. |
  | NextToken | string | The pagination token. |


## com.datadoghq.aws.outposts.listTagsForResource
**List tags for resource** — Lists the tags for the specified resource.
- Stability: stable
- Permissions: `outposts:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Tags | object | The resource tags. |


## com.datadoghq.aws.outposts.startCapacityTask
**Start capacity task** — Starts the specified capacity task. You can have one active capacity task for each order and each Outpost.
- Stability: stable
- Permissions: `outposts:StartCapacityTask`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostIdentifier | string | yes | The ID or ARN of the Outposts associated with the specified capacity task. |
  | orderId | string | no | The ID of the Amazon Web Services Outposts order associated with the specified capacity task. |
  | assetId | string | no | The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration. |
  | instancePools | array<object> | yes | The instance pools specified in the capacity task. |
  | instancesToExclude | object | no | List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task. |
  | dryRun | boolean | no | You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan. |
  | taskActionOnBlockingInstances | string | no | Specify one of the following options in case an instance is blocking the capacity task from running. WAIT_FOR_EVACUATION - Checks every 10 minutes over 48 hours to determine if instances have stopp... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CapacityTaskId | string | ID of the capacity task that you want to start. |
  | OutpostId | string | ID of the Outpost associated with the capacity task. |
  | OrderId | string | ID of the Amazon Web Services Outposts order of the host associated with the capacity task. |
  | AssetId | string | The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an       Outposts server configuration. |
  | RequestedInstancePools | array<object> | List of the instance pools requested in the specified capacity task. |
  | InstancesToExclude | object | User-specified instances that must not be stopped in order to free up the capacity needed       to run the capacity task. |
  | DryRun | boolean | Results of the dry run showing if the specified capacity task is above or below the       available instance capacity. |
  | CapacityTaskStatus | string | Status of the specified capacity task. |
  | Failed | object | Reason that the specified capacity task failed. |
  | CreationDate | string | Date that the specified capacity task was created. |
  | CompletionDate | string | Date that the specified capacity task ran successfully. |
  | LastModifiedDate | string | Date that the specified capacity task was last modified. |
  | TaskActionOnBlockingInstances | string | User-specified option in case an instance is blocking the capacity task from       running.                                                          WAIT_FOR_EVACUATION - Checks every 10 minutes ov... |


## com.datadoghq.aws.outposts.startConnection
**Start connection** — Amazon Web Services uses this action to install Outpost servers. Starts the connection required for Outpost server installation. Use CloudTrail to monitor this action or Amazon Web Services managed policy for Amazon Web Services Outposts to secure it. For more information, see  Amazon Web Services managed policies for Amazon Web Services Outposts and Logging Amazon Web Services Outposts API calls with Amazon Web Services CloudTrail in the Amazon Web Services Outposts User Guide.
- Stability: stable
- Permissions: `outposts:StartConnection`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | deviceSerialNumber | string | no | The serial number of the dongle. |
  | assetId | string | yes | The ID of the Outpost server. |
  | clientPublicKey | string | yes | The public key of the client. |
  | networkInterfaceDeviceIndex | number | yes | The device index of the network interface on the Outpost server. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ConnectionId | string | The ID of the connection. |
  | UnderlayIpAddress | string | The underlay IP address. |


## com.datadoghq.aws.outposts.tagResource
**Tag resource** — Adds tags to the specified resource.
- Stability: stable
- Permissions: `outposts:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource. |
  | tags | any | yes | The tags to add to the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.untagResource
**Untag resource** — Removes tags from the specified resource.
- Stability: stable
- Permissions: `outposts:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource. |
  | tagKeys | array<string> | yes | The tag keys. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.outposts.updateOutpost
**Update outpost** — Updates an Outpost.
- Stability: stable
- Permissions: `outposts:UpdateOutpost`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | outpostId | string | yes | The ID or ARN of the Outpost. |
  | name | string | no | The name of the Outpost. |
  | description | string | no | The description of the Outpost. |
  | supportedHardwareType | string | no | The type of hardware for this Outpost. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Outpost | object | Information about an Outpost. |


## com.datadoghq.aws.outposts.updateSite
**Update site** — Updates the specified site.
- Stability: stable
- Permissions: `outposts:UpdateSite`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |
  | name | string | no | The name of the site. |
  | description | string | no | The description of the site. |
  | notes | string | no | Notes about a site. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Site | object | Information about a site. |


## com.datadoghq.aws.outposts.updateSiteAddress
**Update site address** — Updates the address of the specified site. You can't update a site address if there is an order in progress. You must wait for the order to complete or cancel the order. You can update the operating address before you place an order at the site, or after all Outposts that belong to the site have been deactivated.
- Stability: stable
- Permissions: `outposts:UpdateSiteAddress`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |
  | addressType | string | yes | The type of the address. |
  | address | object | yes | The address for the site. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | AddressType | string | The type of the address. |
  | Address | object | Information about an address. |


## com.datadoghq.aws.outposts.updateSiteRackPhysicalProperties
**Update site rack physical properties** — Update the physical and logistical details for a rack at a site. For more information about hardware requirements for racks, see Network readiness checklist in the Amazon Web Services Outposts User Guide. To update a rack at a site with an order of IN_PROGRESS, you must wait for the order to complete or cancel the order.
- Stability: stable
- Permissions: `outposts:UpdateSiteRackPhysicalProperties`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | siteId | string | yes | The ID or the Amazon Resource Name (ARN) of the site. |
  | powerDrawKva | string | no | The power draw, in kVA, available at the hardware placement position for the rack. |
  | powerPhase | string | no | The power option that you can provide for hardware. Single-phase AC feed: 200 V to 277 V, 50 Hz or 60 Hz Three-phase AC feed: 346 V to 480 V, 50 Hz or 60 Hz |
  | powerConnector | string | no | The power connector that Amazon Web Services should plan to provide for connections to the hardware. Note the correlation between PowerPhase and PowerConnector. Single-phase AC feed L6-30P – (commo... |
  | powerFeedDrop | string | no | Indicates whether the power feed comes above or below the rack. |
  | uplinkGbps | string | no | The uplink speed the rack should support for the connection to the Region. |
  | uplinkCount | string | no | Racks come with two Outpost network devices. Depending on the supported uplink speed at the site, the Outpost network devices provide a variable number of uplinks. Specify the number of uplinks for... |
  | fiberOpticCableType | string | no | The type of fiber that you will use to attach the Outpost to your network. |
  | opticalStandard | string | no | The type of optical standard that you will use to attach the Outpost to your network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information ... |
  | maximumSupportedWeightLbs | string | no | The maximum rack weight that this site can support. NO_LIMIT is over 2000lbs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Site | object | Information about a site. |

