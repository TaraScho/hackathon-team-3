# AWS EC2 Actions
Bundle: `com.datadoghq.aws.ec2` | 33 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eec2)

## com.datadoghq.aws.ec2.addSecurityGroupsToInstance
**Add EC2 instance security groups** — Add new Security Groups to list of already existing Security Groups of a EC2 Instance.
- Stability: stable
- Permissions: `ec2:ModifyInstanceAttribute`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | groups | array<string> | yes | IDs of the new Security Groups to associate with the specified EC2 instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.allocate_hosts
**Allocate hosts** — Allocate dedicated hosts to your account.
- Stability: stable
- Permissions: `ec2:AllocateHosts`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | availabilityZone | string | yes | The Availability Zone in which to allocate the Dedicated Host. |
  | instanceType | string | no | The instance type supported by the dedicated hosts. If specified, the dedicated hosts support instances of the specified instance type only. One of **Instance type** or **Instance family** must be ... |
  | instanceFamily | string | no | The instance family supported by the dedicated hosts. If specified, the dedicated hosts support multiple instance types within the instance family. One of **Instance type** or **Instance family** m... |
  | quantity | number | no | The number of dedicated hosts to allocate to your account with these parameters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hostIdSet | array<string> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.authorize_security_group_egress
**Authorize security group egress** — Add outbound (egress) rules to a security group.
- Stability: stable
- Permissions: `ec2:AuthorizeSecurityGroupEgress`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupId | string | no | Group ID must be specified in the request |
  | ipPermissions | array<object> | yes | Sets of IP permissions. Specifying a destination security group and a CIDR IP address range in the same set of permissions is not supported. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securityGroupRuleSet | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.authorize_security_group_ingress
**Authorize security group ingress** — Add inbound (ingress) rules to a security group.
- Stability: stable
- Permissions: `ec2:AuthorizeSecurityGroupIngress`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipPermissions | array<object> | yes | Sets of IP permissions. Specifying a destination security group and a CIDR IP address range in the same set of permissions is not supported. |
  | groupId | string | no | A group id or name must be specified. |
  | groupName | string | no | A group id or name must be specified. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securityGroupRuleSet | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.createKeyPair
**Create key pair** — Create an ED25519 or 2048-bit RSA key pair with a name and in the PEM or PPK format. Amazon EC2 stores the public key and displays the private key for you to save to a file. The private key is returned as an unencrypted PEM encoded PKCS#1 private key, or an unencrypted PPK formatted private key for use with PuTTY. If a key with the same name already exists, Amazon EC2 returns an error.
- Stability: stable
- Permissions: `ec2:CreateKeyPair`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | keyName | string | yes | A unique name for the key pair. |
  | keyType | string | no | The type of key pair. `ED25519` keys are not supported for Windows instances. |
  | keyFormat | string | no | The format of the key pair. |
  | tagSpecifications | array<object> | no | The tags to apply to the new key pair. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | keyFingerprint | string | For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.    For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default f... |
  | keyMaterial | string | An unencrypted PEM encoded RSA or ED25519 private key. |
  | keyName | string | The name of the key pair. |
  | keyPairId | string | The ID of the key pair. |
  | tags | array<object> | Any tags applied to the key pair. |
  | tagValue | object |  |
  | tagValueList | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.create_ec2_tags
**Create EC2 tags** — Add or overwrite tags for EC2 resources.
- Stability: stable
- Permissions: `ec2:CreateTags`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |
  | tags | any | yes | The `key:value` format tags to create. The `value` parameter is required, but can be specified with no value, and the value is set to an empty string. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.create_security_group
**Create security group** — Create a security group. A security group acts as a virtual firewall for your instance to control inbound and outbound traffic.
- Stability: stable
- Permissions: `ec2:CreateSecurityGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupName | string | yes | The name of the security group.   Constraints: Up to 255 characters in length. Cannot start with `sg-`.   Constraints for EC2-Classic: ASCII characters  Constraints for EC2-VPC: `a-z`, `A-Z`, `0-9`... |
  | groupDescription | string | yes | A description for the security group. This is for informational purposes only. |
  | vpcId | string | no | The ID of the VPC. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | groupId | string |  |
  | createdTags | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.deleteKeyPair
**Delete key pair** — Delete a key pair by removing the public key from Amazon EC2. If the key pair does not exist no key pairs are removed, but the action is still successful.
- Stability: stable
- Permissions: `ec2:DeleteKeyPair`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | keyName | string | no | The name of the key pair. |
  | keyPairId | string | no | The ID of the key pair. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.delete_ec2_tags
**Delete EC2 tags** — Delete tags from EC2 resources.
- Stability: stable
- Permissions: `ec2:DeleteTags`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |
  | tags | any | no | The `key:value` format tags to delete. Specify a tag key and an optional tag value to delete specific tags. If you specify a tag key without a tag value, any tag with the key is deleted regardless ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.delete_security_group
**Delete security group** — Delete a security group.
- Stability: stable
- Permissions: `ec2:DeleteSecurityGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupId | string | no | A group id or name must be specified. |
  | groupName | string | no | A group id or name must be specified. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describeAvailabilityZones
**Describe availability zones** — Describe the Availability Zones, Local Zones, and Wavelength Zones that are available to you.
- Stability: stable
- Permissions: `ec2:DescribeAvailabilityZones`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | allAvailabilityZones | boolean | no | Include all Availability Zones, Local Zones, and Wavelength Zones regardless of your opt-in status. |
  | filter | array<object> | no | Filter output to include only availability zones that meet the filter criteria. Supported filters: group-name, message, opt-in-status, parent-zoneID, parent-zoneName, region-name, state, zone-id, z... |
  | zoneID | array<string> | no | The IDs of the Availability Zones, Local Zones, and Wavelength Zones. |
  | zoneName | array<string> | no | The names of the Availability Zones, Local Zones, and Wavelength Zones. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | availabilityZoneInfo | array<object> | Information about the Availability Zones, Local Zones, and Wavelength Zones. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describeImages
**Describe images** — Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of the images available to you.
- Stability: stable
- Permissions: `ec2:DescribeImages`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | executableUsers | array<string> | no | Scopes the images by users with explicit launch permissions. Specify an Amazon Web Services account ID, self (the sender of the request), or all (public AMIs).   If you specify an Amazon Web Servic... |
  | filters | array<object> | no | Filter criteria for the images. |
  | imageIds | array<string> | no | The image IDs. Default: Describes all images available to you. |
  | owners | array<string> | no | Scopes the results to images with the specified owners. You can specify a combination of Amazon Web Services account IDs, self, amazon, and aws-marketplace. If you omit this parameter, the results ... |
  | includeDeprecated | boolean | no | Specifies whether to include deprecated AMIs. Default: No deprecated AMIs are included in the response.  If you are the AMI owner, all deprecated AMIs appear in the response regardless of what you ... |
  | includeDisabled | boolean | no | Specifies whether to include disabled AMIs. Default: No disabled AMIs are included in the response. |
  | dryRun | boolean | no | Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is Dry... |
  | maxResults | number | no | The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see Pagination. |
  | nextToken | string | no | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Images | array<object> | Information about the images. |
  | NextToken | string | The token to include in another request to get the next page of items. This value is null when there are no more items to return. |


## com.datadoghq.aws.ec2.describeKeyPairs
**List key pairs** — Describe the specified key pairs or all of your key pairs.
- Stability: stable
- Permissions: `ec2:DescribeKeyPairs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters. |
  | keyNames | array<string> | no | If specified, only return key pairs matching the provided names. |
  | keyPairIds | array<string> | no | If specified, only return key pairs matching the provided IDs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | keyPairs | array<object> | Information about the key pairs. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describeLaunchTemplates
**Describe launch templates** — Describes one or more launch templates. By default, all launch templates are described. Alternatively, you can filter the results.
- Stability: stable
- Permissions: `ec2:DescribeLaunchTemplates`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dryRun | boolean | no | Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is Dry... |
  | launchTemplateIds | array<string> | no | One or more launch template IDs. |
  | launchTemplateNames | array<string> | no | One or more launch template names. |
  | filters | array<object> | no | One or more filters.    create-time - The time the launch template was created.    launch-template-name - The name of the launch template.    tag:<key> - The key/value combination of a tag assigned... |
  | nextToken | string | no | The token to request the next page of results. |
  | maxResults | number | no | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. This value can be between 1 and 200. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | LaunchTemplates | array<object> | Information about the launch templates. |
  | NextToken | string | The token to use to retrieve the next page of results. This value is null when there are no more results to return. |


## com.datadoghq.aws.ec2.describeSecurityGroupRules
**List security group rules** — Describe one or more of your security group rules.
- Stability: stable
- Permissions: `ec2:DescribeSecurityGroupRules`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | One or more filters. |
  | securityGroupRuleIds | array<string> | no | If you specify security group rule IDs, the output includes information for only the specified security group rules. If you do not specify security group rule IDs, the output includes information f... |
  | maxResults | number | no | The maximum number of results to return in a single call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securityGroupRules | array<object> | Information about security group rules. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describeSecurityGroups
**Describe security groups** — Describes the specified security groups or all of your security groups.
- Stability: stable
- Permissions: `ec2:DescribeSecurityGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filters | array<object> | no | The filters. If using multiple filters for rules, the results include security groups for which any combination of rules - not necessarily a single rule - match all filters.    description - The de... |
  | groupIds | array<string> | no | The IDs of the security groups. Required for security groups in a nondefault VPC. Default: Describes all of your security groups. |
  | groupNames | array<string> | no | [Default VPC] The names of the security groups. You can specify either the security group name or the security group ID. Default: Describes all of your security groups. |
  | dryRun | boolean | no | Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is Dry... |
  | nextToken | string | no | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request. |
  | maxResults | number | no | The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. This value can be between 5 and 1000. If this para... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SecurityGroups | array<object> | Information about the security groups. |
  | NextToken | string | The token to include in another request to get the next page of items. This value is null when there are no more items to return. |


## com.datadoghq.aws.ec2.describe_ec2_host
**Describe EC2 host** — Describe a dedicated host.
- Stability: stable
- Permissions: `ec2:DescribeHosts`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | hostId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hostInfo | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describe_ec2_instance
**Describe EC2 instance** — Describe an EC2 instance.
- Stability: stable
- Permissions: `ec2:DescribeInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describe_ec2_instances
**List EC2 instances** — List EC2 instances.
- Stability: stable
- Permissions: `ec2:DescribeInstances`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceIds | array<string> | no | Filter output to include only the specified instances. If you do not specify instance IDs, the output includes information for all instances. |
  | filters | array<object> | no | Filter output to include only instances that meet the filter criteria. If you do not specify filters, the output includes information for all instances. |
  | maxResults | number | no | The maximum number of results to return in a single call. Can be any value between `5` and `1000`. |
  | nextToken | string | no | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instances | array<object> |  |
  | nextToken | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describe_ec2_tags
**Describe EC2 tags** — Describe tags for EC2 resources.
- Stability: stable
- Permissions: `ec2:DescribeTags`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | describedTags | array<object> | An array of tag descriptions. |
  | tagValue | object | A map of tags where both the keys and the values are strings. |
  | tagValueList | object | A map of tags where the keys are strings and the values are lists of strings. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.describe_security_group
**Describe security group** — Describe the specified security group.
- Stability: stable
- Permissions: `ec2:DescribeSecurityGroup`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupName | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securityGroupInfo | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.listAWSEC2Host
**List hosts** — List hosts.
- Stability: stable
- Permissions: `ec2:DescribeHosts`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | hosts | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.modifySecurityGroupRules
**Modify security group rules** — Modify the rules of a security group.
- Stability: stable
- Permissions: `ec2:ModifySecurityGroupRules`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupId | string | yes | The ID of the security group. |
  | securityGroupRules | array<object> | yes | Information about the security group properties to update. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | securityGroupInfo | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.monitor_ec2_instance
**Monitor EC2 instance** — Enable detailed monitoring for a running instance.
- Stability: stable
- Permissions: `ec2:MonitorInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceMonitoringInfo | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.reboot_ec2_instance
**Reboot EC2 instance** — Request a reboot of the specified instance.
- Stability: stable
- Permissions: `ec2:RebootInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | onlyReboot | boolean | no | Disables fetching or waiting on the instance after reboot. This option takes priority over waitForCompletion if set. |
  | waitForCompletion | boolean | no | Wait for the instance to reach the new state before continuing the workflow. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.release_host
**Release host** — Release an on-demand dedicated host.
- Stability: stable
- Permissions: `ec2:ReleaseHosts`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | hostId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.revoke_security_group_egress
**Revoke security group egress** — Remove outbound (egress) rules from a security group.
- Stability: stable
- Permissions: `ec2:RevokeSecurityGroupEgress`
- Access: delete, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | groupId | string | yes |  |
  | ipPermissions | array<object> | no | Sets of IP permissions. Specifying a destination security group and a CIDR IP address range in the same set of permissions is not supported. |
  | securityGroupRuleIds | array<string> | no | The IDs of the security group rules. |
  | dryRun | boolean | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | unknownIpPermissionSet | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.revoke_security_group_ingress
**Revoke security group ingress** — Remove inbound (ingress) rules from a security group.
- Stability: stable
- Permissions: `ec2:RevokeSecurityGroupIngress`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ipPermissions | array<object> | yes | Sets of IP permissions. Specifying a destination security group and a CIDR IP address range in the same set of permissions is not supported. |
  | securityGroupRuleIds | array<string> | no | The IDs of the security group rules. |
  | groupId | string | no | A group id or name must be specified. |
  | groupName | string | no | A group id or name must be specified. |
  | dryRun | boolean | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | unknownIpPermissionSet | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.start_ec2_instance
**Start EC2 instance** — Start an Amazon EBS-backed instance that was previously stopped.
- Stability: stable
- Permissions: `ec2:StartInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | waitForCompletion | boolean | no | Wait for the instance to reach the new state before continuing the workflow. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.stop_ec2_instance
**Stop EC2 instance** — Stop an Amazon EBS-backed instance.
- Stability: stable
- Permissions: `ec2:StopInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | waitForCompletion | boolean | no | Wait for the instance to reach the new state before continuing the workflow. |
  | hibernate | boolean | no | Hibernate the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successfully, a normal shutdown occurs. |
  | force | boolean | no | Force the instance to stop. The instance does not have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair proc... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.terminate_ec2_instance
**Terminate EC2 instance** — Terminate an EC2 instance.
- Stability: stable
- Permissions: `ec2:TerminateInstances`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | waitForCompletion | boolean | no | Wait for the instance to reach the new state before continuing the workflow. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instance | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.unmonitor_ec2_instance
**Unmonitor EC2 instance** — Disable detailed monitoring for a running instance.
- Stability: stable
- Permissions: `ec2:UnmonitorInstances`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | instanceMonitoringInfo | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ec2.updateInstanceSecurityGroups
**Update EC2 instance security groups** — Replace current set of Security Groups associated with a specific EC2 instance with the Security Groups specified.
- Stability: stable
- Permissions: `ec2:ModifyInstanceAttribute`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | instanceId | string | yes |  |
  | groups | array<string> | yes | IDs of the new Security Groups to associate with the specified EC2 instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

