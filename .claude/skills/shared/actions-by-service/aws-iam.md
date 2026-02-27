# AWS IAM Actions
Bundle: `com.datadoghq.aws.iam` | 30 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eiam)

## com.datadoghq.aws.iam.add_user_to_group
**Add user to group** — Add a user to a group.
- Stability: stable
- Permissions: `iam:AddUserToGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name of the group to update. |
  | userName | string | yes | The name of the IAM user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.attachGroupPolicy
**Attach group policy** — Attach the specified managed policy to the specified IAM group.
- Stability: stable
- Permissions: `iam:AttachGroupPolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name (friendly name, not ARN) of the group to attach the policy to. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric chara... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.attachRolePolicy
**Attach role policy** — Attach the specified managed policy to the specified IAM role.
- Stability: stable
- Permissions: `iam:AttachRolePolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | roleName | string | yes | The name (friendly name, not ARN) of the role to attach the policy to. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric charac... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.attachUserPolicy
**Attach user policy** — Attach an IAM managed policy to the specified IAM user.
- Stability: stable
- Permissions: `iam:AttachUserPolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name (friendly name, not ARN) of the IAM user to attach the policy to. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric ch... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.createGroup
**Create group** — Create a new IAM group for your AWS account.
- Stability: stable
- Permissions: `iam:CreateGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | path | string | no | The path to the group. For more information about paths, see IAM identifiers in the IAM User Guide. This parameter is optional. If it is not included, it defaults to a slash (/). This parameter all... |
  | groupName | string | yes | The name of the group to create. Do not include the path in this value. IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Group | object | A structure containing details about the new group. |


## com.datadoghq.aws.iam.createPolicy
**Create policy** — Create a new managed policy for your AWS account.
- Stability: stable
- Permissions: `iam:CreatePolicy`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policyName | string | yes | The friendly name of the policy. IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both ... |
  | path | string | no | The path for the policy. For more information about paths, see IAM identifiers in the IAM User Guide. This parameter is optional. If it is not included, it defaults to a slash (/). This parameter a... |
  | policyDocument | string | yes | The JSON policy document that you want to use as the content for the new policy. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can pr... |
  | description | string | no | A friendly description of the policy. Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy descrip... |
  | tags | any | no | A list of tags that you want to attach to the new IAM customer managed policy. Each tag consists of a key name and an associated value. For more information about tagging, see Tagging IAM resources... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Policy | object | A structure containing details about the new policy. |


## com.datadoghq.aws.iam.createRole
**Create role** — Create a new role for your AWS account.
- Stability: stable
- Permissions: `iam:CreateRole`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | path | string | no | The path to the role. For more information about paths, see IAM Identifiers in the IAM User Guide. This parameter is optional. If it is not included, it defaults to a slash (/). This parameter allo... |
  | roleName | string | yes | The name of the role to create. IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "... |
  | assumeRolePolicyDocument | string | yes | The trust relationship policy document that grants an entity permission to assume the role. In IAM, you must provide a JSON policy that has been converted to a string. However, for CloudFormation t... |
  | description | string | no | A description of the role. |
  | maxSessionDuration | number | no | The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can hav... |
  | permissionsBoundary | string | no | The ARN of the managed policy that is used to set the permissions boundary for the role. A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an e... |
  | tags | any | no | A list of tags that you want to attach to the new role. Each tag consists of a key name and an associated value. For more information about tagging, see Tagging IAM resources in the IAM User Guide.... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Role | object | A structure containing details about the new role. |


## com.datadoghq.aws.iam.create_user
**Create user** — Create a new IAM user for your Amazon Web Services account.
- Stability: stable
- Permissions: `iam:CreateUser`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |
  | path | string | no | The path for the user name. |
  | permissionsBoundary | string | no | The ARN of the policy used to set the permissions boundary for the user. |
  | tags | any | no | A list of tags to attach to the new user. Each tag consists of a key name and an associated value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | user | object | A structure with details about the new IAM user. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.create_user_login
**Create user login** — Create a password for an IAM user.
- Stability: stable
- Permissions: `iam:CreateLoginProfile`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |
  | password | string | yes | The new password for the user. A password can include any printable ASCII character from the space (`\u0020`) through the end of the ASCII character range (`\u00FF`), tab (`\u0009`), line feed (`\u... |
  | passwordResetRequired | boolean | no | Require the user to set a new password on their next sign-in. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | loginProfile | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.deleteAccessKey
**Delete access key** — Delete the access key pair associated with the specified IAM user.
- Stability: stable
- Permissions: `iam:DeleteAccessKey`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | userName | string | no | The name of the user whose access key pair you want to delete. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters wit... |
  | accessKeyId | string | yes | The access key ID for the access key ID and secret access key you want to delete. This parameter allows (through its regex pattern) a string of characters that can consist of any upper or lowercase... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.deleteGroup
**Delete group** — Delete the specified IAM group. The group must not contain any users or have any attached policies.
- Stability: stable
- Permissions: `iam:DeleteGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name of the IAM group to delete. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.deletePolicy
**Delete policy** — Delete the specified managed policy.
- Stability: stable
- Permissions: `iam:DeletePolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to delete. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.deleteRole
**Delete role** — Delete the specified role. The role must not have any policies attached.
- Stability: stable
- Permissions: `iam:DeleteRole`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | roleName | string | yes | The name of the role to delete. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also inclu... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.delete_user
**Delete user** — Delete all items attached to the IAM user; then delete the user.
- Stability: stable
- Permissions: `iam:DeleteUser`, `iam:DeleteLoginProfile`, `iam:ListGroupsForUser`, `iam:RemoveUserFromGroup`, `iam:ListAccessKeys`, `iam:DeleteAccessKey`, `iam:ListSigningCertificates`, `iam:DeleteSigningCertificate`, `iam:ListSSHPublicKeys`, `iam:DeleteSSHPublicKey`, `iam:ListServiceSpecificCredentials`, `iam:DeleteServiceSpecificCredential`, `iam:ListMFADevices`, `iam:DeactivateMFADevice`, `iam:DeleteVirtualMFADevice`, `iam:ListUserPolicies`, `iam:DeleteUserPolicy`, `iam:ListAttachedUserPolicies`, `iam:DetachUserPolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.detachGroupPolicy
**Detach group policy** — Remove the specified managed policy from the specified IAM group.
- Stability: stable
- Permissions: `iam:DetachGroupPolicy`
- Access: update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name (friendly name, not ARN) of the IAM group to detach the policy from. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to detach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.detachRolePolicy
**Detach role policy** — Remove the specified managed policy from the specified IAM role.
- Stability: stable
- Permissions: `iam:DetachRolePolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | roleName | string | yes | The name (friendly name, not ARN) of the IAM role to detach the policy from. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric ... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to detach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.detachUserPolicy
**Detach user policy** — Remove the specified managed policy from the specified user.
- Stability: stable
- Permissions: `iam:DetachUserPolicy`
- Access: update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name (friendly name, not ARN) of the IAM user to detach the policy from. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric ... |
  | policyArn | string | yes | The Amazon Resource Name (ARN) of the IAM policy you want to detach. For more information about ARNs, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.disable_user
**Disable user** — Disable access for the IAM user by revoking all authentication credentials.
- Stability: stable
- Permissions: `iam:DeleteLoginProfile`, `iam:ListAccessKeys`, `iam:DeleteAccessKey`, `iam:ListSigningCertificates`, `iam:DeleteSigningCertificate`, `iam:ListSSHPublicKeys`, `iam:DeleteSSHPublicKey`, `iam:ListServiceSpecificCredentials`, `iam:DeleteServiceSpecificCredential`, `iam:ListMFADevices`, `iam:DeactivateMFADevice`, `iam:DeleteVirtualMFADevice`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |


## com.datadoghq.aws.iam.getGroup
**Get group** — Return a list of IAM users that are in the specified IAM group.
- Stability: stable
- Permissions: `iam:GetGroup`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name of the group. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of... |
  | marker | string | no | Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you r... |
  | maxItems | number | no | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Group | object | A structure that contains details about the group. |
  | Users | array<object> | A list of users in the group. |
  | IsTruncated | boolean | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.... |
  | Marker | string | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |


## com.datadoghq.aws.iam.getUser
**Get user** — Retrieve information about the specified IAM user.
- Stability: stable
- Permissions: `iam:GetUser`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | user | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.listAccessKeys
**List access keys** — Return information about the access key IDs associated with the specified IAM user.
- Stability: stable
- Permissions: `iam:ListAccessKeys`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | The name of the IAM user. |
  | marker | any | no | Pagination parameter. |
  | maxItems | any | no | Indicates the maximum number of items to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | accessKeyMetadata | array<object> | A list of objects containing metadata about the access keys. |
  | isTruncated | any | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items. |
  | marker | any | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.listGroups
**List groups** — List the IAM groups that have the specified path prefix.
- Stability: stable
- Permissions: `iam:ListGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pathPrefix | string | no | The path prefix for filtering the results. For example, the prefix /division_abc/subdivision_xyz/ gets all groups whose path starts with /division_abc/subdivision_xyz/. This parameter is optional. ... |
  | marker | string | no | Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you r... |
  | maxItems | number | no | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Groups | array<object> | A list of groups. |
  | IsTruncated | boolean | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.... |
  | Marker | string | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |


## com.datadoghq.aws.iam.listPolicies
**List policies** — List all the managed policies that are available in your AWS account.
- Stability: stable
- Permissions: `iam:ListPolicies`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | scope | string | no | The scope to use for filtering the results. To list only Amazon Web Services managed policies, set Scope to AWS. To list only the customer managed policies in your Amazon Web Services account, set ... |
  | onlyAttached | boolean | no | A flag to filter the results to only the attached policies. When OnlyAttached is true, the returned list contains only the policies that are attached to an IAM user, group, or role. When OnlyAttach... |
  | pathPrefix | string | no | The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This parameter allows (through its regex pattern) a s... |
  | policyUsageFilter | string | no | The policy usage method to use for filtering the results. To list only permissions policies, set PolicyUsageFilter to PermissionsPolicy. To list only the policies used to set permissions boundaries... |
  | marker | string | no | Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you r... |
  | maxItems | number | no | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Policies | array<object> | A list of policies. |
  | IsTruncated | boolean | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.... |
  | Marker | string | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |


## com.datadoghq.aws.iam.listRoles
**List roles** — List the IAM roles that have the specified path prefix.
- Stability: stable
- Permissions: `iam:ListRoles`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pathPrefix | string | no | The path prefix for filtering the results. For example, the prefix /application_abc/component_xyz/ gets all roles whose path starts with /application_abc/component_xyz/. This parameter is optional.... |
  | marker | string | no | Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you r... |
  | maxItems | number | no | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Roles | array<object> | A list of roles. |
  | IsTruncated | boolean | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.... |
  | Marker | string | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |


## com.datadoghq.aws.iam.listUsers
**List users** — List the IAM users that have the specified path prefix.
- Stability: stable
- Permissions: `iam:ListUsers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | pathPrefix | string | no | The path prefix for filtering the results. For example: /division_abc/subdivision_xyz/, which would get all user names whose path starts with /division_abc/subdivision_xyz/. This parameter is optio... |
  | marker | string | no | Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker element in the response that you r... |
  | maxItems | number | no | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Users | array<object> | A list of users. |
  | IsTruncated | boolean | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.... |
  | Marker | string | When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request. |


## com.datadoghq.aws.iam.putRolePolicy
**Put role policy** — Add or updates an inline policy document that is embedded in the specified IAM role.
- Stability: stable
- Permissions: `iam:PutRolePolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | roleName | string | yes | The name of the role to associate the policy with. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces.... |
  | policyName | string | yes | The name of the policy document. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also incl... |
  | policyDocument | string | yes | The policy document. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation alwa... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.putUserPolicy
**Put user policy** — Add or updates an inline policy document that is embedded in the specified IAM user.
- Stability: stable
- Permissions: `iam:PutUserPolicy`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | userName | string | yes | The name of the user to associate the policy with. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces.... |
  | policyName | string | yes | The name of the policy document. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also incl... |
  | policyDocument | string | yes | The policy document. You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation alwa... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.remove_user_from_group
**Remove user from group** — Remove a user from a group.
- Stability: stable
- Permissions: `iam:RemoveUserFromGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | groupName | string | yes | The name of the group to update. |
  | userName | string | yes | The name of the IAM user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.updateAccessKey
**Update access key** — Change the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user&#x27;s key as part of a key rotation workflow.
- Stability: stable
- Permissions: `iam:UpdateAccessKey`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | userName | string | no | The name of the user whose key you want to update. This parameter allows (through its regex pattern) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces.... |
  | accessKeyId | string | yes | The access key ID of the secret access key you want to update. This parameter allows (through its regex pattern) a string of characters that can consist of any upper or lowercased letter or digit. |
  | status | string | yes | The status you want to assign to the secret access key. Active means that the key can be used for programmatic calls to Amazon Web Services, while Inactive means that the key cannot be used. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iam.updateUser
**Update user** — Update the name and/or the path of the specified IAM user.
- Stability: stable
- Permissions: `iam:UpdateUser`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | userName | string | yes | Name of the user to update. If you're changing the name of the user, this is the original user name. This parameter allows (through its regex pattern) a string of characters consisting of upper and... |
  | newPath | string | no | New path for the IAM user. Include this parameter only if you're changing the user's path. This parameter allows (through its regex pattern) a string of characters consisting of either a forward sl... |
  | newUserName | string | no | New name for the user. Include this parameter only if you're changing the user's name. IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

