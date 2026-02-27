# AWS Bedrock Actions
Bundle: `com.datadoghq.aws.bedrock` | 43 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ebedrock)

## com.datadoghq.aws.bedrock.batchDeleteEvaluationJob
**Batch delete evaluation job** — Creates a batch deletion job.
- Stability: stable
- Permissions: `bedrock:BatchDeleteEvaluationJob`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifiers | array<string> | yes | An array of model evaluation job ARNs to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | errors | array<object> | A JSON object containing the HTTP status codes and the ARNs of model evaluation jobs that failed to be deleted. |
  | evaluationJobs | array<object> | The list of model evaluation jobs to be deleted. |


## com.datadoghq.aws.bedrock.createEvaluationJob
**Create evaluation job** — API operation for creating and managing Amazon Bedrock automatic model evaluation jobs, as well as model evaluation jobs that use human workers.
- Stability: stable
- Permissions: `bedrock:CreateEvaluationJob`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the model evaluation job. Model evaluation job names must unique with your AWS account, and your account's AWS region. |
  | jobDescription | string | no | A description of the model evaluation job. |
  | clientRequestToken | string | no | A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return... |
  | roleArn | string | yes | The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. The service role must have Amazon Bedrock as the service principal, and provide... |
  | customerEncryptionKeyId | string | no | Specify your customer managed key ARN that will be used to encrypt your model evaluation job. |
  | jobTags | array<object> | no | Tags to attach to the model evaluation job. |
  | evaluationConfig | object | yes | Specifies whether the model evaluation job is automatic or uses human worker. |
  | inferenceConfig | object | yes | Specify the models you want to use in your model evaluation job. Automatic model evaluation jobs support a single model, and model evaluation job that use human workers support two models. |
  | outputDataConfig | object | yes | An object that defines where the results of model evaluation job will be saved in Amazon S3. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The ARN of the model evaluation job. |


## com.datadoghq.aws.bedrock.createGuardrailVersion
**Create guardrail version** — Creates a version of the guardrail.
- Stability: stable
- Permissions: `bedrock:CreateGuardrailVersion`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | guardrailIdentifier | string | yes | The unique identifier of the guardrail. This can be an ID or the ARN. |
  | description | string | no | A description of the guardrail version. |
  | clientRequestToken | string | no | A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | guardrailId | string | The unique identifier of the guardrail. |
  | version | string | The number of the version of the guardrail. |


## com.datadoghq.aws.bedrock.createModelCopyJob
**Create model copy job** — Copies a model to another region to enable its use there.
- Stability: stable
- Permissions: `bedrock:CreateModelCopyJob`
- Access: create, read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceModelArn | string | yes | The Amazon Resource Name (ARN) of the model to be copied. |
  | targetModelName | string | yes | A name for the copied model. |
  | modelKmsKeyId | string | no | The ARN of the KMS key that you use to encrypt the model copy. |
  | targetModelTags | array<object> | no | Tags to associate with the target model. For more information, see Tag resources in the Amazon Bedrock User Guide. |
  | clientRequestToken | string | no | A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the model copy job. |


## com.datadoghq.aws.bedrock.createModelCustomizationJob
**Create model customization job** — Creates a fine-tuning job to customize a base foundation model using specified training data.
- Stability: stable
- Permissions: `bedrock:CreateModelCustomizationJob`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | A name for the fine-tuning job. |
  | customModelName | string | yes | A name for the resulting custom model. |
  | roleArn | string | yes | The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to rea... |
  | clientRequestToken | string | no | A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return... |
  | baseModelIdentifier | string | yes | Name of the base model. |
  | customizationType | string | no | The customization type. |
  | customModelKmsKeyId | string | no | The custom model is encrypted at rest using this key. |
  | jobTags | array<object> | no | Tags to attach to the job. |
  | customModelTags | array<object> | no | Tags to attach to the resulting custom model. |
  | trainingDataConfig | object | yes | Information about the training dataset. |
  | validationDataConfig | object | no | Information about the validation dataset. |
  | outputDataConfig | object | yes | S3 location for the output data. |
  | hyperParameters | object | yes | Parameters related to tuning the model. For details on the format for different models, see Custom model hyperparameters. |
  | vpcConfig | object | no | VPC configuration (optional). Configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for this job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | Amazon Resource Name (ARN) of the fine tuning job |


## com.datadoghq.aws.bedrock.createModelImportJob
**Create model import job** — Creates a model import job to import a model customized in another environment, such as Amazon SageMaker.
- Stability: stable
- Permissions: `bedrock:CreateModelImportJob`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the import job. |
  | importedModelName | string | yes | The name of the imported model. |
  | roleArn | string | yes | The Amazon Resource Name (ARN) of the model import job. |
  | modelDataSource | object | yes | The data source for the imported model. |
  | jobTags | array<object> | no | Tags to attach to this import job. |
  | importedModelTags | array<object> | no | Tags to attach to the imported model. |
  | clientRequestToken | string | no | A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return... |
  | vpcConfig | object | no | VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job. |
  | importedModelKmsKeyId | string | no | The imported model is encrypted at rest using this key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the model import job. |


## com.datadoghq.aws.bedrock.deleteCustomModel
**Delete custom model** — Deletes a custom model that you created earlier. For more information, see Custom models in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:DeleteCustomModel`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | modelIdentifier | string | yes | Name of the model to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.deleteGuardrail
**Delete guardrail** — Deletes a guardrail and all its versions, unless a specific version is specified.
- Stability: stable
- Permissions: `bedrock:DeleteGuardrail`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | guardrailIdentifier | string | yes | The unique identifier of the guardrail. This can be an ID or the ARN. |
  | guardrailVersion | string | no | The version of the guardrail. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.deleteImportedModel
**Delete imported model** — Deletes a custom model that you imported earlier. For more information, see Import a customized model in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:DeleteImportedModel`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | modelIdentifier | string | yes | Name of the imported model to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.deleteModelInvocationLoggingConfiguration
**Delete model invocation logging configuration** — Deletes the invocation logging.
- Stability: stable
- Permissions: `bedrock:DeleteModelInvocationLoggingConfiguration`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.deleteProvisionedModelThroughput
**Delete provisioned model throughput** — Deletes a Provisioned Throughput. You cannot delete a Provisioned Throughput before the commitment term is over.
- Stability: stable
- Permissions: `bedrock:DeleteProvisionedModelThroughput`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | provisionedModelId | string | yes | The Amazon Resource Name (ARN) or name of the Provisioned Throughput. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.getCustomModel
**Get custom model** — Get the properties of an Amazon Bedrock custom model that you created.
- Stability: stable
- Permissions: `bedrock:GetCustomModel`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | modelIdentifier | string | yes | Name or Amazon Resource Name (ARN) of the custom model. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | modelArn | string | Amazon Resource Name (ARN) associated with this model. |
  | modelName | string | Model name associated with this model. |
  | jobName | string | Job name associated with this model. |
  | jobArn | string | Job Amazon Resource Name (ARN) associated with this model. |
  | baseModelArn | string | Amazon Resource Name (ARN) of the base model. |
  | customizationType | string | The type of model customization. |
  | modelKmsKeyArn | string | The custom model is encrypted at rest using this key. |
  | hyperParameters | object | Hyperparameter values associated with this model. For details on the format for different models, see Custom model hyperparameters. |
  | trainingDataConfig | object | Contains information about the training dataset. |
  | validationDataConfig | object | Contains information about the validation dataset. |
  | outputDataConfig | object | Output data configuration associated with this custom model. |
  | trainingMetrics | object | Contains training metrics from the job creation. |
  | validationMetrics | array<object> | The validation metrics from the job creation. |
  | creationTime | string | Creation time of the model. |


## com.datadoghq.aws.bedrock.getEvaluationJob
**Get evaluation job** — Retrieves the properties associated with a model evaluation job, including the status of the job. For more information, see Model evaluation.
- Stability: stable
- Permissions: `bedrock:GetEvaluationJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | The Amazon Resource Name (ARN) of the model evaluation job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobName | string | The name of the model evaluation job. |
  | status | string | The status of the model evaluation job. |
  | jobArn | string | The Amazon Resource Name (ARN) of the model evaluation job. |
  | jobDescription | string | The description of the model evaluation job. |
  | roleArn | string | The Amazon Resource Name (ARN) of the IAM service role used in the model evaluation job. |
  | customerEncryptionKeyId | string | The Amazon Resource Name (ARN) of the customer managed key specified when the model evaluation job was created. |
  | jobType | string | The type of model evaluation job. |
  | evaluationConfig | object | Contains details about the type of model evaluation job, the metrics used, the task type selected, the datasets used, and any custom metrics you defined. |
  | inferenceConfig | object | Details about the models you specified in your model evaluation job. |
  | outputDataConfig | object | Amazon S3 location for where output data is saved. |
  | creationTime | string | When the model evaluation job was created. |
  | lastModifiedTime | string | When the model evaluation job was last modified. |
  | failureMessages | array<string> | An array of strings the specify why the model evaluation job has failed. |


## com.datadoghq.aws.bedrock.getFoundationModel
**Get foundation model** — Gets details about an Amazon Bedrock foundation model.
- Stability: stable
- Permissions: `bedrock:GetFoundationModel`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | modelIdentifier | string | yes | The model identifier. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | modelDetails | object | Information about the foundation model. |


## com.datadoghq.aws.bedrock.getGuardrail
**Get guardrail** — Gets details about a guardrail. If you do not specify a version, the response returns details for the DRAFT version.
- Stability: stable
- Permissions: `bedrock:GetGuardrail`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | guardrailIdentifier | string | yes | The unique identifier of the guardrail for which to get details. This can be an ID or the ARN. |
  | guardrailVersion | string | no | The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the DRAFT version. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | name | string | The name of the guardrail. |
  | description | string | The description of the guardrail. |
  | guardrailId | string | The unique identifier of the guardrail. |
  | guardrailArn | string | The ARN of the guardrail. |
  | version | string | The version of the guardrail. |
  | status | string | The status of the guardrail. |
  | topicPolicy | object | The topic policy that was configured for the guardrail. |
  | contentPolicy | object | The content policy that was configured for the guardrail. |
  | wordPolicy | object | The word policy that was configured for the guardrail. |
  | sensitiveInformationPolicy | object | The sensitive information policy that was configured for the guardrail. |
  | contextualGroundingPolicy | object | The contextual grounding policy used in the guardrail. |
  | createdAt | string | The date and time at which the guardrail was created. |
  | updatedAt | string | The date and time at which the guardrail was updated. |
  | statusReasons | array<string> | Appears if the status is FAILED. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted. |
  | failureRecommendations | array<string> | Appears if the status of the guardrail is FAILED. A list of recommendations to carry out before retrying the request. |
  | blockedInputMessaging | string | The message that the guardrail returns when it blocks a prompt. |
  | blockedOutputsMessaging | string | The message that the guardrail returns when it blocks a model response. |
  | kmsKeyArn | string | The ARN of the KMS key that encrypts the guardrail. |


## com.datadoghq.aws.bedrock.getImportedModel
**Get imported model** — Gets properties associated with a customized model you imported.
- Stability: stable
- Permissions: `bedrock:GetImportedModel`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | modelIdentifier | string | yes | Name or Amazon Resource Name (ARN) of the imported model. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | modelArn | string | The Amazon Resource Name (ARN) associated with this imported model. |
  | modelName | string | The name of the imported model. |
  | jobName | string | Job name associated with the imported model. |
  | jobArn | string | Job Amazon Resource Name (ARN) associated with the imported model. |
  | modelDataSource | object | The data source for this imported model. |
  | creationTime | string | Creation time of the imported model. |
  | modelArchitecture | string | The architecture of the imported model. |
  | modelKmsKeyArn | string | The imported model is encrypted at rest using this key. |


## com.datadoghq.aws.bedrock.getInferenceProfile
**Get inference profile** — Gets information about an inference profile. For more information, see the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:GetInferenceProfile`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | inferenceProfileIdentifier | string | yes | The unique identifier of the inference profile. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | inferenceProfileName | string | The name of the inference profile. |
  | models | array<object> | A list of information about each model in the inference profile. |
  | description | string | The description of the inference profile. |
  | createdAt | string | The time at which the inference profile was created. |
  | updatedAt | string | The time at which the inference profile was last updated. |
  | inferenceProfileArn | string | The Amazon Resource Name (ARN) of the inference profile. |
  | inferenceProfileId | string | The unique identifier of the inference profile. |
  | status | string | The status of the inference profile. ACTIVE means that the inference profile is available to use. |
  | type | string | The type of the inference profile. SYSTEM_DEFINED means that the inference profile is defined by Amazon Bedrock. |


## com.datadoghq.aws.bedrock.getModelCopyJob
**Get model copy job** — Retrieves information about a model copy job. For more information, see Copy models to be used in other regions in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:GetModelCopyJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobArn | string | yes | The Amazon Resource Name (ARN) of the model copy job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the model copy job. |
  | status | string | The status of the model copy job. |
  | creationTime | string | The time at which the model copy job was created. |
  | targetModelArn | string | The Amazon Resource Name (ARN) of the copied model. |
  | targetModelName | string | The name of the copied model. |
  | sourceAccountId | string | The unique identifier of the account that the model being copied originated from. |
  | sourceModelArn | string | The Amazon Resource Name (ARN) of the original model being copied. |
  | targetModelKmsKeyArn | string | The Amazon Resource Name (ARN) of the KMS key encrypting the copied model. |
  | targetModelTags | array<object> | The tags associated with the copied model. |
  | failureMessage | string | An error message for why the model copy job failed. |
  | sourceModelName | string | The name of the original model being copied. |


## com.datadoghq.aws.bedrock.getModelCustomizationJob
**Get model customization job** — Retrieves the properties associated with a model-customization job, including the status of the job.
- Stability: stable
- Permissions: `bedrock:GetModelCustomizationJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | Identifier for the customization job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the customization job. |
  | jobName | string | The name of the customization job. |
  | outputModelName | string | The name of the output model. |
  | outputModelArn | string | The Amazon Resource Name (ARN) of the output model. |
  | clientRequestToken | string | The token that you specified in the CreateCustomizationJob request. |
  | roleArn | string | The Amazon Resource Name (ARN) of the IAM role. |
  | status | string | The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the jo... |
  | failureMessage | string | Information about why the job failed. |
  | creationTime | string | Time that the resource was created. |
  | lastModifiedTime | string | Time that the resource was last modified. |
  | endTime | string | Time that the resource transitioned to terminal state. |
  | baseModelArn | string | Amazon Resource Name (ARN) of the base model. |
  | hyperParameters | object | The hyperparameter values for the job. For details on the format for different models, see Custom model hyperparameters. |
  | trainingDataConfig | object | Contains information about the training dataset. |
  | validationDataConfig | object | Contains information about the validation dataset. |
  | outputDataConfig | object | Output data configuration |
  | customizationType | string | The type of model customization. |
  | outputModelKmsKeyArn | string | The custom model is encrypted at rest using this key. |
  | trainingMetrics | object | Contains training metrics from the job creation. |
  | validationMetrics | array<object> | The loss metric for each validator that you provided in the createjob request. |
  | vpcConfig | object | VPC configuration for the custom model job. |


## com.datadoghq.aws.bedrock.getModelImportJob
**Get model import job** — Retrieves the properties associated with an import model job, including the status of the job. For more information, see Import a customized model in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:GetModelImportJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | The identifier of the import job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the import job. |
  | jobName | string | The name of the import job. |
  | importedModelName | string | The name of the imported model. |
  | importedModelArn | string | The Amazon Resource Name (ARN) of the imported model. |
  | roleArn | string | The Amazon Resource Name (ARN) of the IAM role associated with this job. |
  | modelDataSource | object | The data source for the imported model. |
  | status | string | The status of the job. A successful job transitions from in-progress to completed when the imported model is ready to use. If the job failed, the failure message contains information about why the ... |
  | failureMessage | string | Information about why the import job failed. |
  | creationTime | string | The time the resource was created. |
  | lastModifiedTime | string | Time the resource was last modified. |
  | endTime | string | Time that the resource transitioned to terminal state. |
  | vpcConfig | object | The Virtual Private Cloud (VPC) configuration of the import model job. |
  | importedModelKmsKeyArn | string | The imported model is encrypted at rest using this key. |


## com.datadoghq.aws.bedrock.getModelInvocationJob
**Get model invocation job** — Gets details about a batch inference job. For more information, see View details about a batch inference job.
- Stability: stable
- Permissions: `bedrock:GetModelInvocationJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | The Amazon Resource Name (ARN) of the batch inference job. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | jobArn | string | The Amazon Resource Name (ARN) of the batch inference job. |
  | jobName | string | The name of the batch inference job. |
  | modelId | string | The unique identifier of the foundation model used for model inference. |
  | clientRequestToken | string | A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return... |
  | roleArn | string | The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at Create a... |
  | status | string | The status of the batch inference job. |
  | message | string | If the batch inference job failed, this field contains a message describing why the job failed. |
  | submitTime | string | The time at which the batch inference job was submitted. |
  | lastModifiedTime | string | The time at which the batch inference job was last modified. |
  | endTime | string | The time at which the batch inference job ended. |
  | inputDataConfig | object | Details about the location of the input to the batch inference job. |
  | outputDataConfig | object | Details about the location of the output of the batch inference job. |
  | timeoutDurationInHours | number | The number of hours after which batch inference job was set to time out. |
  | jobExpirationTime | string | The time at which the batch inference job times or timed out. |


## com.datadoghq.aws.bedrock.getModelInvocationLoggingConfiguration
**Get model invocation logging configuration** — Gets the current configuration values for model invocation logging.
- Stability: stable
- Permissions: `bedrock:GetModelInvocationLoggingConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | loggingConfig | object | The current configuration values. |


## com.datadoghq.aws.bedrock.getProvisionedModelThroughput
**Get provisioned model throughput** — Returns details for a Provisioned Throughput. For more information, see Provisioned Throughput in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:GetProvisionedModelThroughput`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | provisionedModelId | string | yes | The Amazon Resource Name (ARN) or name of the Provisioned Throughput. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | modelUnits | number | The number of model units allocated to this Provisioned Throughput. |
  | desiredModelUnits | number | The number of model units that was requested for this Provisioned Throughput. |
  | provisionedModelName | string | The name of the Provisioned Throughput. |
  | provisionedModelArn | string | The Amazon Resource Name (ARN) of the Provisioned Throughput. |
  | modelArn | string | The Amazon Resource Name (ARN) of the model associated with this Provisioned Throughput. |
  | desiredModelArn | string | The Amazon Resource Name (ARN) of the model requested to be associated to this Provisioned Throughput. This value differs from the modelArn if updating hasn't completed. |
  | foundationModelArn | string | The Amazon Resource Name (ARN) of the base model for which the Provisioned Throughput was created, or of the base model that the custom model for which the Provisioned Throughput was created was cu... |
  | status | string | The status of the Provisioned Throughput. |
  | creationTime | string | The timestamp of the creation time for this Provisioned Throughput. |
  | lastModifiedTime | string | The timestamp of the last time that this Provisioned Throughput was modified. |
  | failureMessage | string | A failure message for any issues that occurred during creation, updating, or deletion of the Provisioned Throughput. |
  | commitmentDuration | string | Commitment duration of the Provisioned Throughput. |
  | commitmentExpirationTime | string | The timestamp for when the commitment term for the Provisioned Throughput expires. |


## com.datadoghq.aws.bedrock.listCustomModels
**List custom models** — Returns a list of the custom models that you created with the CreateModelCustomizationJob operation. For more information, see Custom models in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListCustomModels`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeBefore | string | no | Return custom models created before the specified time. |
  | creationTimeAfter | string | no | Return custom models created after the specified time. |
  | nameContains | string | no | Return custom models only if the job name contains these characters. |
  | baseModelArnEquals | string | no | Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter. |
  | foundationModelArnEquals | string | no | Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter. |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | sortBy | string | no | The field to sort by in the returned list of models. |
  | sortOrder | string | no | The sort order of the results. |
  | isOwned | boolean | no | Return custom models depending on if the current account owns them (true) or if they were shared with the current account (false). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, use this token when making another request in the nextToken field to return the next batch of results. |
  | modelSummaries | array<object> | Model summaries. |


## com.datadoghq.aws.bedrock.listEvaluationJobs
**List evaluation jobs** — Lists model evaluation jobs.
- Stability: stable
- Permissions: `bedrock:ListEvaluationJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeAfter | string | no | A filter that includes model evaluation jobs created after the time specified. |
  | creationTimeBefore | string | no | A filter that includes model evaluation jobs created prior to the time specified. |
  | statusEquals | string | no | Only return jobs where the status condition is met. |
  | nameContains | string | no | Query parameter string for model evaluation job names. |
  | maxResults | number | no | The maximum number of results to return. |
  | nextToken | string | no | Continuation token from the previous response, for Amazon Bedrock to list the next set of results. |
  | sortBy | string | no | Allows you to sort model evaluation jobs by when they were created. |
  | sortOrder | string | no | How you want the order of jobs sorted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | Continuation token from the previous response, for Amazon Bedrock to list the next set of results. |
  | jobSummaries | array<object> | A summary of the model evaluation jobs. |


## com.datadoghq.aws.bedrock.listFoundationModels
**List foundation models** — Lists available Amazon Bedrock foundation models. You can use request parameters to filter the results. For more information, see Foundation models in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListFoundationModels`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | byProvider | string | no | Return models belonging to the model provider that you specify. |
  | byCustomizationType | string | no | Return models that support the customization type that you specify. For more information, see Custom models in the Amazon Bedrock User Guide. |
  | byOutputModality | string | no | Return models that support the output modality that you specify. |
  | byInferenceType | string | no | Return models that support the inference type that you specify. For more information, see Provisioned Throughput in the Amazon Bedrock User Guide. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | modelSummaries | array<object> | A list of Amazon Bedrock foundation models. |


## com.datadoghq.aws.bedrock.listGuardrails
**List guardrails** — Lists details about all the guardrails in an account.
- Stability: stable
- Permissions: `bedrock:ListGuardrails`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | guardrailIdentifier | string | no | The unique identifier of the guardrail. This can be an ID or the ARN. |
  | maxResults | number | no | The maximum number of results to return in the response. |
  | nextToken | string | no | If there are more results than were returned in the response, the response returns a nextToken that you can send in another ListGuardrails request to see the next batch of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | guardrails | array<object> | A list of objects, each of which contains details about a guardrail. |
  | nextToken | string | If there are more results than were returned in the response, the response returns a nextToken that you can send in another ListGuardrails request to see the next batch of results. |


## com.datadoghq.aws.bedrock.listImportedModels
**List imported models** — Returns a list of models you have imported. You can filter the results based on one or more criteria. For more information, see Import a customized model in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListImportedModels`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeBefore | string | no | Return imported models that created before the specified time. |
  | creationTimeAfter | string | no | Return imported models that were created after the specified time. |
  | nameContains | string | no | Return imported models only if the model name contains these characters. |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | sortBy | string | no | The field to sort by in the returned list of imported models. |
  | sortOrder | string | no | Specifies whetehr to sort the results in ascending or descending order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, use this token when making another request in the nextToken field to return the next batch of results. |
  | modelSummaries | array<object> | Model summaries. |


## com.datadoghq.aws.bedrock.listInferenceProfiles
**List inference profiles** — Returns a list of inference profiles that you can use.
- Stability: stable
- Permissions: `bedrock:ListInferenceProfiles`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | inferenceProfileSummaries | array<object> | A list of information about each inference profile that you can use. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, use this token when making another request in the nextToken field to return the next batch of results. |


## com.datadoghq.aws.bedrock.listModelCopyJobs
**List model copy jobs** — Returns a list of model copy jobs that you have submitted. You can filter the jobs based on one or more criteria. For more information, see Copy models to be used in other regions in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListModelCopyJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeAfter | string | no | Filters for model copy jobs created after the specified time. |
  | creationTimeBefore | string | no | Filters for model copy jobs created before the specified time. |
  | statusEquals | string | no | Filters for model copy jobs whose status matches the value that you specify. |
  | sourceAccountEquals | string | no | Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify. |
  | sourceModelArnEquals | string | no | Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify. |
  | targetModelNameContains | string | no | Filters for model copy jobs in which the name of the copied model contains the string that you specify. |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | sortBy | string | no | The field to sort by in the returned list of model copy jobs. |
  | sortOrder | string | no | Specifies whether to sort the results in ascending or descending order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, use this token when making another request in the nextToken field to return the next batch of results. |
  | modelCopyJobSummaries | array<object> | A list of information about each model copy job. |


## com.datadoghq.aws.bedrock.listModelCustomizationJobs
**List model customization jobs** — Returns a list of model customization jobs that you have submitted. You can filter the jobs based on one or more criteria. For more information, see Custom models in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListModelCustomizationJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeAfter | string | no | Return customization jobs created after the specified time. |
  | creationTimeBefore | string | no | Return customization jobs created before the specified time. |
  | statusEquals | string | no | Return customization jobs with the specified status. |
  | nameContains | string | no | Return customization jobs only if the job name contains these characters. |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | sortBy | string | no | The field to sort by in the returned list of jobs. |
  | sortOrder | string | no | The sort order of the results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, use this token when making another request in the nextToken field to return the next batch of results. |
  | modelCustomizationJobSummaries | array<object> | Job summaries. |


## com.datadoghq.aws.bedrock.listModelImportJobs
**List model import jobs** — Returns a list of import jobs you have submitted. You can filter the results based on one or more criteria. For more information, see Import a customized model in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListModelImportJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeAfter | string | no | Return import jobs that were created after the specified time. |
  | creationTimeBefore | string | no | Return import jobs that were created before the specified time. |
  | statusEquals | string | no | Return imported jobs with the specified status. |
  | nameContains | string | no | Return imported jobs only if the job name contains these characters. |
  | maxResults | number | no | The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the nextToken field when making another... |
  | nextToken | string | no | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | sortBy | string | no | The field to sort by in the returned list of imported jobs. |
  | sortOrder | string | no | Specifies whether to sort the results in ascending or descending order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If the total number of results is greater than the maxResults value provided in the request, enter the token returned in the nextToken field in the response in this field to return the next batch o... |
  | modelImportJobSummaries | array<object> | Import job summaries. |


## com.datadoghq.aws.bedrock.listModelInvocationJobs
**List model invocation jobs** — Lists all batch inference jobs in the account. For more information, see View details about a batch inference job.
- Stability: stable
- Permissions: `bedrock:ListModelInvocationJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | submitTimeAfter | string | no | Specify a time to filter for batch inference jobs that were submitted after the time you specify. |
  | submitTimeBefore | string | no | Specify a time to filter for batch inference jobs that were submitted before the time you specify. |
  | statusEquals | string | no | Specify a status to filter for batch inference jobs whose statuses match the string you specify. |
  | nameContains | string | no | Specify a string to filter for batch inference jobs whose names contain the string. |
  | maxResults | number | no | The maximum number of results to return. If there are more results than the number that you specify, a nextToken value is returned. Use the nextToken in a request to return the next batch of results. |
  | nextToken | string | no | If there were more results than the value you specified in the maxResults field in a previous ListModelInvocationJobs request, the response would have returned a nextToken value. To see the next ba... |
  | sortBy | string | no | An attribute by which to sort the results. |
  | sortOrder | string | no | Specifies whether to sort the results by ascending or descending order. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If there are more results than can fit in the response, a nextToken is returned. Use the nextToken in a request to return the next batch of results. |
  | invocationJobSummaries | array<object> | A list of items, each of which contains a summary about a batch inference job. |


## com.datadoghq.aws.bedrock.listProvisionedModelThroughputs
**List provisioned model throughputs** — Lists the Provisioned Throughputs in the account. For more information, see Provisioned Throughput in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListProvisionedModelThroughputs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | creationTimeAfter | string | no | A filter that returns Provisioned Throughputs created after the specified time. |
  | creationTimeBefore | string | no | A filter that returns Provisioned Throughputs created before the specified time. |
  | statusEquals | string | no | A filter that returns Provisioned Throughputs if their statuses matches the value that you specify. |
  | modelArnEquals | string | no | A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify. |
  | nameContains | string | no | A filter that returns Provisioned Throughputs if their name contains the expression that you specify. |
  | maxResults | number | no | THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a nextToken value. To see the next batch of results, send the ... |
  | nextToken | string | no | If there are more results than the number you specified in the maxResults field, the response returns a nextToken value. To see the next batch of results, specify the nextToken value in this field. |
  | sortBy | string | no | The field by which to sort the returned list of Provisioned Throughputs. |
  | sortOrder | string | no | The sort order of the results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | nextToken | string | If there are more results than the number you specified in the maxResults field, this value is returned. To see the next batch of results, include this value in the nextToken field in another list ... |
  | provisionedModelSummaries | array<object> | A list of summaries, one for each Provisioned Throughput in the response. |


## com.datadoghq.aws.bedrock.listTagsForResource
**List tags for resource** — List the tags associated with the specified resource. For more information, see Tagging resources in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceARN | string | yes | The Amazon Resource Name (ARN) of the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tags | array<object> | An array of the tags associated with this resource. |


## com.datadoghq.aws.bedrock.putModelInvocationLoggingConfiguration
**Put model invocation logging configuration** — Sets the configuration values for model invocation logging.
- Stability: stable
- Permissions: `bedrock:PutModelInvocationLoggingConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | loggingConfig | object | yes | The logging configuration values to set. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.stopEvaluationJob
**Stop evaluation job** — Stops an in-progress model evaluation job.
- Stability: stable
- Permissions: `bedrock:StopEvaluationJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | The ARN of the model evaluation job you want to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.stopModelCustomizationJob
**Stop model customization job** — Stops an active model customization job. For more information, see Custom models in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:StopModelCustomizationJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | Job identifier of the job to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.stopModelInvocationJob
**Stop model invocation job** — Stops a batch inference job. You are only charged for tokens that were already processed. For more information, see Stop a batch inference job.
- Stability: stable
- Permissions: `bedrock:StopModelInvocationJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobIdentifier | string | yes | The Amazon Resource Name (ARN) of the batch inference job to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.tagResource
**Tag resource** — Associates tags with a resource. For more information, see Tagging resources in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceARN | string | yes | The Amazon Resource Name (ARN) of the resource to tag. |
  | tags | any | yes | Tags to associate with the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.untagResource
**Untag resource** — Removes one or more tags from a resource. For more information, see Tagging resources in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceARN | string | yes | The Amazon Resource Name (ARN) of the resource to untag. |
  | tagKeys | array<string> | yes | Tag keys of the tags to remove from the resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.bedrock.updateGuardrail
**Update guardrail** — Updates a guardrail with the values you specify.
- Stability: stable
- Permissions: `bedrock:UpdateGuardrail`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | guardrailIdentifier | string | yes | The unique identifier of the guardrail. This can be an ID or the ARN. |
  | name | string | yes | A name for the guardrail. |
  | description | string | no | A description of the guardrail. |
  | topicPolicyConfig | object | no | The topic policy to configure for the guardrail. |
  | contentPolicyConfig | object | no | The content policy to configure for the guardrail. |
  | wordPolicyConfig | object | no | The word policy to configure for the guardrail. |
  | sensitiveInformationPolicyConfig | object | no | The sensitive information policy to configure for the guardrail. |
  | contextualGroundingPolicyConfig | object | no | The contextual grounding policy configuration used to update a guardrail. |
  | blockedInputMessaging | string | yes | The message to return when the guardrail blocks a prompt. |
  | blockedOutputsMessaging | string | yes | The message to return when the guardrail blocks a model response. |
  | kmsKeyId | string | no | The ARN of the KMS key with which to encrypt the guardrail. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | guardrailId | string | The unique identifier of the guardrail |
  | guardrailArn | string | The ARN of the guardrail. |
  | version | string | The version of the guardrail. |
  | updatedAt | string | The date and time at which the guardrail was updated. |


## com.datadoghq.aws.bedrock.updateProvisionedModelThroughput
**Update provisioned model throughput** — Updates the name or associated model for a Provisioned Throughput. For more information, see Provisioned Throughput in the Amazon Bedrock User Guide.
- Stability: stable
- Permissions: `bedrock:UpdateProvisionedModelThroughput`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | provisionedModelId | string | yes | The Amazon Resource Name (ARN) or name of the Provisioned Throughput to update. |
  | desiredProvisionedModelName | string | no | The new name for this Provisioned Throughput. |
  | desiredModelId | string | no | The Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model. If this P... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

