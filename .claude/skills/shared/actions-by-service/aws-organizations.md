# AWS Organizations Actions
Bundle: `com.datadoghq.aws.organizations` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eorganizations)

## com.datadoghq.aws.organizations.closeAccount
**Close account** — Closes an Amazon Web Services member account within an organization.
- Stability: stable
- Permissions: `organizations:CloseAccount`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | accountId | string | yes | Retrieves the Amazon Web Services account Id for the current CloseAccount API request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.organizations.createAccount
**Create account** — Creates an Amazon Web Services account that is automatically a member of the organization whose credentials made the request.
- Stability: stable
- Permissions: `organizations:CreateAccount`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | email | string | yes | The email address of the owner to assign to the new member account. This email address must not already be associated with another Amazon Web Services account. You must use a valid email address to... |
  | accountName | string | yes | The friendly name of the member account. |
  | roleName | string | no | The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the management account, allowing users in the management account to assume the rol... |
  | iamUserAccessToBilling | string | no | If set to ALLOW, the new account enables IAM users to access account billing information if they have the required permissions. If set to DENY, only the root user of the new account can access acco... |
  | tags | any | no | A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't s... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CreateAccountStatus | object | A structure that contains details about the request to create an account. This response structure might not be fully populated when you first receive it because account creation is an asynchronous ... |


## com.datadoghq.aws.organizations.listAccounts
**List accounts** — Lists all the accounts in the organization.
- Stability: stable
- Permissions: `organizations:ListAccounts`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the val... |
  | maxResults | number | no | The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Accounts | array<object> | A list of objects in the organization. |
  | NextToken | string | If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next... |


## com.datadoghq.aws.organizations.listOrganizationalUnitsForParent
**List organizational units for parent** — Lists the organizational units (OUs) in a parent organizational unit or root.
- Stability: stable
- Permissions: `organizations:ListOrganizationalUnitsForParent`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | parentId | string | yes | The unique identifier (ID) of the root or OU whose child OUs you want to list. The regex pattern for a parent ID string requires one of the following:    Root - A string that begins with "r-" follo... |
  | nextToken | string | no | The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the val... |
  | maxResults | number | no | The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | OrganizationalUnits | array<object> | A list of the OUs in the specified root or parent OU. |
  | NextToken | string | If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next... |


## com.datadoghq.aws.organizations.listRoots
**List roots** — Lists the roots that are defined in the current organization.
- Stability: stable
- Permissions: `organizations:ListRoots`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The parameter for receiving additional results if you receive a NextToken response in a previous request. A NextToken response indicates that more output is available. Set this parameter to the val... |
  | maxResults | number | no | The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Roots | array<object> | A list of roots that are defined in an organization. |
  | NextToken | string | If present, indicates that more output is available than is included in the current response. Use this value in the NextToken request parameter in a subsequent call to the operation to get the next... |


## com.datadoghq.aws.organizations.moveAccount
**Move account** — Moves an account from its current source parent root or organizational unit (OU) to the specified destination parent root or OU.
- Stability: stable
- Permissions: `organizations:MoveAccount`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | accountId | string | yes | The unique identifier (ID) of the account that you want to move. The regex pattern for an account ID string requires exactly 12 digits. |
  | sourceParentId | string | yes | The unique identifier (ID) of the root or organizational unit that you want to move the account from. The regex pattern for a parent ID string requires one of the following:    Root - A string that... |
  | destinationParentId | string | yes | The unique identifier (ID) of the root or organizational unit that you want to move the account to. The regex pattern for a parent ID string requires one of the following:    Root - A string that b... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

