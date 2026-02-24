# AWS API Gateway Actions
Bundle: `com.datadoghq.aws.apigateway` | 117 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eapigateway)

## com.datadoghq.aws.apigateway.createAuthorizer
**Create authorizer** — Adds a new Authorizer resource to an existing RestApi resource.
- Stability: stable
- Permissions: `apigateway:CreateAuthorizer`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | name | string | yes | The name of the authorizer. |
  | type | string | yes | The authorizer type. Valid values are TOKEN for a Lambda function using a single authorization token submitted in a custom header, REQUEST for a Lambda function using incoming request parameters, a... |
  | providerARNs | array<string> | no | A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer. Each element is of this format: arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}. For a TOKEN or ... |
  | authType | string | no | Optional customer-defined field, used in OpenAPI imports and exports without functional impact. |
  | authorizerUri | string | no | Specifies the authorizer's Uniform Resource Identifier (URI). For TOKEN or REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path... |
  | authorizerCredentials | string | no | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resou... |
  | identitySource | string | no | The identity source for which authorization is requested. For a TOKEN or COGNITO_USER_POOLS authorizer, this is required and specifies the request header mapping expression for the custom header ho... |
  | identityValidationExpression | string | no | A validation expression for the incoming identity token. For TOKEN authorizers, this value is a regular expression. For COGNITO_USER_POOLS authorizers, API Gateway will match the aud field of the i... |
  | authorizerResultTtlInSeconds | number | no | The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, t... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the authorizer resource. |
  | name | string | The name of the authorizer. |
  | type | string | The authorizer type. Valid values are TOKEN for a Lambda function using a single authorization token submitted in a custom header, REQUEST for a Lambda function using incoming request parameters, a... |
  | providerARNs | array<string> | A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer. Each element is of this format: arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}. For a TOKEN or ... |
  | authType | string | Optional customer-defined field, used in OpenAPI imports and exports without functional impact. |
  | authorizerUri | string | Specifies the authorizer's Uniform Resource Identifier (URI). For TOKEN or REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path... |
  | authorizerCredentials | string | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resou... |
  | identitySource | string | The identity source for which authorization is requested. For a TOKEN or COGNITO_USER_POOLS authorizer, this is required and specifies the request header mapping expression for the custom header ho... |
  | identityValidationExpression | string | A validation expression for the incoming identity token. For TOKEN authorizers, this value is a regular expression. For COGNITO_USER_POOLS authorizers, API Gateway will match the aud field of the i... |
  | authorizerResultTtlInSeconds | number | The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, t... |


## com.datadoghq.aws.apigateway.createBasePathMapping
**Create base path mapping** — Creates a new BasePathMapping resource.
- Stability: stable
- Permissions: `apigateway:CreateBasePathMapping`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The domain name of the BasePathMapping resource to create. |
  | basePath | string | no | The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do n... |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stage | string | no | The name of the API's stage that you want to use for this mapping. Specify '(none)' if you want callers to explicitly specify the stage name after any base path name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | basePath | string | The base path name that callers of the API must provide as part of the URL after the domain name. |
  | restApiId | string | The string identifier of the associated RestApi. |
  | stage | string | The name of the associated stage. |


## com.datadoghq.aws.apigateway.createDeployment
**Create deployment** — Creates a Deployment resource, which makes a specified RestApi callable over the internet.
- Stability: stable
- Permissions: `apigateway:CreateDeployment`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | no | The name of the Stage resource for the Deployment resource to create. |
  | stageDescription | string | no | The description of the Stage resource for the Deployment resource to create. |
  | description | string | no | The description for the Deployment resource to create. |
  | cacheClusterEnabled | boolean | no | Enables a cache cluster for the Stage resource specified in the input. |
  | cacheClusterSize | string | no | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness. |
  | variables | object | no | A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match [... |
  | canarySettings | object | no | The input configuration for the canary deployment when the deployment is a canary release deployment. |
  | tracingEnabled | boolean | no | Specifies whether active tracing with X-ray is enabled for the Stage. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the deployment resource. |
  | description | string | The description for the deployment resource. |
  | createdDate | string | The date and time that the deployment resource was created. |
  | apiSummary | object | A summary of the RestApi at the date and time that the deployment resource was created. |


## com.datadoghq.aws.apigateway.createDocumentationPart
**Create documentation part** — Creates a documentation part.
- Stability: stable
- Permissions: `apigateway:CreateDocumentationPart`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | location | object | yes | The location of the targeted API entity of the to-be-created documentation part. |
  | properties | string | yes | The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The DocumentationPart identifier, generated by API Gateway when the DocumentationPart is created. |
  | location | object | The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, ... |
  | properties | string | A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only OpenAPI-compliant... |


## com.datadoghq.aws.apigateway.createDocumentationVersion
**Create documentation version** — Creates a documentation version.
- Stability: stable
- Permissions: `apigateway:CreateDocumentationVersion`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationVersion | string | yes | The version identifier of the new snapshot. |
  | stageName | string | no | The stage name to be associated with the new documentation snapshot. |
  | description | string | no | A description about the new documentation snapshot. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | version | string | The version identifier of the API documentation snapshot. |
  | createdDate | string | The date when the API documentation snapshot is created. |
  | description | string | The description of the API documentation snapshot. |


## com.datadoghq.aws.apigateway.createDomainName
**Create domain name** — Creates a new domain name.
- Stability: stable
- Permissions: `apigateway:CreateDomainName`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The name of the DomainName resource. |
  | certificateName | string | no | The user-friendly name of the certificate that will be used by edge-optimized endpoint for this domain name. |
  | certificateBody | string | no | [Deprecated] The body of the server certificate that will be used by edge-optimized endpoint for this domain name provided by your certificate authority. |
  | certificatePrivateKey | string | no | [Deprecated] Your edge-optimized endpoint's domain name certificate's private key. |
  | certificateChain | string | no | [Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines, used by an edge-optimized endpoint for this domain name. If you include ... |
  | certificateArn | string | no | The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint for this domain name. Certificate Manager is the only supported source. |
  | regionalCertificateName | string | no | The user-friendly name of the certificate that will be used by regional endpoint for this domain name. |
  | regionalCertificateArn | string | no | The reference to an Amazon Web Services-managed certificate that will be used by regional endpoint for this domain name. Certificate Manager is the only supported source. |
  | endpointConfiguration | object | no | The endpoint configuration of this DomainName showing the endpoint types of the domain name. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |
  | securityPolicy | string | no | The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are TLS_1_0 and TLS_1_2. |
  | mutualTlsAuthentication | object | no |  |
  | ownershipVerificationCertificateArn | string | no | The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | domainName | string | The custom domain name as an API host name, for example, my-api.example.com. |
  | certificateName | string | The name of the certificate that will be used by edge-optimized endpoint for this domain name. |
  | certificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint for this domain name. Certificate Manager is the only supported source. |
  | certificateUploadDate | string | The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded. |
  | regionalDomainName | string | The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name... |
  | regionalHostedZoneId | string | The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway. |
  | regionalCertificateName | string | The name of the certificate that will be used for validating the regional domain name. |
  | regionalCertificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source. |
  | distributionDomainName | string | The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custo... |
  | distributionHostedZoneId | string | The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is Z2FDTNDATAQYW2 for all the regions. For more information, see Set up a Regional Custom Domain N... |
  | endpointConfiguration | object | The endpoint configuration of this DomainName showing the endpoint types of the domain name. |
  | domainNameStatus | string | The status of the DomainName migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it... |
  | domainNameStatusMessage | string | An optional text message containing detailed information about status of the DomainName migration. |
  | securityPolicy | string | The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are TLS_1_0 and TLS_1_2. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | mutualTlsAuthentication | object | The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted cer... |
  | ownershipVerificationCertificateArn | string | The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the... |


## com.datadoghq.aws.apigateway.createModel
**Create model** — Adds a new Model resource to an existing RestApi resource.
- Stability: stable
- Permissions: `apigateway:CreateModel`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The RestApi identifier under which the Model will be created. |
  | name | string | yes | The name of the model. Must be alphanumeric. |
  | description | string | no | The description of the model. |
  | schema | string | no | The schema for the model. For application/json models, this should be JSON schema draft 4 model. The maximum size of the model is 400 KB. |
  | contentType | string | yes | The content-type for the model. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the model resource. |
  | name | string | The name of the model. Must be an alphanumeric string. |
  | description | string | The description of the model. |
  | schema | string | The schema for the model. For application/json models, this should be JSON schema draft 4 model. Do not include "\*" characters in the description of any properties because such "\*" characters may... |
  | contentType | string | The content-type for the model. |


## com.datadoghq.aws.apigateway.createRequestValidator
**Create request validator** — Creates a RequestValidator of a given RestApi.
- Stability: stable
- Permissions: `apigateway:CreateRequestValidator`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | name | string | no | The name of the to-be-created RequestValidator. |
  | validateRequestBody | boolean | no | A Boolean flag to indicate whether to validate request body according to the configured model schema for the method (true) or not (false). |
  | validateRequestParameters | boolean | no | A Boolean flag to indicate whether to validate request parameters, true, or not false. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of this RequestValidator. |
  | name | string | The name of this RequestValidator |
  | validateRequestBody | boolean | A Boolean flag to indicate whether to validate a request body according to the configured Model schema. |
  | validateRequestParameters | boolean | A Boolean flag to indicate whether to validate request parameters (true) or not (false). |


## com.datadoghq.aws.apigateway.createResource
**Create resource** — Creates a Resource resource.
- Stability: stable
- Permissions: `apigateway:CreateResource`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | parentId | string | yes | The parent resource's identifier. |
  | pathPart | string | yes | The last path segment for this resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The resource's identifier. |
  | parentId | string | The parent resource's identifier. |
  | pathPart | string | The last path segment for this resource. |
  | path | string | The full path for this resource. |
  | resourceMethods | object | Gets an API resource's method of a given HTTP verb. |


## com.datadoghq.aws.apigateway.createRestApi
**Create rest API** — Creates a new RestApi resource.
- Stability: stable
- Permissions: `apigateway:CreateRestApi`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the RestApi. |
  | description | string | no | The description of the RestApi. |
  | version | string | no | A version identifier for the API. |
  | cloneFrom | string | no | The ID of the RestApi that you want to clone from. |
  | binaryMediaTypes | array<string> | no | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | no | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | no | The source of the API key for metering requests according to a usage plan. Valid values are: HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from t... |
  | endpointConfiguration | object | no | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | no | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |
  | disableExecuteApiEndpoint | boolean | no | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The API's identifier. This identifier is unique across all of your APIs in API Gateway. |
  | name | string | The API's name. |
  | description | string | The API's description. |
  | createdDate | string | The timestamp when the API was created. |
  | version | string | A version identifier for the API. |
  | warnings | array<string> | The warning messages reported when failonwarnings is turned on during API import. |
  | binaryMediaTypes | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | The source of the API key for metering requests according to a usage plan. Valid values are: >HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from ... |
  | endpointConfiguration | object | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | disableExecuteApiEndpoint | boolean | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |
  | rootResourceId | string | The API's root resource ID. |


## com.datadoghq.aws.apigateway.createStage
**Create stage** — Creates a new Stage resource that references a pre-existing Deployment for the API.
- Stability: stable
- Permissions: `apigateway:CreateStage`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name for the Stage resource. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters. |
  | deploymentId | string | yes | The identifier of the Deployment resource for the Stage resource. |
  | description | string | no | The description of the Stage resource. |
  | cacheClusterEnabled | boolean | no | Whether cache clustering is enabled for the stage. |
  | cacheClusterSize | string | no | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness. |
  | variables | object | no | A map that defines the stage variables for the new Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+. |
  | documentationVersion | string | no | The version of the associated API documentation. |
  | canarySettings | object | no | The canary deployment settings of this stage. |
  | tracingEnabled | boolean | no | Specifies whether active tracing with X-ray is enabled for the Stage. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | deploymentId | string | The identifier of the Deployment that the stage points to. |
  | clientCertificateId | string | The identifier of a client certificate for an API stage. |
  | stageName | string | The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Ma... |
  | description | string | The stage's description. |
  | cacheClusterEnabled | boolean | Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set CachingEnabled to true for a method. |
  | cacheClusterSize | string | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness. |
  | cacheClusterStatus | string | The status of the cache cluster for the stage, if enabled. |
  | methodSettings | object | A map that defines the method settings for a Stage resource. Keys (designated as /{method_setting_key below) are method paths defined as {resource_path}/{http_method} for an individual method overr... |
  | variables | object | A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+. |
  | documentationVersion | string | The version of the associated API documentation. |
  | accessLogSettings | object | Settings for logging access in this stage. |
  | canarySettings | object | Settings for the canary deployment in this stage. |
  | tracingEnabled | boolean | Specifies whether active tracing with X-ray is enabled for the Stage. |
  | webAclArn | string | The ARN of the WebAcl associated with the Stage. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | createdDate | string | The timestamp when the stage was created. |
  | lastUpdatedDate | string | The timestamp when the stage last updated. |


## com.datadoghq.aws.apigateway.createUsagePlan
**Create usage plan** — Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload.
- Stability: stable
- Permissions: `apigateway:CreateUsagePlan`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the usage plan. |
  | description | string | no | The description of the usage plan. |
  | apiStages | array<object> | no | The associated API stages of the usage plan. |
  | throttle | object | no | The throttling limits of the usage plan. |
  | quota | object | no | The quota of the usage plan. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of a UsagePlan resource. |
  | name | string | The name of a usage plan. |
  | description | string | The description of a usage plan. |
  | apiStages | array<object> | The associated API stages of a usage plan. |
  | throttle | object | A map containing method level throttling information for API stage in a usage plan. |
  | quota | object | The target maximum number of permitted requests per a given unit time interval. |
  | productCode | string | The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.createUsagePlanKey
**Create usage plan key** — Creates a usage plan key for adding an existing API key to a usage plan.
- Stability: stable
- Permissions: `apigateway:CreateUsagePlanKey`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the UsagePlan resource representing the usage plan containing the to-be-created UsagePlanKey resource representing a plan customer. |
  | keyId | string | yes | The identifier of a UsagePlanKey resource for a plan customer. |
  | keyType | string | yes | The type of a UsagePlanKey resource for a plan customer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The Id of a usage plan key. |
  | type | string | The type of a usage plan key. Currently, the valid key type is API_KEY. |
  | value | string | The value of a usage plan key. |
  | name | string | The name of a usage plan key. |


## com.datadoghq.aws.apigateway.createVpcLink
**Create vpc link** — Creates a VPC link, under the caller&#x27;s account in a selected region, in an asynchronous operation that typically takes 2-4 minutes to complete and become operational. The caller must have permissions to create and update VPC Endpoint services.
- Stability: stable
- Permissions: `apigateway:CreateVpcLink`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name used to label and identify the VPC link. |
  | description | string | no | The description of the VPC link. |
  | targetArns | array<string> | yes | The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |
  | name | string | The name used to label and identify the VPC link. |
  | description | string | The description of the VPC link. |
  | targetArns | array<string> | The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner. |
  | status | string | The status of the VPC link. The valid values are AVAILABLE, PENDING, DELETING, or FAILED. Deploying an API will wait if the status is PENDING and will fail if the status is DELETING. |
  | statusMessage | string | A description about the VPC link status. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.deleteApiKey
**Delete API key** — Deletes the ApiKey resource.
- Stability: stable
- Permissions: `apigateway:DeleteApiKey`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | apiKey | string | yes | The identifier of the ApiKey resource to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteAuthorizer
**Delete authorizer** — Deletes an existing Authorizer resource.
- Stability: stable
- Permissions: `apigateway:DeleteAuthorizer`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | authorizerId | string | yes | The identifier of the Authorizer resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteBasePathMapping
**Delete base path mapping** — Deletes the BasePathMapping resource.
- Stability: stable
- Permissions: `apigateway:DeleteBasePathMapping`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The domain name of the BasePathMapping resource to delete. |
  | basePath | string | yes | The base path name of the BasePathMapping resource to delete. To specify an empty base path, set this parameter to '(none)'. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteClientCertificate
**Delete client certificate** — Deletes the ClientCertificate resource.
- Stability: stable
- Permissions: `apigateway:DeleteClientCertificate`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clientCertificateId | string | yes | The identifier of the ClientCertificate resource to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteDeployment
**Delete deployment** — Deletes a Deployment resource. Deleting a deployment will only succeed if there are no Stage resources associated with it.
- Stability: stable
- Permissions: `apigateway:DeleteDeployment`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | deploymentId | string | yes | The identifier of the Deployment resource to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteDocumentationPart
**Delete documentation part** — Deletes a documentation part.
- Stability: stable
- Permissions: `apigateway:DeleteDocumentationPart`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationPartId | string | yes | The identifier of the to-be-deleted documentation part. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteDocumentationVersion
**Delete documentation version** — Deletes a documentation version.
- Stability: stable
- Permissions: `apigateway:DeleteDocumentationVersion`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationVersion | string | yes | The version identifier of a to-be-deleted documentation snapshot. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteDomainName
**Delete domain name** — Deletes the DomainName resource.
- Stability: stable
- Permissions: `apigateway:DeleteDomainName`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The name of the DomainName resource to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteGatewayResponse
**Delete gateway response** — Clears any customization of a GatewayResponse of a specified response type on the given RestApi and resets it with the default settings.
- Stability: stable
- Permissions: `apigateway:DeleteGatewayResponse`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | responseType | string | yes | The response type of the associated GatewayResponse. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteIntegration
**Delete integration** — Represents a delete integration.
- Stability: stable
- Permissions: `apigateway:DeleteIntegration`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a delete integration request's resource identifier. |
  | httpMethod | string | yes | Specifies a delete integration request's HTTP method. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteIntegrationResponse
**Delete integration response** — Represents a delete integration response.
- Stability: stable
- Permissions: `apigateway:DeleteIntegrationResponse`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a delete integration response request's resource identifier. |
  | httpMethod | string | yes | Specifies a delete integration response request's HTTP method. |
  | statusCode | string | yes | Specifies a delete integration response request's status code. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteMethod
**Delete method** — Deletes an existing Method resource.
- Stability: stable
- Permissions: `apigateway:DeleteMethod`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the Method resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteMethodResponse
**Delete method response** — Deletes an existing MethodResponse resource.
- Stability: stable
- Permissions: `apigateway:DeleteMethodResponse`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the MethodResponse resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |
  | statusCode | string | yes | The status code identifier for the MethodResponse resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteModel
**Delete model** — Deletes a model.
- Stability: stable
- Permissions: `apigateway:DeleteModel`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | modelName | string | yes | The name of the model to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteRequestValidator
**Delete request validator** — Deletes a RequestValidator of a given RestApi.
- Stability: stable
- Permissions: `apigateway:DeleteRequestValidator`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | requestValidatorId | string | yes | The identifier of the RequestValidator to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteResource
**Delete resource** — Deletes a Resource resource.
- Stability: stable
- Permissions: `apigateway:DeleteResource`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The identifier of the Resource resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteRestApi
**Delete rest API** — Deletes the specified API.
- Stability: stable
- Permissions: `apigateway:DeleteRestApi`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteStage
**Delete stage** — Deletes a Stage resource.
- Stability: stable
- Permissions: `apigateway:DeleteStage`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the Stage resource to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteUsagePlan
**Delete usage plan** — Deletes a usage plan of a given plan Id.
- Stability: stable
- Permissions: `apigateway:DeleteUsagePlan`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the to-be-deleted usage plan. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteUsagePlanKey
**Delete usage plan key** — Deletes a usage plan key and remove the underlying API key from the associated usage plan.
- Stability: stable
- Permissions: `apigateway:DeleteUsagePlanKey`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the UsagePlan resource representing the usage plan containing the to-be-deleted UsagePlanKey resource representing a plan customer. |
  | keyId | string | yes | The Id of the UsagePlanKey resource to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.deleteVpcLink
**Delete vpc link** — Deletes an existing VpcLink of a specified identifier.
- Stability: stable
- Permissions: `apigateway:DeleteVpcLink`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | vpcLinkId | string | yes | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.flushStageAuthorizersCache
**Flush stage authorizers cache** — Flushes all authorizer cache entries on a stage.
- Stability: stable
- Permissions: `apigateway:FlushStageAuthorizersCache`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the stage to flush. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.flushStageCache
**Flush stage cache** — Flushes a stage&#x27;s cache.
- Stability: stable
- Permissions: `apigateway:FlushStageCache`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the stage to flush its cache. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.generateClientCertificate
**Generate client certificate** — Generates a ClientCertificate resource.
- Stability: stable
- Permissions: `apigateway:GenerateClientCertificate`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | description | string | no | The description of the ClientCertificate. |
  | tags | any | no | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clientCertificateId | string | The identifier of the client certificate. |
  | description | string | The description of the client certificate. |
  | pemEncodedCertificate | string | The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint . |
  | createdDate | string | The timestamp when the client certificate was created. |
  | expirationDate | string | The timestamp when the client certificate will expire. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.getAccount
**Get account** — Gets information about the current Account resource.
- Stability: stable
- Permissions: `apigateway:GetAccount`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | cloudwatchRoleArn | string | The ARN of an Amazon CloudWatch role for the current Account. |
  | throttleSettings | object | Specifies the API request limits configured for the current Account. |
  | features | array<string> | A list of features supported for the account. When usage plans are enabled, the features list will include an entry of "UsagePlans". |
  | apiKeyVersion | string | The version of the API keys used for the account. |


## com.datadoghq.aws.apigateway.getAuthorizer
**Get authorizer** — Describe an existing Authorizer resource.
- Stability: stable
- Permissions: `apigateway:GetAuthorizer`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | authorizerId | string | yes | The identifier of the Authorizer resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the authorizer resource. |
  | name | string | The name of the authorizer. |
  | type | string | The authorizer type. Valid values are TOKEN for a Lambda function using a single authorization token submitted in a custom header, REQUEST for a Lambda function using incoming request parameters, a... |
  | providerARNs | array<string> | A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer. Each element is of this format: arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}. For a TOKEN or ... |
  | authType | string | Optional customer-defined field, used in OpenAPI imports and exports without functional impact. |
  | authorizerUri | string | Specifies the authorizer's Uniform Resource Identifier (URI). For TOKEN or REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path... |
  | authorizerCredentials | string | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resou... |
  | identitySource | string | The identity source for which authorization is requested. For a TOKEN or COGNITO_USER_POOLS authorizer, this is required and specifies the request header mapping expression for the custom header ho... |
  | identityValidationExpression | string | A validation expression for the incoming identity token. For TOKEN authorizers, this value is a regular expression. For COGNITO_USER_POOLS authorizers, API Gateway will match the aud field of the i... |
  | authorizerResultTtlInSeconds | number | The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, t... |


## com.datadoghq.aws.apigateway.getAuthorizers
**Get authorizers** — Describe an existing Authorizers resource.
- Stability: stable
- Permissions: `apigateway:GetAuthorizers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getBasePathMapping
**Get base path mapping** — Describe a BasePathMapping resource.
- Stability: stable
- Permissions: `apigateway:GetBasePathMapping`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The domain name of the BasePathMapping resource to be described. |
  | basePath | string | yes | The base path name that callers of the API must provide as part of the URL after the domain name. This value must be unique for all of the mappings across a single API. Specify '(none)' if you do n... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | basePath | string | The base path name that callers of the API must provide as part of the URL after the domain name. |
  | restApiId | string | The string identifier of the associated RestApi. |
  | stage | string | The name of the associated stage. |


## com.datadoghq.aws.apigateway.getBasePathMappings
**Get base path mappings** — Represents a collection of BasePathMapping resources.
- Stability: stable
- Permissions: `apigateway:GetBasePathMappings`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The domain name of a BasePathMapping resource. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getClientCertificate
**Get client certificate** — Gets information about the current ClientCertificate resource.
- Stability: stable
- Permissions: `apigateway:GetClientCertificate`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clientCertificateId | string | yes | The identifier of the ClientCertificate resource to be described. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clientCertificateId | string | The identifier of the client certificate. |
  | description | string | The description of the client certificate. |
  | pemEncodedCertificate | string | The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint . |
  | createdDate | string | The timestamp when the client certificate was created. |
  | expirationDate | string | The timestamp when the client certificate will expire. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.getClientCertificates
**Get client certificates** — Gets a collection of ClientCertificate resources.
- Stability: stable
- Permissions: `apigateway:GetClientCertificates`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getDeployment
**Get deployment** — Gets information about a Deployment resource.
- Stability: stable
- Permissions: `apigateway:GetDeployment`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | deploymentId | string | yes | The identifier of the Deployment resource to get information about. |
  | embed | array<string> | no | A query parameter to retrieve the specified embedded resources of the returned Deployment resource in the response. In a REST API call, this embed parameter value is a list of comma-separated strin... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the deployment resource. |
  | description | string | The description for the deployment resource. |
  | createdDate | string | The date and time that the deployment resource was created. |
  | apiSummary | object | A summary of the RestApi at the date and time that the deployment resource was created. |


## com.datadoghq.aws.apigateway.getDeployments
**Get deployments** — Gets information about a Deployments collection.
- Stability: stable
- Permissions: `apigateway:GetDeployments`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getDocumentationPart
**Get documentation part** — Gets a documentation part.
- Stability: stable
- Permissions: `apigateway:GetDocumentationPart`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationPartId | string | yes | The string identifier of the associated RestApi. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The DocumentationPart identifier, generated by API Gateway when the DocumentationPart is created. |
  | location | object | The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, ... |
  | properties | string | A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only OpenAPI-compliant... |


## com.datadoghq.aws.apigateway.getDocumentationParts
**Get documentation parts** — Gets documentation parts.
- Stability: stable
- Permissions: `apigateway:GetDocumentationParts`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | type | string | no | The type of API entities of the to-be-retrieved documentation parts. |
  | nameQuery | string | no | The name of API entities of the to-be-retrieved documentation parts. |
  | path | string | no | The path of API entities of the to-be-retrieved documentation parts. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |
  | locationStatus | string | no | The status of the API documentation parts to retrieve. Valid values are DOCUMENTED for retrieving DocumentationPart resources with content and UNDOCUMENTED for DocumentationPart resources without c... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getDocumentationVersion
**Get documentation version** — Gets a documentation version.
- Stability: stable
- Permissions: `apigateway:GetDocumentationVersion`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationVersion | string | yes | The version identifier of the to-be-retrieved documentation snapshot. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | version | string | The version identifier of the API documentation snapshot. |
  | createdDate | string | The date when the API documentation snapshot is created. |
  | description | string | The description of the API documentation snapshot. |


## com.datadoghq.aws.apigateway.getDocumentationVersions
**Get documentation versions** — Gets documentation versions.
- Stability: stable
- Permissions: `apigateway:GetDocumentationVersions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getDomainName
**Get domain name** — Represents a domain name that is contained in a simpler, more intuitive URL that can be called.
- Stability: stable
- Permissions: `apigateway:GetDomainName`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The name of the DomainName resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | domainName | string | The custom domain name as an API host name, for example, my-api.example.com. |
  | certificateName | string | The name of the certificate that will be used by edge-optimized endpoint for this domain name. |
  | certificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint for this domain name. Certificate Manager is the only supported source. |
  | certificateUploadDate | string | The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded. |
  | regionalDomainName | string | The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name... |
  | regionalHostedZoneId | string | The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway. |
  | regionalCertificateName | string | The name of the certificate that will be used for validating the regional domain name. |
  | regionalCertificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source. |
  | distributionDomainName | string | The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custo... |
  | distributionHostedZoneId | string | The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is Z2FDTNDATAQYW2 for all the regions. For more information, see Set up a Regional Custom Domain N... |
  | endpointConfiguration | object | The endpoint configuration of this DomainName showing the endpoint types of the domain name. |
  | domainNameStatus | string | The status of the DomainName migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it... |
  | domainNameStatusMessage | string | An optional text message containing detailed information about status of the DomainName migration. |
  | securityPolicy | string | The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are TLS_1_0 and TLS_1_2. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | mutualTlsAuthentication | object | The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted cer... |
  | ownershipVerificationCertificateArn | string | The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the... |


## com.datadoghq.aws.apigateway.getDomainNames
**Get domain names** — Represents a collection of DomainName resources.
- Stability: stable
- Permissions: `apigateway:GetDomainNames`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getExport
**Get export** — Exports a deployed version of a RestApi in a specified format.
- Stability: stable
- Permissions: `apigateway:GetExport`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the Stage that will be exported. |
  | exportType | string | yes | The type of export. Acceptable values are 'oas30' for OpenAPI 3.0.x and 'swagger' for Swagger/OpenAPI 2.0. |
  | parameters | object | no | A key-value map of query string parameters that specify properties of the export, depending on the requested exportType. For exportType oas30 and swagger, any combination of the following parameter... |
  | accepts | string | no | The content-type of the export, for example application/json. Currently application/json and application/yaml are supported for exportType ofoas30 and swagger. This should be specified in the Accep... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | contentType | string | The content-type header value in the HTTP response. This will correspond to a valid 'accept' type in the request. |
  | contentDisposition | string | The content-disposition header value in the HTTP response. |
  | body | any | The binary blob response to GetExport, which contains the export. |


## com.datadoghq.aws.apigateway.getGatewayResponse
**Get gateway response** — Gets a GatewayResponse of a specified response type on the given RestApi.
- Stability: stable
- Permissions: `apigateway:GetGatewayResponse`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | responseType | string | yes | The response type of the associated GatewayResponse. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | responseType | string | The response type of the associated GatewayResponse. |
  | statusCode | string | The HTTP status code for this GatewayResponse. |
  | responseParameters | object | Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs. |
  | responseTemplates | object | Response templates of the GatewayResponse as a string-to-string map of key-value pairs. |
  | defaultResponse | boolean | A Boolean flag to indicate whether this GatewayResponse is the default gateway response (true) or not (false). A default gateway response is one generated by API Gateway without any customization b... |


## com.datadoghq.aws.apigateway.getGatewayResponses
**Get gateway responses** — Gets the GatewayResponses collection on the given RestApi. If an API developer has not added any definitions for gateway responses, the result will be the API Gateway-generated default GatewayResponses collection for the supported response types.
- Stability: stable
- Permissions: `apigateway:GetGatewayResponses`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. The GatewayResponse collection does not support pagination and the position does not apply here. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. The GatewayResponses collection does not support pagination and the limit does not apply here. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | Returns the entire collection, because of no pagination support. |


## com.datadoghq.aws.apigateway.getIntegration
**Get integration** — Get the integration settings.
- Stability: stable
- Permissions: `apigateway:GetIntegration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a get integration request's resource identifier |
  | httpMethod | string | yes | Specifies a get integration request's HTTP method. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | type | string | Specifies an API method integration type. The valid value is one of the following: For the HTTP and HTTP proxy integrations, each integration can specify a protocol (http/https), port and path. Sta... |
  | httpMethod | string | Specifies the integration's HTTP method type. For the Type property, if you specify MOCK, this property is optional. For Lambda integrations, you must set the integration method to POST. For all ot... |
  | uri | string | Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specifica... |
  | connectionType | string | The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gate... |
  | connectionId | string | The ID of the VpcLink used for the integration when connectionType=VPC_LINK and undefined, otherwise. |
  | credentials | string | Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource N... |
  | requestParameters | object | A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request ... |
  | requestTemplates | object | Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and t... |
  | passthroughBehavior | string | Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping tem... |
  | contentHandling | string | Specifies how to handle request payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the requ... |
  | timeoutInMillis | number | Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. |
  | cacheNamespace | string | Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the cacheNamespace. You can specify the same cacheNamespace across resources to return the same cache... |
  | cacheKeyParameters | array<string> | A list of request parameters whose values API Gateway caches. To be valid values for cacheKeyParameters, these parameters must also be specified for Method requestParameters. |
  | integrationResponses | object | Specifies the integration's responses. |
  | tlsConfig | object | Specifies the TLS configuration for an integration. |


## com.datadoghq.aws.apigateway.getIntegrationResponse
**Get integration response** — Represents a get integration response.
- Stability: stable
- Permissions: `apigateway:GetIntegrationResponse`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a get integration response request's resource identifier. |
  | httpMethod | string | yes | Specifies a get integration response request's HTTP method. |
  | statusCode | string | yes | Specifies a get integration response request's status code. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | Specifies the status code that is used to map the integration response to an existing MethodResponse. |
  | selectionPattern | string | Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error r... |
  | responseParameters | object | A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration re... |
  | responseTemplates | object | Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
  | contentHandling | string | Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the res... |


## com.datadoghq.aws.apigateway.getMethod
**Get method** — Describe an existing Method resource.
- Stability: stable
- Permissions: `apigateway:GetMethod`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the Method resource. |
  | httpMethod | string | yes | Specifies the method request's HTTP method type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | httpMethod | string | The method's HTTP verb. |
  | authorizationType | string | The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user p... |
  | authorizerId | string | The identifier of an Authorizer to use on this method. The authorizationType must be CUSTOM. |
  | apiKeyRequired | boolean | A boolean flag specifying whether a valid ApiKey is required to invoke this method. |
  | requestValidatorId | string | The identifier of a RequestValidator for request validation. |
  | operationName | string | A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in the PetStore example. |
  | requestParameters | object | A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of method.request.{locatio... |
  | requestModels | object | A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key). |
  | methodResponses | object | Gets a method response associated with a given HTTP status code. |
  | methodIntegration | object | Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end. |
  | authorizationScopes | array<string> | A list of authorization scopes configured on the method. The scopes are used with a COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by matching the method ... |


## com.datadoghq.aws.apigateway.getMethodResponse
**Get method response** — Describes a MethodResponse resource.
- Stability: stable
- Permissions: `apigateway:GetMethodResponse`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the MethodResponse resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |
  | statusCode | string | yes | The status code for the MethodResponse resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | The method response's status code. |
  | responseParameters | object | A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associat... |
  | responseModels | object | Specifies the Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a Model name as the value. |


## com.datadoghq.aws.apigateway.getModel
**Get model** — Describes an existing model defined for a RestApi resource.
- Stability: stable
- Permissions: `apigateway:GetModel`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The RestApi identifier under which the Model exists. |
  | modelName | string | yes | The name of the model as an identifier. |
  | flatten | boolean | no | A query parameter of a Boolean value to resolve (true) all external model references and returns a flattened model schema or not (false) The default is false. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the model resource. |
  | name | string | The name of the model. Must be an alphanumeric string. |
  | description | string | The description of the model. |
  | schema | string | The schema for the model. For application/json models, this should be JSON schema draft 4 model. Do not include "\*" characters in the description of any properties because such "\*" characters may... |
  | contentType | string | The content-type for the model. |


## com.datadoghq.aws.apigateway.getModelTemplate
**Get model template** — Generates a sample mapping template that can be used to transform a payload into the structure of a model.
- Stability: stable
- Permissions: `apigateway:GetModelTemplate`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | modelName | string | yes | The name of the model for which to generate a template. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | value | string | The Apache Velocity Template Language (VTL) template content used for the template resource. |


## com.datadoghq.aws.apigateway.getModels
**Get models** — Describes existing Models defined for a RestApi resource.
- Stability: stable
- Permissions: `apigateway:GetModels`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getRequestValidator
**Get request validator** — Gets a RequestValidator of a given RestApi.
- Stability: stable
- Permissions: `apigateway:GetRequestValidator`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | requestValidatorId | string | yes | The identifier of the RequestValidator to be retrieved. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of this RequestValidator. |
  | name | string | The name of this RequestValidator |
  | validateRequestBody | boolean | A Boolean flag to indicate whether to validate a request body according to the configured Model schema. |
  | validateRequestParameters | boolean | A Boolean flag to indicate whether to validate request parameters (true) or not (false). |


## com.datadoghq.aws.apigateway.getRequestValidators
**Get request validators** — Gets the RequestValidators collection of a given RestApi.
- Stability: stable
- Permissions: `apigateway:GetRequestValidators`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getResource
**Get resource** — Lists information about a resource.
- Stability: stable
- Permissions: `apigateway:GetResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The identifier for the Resource resource. |
  | embed | array<string> | no | A query parameter to retrieve the specified resources embedded in the returned Resource representation in the response. This embed parameter value is a list of comma-separated strings. Currently, t... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The resource's identifier. |
  | parentId | string | The parent resource's identifier. |
  | pathPart | string | The last path segment for this resource. |
  | path | string | The full path for this resource. |
  | resourceMethods | object | Gets an API resource's method of a given HTTP verb. |


## com.datadoghq.aws.apigateway.getResources
**Get resources** — Lists information about a collection of Resource resources.
- Stability: stable
- Permissions: `apigateway:GetResources`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |
  | embed | array<string> | no | A query parameter used to retrieve the specified resources embedded in the returned Resources resource in the response. This embed parameter value is a list of comma-separated strings. Currently, t... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getRestApi
**Get rest API** — Lists the RestApi resource in the collection.
- Stability: stable
- Permissions: `apigateway:GetRestApi`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The API's identifier. This identifier is unique across all of your APIs in API Gateway. |
  | name | string | The API's name. |
  | description | string | The API's description. |
  | createdDate | string | The timestamp when the API was created. |
  | version | string | A version identifier for the API. |
  | warnings | array<string> | The warning messages reported when failonwarnings is turned on during API import. |
  | binaryMediaTypes | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | The source of the API key for metering requests according to a usage plan. Valid values are: >HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from ... |
  | endpointConfiguration | object | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | disableExecuteApiEndpoint | boolean | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |
  | rootResourceId | string | The API's root resource ID. |


## com.datadoghq.aws.apigateway.getRestApis
**Get rest APIs** — Lists the RestApis resources for your collection.
- Stability: stable
- Permissions: `apigateway:GetRestApis`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getSdk
**Get sdk** — Generates a client SDK for a RestApi and Stage.
- Stability: stable
- Permissions: `apigateway:GetSdk`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the Stage that the SDK will use. |
  | sdkType | string | yes | The language for the generated SDK. Currently java, javascript, android, objectivec (for iOS), swift (for iOS), and ruby are supported. |
  | parameters | object | no | A string-to-string key-value map of query parameters sdkType-dependent properties of the SDK. For sdkType of objectivec or swift, a parameter named classPrefix is required. For sdkType of android, ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | contentType | string | The content-type header value in the HTTP response. |
  | contentDisposition | string | The content-disposition header value in the HTTP response. |
  | body | any | The binary blob response to GetSdk, which contains the generated SDK. |


## com.datadoghq.aws.apigateway.getSdkType
**Get sdk type** — Gets an SDK type.
- Stability: stable
- Permissions: `apigateway:GetSdkType`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | id | string | yes | The identifier of the queried SdkType instance. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of an SdkType instance. |
  | friendlyName | string | The user-friendly name of an SdkType instance. |
  | description | string | The description of an SdkType. |
  | configurationProperties | array<object> | A list of configuration properties of an SdkType. |


## com.datadoghq.aws.apigateway.getSdkTypes
**Get sdk types** — Gets SDK types.
- Stability: stable
- Permissions: `apigateway:GetSdkTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getStage
**Get stage** — Gets information about a Stage resource.
- Stability: stable
- Permissions: `apigateway:GetStage`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the Stage resource to get information about. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | deploymentId | string | The identifier of the Deployment that the stage points to. |
  | clientCertificateId | string | The identifier of a client certificate for an API stage. |
  | stageName | string | The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Ma... |
  | description | string | The stage's description. |
  | cacheClusterEnabled | boolean | Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set CachingEnabled to true for a method. |
  | cacheClusterSize | string | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness. |
  | cacheClusterStatus | string | The status of the cache cluster for the stage, if enabled. |
  | methodSettings | object | A map that defines the method settings for a Stage resource. Keys (designated as /{method_setting_key below) are method paths defined as {resource_path}/{http_method} for an individual method overr... |
  | variables | object | A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+. |
  | documentationVersion | string | The version of the associated API documentation. |
  | accessLogSettings | object | Settings for logging access in this stage. |
  | canarySettings | object | Settings for the canary deployment in this stage. |
  | tracingEnabled | boolean | Specifies whether active tracing with X-ray is enabled for the Stage. |
  | webAclArn | string | The ARN of the WebAcl associated with the Stage. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | createdDate | string | The timestamp when the stage was created. |
  | lastUpdatedDate | string | The timestamp when the stage last updated. |


## com.datadoghq.aws.apigateway.getStages
**Get stages** — Gets information about one or more Stage resources.
- Stability: stable
- Permissions: `apigateway:GetStages`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | deploymentId | string | no | The stages' deployment identifiers. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | item | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getTags
**Get tags** — Gets the Tags collection for a given resource.
- Stability: stable
- Permissions: `apigateway:GetTags`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The ARN of a resource that can be tagged. |
  | position | string | no | (Not currently supported) The current pagination position in the paged result set. |
  | limit | number | no | (Not currently supported) The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.getUsage
**Get usage** — Gets the usage data of a usage plan in a specified time interval.
- Stability: stable
- Permissions: `apigateway:GetUsage`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the usage plan associated with the usage data. |
  | keyId | string | no | The Id of the API key associated with the resultant usage data. |
  | startDate | string | yes | The starting date (e.g., 2016-01-01) of the usage data. |
  | endDate | string | yes | The ending date (e.g., 2016-12-31) of the usage data. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | usagePlanId | string | The plan Id associated with this usage data. |
  | startDate | string | The starting date of the usage data. |
  | endDate | string | The ending date of the usage data. |
  | position | string |  |
  | items | object | The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, {..., "values" : { "{api_key}" : [ [0, 100], [10... |


## com.datadoghq.aws.apigateway.getUsagePlan
**Get usage plan** — Gets a usage plan of a given plan identifier.
- Stability: stable
- Permissions: `apigateway:GetUsagePlan`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The identifier of the UsagePlan resource to be retrieved. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of a UsagePlan resource. |
  | name | string | The name of a usage plan. |
  | description | string | The description of a usage plan. |
  | apiStages | array<object> | The associated API stages of a usage plan. |
  | throttle | object | A map containing method level throttling information for API stage in a usage plan. |
  | quota | object | The target maximum number of permitted requests per a given unit time interval. |
  | productCode | string | The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.getUsagePlanKey
**Get usage plan key** — Gets a usage plan key of a given key identifier.
- Stability: stable
- Permissions: `apigateway:GetUsagePlanKey`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer. |
  | keyId | string | yes | The key Id of the to-be-retrieved UsagePlanKey resource representing a plan customer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The Id of a usage plan key. |
  | type | string | The type of a usage plan key. Currently, the valid key type is API_KEY. |
  | value | string | The value of a usage plan key. |
  | name | string | The name of a usage plan key. |


## com.datadoghq.aws.apigateway.getUsagePlanKeys
**Get usage plan keys** — Gets all the usage plan keys representing the API keys added to a specified usage plan.
- Stability: stable
- Permissions: `apigateway:GetUsagePlanKeys`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the UsagePlan resource representing the usage plan containing the to-be-retrieved UsagePlanKey resource representing a plan customer. |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |
  | nameQuery | string | no | A query parameter specifying the name of the to-be-returned usage plan keys. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getUsagePlans
**Get usage plans** — Gets all the usage plans of the caller&#x27;s account.
- Stability: stable
- Permissions: `apigateway:GetUsagePlans`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | keyId | string | no | The identifier of the API key associated with the usage plans. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.getVpcLink
**Get vpc link** — Gets a specified VPC link under the caller&#x27;s account in a region.
- Stability: stable
- Permissions: `apigateway:GetVpcLink`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | vpcLinkId | string | yes | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |
  | name | string | The name used to label and identify the VPC link. |
  | description | string | The description of the VPC link. |
  | targetArns | array<string> | The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner. |
  | status | string | The status of the VPC link. The valid values are AVAILABLE, PENDING, DELETING, or FAILED. Deploying an API will wait if the status is PENDING and will fail if the status is DELETING. |
  | statusMessage | string | A description about the VPC link status. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.getVpcLinks
**Get vpc links** — Gets the VpcLinks collection under the caller&#x27;s account in a selected region.
- Stability: stable
- Permissions: `apigateway:GetVpcLinks`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | position | string | no | The current pagination position in the paged result set. |
  | limit | number | no | The maximum number of returned results per page. The default value is 25 and the maximum value is 500. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | position | string |  |
  | items | array<object> | The current page of elements from this collection. |


## com.datadoghq.aws.apigateway.importApiKeys
**Import API keys** — Import API keys from an external source, such as a CSV-formatted file.
- Stability: stable
- Permissions: `apigateway:ImportApiKeys`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | body | any | yes | The payload of the POST request to import API keys. For the payload format, see API Key File Format. |
  | format | string | yes | A query parameter to specify the input format to imported API keys. Currently, only the csv format is supported. |
  | failOnWarnings | boolean | no | A query parameter to indicate whether to rollback ApiKey importation (true) or not (false) when error is encountered. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ids | array<string> | A list of all the ApiKey identifiers. |
  | warnings | array<string> | A list of warning messages. |


## com.datadoghq.aws.apigateway.importDocumentationParts
**Import documentation parts** — Imports documentation parts.
- Stability: stable
- Permissions: `apigateway:ImportDocumentationParts`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | mode | string | no | A query parameter to indicate whether to overwrite (overwrite) any existing DocumentationParts definition or to merge (merge) the new definition into the existing one. The default value is merge. |
  | failOnWarnings | boolean | no | A query parameter to specify whether to rollback the documentation importation (true) or not (false) when a warning is encountered. The default value is false. |
  | body | any | yes | Raw byte array representing the to-be-imported documentation parts. To import from an OpenAPI file, this is a JSON object. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ids | array<string> | A list of the returned documentation part identifiers. |
  | warnings | array<string> | A list of warning messages reported during import of documentation parts. |


## com.datadoghq.aws.apigateway.importRestApi
**Import rest API** — A feature of the API Gateway control service for creating a new API from an external API definition file.
- Stability: stable
- Permissions: `apigateway:ImportRestApi`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | failOnWarnings | boolean | no | A query parameter to indicate whether to rollback the API creation (true) or not (false) when a warning is encountered. The default value is false. |
  | parameters | object | no | A key-value map of context-specific query string parameters specifying the behavior of different API importing operations. The following shows operation-specific parameters and their supported valu... |
  | body | any | yes | The POST request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The API's identifier. This identifier is unique across all of your APIs in API Gateway. |
  | name | string | The API's name. |
  | description | string | The API's description. |
  | createdDate | string | The timestamp when the API was created. |
  | version | string | A version identifier for the API. |
  | warnings | array<string> | The warning messages reported when failonwarnings is turned on during API import. |
  | binaryMediaTypes | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | The source of the API key for metering requests according to a usage plan. Valid values are: >HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from ... |
  | endpointConfiguration | object | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | disableExecuteApiEndpoint | boolean | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |
  | rootResourceId | string | The API's root resource ID. |


## com.datadoghq.aws.apigateway.putGatewayResponse
**Put gateway response** — Creates a customization of a GatewayResponse of a specified response type and status code on the given RestApi.
- Stability: stable
- Permissions: `apigateway:PutGatewayResponse`
- Access: update, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | responseType | string | yes | The response type of the associated GatewayResponse |
  | statusCode | string | no | The HTTP status code of the GatewayResponse. |
  | responseParameters | object | no | Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs. |
  | responseTemplates | object | no | Response templates of the GatewayResponse as a string-to-string map of key-value pairs. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | responseType | string | The response type of the associated GatewayResponse. |
  | statusCode | string | The HTTP status code for this GatewayResponse. |
  | responseParameters | object | Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs. |
  | responseTemplates | object | Response templates of the GatewayResponse as a string-to-string map of key-value pairs. |
  | defaultResponse | boolean | A Boolean flag to indicate whether this GatewayResponse is the default gateway response (true) or not (false). A default gateway response is one generated by API Gateway without any customization b... |


## com.datadoghq.aws.apigateway.putIntegration
**Put integration** — Sets up a method&#x27;s integration.
- Stability: stable
- Permissions: `apigateway:PutIntegration`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a put integration request's resource ID. |
  | httpMethod | string | yes | Specifies the HTTP method for the integration. |
  | type | string | yes | Specifies a put integration input's type. |
  | integrationHttpMethod | string | no | The HTTP method for the integration. |
  | uri | string | no | Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specifica... |
  | connectionType | string | no | The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gate... |
  | connectionId | string | no | The ID of the VpcLink used for the integration. Specify this value only if you specify VPC_LINK as the connection type. |
  | credentials | string | no | Specifies whether credentials are required for a put integration. |
  | requestParameters | object | no | A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request ... |
  | requestTemplates | object | no | Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and t... |
  | passthroughBehavior | string | no | Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Inte... |
  | cacheNamespace | string | no | Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the cacheNamespace. You can specify the same cacheNamespace across resources to return the same cache... |
  | cacheKeyParameters | array<string> | no | A list of request parameters whose values API Gateway caches. To be valid values for cacheKeyParameters, these parameters must also be specified for Method requestParameters. |
  | contentHandling | string | no | Specifies how to handle request payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the requ... |
  | timeoutInMillis | number | no | Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. |
  | tlsConfig | object | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | type | string | Specifies an API method integration type. The valid value is one of the following: For the HTTP and HTTP proxy integrations, each integration can specify a protocol (http/https), port and path. Sta... |
  | httpMethod | string | Specifies the integration's HTTP method type. For the Type property, if you specify MOCK, this property is optional. For Lambda integrations, you must set the integration method to POST. For all ot... |
  | uri | string | Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specifica... |
  | connectionType | string | The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gate... |
  | connectionId | string | The ID of the VpcLink used for the integration when connectionType=VPC_LINK and undefined, otherwise. |
  | credentials | string | Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource N... |
  | requestParameters | object | A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request ... |
  | requestTemplates | object | Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and t... |
  | passthroughBehavior | string | Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping tem... |
  | contentHandling | string | Specifies how to handle request payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the requ... |
  | timeoutInMillis | number | Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. |
  | cacheNamespace | string | Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the cacheNamespace. You can specify the same cacheNamespace across resources to return the same cache... |
  | cacheKeyParameters | array<string> | A list of request parameters whose values API Gateway caches. To be valid values for cacheKeyParameters, these parameters must also be specified for Method requestParameters. |
  | integrationResponses | object | Specifies the integration's responses. |
  | tlsConfig | object | Specifies the TLS configuration for an integration. |


## com.datadoghq.aws.apigateway.putIntegrationResponse
**Put integration response** — Represents a put integration.
- Stability: stable
- Permissions: `apigateway:PutIntegrationResponse`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a put integration response request's resource identifier. |
  | httpMethod | string | yes | Specifies a put integration response request's HTTP method. |
  | statusCode | string | yes | Specifies the status code that is used to map the integration response to an existing MethodResponse. |
  | selectionPattern | string | no | Specifies the selection pattern of a put integration response. |
  | responseParameters | object | no | A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration re... |
  | responseTemplates | object | no | Specifies a put integration response's templates. |
  | contentHandling | string | no | Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the res... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | Specifies the status code that is used to map the integration response to an existing MethodResponse. |
  | selectionPattern | string | Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error r... |
  | responseParameters | object | A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration re... |
  | responseTemplates | object | Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
  | contentHandling | string | Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the res... |


## com.datadoghq.aws.apigateway.putMethod
**Put method** — Add a method to an existing Resource resource.
- Stability: stable
- Permissions: `apigateway:PutMethod`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the new Method resource. |
  | httpMethod | string | yes | Specifies the method request's HTTP method type. |
  | authorizationType | string | yes | The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user p... |
  | authorizerId | string | no | Specifies the identifier of an Authorizer to use on this Method, if the type is CUSTOM or COGNITO_USER_POOLS. The authorizer identifier is generated by API Gateway when you created the authorizer. |
  | apiKeyRequired | boolean | no | Specifies whether the method required a valid ApiKey. |
  | operationName | string | no | A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in the PetStore example. |
  | requestParameters | object | no | A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key defines a method request parameter name matching the pattern of method.request.{lo... |
  | requestModels | object | no | Specifies the Model resources used for the request's content type. Request models are represented as a key/value map, with a content type as the key and a Model name as the value. |
  | requestValidatorId | string | no | The identifier of a RequestValidator for validating the method request. |
  | authorizationScopes | array<string> | no | A list of authorization scopes configured on the method. The scopes are used with a COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by matching the method ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | httpMethod | string | The method's HTTP verb. |
  | authorizationType | string | The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user p... |
  | authorizerId | string | The identifier of an Authorizer to use on this method. The authorizationType must be CUSTOM. |
  | apiKeyRequired | boolean | A boolean flag specifying whether a valid ApiKey is required to invoke this method. |
  | requestValidatorId | string | The identifier of a RequestValidator for request validation. |
  | operationName | string | A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in the PetStore example. |
  | requestParameters | object | A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of method.request.{locatio... |
  | requestModels | object | A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key). |
  | methodResponses | object | Gets a method response associated with a given HTTP status code. |
  | methodIntegration | object | Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end. |
  | authorizationScopes | array<string> | A list of authorization scopes configured on the method. The scopes are used with a COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by matching the method ... |


## com.datadoghq.aws.apigateway.putMethodResponse
**Put method response** — Adds a MethodResponse to an existing Method resource.
- Stability: stable
- Permissions: `apigateway:PutMethodResponse`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the Method resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |
  | statusCode | string | yes | The method response's status code. |
  | responseParameters | object | no | A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header name and the associated value is a Boolean f... |
  | responseModels | object | no | Specifies the Model resources used for the response's content type. Response models are represented as a key/value map, with a content type as the key and a Model name as the value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | The method response's status code. |
  | responseParameters | object | A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associat... |
  | responseModels | object | Specifies the Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a Model name as the value. |


## com.datadoghq.aws.apigateway.putRestApi
**Put rest API** — A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.
- Stability: stable
- Permissions: `apigateway:PutRestApi`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | mode | string | no | The mode query parameter to specify the update mode. Valid values are "merge" and "overwrite". By default, the update mode is "merge". |
  | failOnWarnings | boolean | no | A query parameter to indicate whether to rollback the API update (true) or not (false) when a warning is encountered. The default value is false. |
  | parameters | object | no | Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set ignore=documentation as a parameters value, as in the AWS CLI command of aws ap... |
  | body | any | yes | The PUT request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The API's identifier. This identifier is unique across all of your APIs in API Gateway. |
  | name | string | The API's name. |
  | description | string | The API's description. |
  | createdDate | string | The timestamp when the API was created. |
  | version | string | A version identifier for the API. |
  | warnings | array<string> | The warning messages reported when failonwarnings is turned on during API import. |
  | binaryMediaTypes | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | The source of the API key for metering requests according to a usage plan. Valid values are: >HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from ... |
  | endpointConfiguration | object | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | disableExecuteApiEndpoint | boolean | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |
  | rootResourceId | string | The API's root resource ID. |


## com.datadoghq.aws.apigateway.tagResource
**Tag resource** — Adds or updates a tag on a given resource.
- Stability: stable
- Permissions: `apigateway:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The ARN of a resource that can be tagged. |
  | tags | any | yes | The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with aws:. The tag value can be up to 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.testInvokeAuthorizer
**Test invoke authorizer** — Simulate the execution of an Authorizer in your RestApi with headers, parameters, and an incoming request body.
- Stability: stable
- Permissions: `apigateway:TestInvokeAuthorizer`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | authorizerId | string | yes | Specifies a test invoke authorizer request's Authorizer ID. |
  | headers | object | no | A key-value map of headers to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, should be specified. |
  | multiValueHeaders | object | no | The headers as a map from string to list of values to simulate an incoming invocation request. This is where the incoming authorization token, or identity source, may be specified. |
  | pathWithQueryString | string | no | The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters. |
  | body | string | no | The simulated request body of an incoming invocation request. |
  | stageVariables | object | no | A key-value map of stage variables to simulate an invocation on a deployed Stage. |
  | additionalContext | object | no | A key-value map of additional context variables. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clientStatus | number | The HTTP status code that the client would have received. Value is 0 if the authorizer succeeded. |
  | log | string | The API Gateway execution log for the test authorizer request. |
  | latency | number | The execution latency, in ms, of the test authorizer request. |
  | principalId | string | The principal identity returned by the Authorizer |
  | policy | string | The JSON policy document returned by the Authorizer |
  | authorization | object | The authorization response. |
  | claims | object | The open identity claims, with any supported custom attributes, returned from the Cognito Your User Pool configured for the API. |


## com.datadoghq.aws.apigateway.testInvokeMethod
**Test invoke method** — Simulate the invocation of a Method in your RestApi with headers, parameters, and an incoming request body.
- Stability: stable
- Permissions: `apigateway:TestInvokeMethod`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies a test invoke method request's resource ID. |
  | httpMethod | string | yes | Specifies a test invoke method request's HTTP method. |
  | pathWithQueryString | string | no | The URI path, including query string, of the simulated invocation request. Use this to specify path parameters and query string parameters. |
  | body | string | no | The simulated request body of an incoming invocation request. |
  | headers | object | no | A key-value map of headers to simulate an incoming invocation request. |
  | multiValueHeaders | object | no | The headers as a map from string to list of values to simulate an incoming invocation request. |
  | clientCertificateId | string | no | A ClientCertificate identifier to use in the test invocation. API Gateway will use the certificate when making the HTTPS request to the defined back-end endpoint. |
  | stageVariables | object | no | A key-value map of stage variables to simulate an invocation on a deployed Stage. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | status | number | The HTTP status code. |
  | body | string | The body of the HTTP response. |
  | headers | object | The headers of the HTTP response. |
  | multiValueHeaders | object | The headers of the HTTP response as a map from string to list of values. |
  | log | string | The API Gateway execution log for the test invoke request. |
  | latency | number | The execution latency, in ms, of the test invoke request. |


## com.datadoghq.aws.apigateway.untagResource
**Untag resource** — Removes a tag from a given resource.
- Stability: stable
- Permissions: `apigateway:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The ARN of a resource that can be tagged. |
  | tagKeys | array<string> | yes | The Tag keys to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.apigateway.updateAccount
**Update account** — Changes information about the current Account resource.
- Stability: stable
- Permissions: `apigateway:UpdateAccount`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | cloudwatchRoleArn | string | The ARN of an Amazon CloudWatch role for the current Account. |
  | throttleSettings | object | Specifies the API request limits configured for the current Account. |
  | features | array<string> | A list of features supported for the account. When usage plans are enabled, the features list will include an entry of "UsagePlans". |
  | apiKeyVersion | string | The version of the API keys used for the account. |


## com.datadoghq.aws.apigateway.updateApiKey
**Update API key** — Changes information about an ApiKey resource.
- Stability: stable
- Permissions: `apigateway:UpdateApiKey`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | apiKey | string | yes | The identifier of the ApiKey resource to be updated. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of the API Key. |
  | value | string | The value of the API Key. |
  | name | string | The name of the API Key. |
  | customerId | string | An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace. |
  | description | string | The description of the API Key. |
  | enabled | boolean | Specifies whether the API Key can be used by callers. |
  | createdDate | string | The timestamp when the API Key was created. |
  | lastUpdatedDate | string | The timestamp when the API Key was last updated. |
  | stageKeys | array<string> | A list of Stage resources that are associated with the ApiKey resource. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.updateAuthorizer
**Update authorizer** — Updates an existing Authorizer resource.
- Stability: stable
- Permissions: `apigateway:UpdateAuthorizer`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | authorizerId | string | yes | The identifier of the Authorizer resource. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the authorizer resource. |
  | name | string | The name of the authorizer. |
  | type | string | The authorizer type. Valid values are TOKEN for a Lambda function using a single authorization token submitted in a custom header, REQUEST for a Lambda function using incoming request parameters, a... |
  | providerARNs | array<string> | A list of the Amazon Cognito user pool ARNs for the COGNITO_USER_POOLS authorizer. Each element is of this format: arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}. For a TOKEN or ... |
  | authType | string | Optional customer-defined field, used in OpenAPI imports and exports without functional impact. |
  | authorizerUri | string | Specifies the authorizer's Uniform Resource Identifier (URI). For TOKEN or REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path... |
  | authorizerCredentials | string | Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resou... |
  | identitySource | string | The identity source for which authorization is requested. For a TOKEN or COGNITO_USER_POOLS authorizer, this is required and specifies the request header mapping expression for the custom header ho... |
  | identityValidationExpression | string | A validation expression for the incoming identity token. For TOKEN authorizers, this value is a regular expression. For COGNITO_USER_POOLS authorizers, API Gateway will match the aud field of the i... |
  | authorizerResultTtlInSeconds | number | The TTL in seconds of cached authorizer results. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway will cache authorizer responses. If this field is not set, t... |


## com.datadoghq.aws.apigateway.updateBasePathMapping
**Update base path mapping** — Changes information about the BasePathMapping resource.
- Stability: stable
- Permissions: `apigateway:UpdateBasePathMapping`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The domain name of the BasePathMapping resource to change. |
  | basePath | string | yes | The base path of the BasePathMapping resource to change. To specify an empty base path, set this parameter to '(none)'. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | basePath | string | The base path name that callers of the API must provide as part of the URL after the domain name. |
  | restApiId | string | The string identifier of the associated RestApi. |
  | stage | string | The name of the associated stage. |


## com.datadoghq.aws.apigateway.updateClientCertificate
**Update client certificate** — Changes information about an ClientCertificate resource.
- Stability: stable
- Permissions: `apigateway:UpdateClientCertificate`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | clientCertificateId | string | yes | The identifier of the ClientCertificate resource to be updated. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | clientCertificateId | string | The identifier of the client certificate. |
  | description | string | The description of the client certificate. |
  | pemEncodedCertificate | string | The PEM-encoded public key of the client certificate, which can be used to configure certificate authentication in the integration endpoint . |
  | createdDate | string | The timestamp when the client certificate was created. |
  | expirationDate | string | The timestamp when the client certificate will expire. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.updateDeployment
**Update deployment** — Changes information about a Deployment resource.
- Stability: stable
- Permissions: `apigateway:UpdateDeployment`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | deploymentId | string | yes | The replacement identifier for the Deployment resource to change information about. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the deployment resource. |
  | description | string | The description for the deployment resource. |
  | createdDate | string | The date and time that the deployment resource was created. |
  | apiSummary | object | A summary of the RestApi at the date and time that the deployment resource was created. |


## com.datadoghq.aws.apigateway.updateDocumentationPart
**Update documentation part** — Updates a documentation part.
- Stability: stable
- Permissions: `apigateway:UpdateDocumentationPart`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationPartId | string | yes | The identifier of the to-be-updated documentation part. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The DocumentationPart identifier, generated by API Gateway when the DocumentationPart is created. |
  | location | object | The location of the API entity to which the documentation applies. Valid fields depend on the targeted API entity type. All the valid location fields are not required. If not explicitly specified, ... |
  | properties | string | A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only OpenAPI-compliant... |


## com.datadoghq.aws.apigateway.updateDocumentationVersion
**Update documentation version** — Updates a documentation version.
- Stability: stable
- Permissions: `apigateway:UpdateDocumentationVersion`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | documentationVersion | string | yes | The version identifier of the to-be-updated documentation version. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | version | string | The version identifier of the API documentation snapshot. |
  | createdDate | string | The date when the API documentation snapshot is created. |
  | description | string | The description of the API documentation snapshot. |


## com.datadoghq.aws.apigateway.updateDomainName
**Update domain name** — Changes information about the DomainName resource.
- Stability: stable
- Permissions: `apigateway:UpdateDomainName`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | domainName | string | yes | The name of the DomainName resource to be changed. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | domainName | string | The custom domain name as an API host name, for example, my-api.example.com. |
  | certificateName | string | The name of the certificate that will be used by edge-optimized endpoint for this domain name. |
  | certificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint for this domain name. Certificate Manager is the only supported source. |
  | certificateUploadDate | string | The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded. |
  | regionalDomainName | string | The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name... |
  | regionalHostedZoneId | string | The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway. |
  | regionalCertificateName | string | The name of the certificate that will be used for validating the regional domain name. |
  | regionalCertificateArn | string | The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source. |
  | distributionDomainName | string | The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custo... |
  | distributionHostedZoneId | string | The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is Z2FDTNDATAQYW2 for all the regions. For more information, see Set up a Regional Custom Domain N... |
  | endpointConfiguration | object | The endpoint configuration of this DomainName showing the endpoint types of the domain name. |
  | domainNameStatus | string | The status of the DomainName migration. The valid values are AVAILABLE and UPDATING. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it... |
  | domainNameStatusMessage | string | An optional text message containing detailed information about status of the DomainName migration. |
  | securityPolicy | string | The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are TLS_1_0 and TLS_1_2. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | mutualTlsAuthentication | object | The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted cer... |
  | ownershipVerificationCertificateArn | string | The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the... |


## com.datadoghq.aws.apigateway.updateGatewayResponse
**Update gateway response** — Updates a GatewayResponse of a specified response type on the given RestApi.
- Stability: stable
- Permissions: `apigateway:UpdateGatewayResponse`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | responseType | string | yes | The response type of the associated GatewayResponse. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | responseType | string | The response type of the associated GatewayResponse. |
  | statusCode | string | The HTTP status code for this GatewayResponse. |
  | responseParameters | object | Response parameters (paths, query strings and headers) of the GatewayResponse as a string-to-string map of key-value pairs. |
  | responseTemplates | object | Response templates of the GatewayResponse as a string-to-string map of key-value pairs. |
  | defaultResponse | boolean | A Boolean flag to indicate whether this GatewayResponse is the default gateway response (true) or not (false). A default gateway response is one generated by API Gateway without any customization b... |


## com.datadoghq.aws.apigateway.updateIntegration
**Update integration** — Represents an update integration.
- Stability: stable
- Permissions: `apigateway:UpdateIntegration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Represents an update integration request's resource identifier. |
  | httpMethod | string | yes | Represents an update integration request's HTTP method. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | type | string | Specifies an API method integration type. The valid value is one of the following: For the HTTP and HTTP proxy integrations, each integration can specify a protocol (http/https), port and path. Sta... |
  | httpMethod | string | Specifies the integration's HTTP method type. For the Type property, if you specify MOCK, this property is optional. For Lambda integrations, you must set the integration method to POST. For all ot... |
  | uri | string | Specifies Uniform Resource Identifier (URI) of the integration endpoint. For HTTP or HTTP_PROXY integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specifica... |
  | connectionType | string | The type of the network connection to the integration endpoint. The valid value is INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gate... |
  | connectionId | string | The ID of the VpcLink used for the integration when connectionType=VPC_LINK and undefined, otherwise. |
  | credentials | string | Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource N... |
  | requestParameters | object | A key-value map specifying request parameters that are passed from the method request to the back end. The key is an integration request parameter name and the associated value is a method request ... |
  | requestTemplates | object | Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and t... |
  | passthroughBehavior | string | Specifies how the method request body of an unmapped content type will be passed through the integration request to the back end without transformation. A content type is unmapped if no mapping tem... |
  | contentHandling | string | Specifies how to handle request payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the requ... |
  | timeoutInMillis | number | Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds. |
  | cacheNamespace | string | Specifies a group of related cached parameters. By default, API Gateway uses the resource ID as the cacheNamespace. You can specify the same cacheNamespace across resources to return the same cache... |
  | cacheKeyParameters | array<string> | A list of request parameters whose values API Gateway caches. To be valid values for cacheKeyParameters, these parameters must also be specified for Method requestParameters. |
  | integrationResponses | object | Specifies the integration's responses. |
  | tlsConfig | object | Specifies the TLS configuration for an integration. |


## com.datadoghq.aws.apigateway.updateIntegrationResponse
**Update integration response** — Represents an update integration response.
- Stability: stable
- Permissions: `apigateway:UpdateIntegrationResponse`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | Specifies an update integration response request's resource identifier. |
  | httpMethod | string | yes | Specifies an update integration response request's HTTP method. |
  | statusCode | string | yes | Specifies an update integration response request's status code. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | Specifies the status code that is used to map the integration response to an existing MethodResponse. |
  | selectionPattern | string | Specifies the regular expression (regex) pattern used to choose an integration response based on the response from the back end. For example, if the success response returns nothing and the error r... |
  | responseParameters | object | A key-value map specifying response parameters that are passed to the method response from the back end. The key is a method response header parameter name and the mapped value is an integration re... |
  | responseTemplates | object | Specifies the templates used to transform the integration response body. Response templates are represented as a key/value map, with a content-type as the key and a template as the value. |
  | contentHandling | string | Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors: If this property is not defined, the res... |


## com.datadoghq.aws.apigateway.updateMethod
**Update method** — Updates an existing Method resource.
- Stability: stable
- Permissions: `apigateway:UpdateMethod`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the Method resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | httpMethod | string | The method's HTTP verb. |
  | authorizationType | string | The method's authorization type. Valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, CUSTOM for using a custom authorizer, or COGNITO_USER_POOLS for using a Cognito user p... |
  | authorizerId | string | The identifier of an Authorizer to use on this method. The authorizationType must be CUSTOM. |
  | apiKeyRequired | boolean | A boolean flag specifying whether a valid ApiKey is required to invoke this method. |
  | requestValidatorId | string | The identifier of a RequestValidator for request validation. |
  | operationName | string | A human-friendly operation identifier for the method. For example, you can assign the operationName of ListPets for the GET /pets method in the PetStore example. |
  | requestParameters | object | A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of method.request.{locatio... |
  | requestModels | object | A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key). |
  | methodResponses | object | Gets a method response associated with a given HTTP status code. |
  | methodIntegration | object | Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end. |
  | authorizationScopes | array<string> | A list of authorization scopes configured on the method. The scopes are used with a COGNITO_USER_POOLS authorizer to authorize the method invocation. The authorization works by matching the method ... |


## com.datadoghq.aws.apigateway.updateMethodResponse
**Update method response** — Updates an existing MethodResponse resource.
- Stability: stable
- Permissions: `apigateway:UpdateMethodResponse`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The Resource identifier for the MethodResponse resource. |
  | httpMethod | string | yes | The HTTP verb of the Method resource. |
  | statusCode | string | yes | The status code for the MethodResponse resource. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | statusCode | string | The method response's status code. |
  | responseParameters | object | A key-value map specifying required or optional response parameters that API Gateway can send back to the caller. A key defines a method response header and the value specifies whether the associat... |
  | responseModels | object | Specifies the Model resources used for the response's content-type. Response models are represented as a key/value map, with a content-type as the key and a Model name as the value. |


## com.datadoghq.aws.apigateway.updateModel
**Update model** — Changes information about a model. The maximum size of the model is 400 KB.
- Stability: stable
- Permissions: `apigateway:UpdateModel`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | modelName | string | yes | The name of the model to update. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier for the model resource. |
  | name | string | The name of the model. Must be an alphanumeric string. |
  | description | string | The description of the model. |
  | schema | string | The schema for the model. For application/json models, this should be JSON schema draft 4 model. Do not include "\*" characters in the description of any properties because such "\*" characters may... |
  | contentType | string | The content-type for the model. |


## com.datadoghq.aws.apigateway.updateRequestValidator
**Update request validator** — Updates a RequestValidator of a given RestApi.
- Stability: stable
- Permissions: `apigateway:UpdateRequestValidator`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | requestValidatorId | string | yes | The identifier of RequestValidator to be updated. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of this RequestValidator. |
  | name | string | The name of this RequestValidator |
  | validateRequestBody | boolean | A Boolean flag to indicate whether to validate a request body according to the configured Model schema. |
  | validateRequestParameters | boolean | A Boolean flag to indicate whether to validate request parameters (true) or not (false). |


## com.datadoghq.aws.apigateway.updateResource
**Update resource** — Changes information about a Resource resource.
- Stability: stable
- Permissions: `apigateway:UpdateResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | resourceId | string | yes | The identifier of the Resource resource. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The resource's identifier. |
  | parentId | string | The parent resource's identifier. |
  | pathPart | string | The last path segment for this resource. |
  | path | string | The full path for this resource. |
  | resourceMethods | object | Gets an API resource's method of a given HTTP verb. |


## com.datadoghq.aws.apigateway.updateRestApi
**Update rest API** — Changes information about the specified API.
- Stability: stable
- Permissions: `apigateway:UpdateRestApi`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The API's identifier. This identifier is unique across all of your APIs in API Gateway. |
  | name | string | The API's name. |
  | description | string | The API's description. |
  | createdDate | string | The timestamp when the API was created. |
  | version | string | A version identifier for the API. |
  | warnings | array<string> | The warning messages reported when failonwarnings is turned on during API import. |
  | binaryMediaTypes | array<string> | The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads. |
  | minimumCompressionSize | number | A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is ena... |
  | apiKeySource | string | The source of the API key for metering requests according to a usage plan. Valid values are: >HEADER to read the API key from the X-API-Key header of a request. AUTHORIZER to read the API key from ... |
  | endpointConfiguration | object | The endpoint configuration of this RestApi showing the endpoint types of the API. |
  | policy | string | A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | disableExecuteApiEndpoint | boolean | Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com... |
  | rootResourceId | string | The API's root resource ID. |


## com.datadoghq.aws.apigateway.updateStage
**Update stage** — Changes information about a Stage resource.
- Stability: stable
- Permissions: `apigateway:UpdateStage`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | restApiId | string | yes | The string identifier of the associated RestApi. |
  | stageName | string | yes | The name of the Stage resource to change information about. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | deploymentId | string | The identifier of the Deployment that the stage points to. |
  | clientCertificateId | string | The identifier of a client certificate for an API stage. |
  | stageName | string | The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Ma... |
  | description | string | The stage's description. |
  | cacheClusterEnabled | boolean | Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set CachingEnabled to true for a method. |
  | cacheClusterSize | string | The stage's cache capacity in GB. For more information about choosing a cache size, see Enabling API caching to enhance responsiveness. |
  | cacheClusterStatus | string | The status of the cache cluster for the stage, if enabled. |
  | methodSettings | object | A map that defines the method settings for a Stage resource. Keys (designated as /{method_setting_key below) are method paths defined as {resource_path}/{http_method} for an individual method overr... |
  | variables | object | A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+. |
  | documentationVersion | string | The version of the associated API documentation. |
  | accessLogSettings | object | Settings for logging access in this stage. |
  | canarySettings | object | Settings for the canary deployment in this stage. |
  | tracingEnabled | boolean | Specifies whether active tracing with X-ray is enabled for the Stage. |
  | webAclArn | string | The ARN of the WebAcl associated with the Stage. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |
  | createdDate | string | The timestamp when the stage was created. |
  | lastUpdatedDate | string | The timestamp when the stage last updated. |


## com.datadoghq.aws.apigateway.updateUsage
**Update usage** — Grants a temporary extension to the remaining quota of a usage plan associated with a specified API key.
- Stability: stable
- Permissions: `apigateway:UpdateUsage`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the usage plan associated with the usage data. |
  | keyId | string | yes | The identifier of the API key associated with the usage plan in which a temporary extension is granted to the remaining quota. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | usagePlanId | string | The plan Id associated with this usage data. |
  | startDate | string | The starting date of the usage data. |
  | endDate | string | The ending date of the usage data. |
  | position | string |  |
  | items | object | The usage data, as daily logs of used and remaining quotas, over the specified time interval indexed over the API keys in a usage plan. For example, {..., "values" : { "{api_key}" : [ [0, 100], [10... |


## com.datadoghq.aws.apigateway.updateUsagePlan
**Update usage plan** — Updates a usage plan of a given plan Id.
- Stability: stable
- Permissions: `apigateway:UpdateUsagePlan`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | usagePlanId | string | yes | The Id of the to-be-updated usage plan. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of a UsagePlan resource. |
  | name | string | The name of a usage plan. |
  | description | string | The description of a usage plan. |
  | apiStages | array<object> | The associated API stages of a usage plan. |
  | throttle | object | A map containing method level throttling information for API stage in a usage plan. |
  | quota | object | The target maximum number of permitted requests per a given unit time interval. |
  | productCode | string | The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |


## com.datadoghq.aws.apigateway.updateVpcLink
**Update vpc link** — Updates an existing VpcLink of a specified identifier.
- Stability: stable
- Permissions: `apigateway:UpdateVpcLink`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | vpcLinkId | string | yes | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |
  | patchOperations | array<object> | no | For more information about supported patch operations, see Patch Operations. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | id | string | The identifier of the VpcLink. It is used in an Integration to reference this VpcLink. |
  | name | string | The name used to label and identify the VPC link. |
  | description | string | The description of the VPC link. |
  | targetArns | array<string> | The ARN of the network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same Amazon Web Services account of the API owner. |
  | status | string | The status of the VPC link. The valid values are AVAILABLE, PENDING, DELETING, or FAILED. Deploying an API will wait if the status is PENDING and will fail if the status is DELETING. |
  | statusMessage | string | A description about the VPC link status. |
  | tags | object | The collection of tags. Each tag element is associated with a given resource. |

