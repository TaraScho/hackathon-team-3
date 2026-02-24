# AWS IAM Identity Center Actions
Bundle: `com.datadoghq.aws.iamidentitycenter` | 19 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eiamidentitycenter)

## com.datadoghq.aws.iamidentitycenter.createGroup
**Create group** — Creates a group within the specified identity store.
- Stability: stable
- Permissions: `identitystore:CreateGroup`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | displayName | string | no | A string containing the name of the group. This value is commonly displayed when the group is referenced. Administrator and AWSAdministrators are reserved names and can't be used for users or groups. |
  | description | string | no | A string containing the description of the group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GroupId | string | The identifier of the newly created group in the identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.createGroupMembership
**Create group membership** — Creates a relationship between a member and a group. The following identifiers must be specified: GroupId, IdentityStoreId, and MemberId.
- Stability: stable
- Permissions: `identitystore:CreateGroupMembership`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | groupId | string | yes | The identifier for a group in the identity store. |
  | memberId | object | yes | An object that contains the identifier of a group member. Setting the UserID field to the specific identifier for a user indicates that the user is a member of the group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MembershipId | string | The identifier for a newly created GroupMembership in an identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.createUser
**Create user** — Creates a user within the specified identity store.
- Stability: stable
- Permissions: `identitystore:CreateUser`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | userName | string | no | A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at ... |
  | name | object | no | An object containing the name of the user. |
  | displayName | string | no | A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, "John Doe." |
  | nickName | string | no | A string containing an alternate name for the user. |
  | profileUrl | string | no | A string containing a URL that might be associated with the user. |
  | emails | array<object> | no | A list of Email objects containing email addresses associated with the user. |
  | addresses | array<object> | no | A list of Address objects containing addresses associated with the user. |
  | phoneNumbers | array<object> | no | A list of PhoneNumber objects containing phone numbers associated with the user. |
  | userType | string | no | A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case. |
  | title | string | no | A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case. |
  | preferredLanguage | string | no | A string containing the preferred language of the user. For example, "American English" or "en-us." |
  | locale | string | no | A string containing the geographical region or location of the user. |
  | timezone | string | no | A string containing the time zone of the user. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserId | string | The identifier of the newly created user in the identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.deleteGroup
**Delete group** — Delete a group within an identity store given GroupId.
- Stability: stable
- Permissions: `identitystore:DeleteGroup`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | groupId | string | yes | The identifier for a group in the identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iamidentitycenter.deleteGroupMembership
**Delete group membership** — Delete a membership within a group given MembershipId.
- Stability: stable
- Permissions: `identitystore:DeleteGroupMembership`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | membershipId | string | yes | The identifier for a GroupMembership in an identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iamidentitycenter.deleteUser
**Delete user** — Deletes a user within an identity store given UserId.
- Stability: stable
- Permissions: `identitystore:DeleteUser`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | userId | string | yes | The identifier for a user in the identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iamidentitycenter.describeGroup
**Describe group** — Retrieves the group metadata and attributes from GroupId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:DescribeGroup`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string that contains numbers and lower cas... |
  | groupId | string | yes | The identifier for a group in the identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GroupId | string | The identifier for a group in the identity store. |
  | DisplayName | string | The group’s display name value. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, a... |
  | ExternalIds | array<object> | A list of ExternalId objects that contains the identifiers issued to this resource by an external identity provider. |
  | Description | string | A string containing a description of the group. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.describeGroupMembership
**Describe group membership** — Retrieves membership metadata and attributes from MembershipId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:DescribeGroupMembership`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | membershipId | string | yes | The identifier for a GroupMembership in an identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |
  | MembershipId | string | The identifier for a GroupMembership in an identity store. |
  | GroupId | string | The identifier for a group in the identity store. |
  | MemberId | object |  |


## com.datadoghq.aws.iamidentitycenter.describeUser
**Describe user** — Retrieves the user metadata and attributes from the UserId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:DescribeUser`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string that contains numbers and lower cas... |
  | userId | string | yes | The identifier for a user in the identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserName | string | A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at ... |
  | UserId | string | The identifier for a user in the identity store. |
  | ExternalIds | array<object> | A list of ExternalId objects that contains the identifiers issued to this resource by an external identity provider. |
  | Name | object | The name of the user. |
  | DisplayName | string | The display name of the user. |
  | NickName | string | An alternative descriptive name for the user. |
  | ProfileUrl | string | A URL link for the user's profile. |
  | Emails | array<object> | The email address of the user. |
  | Addresses | array<object> | The physical address of the user. |
  | PhoneNumbers | array<object> | A list of PhoneNumber objects associated with a user. |
  | UserType | string | A string indicating the type of user. |
  | Title | string | A string containing the title of the user. |
  | PreferredLanguage | string | The preferred language of the user. |
  | Locale | string | A string containing the geographical region or location of the user. |
  | Timezone | string | The time zone for a user. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.getGroupId
**Get group ID** — Retrieves GroupId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:GetGroupId`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | alternateIdentifier | object | yes | A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GroupId | string | The identifier for a group in the identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.getGroupMembershipId
**Get group membership ID** — Retrieves the MembershipId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:GetGroupMembershipId`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | groupId | string | yes | The identifier for a group in the identity store. |
  | memberId | object | yes | An object that contains the identifier of a group member. Setting the UserID field to the specific identifier for a user indicates that the user is a member of the group. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MembershipId | string | The identifier for a GroupMembership in an identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.getUserId
**Get user ID** — Retrieves the UserId in an identity store.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:GetUserId`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | alternateIdentifier | object | yes | A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserId | string | The identifier for a user in the identity store. |
  | IdentityStoreId | string | The globally unique identifier for the identity store. |


## com.datadoghq.aws.iamidentitycenter.isMemberInGroups
**Is member in groups** — Checks the user&#x27;s membership in all requested groups and returns if the member exists in all queried groups.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:IsMemberInGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | memberId | object | yes | An object containing the identifier of a group member. |
  | groupIds | array<string> | yes | A list of identifiers for groups in the identity store. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Results | array<object> | A list containing the results of membership existence checks. |


## com.datadoghq.aws.iamidentitycenter.listGroupMemberships
**List group memberships** — For the specified group in the specified identity store, returns the list of all GroupMembership objects and returns results in paginated form.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:ListGroupMemberships`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | groupId | string | yes | The identifier for a group in the identity store. |
  | maxResults | number | no | The maximum number of results to be returned per request. This parameter is used in all List requests to specify how many results to return in one page. |
  | nextToken | string | no | The pagination token used for the ListUsers, ListGroups and ListGroupMemberships API operations. This value is generated by the identity store service. It is returned in the API response if the tot... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GroupMemberships | array<object> | A list of GroupMembership objects in the group. |
  | NextToken | string | The pagination token used for the ListUsers, ListGroups, and ListGroupMemberships API operations. This value is generated by the identity store service. It is returned in the API response if the to... |


## com.datadoghq.aws.iamidentitycenter.listGroupMembershipsForMember
**List group memberships for member** — For the specified member in the specified identity store, returns the list of all GroupMembership objects and returns results in paginated form.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:ListGroupMembershipsForMember`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | memberId | object | yes | An object that contains the identifier of a group member. Setting the UserID field to the specific identifier for a user indicates that the user is a member of the group. |
  | maxResults | number | no | The maximum number of results to be returned per request. This parameter is used in the ListUsers and ListGroups requests to specify how many results to return in one page. The length limit is 50 c... |
  | nextToken | string | no | The pagination token used for the ListUsers, ListGroups, and ListGroupMemberships API operations. This value is generated by the identity store service. It is returned in the API response if the to... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GroupMemberships | array<object> | A list of GroupMembership objects in the group for a specified member. |
  | NextToken | string | The pagination token used for the ListUsers, ListGroups, and ListGroupMemberships API operations. This value is generated by the identity store service. It is returned in the API response if the to... |


## com.datadoghq.aws.iamidentitycenter.listGroups
**List groups** — Lists all groups in the identity store. Returns a paginated list of complete Group objects. Filtering for a Group by the DisplayName attribute is deprecated. Instead, use the GetGroupId API action.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:ListGroups`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string that contains numbers and lower cas... |
  | maxResults | number | no | The maximum number of results to be returned per request. This parameter is used in the ListUsers and ListGroups requests to specify how many results to return in one page. The length limit is 50 c... |
  | nextToken | string | no | The pagination token used for the ListUsers and ListGroups API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more th... |
  | filters | array<object> | no | A list of Filter objects, which is used in the ListUsers and ListGroups requests. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Groups | array<object> | A list of Group objects in the identity store. |
  | NextToken | string | The pagination token used for the ListUsers and ListGroups API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more th... |


## com.datadoghq.aws.iamidentitycenter.listUsers
**List users** — Lists all users in the identity store. Returns a paginated list of complete User objects. Filtering for a User by the UserName attribute is deprecated. Instead, use the GetUserId API action.  If you have administrator access to a member account, you can use this API from the member account. Read about member accounts in the Organizations User Guide.
- Stability: stable
- Permissions: `identitystore:ListUsers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store, such as d-1234567890. In this example, d- is a fixed prefix, and 1234567890 is a randomly generated string that contains numbers and lower cas... |
  | maxResults | number | no | The maximum number of results to be returned per request. This parameter is used in the ListUsers and ListGroups requests to specify how many results to return in one page. The length limit is 50 c... |
  | nextToken | string | no | The pagination token used for the ListUsers and ListGroups API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more th... |
  | filters | array<object> | no | A list of Filter objects, which is used in the ListUsers and ListGroups requests. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Users | array<object> | A list of User objects in the identity store. |
  | NextToken | string | The pagination token used for the ListUsers and ListGroups API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more th... |


## com.datadoghq.aws.iamidentitycenter.updateGroup
**Update group** — For the specified group in the specified identity store, updates the group metadata and attributes.
- Stability: stable
- Permissions: `identitystore:UpdateGroup`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | groupId | string | yes | The identifier for a group in the identity store. |
  | operations | array<object> | yes | A list of AttributeOperation objects to apply to the requested group. These operations might add, replace, or remove an attribute. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.iamidentitycenter.updateUser
**Update user** — For the specified user in the specified identity store, updates the user metadata and attributes.
- Stability: stable
- Permissions: `identitystore:UpdateUser`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | identityStoreId | string | yes | The globally unique identifier for the identity store. |
  | userId | string | yes | The identifier for a user in the identity store. |
  | operations | array<object> | yes | A list of AttributeOperation objects to apply to the requested user. These operations might add, replace, or remove an attribute. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

