# AWS SES Actions
Bundle: `com.datadoghq.aws.ses` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eses)

## com.datadoghq.aws.ses.createTemplate
**Create template** — Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single operation. For more information, see the Amazon SES Developer Guide. You can execute this operation no more than once per second.
- Stability: stable
- Permissions: `ses:CreateTemplate`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | template | object | yes | The content of the email, composed of a subject line and either an HTML part or a text-only part. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ses.deleteTemplate
**Delete template** — Deletes an email template. You can execute this operation no more than once per second.
- Stability: stable
- Permissions: `ses:DeleteTemplate`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | templateName | string | yes | The name of the template to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ses.getTemplate
**Get template** — Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify. You can execute this operation no more than once per second.
- Stability: stable
- Permissions: `ses:GetTemplate`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | templateName | string | yes | The name of the template to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Template | object | The content of the email, composed of a subject line and either an HTML part or a             text-only part. |


## com.datadoghq.aws.ses.listTemplates
**List templates** — Lists the email templates present in your Amazon SES account in the current Amazon Web Services Region. You can execute this operation no more than once per second.
- Stability: stable
- Permissions: `ses:ListTemplates`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A token returned from a previous call to ListTemplates to indicate the position in the list of email templates. |
  | maxItems | number | no | The maximum number of templates to return. This value must be at least 1 and less than or equal to 100. If more than 100 items are requested, the page size will automatically set to 100. If you do ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TemplatesMetadata | array<object> | An array the contains the name and creation time stamp for each template in your Amazon SES             account. |
  | NextToken | string | A token indicating that there are additional email templates available to be listed.             Pass this token to a subsequent call to ListTemplates to retrieve the next             set of email ... |


## com.datadoghq.aws.ses.sendBulkTemplatedEmail
**Send bulk templated email** — Composes an email message to multiple destinations. The message body is created using an email template. To send email using this operation, your call must meet the following requirements: The call must refer to an existing email template. You can create email templates using CreateTemplate. The message must be sent from a verified email address or domain. If your account is still in the Amazon SES sandbox, you may send only to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide. The maximum message size is 10 MB. Each Destination parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message is rejected, even if the message contains other recipients that are valid. The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the SendBulkTemplatedEmail operation several times to send the message to each group. The number of destinations you can contact in a single call can be limited by your account's maximum sending rate.
- Stability: stable
- Permissions: `ses:SendBulkTemplatedEmail`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | source | string | yes | The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about ... |
  | sourceArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specifie... |
  | replyToAddresses | array<string> | no | The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply. |
  | returnPath | string | no | The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the r... |
  | returnPathArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in ... |
  | configurationSetName | string | no | The name of the configuration set to use when you send an email using SendBulkTemplatedEmail. |
  | defaultTags | array<object> | no | A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using SendBulkTemplatedEmail. |
  | template | string | yes | The template to use when sending this email. |
  | templateArn | string | no | The ARN of the template to use when sending this email. |
  | defaultTemplateData | string | yes | A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is availabl... |
  | destinations | array<object> | yes | One or more Destination objects. All of the recipients in a Destination receive the same version of the email. You can specify up to 50 Destination objects within a Destinations array. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Status | array<object> | One object per intended recipient. Check each response object and retry any messages             with a failure status. (Note that order of responses will be respective to order of             dest... |


## com.datadoghq.aws.ses.sendEmail
**Send email** — Composes an email message and immediately queues it for sending. To send email using this operation, your message must meet the following requirements: The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation results in an "Email address not verified" error. If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide. The maximum message size is 10 MB. The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message is rejected, even if the message contains other recipients that are valid. The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the SendEmail operation several times to send the message to each group. <important> For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your sending quota). For more information about sending quotas in Amazon SES, see Managing Your Amazon SES Sending Limits in the Amazon SES Developer Guide. </important>.
- Stability: stable
- Permissions: `ses:SendEmail`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | source | string | yes | The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about ... |
  | destination | object | yes | The destination for this email, composed of To:, CC:, and BCC: fields. |
  | message | object | yes | The message to be sent. |
  | replyToAddresses | array<string> | no | The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply. |
  | returnPath | string | no | The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the r... |
  | sourceArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specifie... |
  | returnPathArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in ... |
  | tags | any | no | A list of tags, in the form of name/value pairs, to apply to an email that you send using SendEmail. Tags correspond to characteristics of the email that you define, so that you can publish email s... |
  | configurationSetName | string | no | The name of the configuration set to use when you send an email using SendEmail. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MessageId | string | The unique message identifier returned from the SendEmail action. |


## com.datadoghq.aws.ses.sendTemplatedEmail
**Send templated email** — Composes an email message using an email template and immediately queues it for sending. To send email using this operation, your call must meet the following requirements: The call must refer to an existing email template. You can create email templates using the CreateTemplate operation. The message must be sent from a verified email address or domain. If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide. The maximum message size is 10 MB. Calls to the SendTemplatedEmail operation may only include one Destination parameter. A destination is a set of recipients that receives the same version of the email. The Destination parameter can include up to 50 recipients, across the To:, CC: and BCC: fields. The Destination parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message is rejected, even if the message contains other recipients that are valid. <important> If your call to the SendTemplatedEmail operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can't render the email because the template contains errors, it doesn't send the email. Additionally, because it already accepted the message, Amazon SES doesn't return a message stating that it was unable to send the email. For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see Sending Personalized Email Using the Amazon SES API in the Amazon Simple Email Service Developer Guide. </important>.
- Stability: stable
- Permissions: `ses:SendTemplatedEmail`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | source | string | yes | The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about ... |
  | destination | object | yes | The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields. |
  | replyToAddresses | array<string> | no | The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply. |
  | returnPath | string | no | The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the r... |
  | sourceArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specifie... |
  | returnPathArn | string | no | This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in ... |
  | tags | any | no | A list of tags, in the form of name/value pairs, to apply to an email that you send using SendTemplatedEmail. Tags correspond to characteristics of the email that you define, so that you can publis... |
  | configurationSetName | string | no | The name of the configuration set to use when you send an email using SendTemplatedEmail. |
  | template | string | yes | The template to use when sending this email. |
  | templateArn | string | no | The ARN of the template to use when sending this email. |
  | templateData | string | yes | A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MessageId | string | The unique message identifier returned from the SendTemplatedEmail             action. |


## com.datadoghq.aws.ses.updateTemplate
**Update template** — Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single operation. For more information, see the Amazon SES Developer Guide. You can execute this operation no more than once per second.
- Stability: stable
- Permissions: `ses:UpdateTemplate`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | template | object | yes | The content of the email, composed of a subject line and either an HTML part or a text-only part. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

