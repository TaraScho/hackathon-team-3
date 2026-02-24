# AWS Lambda Actions
Bundle: `com.datadoghq.aws.lambda` | 7 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Elambda)

## com.datadoghq.aws.lambda.createFunction
**Create function** — Creates a Lambda function. To create a function, you need a deployment package and an execution role.
- Stability: stable
- Permissions: `lambda:CreateFunction`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | yes | The name or ARN of the Lambda function. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. |
  | role | string | yes | The Amazon Resource Name (ARN) of the function's execution role. |
  | code | any | yes | Choose how to provide the code for the function. |
  | description | string | no | A description of the function. |
  | timeout | number | no | The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see Lambda executi... |
  | memorySize | number | no | The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB. |
  | publish | boolean | no | Set to true to publish the first version of the function during creation. |
  | vpcConfig | object | no | For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the i... |
  | deadLetterConfig | object | no | A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see Dead-letter queues. |
  | environment | object | no | Environment variables that are accessible from function code during execution. |
  | kmsKeyArn | string | no | The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's environment variables. When Lambda SnapStart is activated, Lambda also uses this key is to en... |
  | tracingConfig | object | no | Set Mode to Active to sample and trace a subset of incoming requests with X-Ray. |
  | tags | any | no | A list of tags to apply to the function. |
  | layers | array<string> | no | A list of function layers to add to the function's execution environment. Specify each layer by its ARN, including the version. |
  | fileSystemConfigs | array<object> | no | Connection settings for an Amazon EFS file system. |
  | codeSigningConfigArn | string | no | To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for t... |
  | architecture | string | no | The instruction set architecture that the function supports. The default value is x86_64. |
  | ephemeralStorage | object | no | The size of the function's /tmp directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see Configuring ephemeral storage (console). |
  | snapStart | object | no | The function's SnapStart setting. |
  | loggingConfig | object | no | The function's Amazon CloudWatch Logs configuration settings. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | FunctionName | string | The name of the function. |
  | FunctionArn | string | The function's Amazon Resource Name (ARN). |
  | Runtime | string | The identifier of the function's  runtime. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a cont... |
  | Role | string | The function's execution role. |
  | Handler | string | The function that Lambda calls to begin running your function. |
  | CodeSize | number | The size of the function's deployment package, in bytes. |
  | Description | string | The function's description. |
  | Timeout | number | The amount of time in seconds that Lambda allows a function to run before stopping it. |
  | MemorySize | number | The amount of memory available to the function at runtime. |
  | LastModified | string | The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD). |
  | CodeSha256 | string | The SHA256 hash of the function's deployment package. |
  | Version | string | The version of the Lambda function. |
  | VpcConfig | object | The function's networking configuration. |
  | DeadLetterConfig | object | The function's dead letter queue. |
  | Environment | object | The function's environment variables. Omitted from CloudTrail logs. |
  | KMSKeyArn | string | The KMS key that's used to encrypt the function's environment variables. When Lambda SnapStart is activated, this key is also used to encrypt the function's snapshot. This key is returned only if y... |
  | TracingConfig | object | The function's X-Ray tracing configuration. |
  | MasterArn | string | For Lambda@Edge functions, the ARN of the main function. |
  | RevisionId | string | The latest updated revision of the function or alias. |
  | Layers | array<object> | The function's layers. |
  | State | string | The current state of the function. When the state is Inactive, you can reactivate the function by invoking it. |
  | StateReason | string | The reason for the function's current state. |
  | StateReasonCode | string | The reason code for the function's current state. When the code is Creating, you can't invoke or modify the function. |
  | LastUpdateStatus | string | The status of the last update that was performed on the function. This is first set to Successful after function creation completes. |
  | LastUpdateStatusReason | string | The reason for the last update that was performed on the function. |
  | LastUpdateStatusReasonCode | string | The reason code for the last update that was performed on the function. |
  | FileSystemConfigs | array<object> | Connection settings for an Amazon EFS file system. |
  | PackageType | string | The type of deployment package. Set to Image for container image and set Zip for .zip file archive. |
  | ImageConfigResponse | object | The function's image configuration values. |
  | SigningProfileVersionArn | string | The ARN of the signing profile version. |
  | SigningJobArn | string | The ARN of the signing job. |
  | Architectures | array<string> | The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is x86_64. |
  | EphemeralStorage | object | The size of the function's /tmp directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see Configuring ephemeral storage (console). |
  | SnapStart | object | Set ApplyOn to PublishedVersions to create a snapshot of the initialized execution environment when you publish a function version. For more information, see Improving startup performance with Lamb... |
  | RuntimeVersionConfig | object | The ARN of the runtime and any errors that occured. |
  | LoggingConfig | object | The function's Amazon CloudWatch Logs configuration settings. |


## com.datadoghq.aws.lambda.deleteFunction
**Delete function** — Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted.
- Stability: stable
- Permissions: `lambda:DeleteFunction`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | yes | The name or ARN of the Lambda function or version.  Name formats     Function name – my-function (name-only), my-function:1 (with version).    Function ARN – arn:aws:lambda:us-west-2:123456789012:f... |
  | qualifier | string | no | Specify a version to delete. You can't delete a version that an alias references. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.lambda.getAWSLambdaExecution
**Get lambda execution history** — Get logs for the last execution of a specified Lambda function.
- Stability: stable
- Permissions: `logs:FilterLogEvents`, `logs:DescribeLogStreams`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | yes | The name of the Lambda function, version, or alias. This can only be the function name (`my-function`). |
  | executionCount | number | no |  |
  | logGroupName | string | no | Custom CloudWatch log group for your function. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | executions | array<object> |  |


## com.datadoghq.aws.lambda.getAWSLambdaFunction
**Describe function** — Get details about a function.
- Stability: stable
- Permissions: `lambda:GetFunction`, `lambda:GetFunctionCodeSigningConfig`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceId | string | yes | The name of the Lambda function, version, or alias. This can be the function name ("my-function"), name with alias ("my-function:v1"), ARN ("arn:aws:lambda:us-west-2:123456789012:function:my-functi... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | function | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.lambda.invoke_lambda
**Invoke lambda function** — Invoke a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously.
- Stability: stable
- Permissions: `lambda:InvokeFunction`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | yes | The name of the Lambda function, version, or alias. This can be the function name (`my-function`), name with alias (`my-function:v1`), ARN (`arn:aws:lambda:us-west-2:123456789012:function:my-functi... |
  | invocationType | string | no | The invocation type of the Lambda function. The default is `RequestResponse`, which invokes the function synchronously and includes the result in the action output. To invoke a function asynchronou... |
  | qualifier | string | no | An optional version or alias to invoke a published version of the function. |
  | inputPayload | any | no | The JSON to provide to a Lambda function as input. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | statusCode | number | The HTTP status code is in the 200 range for a successful request. For the `RequestResponse` invocation type, this status code is 200. For the `Event` invocation type, this status code is 202. For ... |
  | functionError | string | If present, indicates that an error occurred during function execution. Details about the error are included in the response payload. |
  | payload | any |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.lambda.listAWSLambdaFunction
**List functions** — List functions.
- Stability: stable
- Permissions: `lambda:ListFunctions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | no | Function name to filter results by. This will perform a basic case insensitive string search. |
  | limit | number | no | Numeric limit on results returned in List Lambda Functions response. Must be greater than or equal to 1 and less than or equal to 1250. If omitted, will default to 1250. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | functions | array<object> |  |


## com.datadoghq.aws.lambda.putFunctionConcurrency
**Put function concurrency** — Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level. Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use GetFunction to see the current setting for a function. Use GetAccountSettings to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren&#x27;t configured with a per-function limit. For more information, see Lambda function scaling.
- Stability: stable
- Permissions: `lambda:PutFunctionConcurrency`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | functionName | string | yes | The name or ARN of the Lambda function.  Name formats     Function name – my-function.    Function ARN – arn:aws:lambda:us-west-2:123456789012:function:my-function.    Partial ARN – 123456789012:fu... |
  | reservedConcurrentExecutions | number | yes | The number of simultaneous executions to reserve for the function. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ReservedConcurrentExecutions | number | The number of concurrent executions that are reserved for this function. For more information, see Managing Lambda reserved concurrency. |

