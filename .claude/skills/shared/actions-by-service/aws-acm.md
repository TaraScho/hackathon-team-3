# AWS Certificate Manager Actions
Bundle: `com.datadoghq.aws.acm` | 6 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eacm)

## com.datadoghq.aws.acm.deleteCertificate
**Delete certificate** — Delete a certificate and its associated private key.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | certificateARN | string | yes | The ARN of the ACM certificate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.acm.describeCertificate
**Describe certificate** — Return detailed metadata about the specified ACM certificate.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | certificateARN | string | yes | The ARN of the ACM certificate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | certificate | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.acm.listCertificates
**List certificates** — Retrieve a list of certificate ARNs and domain names.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | certificateStatuses | array<string> | no | Filter the certificate list by status value. |
  | limit | number | no | Number of items to return. |
  | nextToken | any | no | The pagination token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | certificateSummaryList | array<object> | A list of ACM certificates. |
  | nextToken | any | When the list is truncated, this value is present and contains the value to use for the NextToken parameter in a subsequent pagination request. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.acm.renewCertificate
**Renew certificate** — Renew an eligible certificate.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | certificateARN | string | yes | The ARN of the ACM certificate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.acm.requestPrivateCertificate
**Request private certificate** — Request a private certificate for use with other AWS services.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | Fully qualified domain name (FQDN) that you want to secure with an ACM certificate. |
  | certificateAuthorityARN | string | yes | ARN of the private certificate authority (CA) that will be used to issue the certificate. |
  | additionalDomainNames | array<string> | no | Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. |
  | tags | any | no | One or more resource tags to associate with the certificate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | certificateARN | string | String that contains the ARN of the issued certificate. This must be of the form:  arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012 |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.acm.requestPublicCertificate
**Request public certificate** — Request a public certificate for use with other AWS services with DNS validation.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | Fully qualified domain name (FQDN) that you want to secure with an ACM certificate. |
  | additionalDomainNames | array<string> | no | Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. |
  | tags | any | no | One or more resource tags to associate with the certificate. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | certificateARN | string | String that contains the ARN of the issued certificate. This must be of the form:  arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012 |
  | amzRequestId | string | The unique identifier for the request. |

