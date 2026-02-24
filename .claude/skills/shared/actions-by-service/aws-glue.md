# AWS Glue Actions
Bundle: `com.datadoghq.aws.glue` | 220 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eglue)

## com.datadoghq.aws.glue.batchCreatePartition
**Batch create partition** — Creates one or more partitions in a batch operation.
- Stability: stable
- Permissions: `glue:BatchCreatePartition`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the catalog in which the partition is to be created. Currently, this should be the Amazon Web Services account ID. |
  | databaseName | string | yes | The name of the metadata database in which the partition is to be created. |
  | tableName | string | yes | The name of the metadata table in which the partition is to be created. |
  | partitionInputList | array<object> | yes | A list of PartitionInput structures that define the partitions to be created. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | The errors encountered when trying to create the requested partitions. |


## com.datadoghq.aws.glue.batchDeleteConnection
**Batch delete connection** — Deletes a list of connection definitions from the Data Catalog.
- Stability: stable
- Permissions: `glue:BatchDeleteConnection`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | connectionNameList | array<string> | yes | A list of names of the connections to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Succeeded | array<string> | A list of names of the connection definitions that were successfully deleted. |
  | Errors | object | A map of the names of connections that were not successfully deleted to error details. |


## com.datadoghq.aws.glue.batchDeletePartition
**Batch delete partition** — Deletes one or more partitions in a batch operation.
- Stability: stable
- Permissions: `glue:BatchDeletePartition`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the table in question resides. |
  | tableName | string | yes | The name of the table that contains the partitions to be deleted. |
  | partitionsToDelete | array<object> | yes | A list of PartitionInput structures that define the partitions to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | The errors encountered when trying to delete the requested partitions. |


## com.datadoghq.aws.glue.batchDeleteTable
**Batch delete table** — Deletes multiple tables at once.  After completing this operation, you no longer have access to the table versions and partitions that belong to the deleted table. Glue deletes these &quot;orphaned&quot; resources asynchronously in a timely manner, at the discretion of the service. To ensure the immediate deletion of all related resources, before calling BatchDeleteTable, use DeleteTableVersion or BatchDeleteTableVersion, and DeletePartition or BatchDeletePartition, to delete any resources that belong to the table.
- Stability: stable
- Permissions: `glue:BatchDeleteTable`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the tables to delete reside. For Hive compatibility, this name is entirely lowercase. |
  | tablesToDelete | array<string> | yes | A list of the table to delete. |
  | transactionId | string | no | The transaction ID at which to delete the table contents. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | A list of errors encountered in attempting to delete the specified tables. |


## com.datadoghq.aws.glue.batchDeleteTableVersion
**Batch delete table version** — Deletes a specified batch of versions of a table.
- Stability: stable
- Permissions: `glue:BatchDeleteTableVersion`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | tableName | string | yes | The name of the table. For Hive compatibility, this name is entirely lowercase. |
  | versionIds | array<string> | yes | A list of the IDs of versions to be deleted. A VersionId is a string representation of an integer. Each version is incremented by 1. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | A list of errors encountered while trying to delete the specified table versions. |


## com.datadoghq.aws.glue.batchGetBlueprints
**Batch get blueprints** — Retrieves information about a list of blueprints.
- Stability: stable
- Permissions: `glue:BatchGetBlueprints`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | names | array<string> | yes | A list of blueprint names. |
  | includeBlueprint | boolean | no | Specifies whether or not to include the blueprint in the response. |
  | includeParameterSpec | boolean | no | Specifies whether or not to include the parameters, as a JSON string, for the blueprint in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Blueprints | array<object> | Returns a list of blueprint as a Blueprints object. |
  | MissingBlueprints | array<string> | Returns a list of BlueprintNames that were not found. |


## com.datadoghq.aws.glue.batchGetCrawlers
**Batch get crawlers** — Returns a list of resource metadata for a given list of crawler names. After calling the ListCrawlers operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that use tags.
- Stability: stable
- Permissions: `glue:BatchGetCrawlers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerNames | array<string> | yes | A list of crawler names, which might be the names returned from the ListCrawlers operation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Crawlers | array<object> | A list of crawler definitions. |
  | CrawlersNotFound | array<string> | A list of names of crawlers that were not found. |


## com.datadoghq.aws.glue.batchGetCustomEntityTypes
**Batch get custom entity types** — Retrieves the details for the custom patterns specified by a list of names.
- Stability: stable
- Permissions: `glue:BatchGetCustomEntityTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | names | array<string> | yes | A list of names of the custom patterns that you want to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CustomEntityTypes | array<object> | A list of CustomEntityType objects representing the custom patterns that have been created. |
  | CustomEntityTypesNotFound | array<string> | A list of the names of custom patterns that were not found. |


## com.datadoghq.aws.glue.batchGetDataQualityResult
**Batch get data quality result** — Retrieves a list of data quality results for the specified result IDs.
- Stability: stable
- Permissions: `glue:BatchGetDataQualityResult`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resultIds | array<string> | yes | A list of unique result IDs for the data quality results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Results | array<object> | A list of DataQualityResult objects representing the data quality results. |
  | ResultsNotFound | array<string> | A list of result IDs for which results were not found. |


## com.datadoghq.aws.glue.batchGetDevEndpoints
**Batch get dev endpoints** — Returns a list of resource metadata for a given list of development endpoint names. After calling the ListDevEndpoints operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that use tags.
- Stability: stable
- Permissions: `glue:BatchGetDevEndpoints`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | devEndpointNames | array<string> | yes | The list of DevEndpoint names, which might be the names returned from the ListDevEndpoint operation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DevEndpoints | array<object> | A list of DevEndpoint definitions. |
  | DevEndpointsNotFound | array<string> | A list of DevEndpoints not found. |


## com.datadoghq.aws.glue.batchGetJobs
**Batch get jobs** — Returns a list of resource metadata for a given list of job names. After calling the ListJobs operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that use tags.
- Stability: stable
- Permissions: `glue:BatchGetJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobNames | array<string> | yes | A list of job names, which might be the names returned from the ListJobs operation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Jobs | array<object> | A list of job definitions. |
  | JobsNotFound | array<string> | A list of names of jobs not found. |


## com.datadoghq.aws.glue.batchGetPartition
**Batch get partition** — Retrieves partitions in a batch request.
- Stability: stable
- Permissions: `glue:BatchGetPartition`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | partitionsToGet | array<object> | yes | A list of partition values identifying the partitions to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Partitions | array<object> | A list of the requested partitions. |
  | UnprocessedKeys | array<object> | A list of the partition values in the request for which partitions were not returned. |


## com.datadoghq.aws.glue.batchGetTableOptimizer
**Batch get table optimizer** — Returns the configuration for the specified table optimizers.
- Stability: stable
- Permissions: `glue:BatchGetTableOptimizer`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | entries | array<object> | yes | A list of BatchGetTableOptimizerEntry objects specifying the table optimizers to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TableOptimizers | array<object> | A list of BatchTableOptimizer objects. |
  | Failures | array<object> | A list of errors from the operation. |


## com.datadoghq.aws.glue.batchGetTriggers
**Batch get triggers** — Returns a list of resource metadata for a given list of trigger names. After calling the ListTriggers operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that use tags.
- Stability: stable
- Permissions: `glue:BatchGetTriggers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | triggerNames | array<string> | yes | A list of trigger names, which may be the names returned from the ListTriggers operation. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Triggers | array<object> | A list of trigger definitions. |
  | TriggersNotFound | array<string> | A list of names of triggers not found. |


## com.datadoghq.aws.glue.batchGetWorkflows
**Batch get workflows** — Returns a list of resource metadata for a given list of workflow names. After calling the ListWorkflows operation, you can call this operation to access the data to which you have been granted permissions. This operation supports all IAM permissions, including permission conditions that use tags.
- Stability: stable
- Permissions: `glue:BatchGetWorkflows`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | names | array<string> | yes | A list of workflow names, which may be the names returned from the ListWorkflows operation. |
  | includeGraph | boolean | no | Specifies whether to include a graph when returning the workflow resource metadata. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Workflows | array<object> | A list of workflow resource metadata. |
  | MissingWorkflows | array<string> | A list of names of workflows not found. |


## com.datadoghq.aws.glue.batchPutDataQualityStatisticAnnotation
**Batch put data quality statistic annotation** — Annotate datapoints over time for a specific data quality statistic.
- Stability: stable
- Permissions: `glue:BatchPutDataQualityStatisticAnnotation`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | inclusionAnnotations | array<object> | yes | A list of DatapointInclusionAnnotation's. |
  | clientToken | string | no | Client Token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | FailedInclusionAnnotations | array<object> | A list of AnnotationError's. |


## com.datadoghq.aws.glue.batchStopJobRun
**Batch stop job run** — Stops one or more job runs for a specified job definition.
- Stability: stable
- Permissions: `glue:BatchStopJobRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition for which to stop job runs. |
  | jobRunIds | array<string> | yes | A list of the JobRunIds that should be stopped for that job definition. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SuccessfulSubmissions | array<object> | A list of the JobRuns that were successfully submitted for stopping. |
  | Errors | array<object> | A list of the errors that were encountered in trying to stop JobRuns, including the JobRunId for which each error was encountered and details about the error. |


## com.datadoghq.aws.glue.batchUpdatePartition
**Batch update partition** — Updates one or more partitions in a batch operation.
- Stability: stable
- Permissions: `glue:BatchUpdatePartition`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the catalog in which the partition is to be updated. Currently, this should be the Amazon Web Services account ID. |
  | databaseName | string | yes | The name of the metadata database in which the partition is to be updated. |
  | tableName | string | yes | The name of the metadata table in which the partition is to be updated. |
  | entries | array<object> | yes | A list of up to 100 BatchUpdatePartitionRequestEntry objects to update. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | The errors encountered when trying to update the requested partitions. A list of BatchUpdatePartitionFailureEntry objects. |


## com.datadoghq.aws.glue.cancelDataQualityRuleRecommendationRun
**Cancel data quality rule recommendation run** — Cancels the specified recommendation run that was being used to generate rules.
- Stability: stable
- Permissions: `glue:CancelDataQualityRuleRecommendationRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | runId | string | yes | The unique run identifier associated with this run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.cancelDataQualityRulesetEvaluationRun
**Cancel data quality ruleset evaluation run** — Cancels a run where a ruleset is being evaluated against a data source.
- Stability: stable
- Permissions: `glue:CancelDataQualityRulesetEvaluationRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | runId | string | yes | The unique run identifier associated with this run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.cancelMLTaskRun
**Cancel mltask run** — Cancels (stops) a task run. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can cancel a machine learning task run at any time by calling CancelMLTaskRun with a task run&#x27;s parent transform&#x27;s TransformID and the task run&#x27;s TaskRunId.
- Stability: stable
- Permissions: `glue:CancelMLTaskRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | taskRunId | string | yes | A unique identifier for the task run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | The unique identifier of the machine learning transform. |
  | TaskRunId | string | The unique identifier for the task run. |
  | Status | string | The status for this run. |


## com.datadoghq.aws.glue.cancelStatement
**Cancel statement** — Cancels the statement.
- Stability: stable
- Permissions: `glue:CancelStatement`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sessionId | string | yes | The Session ID of the statement to be cancelled. |
  | id | number | yes | The ID of the statement to be cancelled. |
  | requestOrigin | string | no | The origin of the request to cancel the statement. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.checkSchemaVersionValidity
**Check schema version validity** — Validates the supplied schema. This call has no side effects, it simply validates using the supplied schema using DataFormat as the format. Since it does not take a schema set name, no compatibility checks are performed.
- Stability: stable
- Permissions: `glue:CheckSchemaVersionValidity`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dataFormat | string | yes | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | schemaDefinition | string | yes | The definition of the schema that has to be validated. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Valid | boolean | Return true, if the schema is valid and false otherwise. |
  | Error | string | A validation failure error message. |


## com.datadoghq.aws.glue.createBlueprint
**Create blueprint** — Registers a blueprint with Glue.
- Stability: stable
- Permissions: `glue:CreateBlueprint`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the blueprint. |
  | description | string | no | A description of the blueprint. |
  | blueprintLocation | string | yes | Specifies a path in Amazon S3 where the blueprint is published. |
  | tags | any | no | The tags to be applied to this blueprint. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | Returns the name of the blueprint that was registered. |


## com.datadoghq.aws.glue.createClassifier
**Create classifier** — Creates a classifier in the user&#x27;s account. This can be a GrokClassifier, an XMLClassifier, a JsonClassifier, or a CsvClassifier, depending on which field of the request is present.
- Stability: stable
- Permissions: `glue:CreateClassifier`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | grokClassifier | object | no | A GrokClassifier object specifying the classifier to create. |
  | xMLClassifier | object | no | An XMLClassifier object specifying the classifier to create. |
  | jsonClassifier | object | no | A JsonClassifier object specifying the classifier to create. |
  | csvClassifier | object | no | A CsvClassifier object specifying the classifier to create. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createConnection
**Create connection** — Creates a connection definition in the Data Catalog. Connections used for creating federated resources require the IAM glue:PassConnection permission.
- Stability: stable
- Permissions: `glue:CreateConnection`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which to create the connection. If none is provided, the Amazon Web Services account ID is used by default. |
  | connectionInput | object | yes | A ConnectionInput object defining the connection to create. |
  | tags | any | no | The tags you assign to the connection. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CreateConnectionStatus | string | The status of the connection creation request. The request can take some time for certain authentication types, for example when creating an OAuth connection with token exchange over VPC. |


## com.datadoghq.aws.glue.createCrawler
**Create crawler** — Creates a new crawler with specified targets, role, configuration, and optional schedule. At least one crawl target must be specified, in the s3Targets field, the jdbcTargets field, or the DynamoDBTargets field.
- Stability: stable
- Permissions: `glue:CreateCrawler`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the new crawler. |
  | role | string | yes | The IAM role or Amazon Resource Name (ARN) of an IAM role used by the new crawler to access customer resources. |
  | databaseName | string | no | The Glue database where results are written, such as: arn:aws:daylight:us-east-1::database/sometable/*. |
  | description | string | no | A description of the new crawler. |
  | targets | object | yes | A list of collection of targets to crawl. |
  | schedule | string | no | A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers. For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *). |
  | classifiers | array<string> | no | A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a g... |
  | tablePrefix | string | no | The table prefix used for catalog tables that are created. |
  | schemaChangePolicy | object | no | The policy for the crawler's update and deletion behavior. |
  | recrawlPolicy | object | no | A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run. |
  | lineageConfiguration | object | no | Specifies data lineage configuration settings for the crawler. |
  | lakeFormationConfiguration | object | no | Specifies Lake Formation configuration settings for the crawler. |
  | configuration | string | no | Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see Setting crawler configuration options. |
  | crawlerSecurityConfiguration | string | no | The name of the SecurityConfiguration structure to be used by this crawler. |
  | tags | any | no | The tags to use with this crawler request. You may use tags to limit access to the crawler. For more information about tags in Glue, see Amazon Web Services Tags in Glue in the developer guide. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createCustomEntityType
**Create custom entity type** — Creates a custom pattern that is used to detect sensitive data across the columns and rows of your structured data. Each custom pattern you create specifies a regular expression and an optional list of context words. If no context words are passed only a regular expression is checked.
- Stability: stable
- Permissions: `glue:CreateCustomEntityType`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per Amazon Web Services account. |
  | regexString | string | yes | A regular expression string that is used for detecting sensitive data in a custom pattern. |
  | contextWords | array<string> | no | A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data. If no context words are passed only ... |
  | tags | any | no | A list of tags applied to the custom entity type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the custom pattern you created. |


## com.datadoghq.aws.glue.createDataQualityRuleset
**Create data quality ruleset** — Creates a data quality ruleset with DQDL rules applied to a specified Glue table. You create the ruleset using the Data Quality Definition Language (DQDL). For more information, see the Glue developer guide.
- Stability: stable
- Permissions: `glue:CreateDataQualityRuleset`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | A unique name for the data quality ruleset. |
  | description | string | no | A description of the data quality ruleset. |
  | ruleset | string | yes | A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide. |
  | tags | any | no | A list of tags applied to the data quality ruleset. |
  | targetTable | object | no | A target table associated with the data quality ruleset. |
  | dataQualitySecurityConfiguration | string | no | The name of the security configuration created with the data quality encryption option. |
  | clientToken | string | no | Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | A unique name for the data quality ruleset. |


## com.datadoghq.aws.glue.createDatabase
**Create database** — Creates a new database in a Data Catalog.
- Stability: stable
- Permissions: `glue:CreateDatabase`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which to create the database. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseInput | object | yes | The metadata for the database. |
  | tags | any | no | The tags you assign to the database. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createDevEndpoint
**Create dev endpoint** — Creates a new development endpoint.
- Stability: stable
- Permissions: `glue:CreateDevEndpoint`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | endpointName | string | yes | The name to be assigned to the new DevEndpoint. |
  | roleArn | string | yes | The IAM role for the DevEndpoint. |
  | securityGroupIds | array<string> | no | Security group IDs for the security groups to be used by the new DevEndpoint. |
  | subnetId | string | no | The subnet ID for the new DevEndpoint to use. |
  | publicKey | string | no | The public key to be used by this DevEndpoint for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys. |
  | publicKeys | array<string> | no | A list of public keys to be used by the development endpoints for authentication. The use of this attribute is preferred over a single public key because the public keys allow you to have a differe... |
  | numberOfNodes | number | no | The number of Glue Data Processing Units (DPUs) to allocate to this DevEndpoint. |
  | workerType | string | no | The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.   For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory... |
  | glueVersion | string | no | Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.  For mo... |
  | numberOfWorkers | number | no | The number of workers of a defined workerType that are allocated to the development endpoint. The maximum number of workers you can define are 299 for G.1X, and 149 for G.2X. |
  | extraPythonLibsS3Path | string | no | The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your DevEndpoint. Multiple values must be complete paths separated by a comma.  You can only use pure Pytho... |
  | extraJarsS3Path | string | no | The path to one or more Java .jar files in an S3 bucket that should be loaded in your DevEndpoint. |
  | securityConfiguration | string | no | The name of the SecurityConfiguration structure to be used with this DevEndpoint. |
  | tags | any | no | The tags to use with this DevEndpoint. You may use tags to limit access to the DevEndpoint. For more information about tags in Glue, see Amazon Web Services Tags in Glue in the developer guide. |
  | arguments | object | no | A map of arguments used to configure the DevEndpoint. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | EndpointName | string | The name assigned to the new DevEndpoint. |
  | Status | string | The current status of the new DevEndpoint. |
  | SecurityGroupIds | array<string> | The security groups assigned to the new DevEndpoint. |
  | SubnetId | string | The subnet ID assigned to the new DevEndpoint. |
  | RoleArn | string | The Amazon Resource Name (ARN) of the role assigned to the new DevEndpoint. |
  | YarnEndpointAddress | string | The address of the YARN endpoint used by this DevEndpoint. |
  | ZeppelinRemoteSparkInterpreterPort | number | The Apache Zeppelin port for the remote Apache Spark interpreter. |
  | NumberOfNodes | number | The number of Glue Data Processing Units (DPUs) allocated to this DevEndpoint. |
  | WorkerType | string | The type of predefined worker that is allocated to the development endpoint. May be a value of Standard, G.1X, or G.2X. |
  | GlueVersion | string | Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints.  For mo... |
  | NumberOfWorkers | number | The number of workers of a defined workerType that are allocated to the development endpoint. |
  | AvailabilityZone | string | The Amazon Web Services Availability Zone where this DevEndpoint is located. |
  | VpcId | string | The ID of the virtual private cloud (VPC) used by this DevEndpoint. |
  | ExtraPythonLibsS3Path | string | The paths to one or more Python libraries in an S3 bucket that will be loaded in your DevEndpoint. |
  | ExtraJarsS3Path | string | Path to one or more Java .jar files in an S3 bucket that will be loaded in your DevEndpoint. |
  | FailureReason | string | The reason for a current failure in this DevEndpoint. |
  | SecurityConfiguration | string | The name of the SecurityConfiguration structure being used with this DevEndpoint. |
  | CreatedTimestamp | string | The point in time at which this DevEndpoint was created. |
  | Arguments | object | The map of arguments used to configure this DevEndpoint. Valid arguments are:    "--enable-glue-datacatalog": ""    You can specify a version of Python support for development endpoints by using th... |


## com.datadoghq.aws.glue.createJob
**Create job** — Creates a new job definition.
- Stability: stable
- Permissions: `glue:CreateJob`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name you assign to this job definition. It must be unique in your account. |
  | jobMode | string | no | A mode that describes how a job was created. Valid values are:    SCRIPT - The job was created using the Glue Studio script editor.    VISUAL - The job was created using the Glue Studio visual edit... |
  | jobRunQueuingEnabled | boolean | no | Specifies whether job run queuing is enabled for the job runs for this job. A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be co... |
  | description | string | no | Description of the job being defined. |
  | logUri | string | no | This field is reserved for future use. |
  | role | string | yes | The name or Amazon Resource Name (ARN) of the IAM role associated with this job. |
  | executionProperty | object | no | An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job. |
  | command | object | yes | The JobCommand that runs this job. |
  | defaultArguments | object | no | The default arguments for every run of this job, specified as name-value pairs. You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself con... |
  | nonOverridableArguments | object | no | Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs. |
  | connections | object | no | The connections used for this job. |
  | maxRetries | number | no | The maximum number of times to retry this job if it fails. |
  | allocatedCapacity | number | no | This parameter is deprecated. Use MaxCapacity instead. The number of Glue data processing units (DPUs) to allocate to this Job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a r... |
  | timeout | number | no | The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours) for batch jobs. ... |
  | maxCapacity | number | no | For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of proces... |
  | securityConfiguration | string | no | The name of the SecurityConfiguration structure to be used with this job. |
  | tags | any | no | The tags to use with this job. You may use tags to limit access to the job. For more information about tags in Glue, see Amazon Web Services Tags in Glue in the developer guide. |
  | notificationProperty | object | no | Specifies configuration properties of a job notification. |
  | glueVersion | string | no | In Spark jobs, GlueVersion determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark.  Ray jobs shou... |
  | numberOfWorkers | number | no | The number of workers of a defined workerType that are allocated when a job runs. |
  | workerType | string | no | The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.   For the G.1X worker type,... |
  | codeGenConfigurationNodes | object | no | The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based. |
  | executionClass | string | no | Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resource... |
  | sourceControlDetails | object | no | The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository. |
  | maintenanceWindow | string | no | This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to r... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The unique name that was provided for this job definition. |


## com.datadoghq.aws.glue.createMLTransform
**Create mltransform** — Creates a Glue machine learning transform. This operation creates the transform and all the necessary parameters to train it. Call this operation as the first step in the process of using a machine learning transform (such as the FindMatches transform) for deduplicating data. You can provide an optional Description, in addition to the parameters that you want to use for your algorithm. You must also specify certain parameters for the tasks that Glue runs on your behalf as part of learning from your data and creating a high-quality machine learning transform. These parameters include Role, and optionally, AllocatedCapacity, Timeout, and MaxRetries. For more information, see Jobs.
- Stability: stable
- Permissions: `glue:CreateMLTransform`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The unique name that you give the transform when you create it. |
  | description | string | no | A description of the machine learning transform that is being defined. The default is an empty string. |
  | inputRecordTables | array<object> | yes | A list of Glue table definitions used by the transform. |
  | parameters | object | yes | The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type. |
  | role | string | yes | The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both Glue service role permissions to Glue resources, and Amazon S3 permission... |
  | glueVersion | string | no | This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults ... |
  | maxCapacity | number | no | The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing... |
  | workerType | string | no | The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.   For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 5... |
  | numberOfWorkers | number | no | The number of workers of a defined workerType that are allocated when this task runs. If WorkerType is set, then NumberOfWorkers is required (and vice versa). |
  | timeout | number | no | The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The d... |
  | maxRetries | number | no | The maximum number of times to retry a task for this transform after a task run fails. |
  | tags | any | no | The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in Glue, see Amazon Web Services Tags in Gl... |
  | transformEncryption | object | no | The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | A unique identifier that is generated for the transform. |


## com.datadoghq.aws.glue.createPartition
**Create partition** — Creates a new partition.
- Stability: stable
- Permissions: `glue:CreatePartition`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The Amazon Web Services account ID of the catalog in which the partition is to be created. |
  | databaseName | string | yes | The name of the metadata database in which the partition is to be created. |
  | tableName | string | yes | The name of the metadata table in which the partition is to be created. |
  | partitionInput | object | yes | A PartitionInput structure defining the partition to be created. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createPartitionIndex
**Create partition index** — Creates a specified partition index in an existing table.
- Stability: stable
- Permissions: `glue:CreatePartitionIndex`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The catalog ID where the table resides. |
  | databaseName | string | yes | Specifies the name of a database in which you want to create a partition index. |
  | tableName | string | yes | Specifies the name of a table in which you want to create a partition index. |
  | partitionIndex | object | yes | Specifies a PartitionIndex structure to create a partition index in an existing table. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createRegistry
**Create registry** — Creates a new registry which may be used to hold a collection of schemas.
- Stability: stable
- Permissions: `glue:CreateRegistry`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryName | string | yes | Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace. |
  | description | string | no | A description of the registry. If description is not provided, there will not be any default value for this. |
  | tags | any | no | Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryArn | string | The Amazon Resource Name (ARN) of the newly created registry. |
  | RegistryName | string | The name of the registry. |
  | Description | string | A description of the registry. |
  | Tags | object | The tags for the registry. |


## com.datadoghq.aws.glue.createSchema
**Create schema** — Creates a new schema set and registers the schema definition. Returns an error if the schema set already exists without actually registering the version. When the schema set is created, a version checkpoint will be set to the first version. Compatibility mode &quot;DISABLED&quot; restricts any additional schema versions from being added after the first schema version. For all other compatibility modes, validation of compatibility settings will be applied only from the second version onwards when the RegisterSchemaVersion API is used. When this API is called without a RegistryId, this will create an entry for a &quot;default-registry&quot; in the registry database tables, if it is not already present.
- Stability: stable
- Permissions: `glue:CreateSchema`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | object | no | This is a wrapper shape to contain the registry identity fields. If this is not provided, the default registry will be used. The ARN format for the same will be: arn:aws:glue:us-east-2:<customer id... |
  | schemaName | string | yes | Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace. |
  | dataFormat | string | yes | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | compatibility | string | no | The compatibility mode of the schema. The possible values are:    NONE: No compatibility mode applies. You can use this choice in development scenarios or if you do not know the compatibility mode ... |
  | description | string | no | An optional description of the schema. If description is not provided, there will not be any automatic default value for this. |
  | tags | any | no | Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API. If specified, follows the Amazon Web Services tags-on-create pattern. |
  | schemaDefinition | string | no | The schema definition using the DataFormat setting for SchemaName. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryName | string | The name of the registry. |
  | RegistryArn | string | The Amazon Resource Name (ARN) of the registry. |
  | SchemaName | string | The name of the schema. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | Description | string | A description of the schema if specified when created. |
  | DataFormat | string | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | Compatibility | string | The schema compatibility mode. |
  | SchemaCheckpoint | number | The version number of the checkpoint (the last time the compatibility mode was changed). |
  | LatestSchemaVersion | number | The latest version of the schema associated with the returned schema definition. |
  | NextSchemaVersion | number | The next version of the schema associated with the returned schema definition. |
  | SchemaStatus | string | The status of the schema. |
  | Tags | object | The tags for the schema. |
  | SchemaVersionId | string | The unique identifier of the first schema version. |
  | SchemaVersionStatus | string | The status of the first schema version created. |


## com.datadoghq.aws.glue.createScript
**Create script** — Transforms a directed acyclic graph (DAG) into code.
- Stability: stable
- Permissions: `glue:CreateScript`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dagNodes | array<object> | no | A list of the nodes in the DAG. |
  | dagEdges | array<object> | no | A list of the edges in the DAG. |
  | language | string | no | The programming language of the resulting code from the DAG. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | PythonScript | string | The Python script generated from the DAG. |
  | ScalaCode | string | The Scala code generated from the DAG. |


## com.datadoghq.aws.glue.createSecurityConfiguration
**Create security configuration** — Creates a new security configuration. A security configuration is a set of security properties that can be used by Glue. You can use a security configuration to encrypt data at rest. For information about using security configurations in Glue, see Encrypting Data Written by Crawlers, Jobs, and Development Endpoints.
- Stability: stable
- Permissions: `glue:CreateSecurityConfiguration`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name for the new security configuration. |
  | encryptionConfiguration | object | yes | The encryption configuration for the new security configuration. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name assigned to the new security configuration. |
  | CreatedTimestamp | string | The time at which the new security configuration was created. |


## com.datadoghq.aws.glue.createSession
**Create session** — Creates a new session.
- Stability: stable
- Permissions: `glue:CreateSession`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | id | string | yes | The ID of the session request. |
  | description | string | no | The description of the session. |
  | role | string | yes | The IAM Role ARN |
  | command | object | yes | The SessionCommand that runs the job. |
  | timeout | number | no | The number of minutes before session times out. Default for Spark ETL jobs is 48 hours (2880 minutes), the maximum session lifetime for this job type. Consult the documentation for other job types. |
  | idleTimeout | number | no | The number of minutes when idle before session times out. Default for Spark ETL jobs is value of Timeout. Consult the documentation for other job types. |
  | defaultArguments | object | no | A map array of key-value pairs. Max is 75 pairs. |
  | connections | object | no | The number of connections to use for the session. |
  | maxCapacity | number | no | The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory. |
  | numberOfWorkers | number | no | The number of workers of a defined WorkerType to use for the session. |
  | workerType | string | no | The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, or G.8X for Spark jobs. Accepts the value Z.2X for Ray notebooks.   For the G.1X worker type, e... |
  | securityConfiguration | string | no | The name of the SecurityConfiguration structure to be used with the session |
  | glueVersion | string | no | The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0. |
  | tags | any | no | The map of key value pairs (tags) belonging to the session. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Session | object | Returns the session object in the response. |


## com.datadoghq.aws.glue.createTable
**Create table** — Creates a new table definition in the Data Catalog.
- Stability: stable
- Permissions: `glue:CreateTable`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which to create the Table. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase. |
  | tableInput | object | yes | The TableInput object that defines the metadata table to create in the catalog. |
  | partitionIndexes | array<object> | no | A list of partition indexes, PartitionIndex structures, to create in the table. |
  | transactionId | string | no | The ID of the transaction. |
  | openTableFormatInput | object | no | Specifies an OpenTableFormatInput structure when creating an open format table. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createTableOptimizer
**Create table optimizer** — Creates a new table optimizer for a specific function. compaction is the only currently supported optimizer type.
- Stability: stable
- Permissions: `glue:CreateTableOptimizer`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | yes | The Catalog ID of the table. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. |
  | tableName | string | yes | The name of the table. |
  | type | string | yes | The type of table optimizer. Currently, the only valid value is compaction. |
  | tableOptimizerConfiguration | object | yes | A TableOptimizerConfiguration object representing the configuration of a table optimizer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createTrigger
**Create trigger** — Creates a new trigger.
- Stability: stable
- Permissions: `glue:CreateTrigger`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger. |
  | workflowName | string | no | The name of the workflow associated with the trigger. |
  | type | string | yes | The type of the new trigger. |
  | schedule | string | no | A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers. For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *). This fi... |
  | predicate | object | no | A predicate to specify when the new trigger should fire. This field is required when the trigger type is CONDITIONAL. |
  | actions | array<object> | yes | The actions initiated by this trigger when it fires. |
  | description | string | no | A description of the new trigger. |
  | startOnCreation | boolean | no | Set to true to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers. |
  | tags | any | no | The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in Glue, see Amazon Web Services Tags in Glue in the developer guide. |
  | eventBatchingCondition | object | no | Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the trigger. |


## com.datadoghq.aws.glue.createUsageProfile
**Create usage profile** — Creates a Glue usage profile.
- Stability: stable
- Permissions: `glue:CreateUsageProfile`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the usage profile. |
  | description | string | no | A description of the usage profile. |
  | configuration | object | yes | A ProfileConfiguration object specifying the job and session values for the profile. |
  | tags | any | no | A list of tags applied to the usage profile. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the usage profile that was created. |


## com.datadoghq.aws.glue.createUserDefinedFunction
**Create user defined function** — Creates a new function definition in the Data Catalog.
- Stability: stable
- Permissions: `glue:CreateUserDefinedFunction`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which to create the function. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which to create the function. |
  | functionInput | object | yes | A FunctionInput object that defines the function to create in the Data Catalog. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.createWorkflow
**Create workflow** — Creates a new workflow.
- Stability: stable
- Permissions: `glue:CreateWorkflow`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name to be assigned to the workflow. It should be unique within your account. |
  | description | string | no | A description of the workflow. |
  | defaultRunProperties | object | no | A collection of properties to be used as part of each execution of the workflow. |
  | tags | any | no | The tags to be used with this workflow. |
  | maxConcurrentRuns | number | no | You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs.... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the workflow which was provided as part of the request. |


## com.datadoghq.aws.glue.deleteBlueprint
**Delete blueprint** — Deletes an existing blueprint.
- Stability: stable
- Permissions: `glue:DeleteBlueprint`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the blueprint to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | Returns the name of the blueprint that was deleted. |


## com.datadoghq.aws.glue.deleteClassifier
**Delete classifier** — Removes a classifier from the Data Catalog.
- Stability: stable
- Permissions: `glue:DeleteClassifier`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the classifier to remove. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteColumnStatisticsForPartition
**Delete column statistics for partition** — Delete the partition column statistics of a column. The Identity and Access Management (IAM) permission required for this operation is DeletePartition.
- Stability: stable
- Permissions: `glue:DeleteColumnStatisticsForPartition`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | partitionValues | array<string> | yes | A list of partition values identifying the partition. |
  | columnName | string | yes | Name of the column. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteColumnStatisticsForTable
**Delete column statistics for table** — Retrieves table statistics of columns. The Identity and Access Management (IAM) permission required for this operation is DeleteTable.
- Stability: stable
- Permissions: `glue:DeleteColumnStatisticsForTable`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | columnName | string | yes | The name of the column. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteConnection
**Delete connection** — Deletes a connection from the Data Catalog.
- Stability: stable
- Permissions: `glue:DeleteConnection`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | connectionName | string | yes | The name of the connection to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteCrawler
**Delete crawler** — Removes a specified crawler from the Glue Data Catalog, unless the crawler state is RUNNING.
- Stability: stable
- Permissions: `glue:DeleteCrawler`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the crawler to remove. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteCustomEntityType
**Delete custom entity type** — Deletes a custom pattern by specifying its name.
- Stability: stable
- Permissions: `glue:DeleteCustomEntityType`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the custom pattern that you want to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the custom pattern you deleted. |


## com.datadoghq.aws.glue.deleteDataQualityRuleset
**Delete data quality ruleset** — Deletes a data quality ruleset.
- Stability: stable
- Permissions: `glue:DeleteDataQualityRuleset`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | A name for the data quality ruleset. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteDatabase
**Delete database** — Removes a specified database from a Data Catalog.  After completing this operation, you no longer have access to the tables (and all table versions and partitions that might belong to the tables) and the user-defined functions in the deleted database. Glue deletes these &quot;orphaned&quot; resources asynchronously in a timely manner, at the discretion of the service. To ensure the immediate deletion of all related resources, before calling DeleteDatabase, use DeleteTableVersion or BatchDeleteTableVersion, DeletePartition or BatchDeletePartition, DeleteUserDefinedFunction, and DeleteTable or BatchDeleteTable, to delete any resources that belong to the database.
- Stability: stable
- Permissions: `glue:DeleteDatabase`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the database resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | name | string | yes | The name of the database to delete. For Hive compatibility, this must be all lowercase. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteDevEndpoint
**Delete dev endpoint** — Deletes a specified development endpoint.
- Stability: stable
- Permissions: `glue:DeleteDevEndpoint`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | endpointName | string | yes | The name of the DevEndpoint. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteJob
**Delete job** — Deletes a specified job definition. If the job definition is not found, no exception is thrown.
- Stability: stable
- Permissions: `glue:DeleteJob`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobName | string | The name of the job definition that was deleted. |


## com.datadoghq.aws.glue.deleteMLTransform
**Delete mltransform** — Deletes a Glue machine learning transform. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue. If you no longer need a transform, you can delete it by calling DeleteMLTransforms. However, any Glue jobs that still reference the deleted transform will no longer succeed.
- Stability: stable
- Permissions: `glue:DeleteMLTransform`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the transform to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | The unique identifier of the transform that was deleted. |


## com.datadoghq.aws.glue.deletePartition
**Delete partition** — Deletes a specified partition.
- Stability: stable
- Permissions: `glue:DeletePartition`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the table in question resides. |
  | tableName | string | yes | The name of the table that contains the partition to be deleted. |
  | partitionValues | array<string> | yes | The values that define the partition. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deletePartitionIndex
**Delete partition index** — Deletes a specified partition index from an existing table.
- Stability: stable
- Permissions: `glue:DeletePartitionIndex`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The catalog ID where the table resides. |
  | databaseName | string | yes | Specifies the name of a database from which you want to delete a partition index. |
  | tableName | string | yes | Specifies the name of a table from which you want to delete a partition index. |
  | indexName | string | yes | The name of the partition index to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteRegistry
**Delete registry** — Delete the entire registry including schema and all of its versions. To get the status of the delete operation, you can call the GetRegistry API after the asynchronous call. Deleting a registry will deactivate all online operations for the registry such as the UpdateRegistry, CreateSchema, UpdateSchema, and RegisterSchemaVersion APIs.
- Stability: stable
- Permissions: `glue:DeleteRegistry`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | object | yes | This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryName | string | The name of the registry being deleted. |
  | RegistryArn | string | The Amazon Resource Name (ARN) of the registry being deleted. |
  | Status | string | The status of the registry. A successful operation will return the Deleting status. |


## com.datadoghq.aws.glue.deleteResourcePolicy
**Delete resource policy** — Deletes a specified policy.
- Stability: stable
- Permissions: `glue:DeleteResourcePolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | policyHashCondition | string | no | The hash value returned when this policy was set. |
  | resourceArn | string | no | The ARN of the Glue resource for the resource policy to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteSchema
**Delete schema** — Deletes the entire schema set, including the schema set and all of its versions. To get the status of the delete operation, you can call GetSchema API after the asynchronous call. Deleting a registry will deactivate all online operations for the schema, such as the GetSchemaByDefinition, and RegisterSchemaVersion APIs.
- Stability: stable
- Permissions: `glue:DeleteSchema`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema being deleted. |
  | SchemaName | string | The name of the schema being deleted. |
  | Status | string | The status of the schema. |


## com.datadoghq.aws.glue.deleteSchemaVersions
**Delete schema versions** — Remove versions from the specified schema. A version number or range may be supplied. If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS_FULL, an error is returned. Calling the GetSchemaVersions API after this call will list the status of the deleted versions. When the range of version numbers contains check pointed versions, the API will return a 409 conflict and will not proceed with the deletion. You have to remove the checkpoint first using the DeleteSchemaCheckpoint API before using this API. You cannot use the DeleteSchemaVersions API to delete the first schema version in the schema set. The first schema version can only be deleted by the DeleteSchema API. This operation will also delete the attached SchemaVersionMetadata under the schema versions. Hard deletes will be enforced on the database. If the compatibility mode forbids deleting of a version that is necessary, such as BACKWARDS_FULL, an error is returned.
- Stability: stable
- Permissions: `glue:DeleteSchemaVersions`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure that may contain the schema name and Amazon Resource Name (ARN). |
  | versions | string | yes | A version range may be supplied which may be of the format:   a single version number, 5   a range, 5-8 : deletes versions 5, 6, 7, 8 |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaVersionErrors | array<object> | A list of SchemaVersionErrorItem objects, each containing an error and schema version. |


## com.datadoghq.aws.glue.deleteSecurityConfiguration
**Delete security configuration** — Deletes a specified security configuration.
- Stability: stable
- Permissions: `glue:DeleteSecurityConfiguration`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the security configuration to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteSession
**Delete session** — Deletes the session.
- Stability: stable
- Permissions: `glue:DeleteSession`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | id | string | yes | The ID of the session to be deleted. |
  | requestOrigin | string | no | The name of the origin of the delete session request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Id | string | Returns the ID of the deleted session. |


## com.datadoghq.aws.glue.deleteTable
**Delete table** — Removes a table definition from the Data Catalog.  After completing this operation, you no longer have access to the table versions and partitions that belong to the deleted table. Glue deletes these &quot;orphaned&quot; resources asynchronously in a timely manner, at the discretion of the service. To ensure the immediate deletion of all related resources, before calling DeleteTable, use DeleteTableVersion or BatchDeleteTableVersion, and DeletePartition or BatchDeletePartition, to delete any resources that belong to the table.
- Stability: stable
- Permissions: `glue:DeleteTable`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | name | string | yes | The name of the table to be deleted. For Hive compatibility, this name is entirely lowercase. |
  | transactionId | string | no | The transaction ID at which to delete the table contents. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteTableOptimizer
**Delete table optimizer** — Deletes an optimizer and all associated metadata for a table. The optimization will no longer be performed on the table.
- Stability: stable
- Permissions: `glue:DeleteTableOptimizer`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | yes | The Catalog ID of the table. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. |
  | tableName | string | yes | The name of the table. |
  | type | string | yes | The type of table optimizer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteTableVersion
**Delete table version** — Deletes a specified version of a table.
- Stability: stable
- Permissions: `glue:DeleteTableVersion`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | tableName | string | yes | The name of the table. For Hive compatibility, this name is entirely lowercase. |
  | versionId | string | yes | The ID of the table version to be deleted. A VersionID is a string representation of an integer. Each version is incremented by 1. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteTrigger
**Delete trigger** — Deletes a specified trigger. If the trigger is not found, no exception is thrown.
- Stability: stable
- Permissions: `glue:DeleteTrigger`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the trigger that was deleted. |


## com.datadoghq.aws.glue.deleteUsageProfile
**Delete usage profile** — Deletes the Glue specified usage profile.
- Stability: stable
- Permissions: `glue:DeleteUsageProfile`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the usage profile to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteUserDefinedFunction
**Delete user defined function** — Deletes an existing function definition from the Data Catalog.
- Stability: stable
- Permissions: `glue:DeleteUserDefinedFunction`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the function to be deleted is located. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the function is located. |
  | functionName | string | yes | The name of the function definition to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.deleteWorkflow
**Delete workflow** — Deletes a workflow.
- Stability: stable
- Permissions: `glue:DeleteWorkflow`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow to be deleted. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | Name of the workflow specified in input. |


## com.datadoghq.aws.glue.getBlueprint
**Get blueprint** — Retrieves the details of a blueprint.
- Stability: stable
- Permissions: `glue:GetBlueprint`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the blueprint. |
  | includeBlueprint | boolean | no | Specifies whether or not to include the blueprint in the response. |
  | includeParameterSpec | boolean | no | Specifies whether or not to include the parameter specification. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Blueprint | object | Returns a Blueprint object. |


## com.datadoghq.aws.glue.getBlueprintRun
**Get blueprint run** — Retrieves the details of a blueprint run.
- Stability: stable
- Permissions: `glue:GetBlueprintRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | blueprintName | string | yes | The name of the blueprint. |
  | runId | string | yes | The run ID for the blueprint run you want to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | BlueprintRun | object | Returns a BlueprintRun object. |


## com.datadoghq.aws.glue.getBlueprintRuns
**Get blueprint runs** — Retrieves the details of blueprint runs for a specified blueprint.
- Stability: stable
- Permissions: `glue:GetBlueprintRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | blueprintName | string | yes | The name of the blueprint. |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | BlueprintRuns | array<object> | Returns a list of BlueprintRun objects. |
  | NextToken | string | A continuation token, if not all blueprint runs have been returned. |


## com.datadoghq.aws.glue.getCatalogImportStatus
**Get catalog import status** — Retrieves the status of a migration operation.
- Stability: stable
- Permissions: `glue:GetCatalogImportStatus`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the catalog to migrate. Currently, this should be the Amazon Web Services account ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ImportStatus | object | The status of the specified catalog migration. |


## com.datadoghq.aws.glue.getClassifier
**Get classifier** — Retrieve a classifier by name.
- Stability: stable
- Permissions: `glue:GetClassifier`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the classifier to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Classifier | object | The requested classifier. |


## com.datadoghq.aws.glue.getClassifiers
**Get classifiers** — Lists all classifier objects in the Data Catalog.
- Stability: stable
- Permissions: `glue:GetClassifiers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The size of the list to return (optional). |
  | nextToken | string | no | An optional continuation token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Classifiers | array<object> | The requested list of classifier objects. |
  | NextToken | string | A continuation token. |


## com.datadoghq.aws.glue.getColumnStatisticsForPartition
**Get column statistics for partition** — Retrieves partition statistics of columns. The Identity and Access Management (IAM) permission required for this operation is GetPartition.
- Stability: stable
- Permissions: `glue:GetColumnStatisticsForPartition`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | partitionValues | array<string> | yes | A list of partition values identifying the partition. |
  | columnNames | array<string> | yes | A list of the column names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsList | array<object> | List of ColumnStatistics that failed to be retrieved. |
  | Errors | array<object> | Error occurred during retrieving column statistics data. |


## com.datadoghq.aws.glue.getColumnStatisticsForTable
**Get column statistics for table** — Retrieves table statistics of columns. The Identity and Access Management (IAM) permission required for this operation is GetTable.
- Stability: stable
- Permissions: `glue:GetColumnStatisticsForTable`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | columnNames | array<string> | yes | A list of the column names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsList | array<object> | List of ColumnStatistics. |
  | Errors | array<object> | List of ColumnStatistics that failed to be retrieved. |


## com.datadoghq.aws.glue.getColumnStatisticsTaskRun
**Get column statistics task run** — Get the associated metadata or information for a task run, given a task run ID.
- Stability: stable
- Permissions: `glue:GetColumnStatisticsTaskRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | columnStatisticsTaskRunId | string | yes | The identifier for the particular column statistics task run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsTaskRun | object | A ColumnStatisticsTaskRun object representing the details of the column stats run. |


## com.datadoghq.aws.glue.getColumnStatisticsTaskRuns
**Get column statistics task runs** — Retrieves information about all runs associated with the specified table.
- Stability: stable
- Permissions: `glue:GetColumnStatisticsTaskRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | databaseName | string | yes | The name of the database where the table resides. |
  | tableName | string | yes | The name of the table. |
  | maxResults | number | no | The maximum size of the response. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsTaskRuns | array<object> | A list of column statistics task runs. |
  | NextToken | string | A continuation token, if not all task runs have yet been returned. |


## com.datadoghq.aws.glue.getConnection
**Get connection** — Retrieves a connection definition from the Data Catalog.
- Stability: stable
- Permissions: `glue:GetConnection`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | name | string | yes | The name of the connection definition to retrieve. |
  | hidePassword | boolean | no | Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Connection | object | The requested connection definition. |


## com.datadoghq.aws.glue.getConnections
**Get connections** — Retrieves a list of connection definitions from the Data Catalog.
- Stability: stable
- Permissions: `glue:GetConnections`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | filter | object | no | A filter that controls which connections are returned. |
  | hidePassword | boolean | no | Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this ... |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | maxResults | number | no | The maximum number of connections to return in one response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ConnectionList | array<object> | A list of requested connection definitions. |
  | NextToken | string | A continuation token, if the list of connections returned does not include the last of the filtered connections. |


## com.datadoghq.aws.glue.getCrawler
**Get crawler** — Retrieves metadata for a specified crawler.
- Stability: stable
- Permissions: `glue:GetCrawler`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the crawler to retrieve metadata for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Crawler | object | The metadata for the specified crawler. |


## com.datadoghq.aws.glue.getCrawlerMetrics
**Get crawler metrics** — Retrieves metrics about specified crawlers.
- Stability: stable
- Permissions: `glue:GetCrawlerMetrics`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerNameList | array<string> | no | A list of the names of crawlers about which to retrieve metrics. |
  | maxResults | number | no | The maximum size of a list to return. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CrawlerMetricsList | array<object> | A list of metrics for the specified crawler. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.getCrawlers
**Get crawlers** — Retrieves metadata for all crawlers defined in the customer account.
- Stability: stable
- Permissions: `glue:GetCrawlers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The number of crawlers to return on each call. |
  | nextToken | string | no | A continuation token, if this is a continuation request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Crawlers | array<object> | A list of crawler metadata. |
  | NextToken | string | A continuation token, if the returned list has not reached the end of those defined in this customer account. |


## com.datadoghq.aws.glue.getCustomEntityType
**Get custom entity type** — Retrieves the details of a custom pattern by specifying its name.
- Stability: stable
- Permissions: `glue:GetCustomEntityType`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the custom pattern that you want to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the custom pattern that you retrieved. |
  | RegexString | string | A regular expression string that is used for detecting sensitive data in a custom pattern. |
  | ContextWords | array<string> | A list of context words if specified when you created the custom pattern. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sen... |


## com.datadoghq.aws.glue.getDataCatalogEncryptionSettings
**Get data catalog encryption settings** — Retrieves the security configuration for a specified catalog.
- Stability: stable
- Permissions: `glue:GetDataCatalogEncryptionSettings`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog to retrieve the security configuration for. If none is provided, the Amazon Web Services account ID is used by default. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DataCatalogEncryptionSettings | object | The requested security configuration. |


## com.datadoghq.aws.glue.getDataQualityModel
**Get data quality model** — Retrieve the training status of the model along with more information (CompletedOn, StartedOn, FailureReason).
- Stability: stable
- Permissions: `glue:GetDataQualityModel`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | statisticId | string | no | The Statistic ID. |
  | profileId | string | yes | The Profile ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Status | string | The training status of the data quality model. |
  | StartedOn | string | The timestamp when the data quality model training started. |
  | CompletedOn | string | The timestamp when the data quality model training completed. |
  | FailureReason | string | The training failure reason. |


## com.datadoghq.aws.glue.getDataQualityModelResult
**Get data quality model result** — Retrieve a statistic&#x27;s predictions for a given Profile ID.
- Stability: stable
- Permissions: `glue:GetDataQualityModelResult`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | statisticId | string | yes | The Statistic ID. |
  | profileId | string | yes | The Profile ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CompletedOn | string | The timestamp when the data quality model training completed. |
  | Model | array<object> | A list of StatisticModelResult |


## com.datadoghq.aws.glue.getDataQualityResult
**Get data quality result** — Retrieves the result of a data quality rule evaluation.
- Stability: stable
- Permissions: `glue:GetDataQualityResult`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resultId | string | yes | A unique result ID for the data quality result. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ResultId | string | A unique result ID for the data quality result. |
  | ProfileId | string | The Profile ID for the data quality result. |
  | Score | number | An aggregate data quality score. Represents the ratio of rules that passed to the total number of rules. |
  | DataSource | object | The table associated with the data quality result, if any. |
  | RulesetName | string | The name of the ruleset associated with the data quality result. |
  | EvaluationContext | string | In the context of a job in Glue Studio, each node in the canvas is typically assigned some sort of name and data quality nodes will have names. In the case of multiple nodes, the evaluationContext ... |
  | StartedOn | string | The date and time when the run for this data quality result started. |
  | CompletedOn | string | The date and time when the run for this data quality result was completed. |
  | JobName | string | The job name associated with the data quality result, if any. |
  | JobRunId | string | The job run ID associated with the data quality result, if any. |
  | RulesetEvaluationRunId | string | The unique run ID associated with the ruleset evaluation. |
  | RuleResults | array<object> | A list of DataQualityRuleResult objects representing the results for each rule. |
  | AnalyzerResults | array<object> | A list of DataQualityAnalyzerResult objects representing the results for each analyzer. |
  | Observations | array<object> | A list of DataQualityObservation objects representing the observations generated after evaluating the rules and analyzers. |


## com.datadoghq.aws.glue.getDataQualityRuleRecommendationRun
**Get data quality rule recommendation run** — Gets the specified recommendation run that was used to generate rules.
- Stability: stable
- Permissions: `glue:GetDataQualityRuleRecommendationRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | runId | string | yes | The unique run identifier associated with this run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The unique run identifier associated with this run. |
  | DataSource | object | The data source (an Glue table) associated with this run. |
  | Role | string | An IAM role supplied to encrypt the results of the run. |
  | NumberOfWorkers | number | The number of G.1X workers to be used in the run. The default is 5. |
  | Timeout | number | The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). |
  | Status | string | The status for this run. |
  | ErrorString | string | The error strings that are associated with the run. |
  | StartedOn | string | The date and time when this run started. |
  | LastModifiedOn | string | A timestamp. The last point in time when this data quality rule recommendation run was modified. |
  | CompletedOn | string | The date and time when this run was completed. |
  | ExecutionTime | number | The amount of time (in seconds) that the run consumed resources. |
  | RecommendedRuleset | string | When a start rule recommendation run completes, it creates a recommended ruleset (a set of rules). This member has those rules in Data Quality Definition Language (DQDL) format. |
  | CreatedRulesetName | string | The name of the ruleset that was created by the run. |
  | DataQualitySecurityConfiguration | string | The name of the security configuration created with the data quality encryption option. |


## com.datadoghq.aws.glue.getDataQualityRuleset
**Get data quality ruleset** — Returns an existing ruleset by identifier or name.
- Stability: stable
- Permissions: `glue:GetDataQualityRuleset`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the ruleset. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the ruleset. |
  | Description | string | A description of the ruleset. |
  | Ruleset | string | A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide. |
  | TargetTable | object | The name and database name of the target table. |
  | CreatedOn | string | A timestamp. The time and date that this data quality ruleset was created. |
  | LastModifiedOn | string | A timestamp. The last point in time when this data quality ruleset was modified. |
  | RecommendationRunId | string | When a ruleset was created from a recommendation run, this run ID is generated to link the two together. |
  | DataQualitySecurityConfiguration | string | The name of the security configuration created with the data quality encryption option. |


## com.datadoghq.aws.glue.getDataQualityRulesetEvaluationRun
**Get data quality ruleset evaluation run** — Retrieves a specific run where a ruleset is evaluated against a data source.
- Stability: stable
- Permissions: `glue:GetDataQualityRulesetEvaluationRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | runId | string | yes | The unique run identifier associated with this run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The unique run identifier associated with this run. |
  | DataSource | object | The data source (an Glue table) associated with this evaluation run. |
  | Role | string | An IAM role supplied to encrypt the results of the run. |
  | NumberOfWorkers | number | The number of G.1X workers to be used in the run. The default is 5. |
  | Timeout | number | The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). |
  | AdditionalRunOptions | object | Additional run options you can specify for an evaluation run. |
  | Status | string | The status for this run. |
  | ErrorString | string | The error strings that are associated with the run. |
  | StartedOn | string | The date and time when this run started. |
  | LastModifiedOn | string | A timestamp. The last point in time when this data quality rule recommendation run was modified. |
  | CompletedOn | string | The date and time when this run was completed. |
  | ExecutionTime | number | The amount of time (in seconds) that the run consumed resources. |
  | RulesetNames | array<string> | A list of ruleset names for the run. Currently, this parameter takes only one Ruleset name. |
  | ResultIds | array<string> | A list of result IDs for the data quality results for the run. |
  | AdditionalDataSources | object | A map of reference strings to additional data sources you can specify for an evaluation run. |


## com.datadoghq.aws.glue.getDatabase
**Get database** — Retrieves the definition of a specified database.
- Stability: stable
- Permissions: `glue:GetDatabase`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the database resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | name | string | yes | The name of the database to retrieve. For Hive compatibility, this should be all lowercase. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Database | object | The definition of the specified database in the Data Catalog. |


## com.datadoghq.aws.glue.getDatabases
**Get databases** — Retrieves all databases defined in a given Data Catalog.
- Stability: stable
- Permissions: `glue:GetDatabases`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog from which to retrieve Databases. If none is provided, the Amazon Web Services account ID is used by default. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | maxResults | number | no | The maximum number of databases to return in one response. |
  | resourceShareType | string | no | Allows you to specify that you want to list the databases shared with your account. The allowable values are FEDERATED, FOREIGN or ALL.    If set to FEDERATED, will list the federated databases (re... |
  | attributesToGet | array<string> | no | Specifies the database fields returned by the GetDatabases call. This parameter doesn’t accept an empty list. The request must include the NAME. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DatabaseList | array<object> | A list of Database objects from the specified catalog. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.getDataflowGraph
**Get dataflow graph** — Transforms a Python script into a directed acyclic graph (DAG).
- Stability: stable
- Permissions: `glue:GetDataflowGraph`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | pythonScript | string | no | The Python script to transform. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DagNodes | array<object> | A list of the nodes in the resulting DAG. |
  | DagEdges | array<object> | A list of the edges in the resulting DAG. |


## com.datadoghq.aws.glue.getDevEndpoint
**Get dev endpoint** — Retrieves information about a specified development endpoint.  When you create a development endpoint in a virtual private cloud (VPC), Glue returns only a private IP address, and the public IP address field is not populated. When you create a non-VPC development endpoint, Glue returns only a public IP address.
- Stability: stable
- Permissions: `glue:GetDevEndpoint`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | endpointName | string | yes | Name of the DevEndpoint to retrieve information for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DevEndpoint | object | A DevEndpoint definition. |


## com.datadoghq.aws.glue.getDevEndpoints
**Get dev endpoints** — Retrieves all the development endpoints in this Amazon Web Services account.  When you create a development endpoint in a virtual private cloud (VPC), Glue returns only a private IP address and the public IP address field is not populated. When you create a non-VPC development endpoint, Glue returns only a public IP address.
- Stability: stable
- Permissions: `glue:GetDevEndpoints`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum size of information to return. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DevEndpoints | array<object> | A list of DevEndpoint definitions. |
  | NextToken | string | A continuation token, if not all DevEndpoint definitions have yet been returned. |


## com.datadoghq.aws.glue.getJob
**Get job** — Retrieves an existing job definition.
- Stability: stable
- Permissions: `glue:GetJob`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Job | object | The requested job definition. |


## com.datadoghq.aws.glue.getJobBookmark
**Get job bookmark** — Returns information on a job bookmark entry. For more information about enabling and using job bookmarks, see Tracking processed data using job bookmarks, Job parameters used by Glue, and Job structure.
- Stability: stable
- Permissions: `glue:GetJobBookmark`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job in question. |
  | runId | string | no | The unique run identifier associated with this job run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobBookmarkEntry | object | A structure that defines a point that a job can resume processing. |


## com.datadoghq.aws.glue.getJobRun
**Get job run** — Retrieves the metadata for a given job run. Job run history is accessible for 90 days for your workflow and job run.
- Stability: stable
- Permissions: `glue:GetJobRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | Name of the job definition being run. |
  | runId | string | yes | The ID of the job run. |
  | predecessorsIncluded | boolean | no | True if a list of predecessor runs should be returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobRun | object | The requested job-run metadata. |


## com.datadoghq.aws.glue.getJobRuns
**Get job runs** — Retrieves metadata for all runs of a given job definition.
- Stability: stable
- Permissions: `glue:GetJobRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition for which to retrieve all job runs. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | maxResults | number | no | The maximum size of the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobRuns | array<object> | A list of job-run metadata objects. |
  | NextToken | string | A continuation token, if not all requested job runs have been returned. |


## com.datadoghq.aws.glue.getJobs
**Get jobs** — Retrieves all current job definitions.
- Stability: stable
- Permissions: `glue:GetJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | maxResults | number | no | The maximum size of the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Jobs | array<object> | A list of job definitions. |
  | NextToken | string | A continuation token, if not all job definitions have yet been returned. |


## com.datadoghq.aws.glue.getMLTaskRun
**Get mltask run** — Gets details for a specific task run on a machine learning transform. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can check the stats of any task run by calling GetMLTaskRun with the TaskRunID and its parent transform&#x27;s TransformID.
- Stability: stable
- Permissions: `glue:GetMLTaskRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | taskRunId | string | yes | The unique identifier of the task run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | The unique identifier of the task run. |
  | TaskRunId | string | The unique run identifier associated with this run. |
  | Status | string | The status for this task run. |
  | LogGroupName | string | The names of the log groups that are associated with the task run. |
  | Properties | object | The list of properties that are associated with the task run. |
  | ErrorString | string | The error strings that are associated with the task run. |
  | StartedOn | string | The date and time when this task run started. |
  | LastModifiedOn | string | The date and time when this task run was last modified. |
  | CompletedOn | string | The date and time when this task run was completed. |
  | ExecutionTime | number | The amount of time (in seconds) that the task run consumed resources. |


## com.datadoghq.aws.glue.getMLTaskRuns
**Get mltask runs** — Gets a list of runs for a machine learning transform. Machine learning task runs are asynchronous tasks that Glue runs on your behalf as part of various machine learning workflows. You can get a sortable, filterable list of machine learning task runs by calling GetMLTaskRuns with their parent transform&#x27;s TransformID and other optional parameters as documented in this section. This operation returns a list of historic runs and must be paginated.
- Stability: stable
- Permissions: `glue:GetMLTaskRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | nextToken | string | no | A token for pagination of the results. The default is empty. |
  | maxResults | number | no | The maximum number of results to return. |
  | filter | object | no | The filter criteria, in the TaskRunFilterCriteria structure, for the task run. |
  | sort | object | no | The sorting criteria, in the TaskRunSortCriteria structure, for the task run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskRuns | array<object> | A list of task runs that are associated with the transform. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.getMLTransform
**Get mltransform** — Gets a Glue machine learning transform artifact and all its corresponding metadata. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue. You can retrieve their metadata by calling GetMLTransform.
- Stability: stable
- Permissions: `glue:GetMLTransform`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the transform, generated at the time that the transform was created. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | The unique identifier of the transform, generated at the time that the transform was created. |
  | Name | string | The unique name given to the transform when it was created. |
  | Description | string | A description of the transform. |
  | Status | string | The last known status of the transform (to indicate whether it can be used or not). One of "NOT_READY", "READY", or "DELETING". |
  | CreatedOn | string | The date and time when the transform was created. |
  | LastModifiedOn | string | The date and time when the transform was last modified. |
  | InputRecordTables | array<object> | A list of Glue table definitions used by the transform. |
  | Parameters | object | The configuration parameters that are specific to the algorithm used. |
  | EvaluationMetrics | object | The latest evaluation metrics. |
  | LabelCount | number | The number of labels available for this transform. |
  | Schema | array<object> | The Map<Column, Type> object that represents the schema that this transform accepts. Has an upper bound of 100 columns. |
  | Role | string | The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. |
  | GlueVersion | string | This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults ... |
  | MaxCapacity | number | The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing... |
  | WorkerType | string | The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.   For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 5... |
  | NumberOfWorkers | number | The number of workers of a defined workerType that are allocated when this task runs. |
  | Timeout | number | The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The de... |
  | MaxRetries | number | The maximum number of times to retry a task for this transform after a task run fails. |
  | TransformEncryption | object | The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS. |


## com.datadoghq.aws.glue.getMLTransforms
**Get mltransforms** — Gets a sortable, filterable list of existing Glue machine learning transforms. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by Glue, and you can retrieve their metadata by calling GetMLTransforms.
- Stability: stable
- Permissions: `glue:GetMLTransforms`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |
  | filter | object | no | The filter transformation criteria. |
  | sort | object | no | The sorting criteria. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Transforms | array<object> | A list of machine learning transforms. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.getMapping
**Get mapping** — Creates mappings.
- Stability: stable
- Permissions: `glue:GetMapping`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | source | object | yes | Specifies the source table. |
  | sinks | array<object> | no | A list of target tables. |
  | location | object | no | Parameters for the mapping. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Mapping | array<object> | A list of mappings to the specified targets. |


## com.datadoghq.aws.glue.getPartition
**Get partition** — Retrieves information about a specified partition.
- Stability: stable
- Permissions: `glue:GetPartition`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partition in question resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partition resides. |
  | tableName | string | yes | The name of the partition's table. |
  | partitionValues | array<string> | yes | The values that define the partition. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Partition | object | The requested information, in the form of a Partition object. |


## com.datadoghq.aws.glue.getPartitionIndexes
**Get partition indexes** — Retrieves the partition indexes associated with a table.
- Stability: stable
- Permissions: `glue:GetPartitionIndexes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The catalog ID where the table resides. |
  | databaseName | string | yes | Specifies the name of a database from which you want to retrieve partition indexes. |
  | tableName | string | yes | Specifies the name of a table for which you want to retrieve the partition indexes. |
  | nextToken | string | no | A continuation token, included if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | PartitionIndexDescriptorList | array<object> | A list of index descriptors. |
  | NextToken | string | A continuation token, present if the current list segment is not the last. |


## com.datadoghq.aws.glue.getPartitions
**Get partitions** — Retrieves information about the partitions in a table.
- Stability: stable
- Permissions: `glue:GetPartitions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | expression | string | no | An expression that filters the partitions to be returned. The expression uses SQL syntax similar to the SQL WHERE filter clause. The SQL statement parser JSQLParser parses the expression.   Operato... |
  | nextToken | string | no | A continuation token, if this is not the first call to retrieve these partitions. |
  | segment | object | no | The segment of the table's partitions to scan in this request. |
  | maxResults | number | no | The maximum number of partitions to return in a single response. |
  | excludeColumnSchema | boolean | no | When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the prob... |
  | transactionId | string | no | The transaction ID at which to read the partition contents. |
  | queryAsOfTime | string | no | The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with TransactionId. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Partitions | array<object> | A list of requested partitions. |
  | NextToken | string | A continuation token, if the returned list of partitions does not include the last one. |


## com.datadoghq.aws.glue.getRegistry
**Get registry** — Describes the specified registry in detail.
- Stability: stable
- Permissions: `glue:GetRegistry`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | object | yes | This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryName | string | The name of the registry. |
  | RegistryArn | string | The Amazon Resource Name (ARN) of the registry. |
  | Description | string | A description of the registry. |
  | Status | string | The status of the registry. |
  | CreatedTime | string | The date and time the registry was created. |
  | UpdatedTime | string | The date and time the registry was updated. |


## com.datadoghq.aws.glue.getResourcePolicies
**Get resource policies** — Retrieves the resource policies set on individual resources by Resource Access Manager during cross-account permission grants. Also retrieves the Data Catalog resource policy. If you enabled metadata encryption in Data Catalog settings, and you do not have permission on the KMS key, the operation can&#x27;t return the Data Catalog resource policy.
- Stability: stable
- Permissions: `glue:GetResourcePolicies`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | GetResourcePoliciesResponseList | array<object> | A list of the individual resource policies and the account-level resource policy. |
  | NextToken | string | A continuation token, if the returned list does not contain the last resource policy available. |


## com.datadoghq.aws.glue.getResourcePolicy
**Get resource policy** — Retrieves a specified resource policy.
- Stability: stable
- Permissions: `glue:GetResourcePolicy`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | no | The ARN of the Glue resource for which to retrieve the resource policy. If not supplied, the Data Catalog resource policy is returned. Use GetResourcePolicies to view all existing resource policies... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | PolicyInJson | string | Contains the requested policy document, in JSON format. |
  | PolicyHash | string | Contains the hash value associated with this policy. |
  | CreateTime | string | The date and time at which the policy was created. |
  | UpdateTime | string | The date and time at which the policy was last updated. |


## com.datadoghq.aws.glue.getSchema
**Get schema** — Describes the specified schema in detail.
- Stability: stable
- Permissions: `glue:GetSchema`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either SchemaArn or SchemaName and Registr... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryName | string | The name of the registry. |
  | RegistryArn | string | The Amazon Resource Name (ARN) of the registry. |
  | SchemaName | string | The name of the schema. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | Description | string | A description of schema if specified when created |
  | DataFormat | string | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | Compatibility | string | The compatibility mode of the schema. |
  | SchemaCheckpoint | number | The version number of the checkpoint (the last time the compatibility mode was changed). |
  | LatestSchemaVersion | number | The latest version of the schema associated with the returned schema definition. |
  | NextSchemaVersion | number | The next version of the schema associated with the returned schema definition. |
  | SchemaStatus | string | The status of the schema. |
  | CreatedTime | string | The date and time the schema was created. |
  | UpdatedTime | string | The date and time the schema was updated. |


## com.datadoghq.aws.glue.getSchemaByDefinition
**Get schema by definition** — Retrieves a schema by the SchemaDefinition. The schema definition is sent to the Schema Registry, canonicalized, and hashed. If the hash is matched within the scope of the SchemaName or ARN (or the default registry, if none is supplied), that schema’s metadata is returned. Otherwise, a 404 or NotFound error is returned. Schema versions in Deleted statuses will not be included in the results.
- Stability: stable
- Permissions: `glue:GetSchemaByDefinition`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of SchemaArn or SchemaName has to be p... |
  | schemaDefinition | string | yes | The definition of the schema for which schema details are required. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaVersionId | string | The schema ID of the schema version. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | DataFormat | string | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | Status | string | The status of the schema version. |
  | CreatedTime | string | The date and time the schema was created. |


## com.datadoghq.aws.glue.getSchemaVersion
**Get schema version** — Get the specified schema by its unique ID assigned when a version of the schema is created or registered. Schema versions in Deleted status will not be included in the results.
- Stability: stable
- Permissions: `glue:GetSchemaVersion`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | no | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either SchemaArn or SchemaName and Registr... |
  | schemaVersionId | string | no | The SchemaVersionId of the schema version. This field is required for fetching by schema ID. Either this or the SchemaId wrapper has to be provided. |
  | schemaVersionNumber | object | no | The version number of the schema. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaVersionId | string | The SchemaVersionId of the schema version. |
  | SchemaDefinition | string | The schema definition for the schema ID. |
  | DataFormat | string | The data format of the schema definition. Currently AVRO, JSON and PROTOBUF are supported. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | VersionNumber | number | The version number of the schema. |
  | Status | string | The status of the schema version. |
  | CreatedTime | string | The date and time the schema version was created. |


## com.datadoghq.aws.glue.getSchemaVersionsDiff
**Get schema versions diff** — Fetches the schema version difference in the specified difference type between two stored schema versions in the Schema Registry. This API allows you to compare two schema versions between two schema definitions under the same schema.
- Stability: stable
- Permissions: `glue:GetSchemaVersionsDiff`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of SchemaArn or SchemaName has to be p... |
  | firstSchemaVersionNumber | object | yes | The first of the two schema versions to be compared. |
  | secondSchemaVersionNumber | object | yes | The second of the two schema versions to be compared. |
  | schemaDiffType | string | yes | Refers to SYNTAX_DIFF, which is the currently supported diff type. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Diff | string | The difference between schemas as a string in JsonPatch format. |


## com.datadoghq.aws.glue.getSecurityConfiguration
**Get security configuration** — Retrieves a specified security configuration.
- Stability: stable
- Permissions: `glue:GetSecurityConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the security configuration to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SecurityConfiguration | object | The requested security configuration. |


## com.datadoghq.aws.glue.getSecurityConfigurations
**Get security configurations** — Retrieves a list of all security configurations.
- Stability: stable
- Permissions: `glue:GetSecurityConfigurations`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum number of results to return. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SecurityConfigurations | array<object> | A list of security configurations. |
  | NextToken | string | A continuation token, if there are more security configurations to return. |


## com.datadoghq.aws.glue.getSession
**Get session** — Retrieves the session.
- Stability: stable
- Permissions: `glue:GetSession`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | id | string | yes | The ID of the session. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Session | object | The session object is returned in the response. |


## com.datadoghq.aws.glue.getStatement
**Get statement** — Retrieves the statement.
- Stability: stable
- Permissions: `glue:GetStatement`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sessionId | string | yes | The Session ID of the statement. |
  | id | number | yes | The Id of the statement. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Statement | object | Returns the statement. |


## com.datadoghq.aws.glue.getTable
**Get table** — Retrieves the Table definition in a Data Catalog for a specified table.
- Stability: stable
- Permissions: `glue:GetTable`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | name | string | yes | The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase. |
  | transactionId | string | no | The transaction ID at which to read the table contents. |
  | queryAsOfTime | string | no | The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with TransactionId. |
  | includeStatusDetails | boolean | no | Specifies whether to include status details related to a request to create or update an Glue Data Catalog view. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Table | object | The Table object that defines the specified table. |


## com.datadoghq.aws.glue.getTableOptimizer
**Get table optimizer** — Returns the configuration of all optimizers associated with a specified table.
- Stability: stable
- Permissions: `glue:GetTableOptimizer`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | yes | The Catalog ID of the table. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. |
  | tableName | string | yes | The name of the table. |
  | type | string | yes | The type of table optimizer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CatalogId | string | The Catalog ID of the table. |
  | DatabaseName | string | The name of the database in the catalog in which the table resides. |
  | TableName | string | The name of the table. |
  | TableOptimizer | object | The optimizer associated with the specified table. |


## com.datadoghq.aws.glue.getTableVersion
**Get table version** — Retrieves a specified version of a table.
- Stability: stable
- Permissions: `glue:GetTableVersion`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | tableName | string | yes | The name of the table. For Hive compatibility, this name is entirely lowercase. |
  | versionId | string | no | The ID value of the table version to be retrieved. A VersionID is a string representation of an integer. Each version is incremented by 1. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TableVersion | object | The requested table version. |


## com.datadoghq.aws.glue.getTableVersions
**Get table versions** — Retrieves a list of strings that identify available versions of a specified table.
- Stability: stable
- Permissions: `glue:GetTableVersions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | tableName | string | yes | The name of the table. For Hive compatibility, this name is entirely lowercase. |
  | nextToken | string | no | A continuation token, if this is not the first call. |
  | maxResults | number | no | The maximum number of table versions to return in one response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TableVersions | array<object> | A list of strings identifying available versions of the specified table. |
  | NextToken | string | A continuation token, if the list of available versions does not include the last one. |


## com.datadoghq.aws.glue.getTables
**Get tables** — Retrieves the definitions of some or all of the tables in a given Database.
- Stability: stable
- Permissions: `glue:GetTables`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase. |
  | expression | string | no | A regular expression pattern. If present, only those tables whose names match the pattern are returned. |
  | nextToken | string | no | A continuation token, included if this is a continuation call. |
  | maxResults | number | no | The maximum number of tables to return in a single response. |
  | transactionId | string | no | The transaction ID at which to read the table contents. |
  | queryAsOfTime | string | no | The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with TransactionId. |
  | includeStatusDetails | boolean | no | Specifies whether to include status details related to a request to create or update an Glue Data Catalog view. |
  | attributesToGet | array<string> | no | Specifies the table fields returned by the GetTables call. This parameter doesn’t accept an empty list. The request must include NAME. The following are the valid combinations of values:    NAME - ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TableList | array<object> | A list of the requested Table objects. |
  | NextToken | string | A continuation token, present if the current list segment is not the last. |


## com.datadoghq.aws.glue.getTags
**Get tags** — Retrieves a list of tags associated with a resource.
- Stability: stable
- Permissions: `glue:GetTags`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource for which to retrieve tags. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Tags | object | The requested tags. |


## com.datadoghq.aws.glue.getTrigger
**Get trigger** — Retrieves the definition of a trigger.
- Stability: stable
- Permissions: `glue:GetTrigger`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Trigger | object | The requested trigger definition. |


## com.datadoghq.aws.glue.getTriggers
**Get triggers** — Gets all the triggers associated with a job.
- Stability: stable
- Permissions: `glue:GetTriggers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | dependentJobName | string | no | The name of the job to retrieve triggers for. The trigger that can start this job is returned, and if there is no such trigger, all triggers are returned. |
  | maxResults | number | no | The maximum size of the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Triggers | array<object> | A list of triggers for the specified job. |
  | NextToken | string | A continuation token, if not all the requested triggers have yet been returned. |


## com.datadoghq.aws.glue.getUsageProfile
**Get usage profile** — Retrieves information about the specified Glue usage profile.
- Stability: stable
- Permissions: `glue:GetUsageProfile`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the usage profile to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the usage profile. |
  | Description | string | A description of the usage profile. |
  | Configuration | object | A ProfileConfiguration object specifying the job and session values for the profile. |
  | CreatedOn | string | The date and time when the usage profile was created. |
  | LastModifiedOn | string | The date and time when the usage profile was last modified. |


## com.datadoghq.aws.glue.getUserDefinedFunction
**Get user defined function** — Retrieves a specified function definition from the Data Catalog.
- Stability: stable
- Permissions: `glue:GetUserDefinedFunction`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the function to be retrieved is located. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the function is located. |
  | functionName | string | yes | The name of the function. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserDefinedFunction | object | The requested function definition. |


## com.datadoghq.aws.glue.getUserDefinedFunctions
**Get user defined functions** — Retrieves multiple function definitions from the Data Catalog.
- Stability: stable
- Permissions: `glue:GetUserDefinedFunctions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the functions to be retrieved are located. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | no | The name of the catalog database where the functions are located. If none is provided, functions from all the databases across the catalog will be returned. |
  | pattern | string | yes | An optional function-name pattern string that filters the function definitions returned. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |
  | maxResults | number | no | The maximum number of functions to return in one response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | UserDefinedFunctions | array<object> | A list of requested function definitions. |
  | NextToken | string | A continuation token, if the list of functions returned does not include the last requested function. |


## com.datadoghq.aws.glue.getWorkflow
**Get workflow** — Retrieves resource metadata for a workflow.
- Stability: stable
- Permissions: `glue:GetWorkflow`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the workflow to retrieve. |
  | includeGraph | boolean | no | Specifies whether to include a graph when returning the workflow resource metadata. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Workflow | object | The resource metadata for the workflow. |


## com.datadoghq.aws.glue.getWorkflowRun
**Get workflow run** — Retrieves the metadata for a given workflow run. Job run history is accessible for 90 days for your workflow and job run.
- Stability: stable
- Permissions: `glue:GetWorkflowRun`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow being run. |
  | runId | string | yes | The ID of the workflow run. |
  | includeGraph | boolean | no | Specifies whether to include the workflow graph in response or not. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Run | object | The requested workflow run metadata. |


## com.datadoghq.aws.glue.getWorkflowRunProperties
**Get workflow run properties** — Retrieves the workflow run properties which were set during the run.
- Stability: stable
- Permissions: `glue:GetWorkflowRunProperties`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow which was run. |
  | runId | string | yes | The ID of the workflow run whose run properties should be returned. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunProperties | object | The workflow run properties which were set during the specified run. |


## com.datadoghq.aws.glue.getWorkflowRuns
**Get workflow runs** — Retrieves metadata for all runs of a given workflow.
- Stability: stable
- Permissions: `glue:GetWorkflowRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow whose metadata of runs should be returned. |
  | includeGraph | boolean | no | Specifies whether to include the workflow graph in response or not. |
  | nextToken | string | no | The maximum size of the response. |
  | maxResults | number | no | The maximum number of workflow runs to be included in the response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Runs | array<object> | A list of workflow run metadata objects. |
  | NextToken | string | A continuation token, if not all requested workflow runs have been returned. |


## com.datadoghq.aws.glue.importCatalogToGlue
**Import catalog to glue** — Imports an existing Amazon Athena Data Catalog to Glue.
- Stability: stable
- Permissions: `glue:ImportCatalogToGlue`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the catalog to import. Currently, this should be the Amazon Web Services account ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.listBlueprints
**List blueprints** — Lists all the blueprint names in an account.
- Stability: stable
- Permissions: `glue:ListBlueprints`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |
  | tags | any | no | Filters the list by an Amazon Web Services resource tag. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Blueprints | array<string> | List of names of blueprints in the account. |
  | NextToken | string | A continuation token, if not all blueprint names have been returned. |


## com.datadoghq.aws.glue.listColumnStatisticsTaskRuns
**List column statistics task runs** — List all task runs for a particular account.
- Stability: stable
- Permissions: `glue:ListColumnStatisticsTaskRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum size of the response. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsTaskRunIds | array<string> | A list of column statistics task run IDs. |
  | NextToken | string | A continuation token, if not all task run IDs have yet been returned. |


## com.datadoghq.aws.glue.listCrawlers
**List crawlers** — Retrieves the names of all crawler resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names. This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tag are retrieved.
- Stability: stable
- Permissions: `glue:ListCrawlers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | The maximum size of a list to return. |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | tags | any | no | Specifies to return only these tagged resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CrawlerNames | array<string> | The names of all crawlers in the account, or the crawlers with the specified tags. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.listCrawls
**List crawls** — Returns all the crawls of a specified crawler. Returns only the crawls that have occurred since the launch date of the crawler history feature, and only retains up to 12 months of crawls. Older crawls will not be returned. Use this API to retrieve all the crawls of a specified crawler, all the crawls of a specified crawler within a limited count, all the crawls of a specified crawler in a specific time range, and all the crawls of a specified crawler with a particular state, crawl ID, or DPU hour value.
- Stability: stable
- Permissions: `glue:ListCrawls`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerName | string | yes | The name of the crawler whose runs you want to retrieve. |
  | maxResults | number | no | The maximum number of results to return. The default is 20, and maximum is 100. |
  | filters | array<object> | no | Filters the crawls by the criteria you specify in a list of CrawlsFilter objects. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Crawls | array<object> | A list of CrawlerHistory objects representing the crawl runs that meet your criteria. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.listCustomEntityTypes
**List custom entity types** — Lists all the custom patterns that have been created.
- Stability: stable
- Permissions: `glue:ListCustomEntityTypes`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |
  | tags | any | no | A list of key-value pair tags. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CustomEntityTypes | array<object> | A list of CustomEntityType objects representing custom patterns. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.listDataQualityResults
**List data quality results** — Returns all data quality execution results for your account.
- Stability: stable
- Permissions: `glue:ListDataQualityResults`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filter | object | no | The filter criteria. |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Results | array<object> | A list of DataQualityResultDescription objects. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.listDataQualityRuleRecommendationRuns
**List data quality rule recommendation runs** — Lists the recommendation runs meeting the filter criteria.
- Stability: stable
- Permissions: `glue:ListDataQualityRuleRecommendationRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filter | object | no | The filter criteria. |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Runs | array<object> | A list of DataQualityRuleRecommendationRunDescription objects. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.listDataQualityRulesetEvaluationRuns
**List data quality ruleset evaluation runs** — Lists all the runs meeting the filter criteria, where a ruleset is evaluated against a data source.
- Stability: stable
- Permissions: `glue:ListDataQualityRulesetEvaluationRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | filter | object | no | The filter criteria. |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Runs | array<object> | A list of DataQualityRulesetEvaluationRunDescription objects representing data quality ruleset runs. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.listDataQualityRulesets
**List data quality rulesets** — Returns a paginated list of rulesets for the specified list of Glue tables.
- Stability: stable
- Permissions: `glue:ListDataQualityRulesets`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A paginated token to offset the results. |
  | maxResults | number | no | The maximum number of results to return. |
  | filter | object | no | The filter criteria. |
  | tags | any | no | A list of key-value pair tags. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Rulesets | array<object> | A paginated list of rulesets for the specified list of Glue tables. |
  | NextToken | string | A pagination token, if more results are available. |


## com.datadoghq.aws.glue.listDataQualityStatisticAnnotations
**List data quality statistic annotations** — Retrieve annotations for a data quality statistic.
- Stability: stable
- Permissions: `glue:ListDataQualityStatisticAnnotations`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | statisticId | string | no | The Statistic ID. |
  | profileId | string | no | The Profile ID. |
  | timestampFilter | object | no | A timestamp filter. |
  | maxResults | number | no | The maximum number of results to return in this request. |
  | nextToken | string | no | A pagination token to retrieve the next set of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Annotations | array<object> | A list of StatisticAnnotation applied to the Statistic |
  | NextToken | string | A pagination token to retrieve the next set of results. |


## com.datadoghq.aws.glue.listDataQualityStatistics
**List data quality statistics** — Retrieves a list of data quality statistics.
- Stability: stable
- Permissions: `glue:ListDataQualityStatistics`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | statisticId | string | no | The Statistic ID. |
  | profileId | string | no | The Profile ID. |
  | timestampFilter | object | no | A timestamp filter. |
  | maxResults | number | no | The maximum number of results to return in this request. |
  | nextToken | string | no | A pagination token to request the next page of results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Statistics | array<object> | A StatisticSummaryList. |
  | NextToken | string | A pagination token to request the next page of results. |


## com.datadoghq.aws.glue.listDevEndpoints
**List dev endpoints** — Retrieves the names of all DevEndpoint resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names. This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tag are retrieved.
- Stability: stable
- Permissions: `glue:ListDevEndpoints`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |
  | tags | any | no | Specifies to return only these tagged resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | DevEndpointNames | array<string> | The names of all the DevEndpoints in the account, or the DevEndpoints with the specified tags. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.listJobs
**List jobs** — Retrieves the names of all job resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names. This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tag are retrieved.
- Stability: stable
- Permissions: `glue:ListJobs`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |
  | tags | any | no | Specifies to return only these tagged resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobNames | array<string> | The names of all jobs in the account, or the jobs with the specified tags. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.listMLTransforms
**List mltransforms** — Retrieves a sortable, filterable list of existing Glue machine learning transforms in this Amazon Web Services account, or the resources with the specified tag. This operation takes the optional Tags field, which you can use as a filter of the responses so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tags are retrieved.
- Stability: stable
- Permissions: `glue:ListMLTransforms`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |
  | filter | object | no | A TransformFilterCriteria used to filter the machine learning transforms. |
  | sort | object | no | A TransformSortCriteria used to sort the machine learning transforms. |
  | tags | any | no | Specifies to return only these tagged resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformIds | array<string> | The identifiers of all the machine learning transforms in the account, or the machine learning transforms with the specified tags. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.listRegistries
**List registries** — Returns a list of registries that you have created, with minimal registry information. Registries in the Deleting status will not be included in the results. Empty results will be returned if there are no registries available.
- Stability: stable
- Permissions: `glue:ListRegistries`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | maxResults | number | no | Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Registries | array<object> | An array of RegistryDetailedListItem objects containing minimal details of each registry. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.listSchemaVersions
**List schema versions** — Returns a list of schema versions that you have created, with minimal information. Schema versions in Deleted status will not be included in the results. Empty results will be returned if there are no schema versions available.
- Stability: stable
- Permissions: `glue:ListSchemaVersions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either SchemaArn or SchemaName and Registr... |
  | maxResults | number | no | Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Schemas | array<object> | An array of SchemaVersionList objects containing details of each schema version. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.listSchemas
**List schemas** — Returns a list of schemas with minimal details. Schemas in Deleting status will not be included in the results. Empty results will be returned if there are no schemas available. When the RegistryId is not provided, all the schemas across registries will be part of the API response.
- Stability: stable
- Permissions: `glue:ListSchemas`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | object | no | A wrapper structure that may contain the registry name and Amazon Resource Name (ARN). |
  | maxResults | number | no | Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Schemas | array<object> | An array of SchemaListItem objects containing details of each schema. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.listSessions
**List sessions** — Retrieve a list of sessions.
- Stability: stable
- Permissions: `glue:ListSessions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | The token for the next set of results, or null if there are no more result. |
  | maxResults | number | no | The maximum number of results. |
  | tags | any | no | Tags belonging to the session. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Ids | array<string> | Returns the ID of the session. |
  | Sessions | array<object> | Returns the session object. |
  | NextToken | string | The token for the next set of results, or null if there are no more result. |


## com.datadoghq.aws.glue.listStatements
**List statements** — Lists statements for the session.
- Stability: stable
- Permissions: `glue:ListStatements`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sessionId | string | yes | The Session ID of the statements. |
  | requestOrigin | string | no | The origin of the request to list statements. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Statements | array<object> | Returns the list of statements. |
  | NextToken | string | A continuation token, if not all statements have yet been returned. |


## com.datadoghq.aws.glue.listTableOptimizerRuns
**List table optimizer runs** — Lists the history of previous optimizer runs for a specific table.
- Stability: stable
- Permissions: `glue:ListTableOptimizerRuns`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | yes | The Catalog ID of the table. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. |
  | tableName | string | yes | The name of the table. |
  | type | string | yes | The type of table optimizer. Currently, the only valid value is compaction. |
  | maxResults | number | no | The maximum number of optimizer runs to return on each call. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | CatalogId | string | The Catalog ID of the table. |
  | DatabaseName | string | The name of the database in the catalog in which the table resides. |
  | TableName | string | The name of the table. |
  | NextToken | string | A continuation token for paginating the returned list of optimizer runs, returned if the current segment of the list is not the last. |
  | TableOptimizerRuns | array<object> | A list of the optimizer runs associated with a table. |


## com.datadoghq.aws.glue.listTriggers
**List triggers** — Retrieves the names of all trigger resources in this Amazon Web Services account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names. This operation takes the optional Tags field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tag are retrieved.
- Stability: stable
- Permissions: `glue:ListTriggers`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | dependentJobName | string | no | The name of the job for which to retrieve triggers. The trigger that can start this job is returned. If there is no such trigger, all triggers are returned. |
  | maxResults | number | no | The maximum size of a list to return. |
  | tags | any | no | Specifies to return only these tagged resources. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TriggerNames | array<string> | The names of all triggers in the account, or the triggers with the specified tags. |
  | NextToken | string | A continuation token, if the returned list does not contain the last metric available. |


## com.datadoghq.aws.glue.listUsageProfiles
**List usage profiles** — List all the Glue usage profiles.
- Stability: stable
- Permissions: `glue:ListUsageProfiles`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, included if this is a continuation call. |
  | maxResults | number | no | The maximum number of usage profiles to return in a single response. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Profiles | array<object> | A list of usage profile (UsageProfileDefinition) objects. |
  | NextToken | string | A continuation token, present if the current list segment is not the last. |


## com.datadoghq.aws.glue.listWorkflows
**List workflows** — Lists names of workflows created in the account.
- Stability: stable
- Permissions: `glue:ListWorkflows`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | nextToken | string | no | A continuation token, if this is a continuation request. |
  | maxResults | number | no | The maximum size of a list to return. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Workflows | array<string> | List of names of workflows in the account. |
  | NextToken | string | A continuation token, if not all workflow names have been returned. |


## com.datadoghq.aws.glue.putDataCatalogEncryptionSettings
**Put data catalog encryption settings** — Sets the security configuration for a specified catalog. After the configuration has been set, the specified encryption is applied to every catalog write thereafter.
- Stability: stable
- Permissions: `glue:PutDataCatalogEncryptionSettings`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog to set the security configuration for. If none is provided, the Amazon Web Services account ID is used by default. |
  | dataCatalogEncryptionSettings | object | yes | The security configuration to set. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.putDataQualityProfileAnnotation
**Put data quality profile annotation** — Annotate all datapoints for a Profile.
- Stability: stable
- Permissions: `glue:PutDataQualityProfileAnnotation`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | profileId | string | yes | The ID of the data quality monitoring profile to annotate. |
  | inclusionAnnotation | string | yes | The inclusion annotation value to apply to the profile. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.putResourcePolicy
**Put resource policy** — Sets the Data Catalog resource policy for access control.
- Stability: stable
- Permissions: `glue:PutResourcePolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | policyInJson | string | yes | Contains the policy document to set, in JSON format. |
  | resourceArn | string | no | Do not use. For internal use only. |
  | policyHashCondition | string | no | The hash value returned when the previous policy was set using PutResourcePolicy. Its purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no previous policy has... |
  | policyExistsCondition | string | no | A value of MUST_EXIST is used to update a policy. A value of NOT_EXIST is used to create a new policy. If a value of NONE or a null value is used, the call does not depend on the existence of a pol... |
  | enableHybrid | string | no | If 'TRUE', indicates that you are using both methods to grant cross-account access to Data Catalog resources:   By directly updating the resource policy with PutResourePolicy    By using the Grant ... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | PolicyHash | string | A hash of the policy that has just been set. This must be included in a subsequent call that overwrites or updates this policy. |


## com.datadoghq.aws.glue.putSchemaVersionMetadata
**Put schema version metadata** — Puts the metadata key value pair for a specified schema version ID. A maximum of 10 key value pairs will be allowed per schema version. They can be added over one or more calls.
- Stability: stable
- Permissions: `glue:PutSchemaVersionMetadata`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | no | The unique ID for the schema. |
  | schemaVersionNumber | object | no | The version number of the schema. |
  | schemaVersionId | string | no | The unique version ID of the schema version. |
  | metadataKeyValue | object | yes | The metadata key's corresponding value. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaArn | string | The Amazon Resource Name (ARN) for the schema. |
  | SchemaName | string | The name for the schema. |
  | RegistryName | string | The name for the registry. |
  | LatestVersion | boolean | The latest version of the schema. |
  | VersionNumber | number | The version number of the schema. |
  | SchemaVersionId | string | The unique version ID of the schema version. |
  | MetadataKey | string | The metadata key. |
  | MetadataValue | string | The value of the metadata key. |


## com.datadoghq.aws.glue.putWorkflowRunProperties
**Put workflow run properties** — Puts the specified workflow run properties for the given workflow run. If a property already exists for the specified run, then it overrides the value. If not, it adds the property to existing properties.
- Stability: stable
- Permissions: `glue:PutWorkflowRunProperties`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow which was run. |
  | runId | string | yes | The ID of the workflow run for which the run properties should be updated. |
  | runProperties | object | yes | The properties to put for the specified run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.querySchemaVersionMetadata
**Query schema version metadata** — Queries for the schema version metadata information.
- Stability: stable
- Permissions: `glue:QuerySchemaVersionMetadata`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | no | A wrapper structure that may contain the schema name and Amazon Resource Name (ARN). |
  | schemaVersionNumber | object | no | The version number of the schema. |
  | schemaVersionId | string | no | The unique version ID of the schema version. |
  | metadataList | array<object> | no | Search key-value pairs for metadata, if they are not provided all the metadata information will be fetched. |
  | maxResults | number | no | Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page. |
  | nextToken | string | no | A continuation token, if this is a continuation call. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | MetadataInfoMap | object | A map of a metadata key and associated values. |
  | SchemaVersionId | string | The unique version ID of the schema version. |
  | NextToken | string | A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last. |


## com.datadoghq.aws.glue.registerSchemaVersion
**Register schema version** — Adds a new version to the existing schema. Returns an error if new version of schema does not meet the compatibility requirements of the schema set. This API will not create a new schema set and will return a 404 error if the schema set is not already present in the Schema Registry. If this is the first schema definition to be registered in the Schema Registry, this API will store the schema version and return immediately. Otherwise, this call has the potential to run longer than other operations due to compatibility modes. You can call the GetSchemaVersion API with the SchemaVersionId to check compatibility modes. If the same schema definition is already stored in Schema Registry as a version, the schema ID of the existing schema is returned to the caller.
- Stability: stable
- Permissions: `glue:RegisterSchemaVersion`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either SchemaArn or SchemaName and Registr... |
  | schemaDefinition | string | yes | The schema definition using the DataFormat setting for the SchemaName. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaVersionId | string | The unique ID that represents the version of this schema. |
  | VersionNumber | number | The version of this schema (for sync flow only, in case this is the first version). |
  | Status | string | The status of the schema version. |


## com.datadoghq.aws.glue.removeSchemaVersionMetadata
**Remove schema version metadata** — Removes a key value pair from the schema version metadata for the specified schema version ID.
- Stability: stable
- Permissions: `glue:RemoveSchemaVersionMetadata`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | no | A wrapper structure that may contain the schema name and Amazon Resource Name (ARN). |
  | schemaVersionNumber | object | no | The version number of the schema. |
  | schemaVersionId | string | no | The unique version ID of the schema version. |
  | metadataKeyValue | object | yes | The value of the metadata key. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | SchemaName | string | The name of the schema. |
  | RegistryName | string | The name of the registry. |
  | LatestVersion | boolean | The latest version of the schema. |
  | VersionNumber | number | The version number of the schema. |
  | SchemaVersionId | string | The version ID for the schema version. |
  | MetadataKey | string | The metadata key. |
  | MetadataValue | string | The value of the metadata key. |


## com.datadoghq.aws.glue.resetJobBookmark
**Reset job bookmark** — Resets a bookmark entry. For more information about enabling and using job bookmarks, see Tracking processed data using job bookmarks, Job parameters used by Glue, and Job structure.
- Stability: stable
- Permissions: `glue:ResetJobBookmark`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job in question. |
  | runId | string | no | The unique run identifier associated with this job run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobBookmarkEntry | object | The reset bookmark entry. |


## com.datadoghq.aws.glue.resumeWorkflowRun
**Resume workflow run** — Restarts selected nodes of a previous partially completed workflow run and resumes the workflow run. The selected nodes and all nodes that are downstream from the selected nodes are run.
- Stability: stable
- Permissions: `glue:ResumeWorkflowRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the workflow to resume. |
  | runId | string | yes | The ID of the workflow run to resume. |
  | nodeIds | array<string> | yes | A list of the node IDs for the nodes you want to restart. The nodes that are to be restarted must have a run attempt in the original run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The new ID assigned to the resumed workflow run. Each resume of a workflow run will have a new run ID. |
  | NodeIds | array<string> | A list of the node IDs for the nodes that were actually restarted. |


## com.datadoghq.aws.glue.runStatement
**Run statement** — Executes the statement.
- Stability: stable
- Permissions: `glue:RunStatement`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sessionId | string | yes | The Session Id of the statement to be run. |
  | code | string | yes | The statement code to be run. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Id | number | Returns the Id of the statement that was run. |


## com.datadoghq.aws.glue.searchTables
**Search tables** — Searches a set of tables based on properties in the table metadata as well as on the parent database. You can search against text or filter conditions.  You can only get tables that you have access to based on the security policies defined in Lake Formation. You need at least read-only access to the table for it to be returned. If you do not have access to all the columns in the table, these columns will not be searched against when returning the list of tables back to you. If you have access to the columns but not the data in the columns, those columns and the associated metadata for those columns will be included in the search.
- Stability: stable
- Permissions: `glue:SearchTables`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | A unique identifier, consisting of  account_id . |
  | nextToken | string | no | A continuation token, included if this is a continuation call. |
  | filters | array<object> | no | A list of key-value pairs, and a comparator used to filter the search results. Returns all entities matching the predicate. The Comparator member of the PropertyPredicate struct is used only for ti... |
  | searchText | string | no | A string used for a text search. Specifying a value in quotes filters based on an exact match to the value. |
  | sortCriteria | array<object> | no | A list of criteria for sorting the results by a field name, in an ascending or descending order. |
  | maxResults | number | no | The maximum number of tables to return in a single response. |
  | resourceShareType | string | no | Allows you to specify that you want to search the tables shared with your account. The allowable values are FOREIGN or ALL.    If set to FOREIGN, will search the tables shared with your account.   ... |
  | includeStatusDetails | boolean | no | Specifies whether to include status details related to a request to create or update an Glue Data Catalog view. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | NextToken | string | A continuation token, present if the current list segment is not the last. |
  | TableList | array<object> | A list of the requested Table objects. The SearchTables response returns only the tables that you have access to. |


## com.datadoghq.aws.glue.startBlueprintRun
**Start blueprint run** — Starts a new run of the specified blueprint.
- Stability: stable
- Permissions: `glue:StartBlueprintRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | blueprintName | string | yes | The name of the blueprint. |
  | parameters | string | no | Specifies the parameters as a BlueprintParameters object. |
  | roleArn | string | yes | Specifies the IAM role used to create the workflow. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The run ID for this blueprint run. |


## com.datadoghq.aws.glue.startColumnStatisticsTaskRun
**Start column statistics task run** — Starts a column statistics task run, for a specified table and columns.
- Stability: stable
- Permissions: `glue:StartColumnStatisticsTaskRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | databaseName | string | yes | The name of the database where the table resides. |
  | tableName | string | yes | The name of the table to generate statistics. |
  | columnNameList | array<string> | no | A list of the column names to generate statistics. If none is supplied, all column names for the table will be used by default. |
  | role | string | yes | The IAM role that the service assumes to generate statistics. |
  | sampleSize | number | no | The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats. |
  | catalogID | string | no | The ID of the Data Catalog where the table reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | securityConfiguration | string | no | Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ColumnStatisticsTaskRunId | string | The identifier for the column statistics task run. |


## com.datadoghq.aws.glue.startCrawler
**Start crawler** — Starts a crawl using the specified crawler, regardless of what is scheduled. If the crawler is already running, returns a CrawlerRunningException.
- Stability: stable
- Permissions: `glue:StartCrawler`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the crawler to start. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.startCrawlerSchedule
**Start crawler schedule** — Changes the schedule state of the specified crawler to SCHEDULED, unless the crawler is already running or the schedule state is already SCHEDULED.
- Stability: stable
- Permissions: `glue:StartCrawlerSchedule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerName | string | yes | Name of the crawler to schedule. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.startDataQualityRuleRecommendationRun
**Start data quality rule recommendation run** — Starts a recommendation run that is used to generate rules when you don&#x27;t know what rules to write. Glue Data Quality analyzes the data and comes up with recommendations for a potential ruleset. You can then triage the ruleset and modify the generated ruleset to your liking. Recommendation runs are automatically deleted after 90 days.
- Stability: stable
- Permissions: `glue:StartDataQualityRuleRecommendationRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dataSource | object | yes | The data source (Glue table) associated with this run. |
  | role | string | yes | An IAM role supplied to encrypt the results of the run. |
  | numberOfWorkers | number | no | The number of G.1X workers to be used in the run. The default is 5. |
  | timeout | number | no | The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). |
  | createdRulesetName | string | no | A name for the ruleset. |
  | dataQualitySecurityConfiguration | string | no | The name of the security configuration created with the data quality encryption option. |
  | clientToken | string | no | Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The unique run identifier associated with this run. |


## com.datadoghq.aws.glue.startDataQualityRulesetEvaluationRun
**Start data quality ruleset evaluation run** — Once you have a ruleset definition (either recommended or your own), you call this operation to evaluate the ruleset against a data source (Glue table). The evaluation computes results which you can retrieve with the GetDataQualityResult API.
- Stability: stable
- Permissions: `glue:StartDataQualityRulesetEvaluationRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | dataSource | object | yes | The data source (Glue table) associated with this run. |
  | role | string | yes | An IAM role supplied to encrypt the results of the run. |
  | numberOfWorkers | number | no | The number of G.1X workers to be used in the run. The default is 5. |
  | timeout | number | no | The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). |
  | clientToken | string | no | Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource. |
  | additionalRunOptions | object | no | Additional run options you can specify for an evaluation run. |
  | rulesetNames | array<string> | yes | A list of ruleset names. |
  | additionalDataSources | object | no | A map of reference strings to additional data sources you can specify for an evaluation run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | The unique run identifier associated with this run. |


## com.datadoghq.aws.glue.startExportLabelsTaskRun
**Start export labels task run** — Begins an asynchronous task to export all labeled data for a particular transform. This task is the only label-related API call that is not part of the typical active learning workflow. You typically use StartExportLabelsTaskRun when you want to work with all of your existing labels at the same time, such as when you want to remove or change labels that were previously submitted as truth. This API operation accepts the TransformId whose labels you want to export and an Amazon Simple Storage Service (Amazon S3) path to export the labels to. The operation returns a TaskRunId. You can check on the status of your task run by calling the GetMLTaskRun API.
- Stability: stable
- Permissions: `glue:StartExportLabelsTaskRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | outputS3Path | string | yes | The Amazon S3 path where you export the labels. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskRunId | string | The unique identifier for the task run. |


## com.datadoghq.aws.glue.startImportLabelsTaskRun
**Start import labels task run** — Enables you to provide additional labels (examples of truth) to be used to teach the machine learning transform and improve its quality. This API operation is generally used as part of the active learning workflow that starts with the StartMLLabelingSetGenerationTaskRun call and that ultimately results in improving the quality of your machine learning transform.  After the StartMLLabelingSetGenerationTaskRun finishes, Glue machine learning will have generated a series of questions for humans to answer. (Answering these questions is often called &quot;labeling&quot; in the machine learning workflows.) In the case of the FindMatches transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?” After the labeling process is finished, users upload their answers (labels) with a call to StartImportLabelsTaskRun. After StartImportLabelsTaskRun finishes, all future runs of the machine learning transform use the new and improved labels and perform a higher-quality transformation. By default, StartMLLabelingSetGenerationTaskRun continually learns from and combines all labels that you upload unless you set Replace to true. If you set Replace to true, StartImportLabelsTaskRun deletes and forgets all previously uploaded labels and learns only from the exact set that you upload. Replacing labels can be helpful if you realize that you previously uploaded incorrect labels, and you believe that they are having a negative effect on your transform quality. You can check on the status of your task run by calling the GetMLTaskRun operation.
- Stability: stable
- Permissions: `glue:StartImportLabelsTaskRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | inputS3Path | string | yes | The Amazon Simple Storage Service (Amazon S3) path from where you import the labels. |
  | replaceAllLabels | boolean | no | Indicates whether to overwrite your existing labels. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskRunId | string | The unique identifier for the task run. |


## com.datadoghq.aws.glue.startJobRun
**Start job run** — Starts a job run using a job definition.
- Stability: stable
- Permissions: `glue:StartJobRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition to use. |
  | jobRunQueuingEnabled | boolean | no | Specifies whether job run queuing is enabled for the job run. A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for que... |
  | jobRunId | string | no | The ID of a previous JobRun to retry. |
  | arguments | object | no | The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself. You can specify arguments here that your own job-execution script ... |
  | allocatedCapacity | number | no | This field is deprecated. Use MaxCapacity instead. The number of Glue data processing units (DPUs) to allocate to this JobRun. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a re... |
  | timeout | number | no | The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. This value overrides the timeout value set in the par... |
  | maxCapacity | number | no | For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of proces... |
  | securityConfiguration | string | no | The name of the SecurityConfiguration structure to be used with this job run. |
  | notificationProperty | object | no | Specifies configuration properties of a job run notification. |
  | workerType | string | no | The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.   For the G.1X worker type,... |
  | numberOfWorkers | number | no | The number of workers of a defined workerType that are allocated when a job runs. |
  | executionClass | string | no | Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resource... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobRunId | string | The ID assigned to this job run. |


## com.datadoghq.aws.glue.startMLEvaluationTaskRun
**Start mlevaluation task run** — Starts a task to estimate the quality of the transform.  When you provide label sets as examples of truth, Glue machine learning uses some of those examples to learn from them. The rest of the labels are used as a test to estimate quality. Returns a unique identifier for the run. You can call GetMLTaskRun to get more information about the stats of the EvaluationTaskRun.
- Stability: stable
- Permissions: `glue:StartMLEvaluationTaskRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskRunId | string | The unique identifier associated with this run. |


## com.datadoghq.aws.glue.startMLLabelingSetGenerationTaskRun
**Start mllabeling set generation task run** — Starts the active learning workflow for your machine learning transform to improve the transform&#x27;s quality by generating label sets and adding labels. When the StartMLLabelingSetGenerationTaskRun finishes, Glue will have generated a &quot;labeling set&quot; or a set of questions for humans to answer. In the case of the FindMatches transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?”  After the labeling process is finished, you can upload your labels with a call to StartImportLabelsTaskRun. After StartImportLabelsTaskRun finishes, all future runs of the machine learning transform will use the new and improved labels and perform a higher-quality transformation.
- Stability: stable
- Permissions: `glue:StartMLLabelingSetGenerationTaskRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | The unique identifier of the machine learning transform. |
  | outputS3Path | string | yes | The Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TaskRunId | string | The unique run identifier that is associated with this task run. |


## com.datadoghq.aws.glue.startTrigger
**Start trigger** — Starts an existing trigger. See Triggering Jobs for information about how different types of trigger are started.
- Stability: stable
- Permissions: `glue:StartTrigger`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger to start. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the trigger that was started. |


## com.datadoghq.aws.glue.startWorkflowRun
**Start workflow run** — Starts a new run of the specified workflow.
- Stability: stable
- Permissions: `glue:StartWorkflowRun`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the workflow to start. |
  | runProperties | object | no | The workflow run properties for the new workflow run. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RunId | string | An Id for the new run. |


## com.datadoghq.aws.glue.stopColumnStatisticsTaskRun
**Stop column statistics task run** — Stops a task run for the specified table.
- Stability: stable
- Permissions: `glue:StopColumnStatisticsTaskRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | databaseName | string | yes | The name of the database where the table resides. |
  | tableName | string | yes | The name of the table. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.stopCrawler
**Stop crawler** — If the specified crawler is running, stops the crawl.
- Stability: stable
- Permissions: `glue:StopCrawler`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the crawler to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.stopCrawlerSchedule
**Stop crawler schedule** — Sets the schedule state of the specified crawler to NOT_SCHEDULED, but does not stop the crawler if it is already running.
- Stability: stable
- Permissions: `glue:StopCrawlerSchedule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerName | string | yes | Name of the crawler whose schedule state to set. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.stopSession
**Stop session** — Stops the session.
- Stability: stable
- Permissions: `glue:StopSession`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | id | string | yes | The ID of the session to be stopped. |
  | requestOrigin | string | no | The origin of the request. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Id | string | Returns the Id of the stopped session. |


## com.datadoghq.aws.glue.stopTrigger
**Stop trigger** — Stops a specified trigger.
- Stability: stable
- Permissions: `glue:StopTrigger`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the trigger that was stopped. |


## com.datadoghq.aws.glue.stopWorkflowRun
**Stop workflow run** — Stops the execution of the specified workflow run.
- Stability: stable
- Permissions: `glue:StopWorkflowRun`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the workflow to stop. |
  | runId | string | yes | The ID of the workflow run to stop. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.tagResource
**Tag resource** — Adds tags to a resource. A tag is a label you can assign to an Amazon Web Services resource. In Glue, you can tag only certain resources. For information about what resources you can tag, see Amazon Web Services Tags in Glue.
- Stability: stable
- Permissions: `glue:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The ARN of the Glue resource to which to add the tags. For more information about Glue resource ARNs, see the Glue ARN string pattern. |
  | tagsToAdd | object | yes | Tags to add to this resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.untagResource
**Untag resource** — Removes tags from a resource.
- Stability: stable
- Permissions: `glue:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource from which to remove the tags. |
  | tagsToRemove | array<string> | yes | Tags to remove from this resource. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateBlueprint
**Update blueprint** — Updates a registered blueprint.
- Stability: stable
- Permissions: `glue:UpdateBlueprint`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the blueprint. |
  | description | string | no | A description of the blueprint. |
  | blueprintLocation | string | yes | Specifies a path in Amazon S3 where the blueprint is published. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | Returns the name of the blueprint that was updated. |


## com.datadoghq.aws.glue.updateClassifier
**Update classifier** — Modifies an existing classifier (a GrokClassifier, an XMLClassifier, a JsonClassifier, or a CsvClassifier, depending on which field is present).
- Stability: stable
- Permissions: `glue:UpdateClassifier`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | grokClassifier | object | no | A GrokClassifier object with updated fields. |
  | xMLClassifier | object | no | An XMLClassifier object with updated fields. |
  | jsonClassifier | object | no | A JsonClassifier object with updated fields. |
  | csvClassifier | object | no | A CsvClassifier object with updated fields. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateColumnStatisticsForPartition
**Update column statistics for partition** — Creates or updates partition statistics of columns. The Identity and Access Management (IAM) permission required for this operation is UpdatePartition.
- Stability: stable
- Permissions: `glue:UpdateColumnStatisticsForPartition`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | partitionValues | array<string> | yes | A list of partition values identifying the partition. |
  | columnStatisticsList | array<object> | yes | A list of the column statistics. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | Error occurred during updating column statistics data. |


## com.datadoghq.aws.glue.updateColumnStatisticsForTable
**Update column statistics for table** — Creates or updates table statistics of columns. The Identity and Access Management (IAM) permission required for this operation is UpdateTable.
- Stability: stable
- Permissions: `glue:UpdateColumnStatisticsForTable`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the partitions reside. |
  | tableName | string | yes | The name of the partitions' table. |
  | columnStatisticsList | array<object> | yes | A list of the column statistics. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Errors | array<object> | List of ColumnStatisticsErrors. |


## com.datadoghq.aws.glue.updateConnection
**Update connection** — Updates a connection definition in the Data Catalog.
- Stability: stable
- Permissions: `glue:UpdateConnection`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | name | string | yes | The name of the connection definition to update. |
  | connectionInput | object | yes | A ConnectionInput object that redefines the connection in question. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateCrawler
**Update crawler** — Updates a crawler. If a crawler is running, you must stop it using StopCrawler before updating it.
- Stability: stable
- Permissions: `glue:UpdateCrawler`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the new crawler. |
  | role | string | no | The IAM role or Amazon Resource Name (ARN) of an IAM role that is used by the new crawler to access customer resources. |
  | databaseName | string | no | The Glue database where results are stored, such as: arn:aws:daylight:us-east-1::database/sometable/*. |
  | description | string | no | A description of the new crawler. |
  | targets | object | no | A list of targets to crawl. |
  | schedule | string | no | A cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers. For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *). |
  | classifiers | array<string> | no | A list of custom classifiers that the user has registered. By default, all built-in classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a g... |
  | tablePrefix | string | no | The table prefix used for catalog tables that are created. |
  | schemaChangePolicy | object | no | The policy for the crawler's update and deletion behavior. |
  | recrawlPolicy | object | no | A policy that specifies whether to crawl the entire dataset again, or to crawl only folders that were added since the last crawler run. |
  | lineageConfiguration | object | no | Specifies data lineage configuration settings for the crawler. |
  | lakeFormationConfiguration | object | no | Specifies Lake Formation configuration settings for the crawler. |
  | configuration | string | no | Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior. For more information, see Setting crawler configuration options. |
  | crawlerSecurityConfiguration | string | no | The name of the SecurityConfiguration structure to be used by this crawler. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateCrawlerSchedule
**Update crawler schedule** — Updates the schedule of a crawler using a cron expression.
- Stability: stable
- Permissions: `glue:UpdateCrawlerSchedule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | crawlerName | string | yes | The name of the crawler whose schedule to update. |
  | schedule | string | no | The updated cron expression used to specify the schedule (see Time-Based Schedules for Jobs and Crawlers. For example, to run something every day at 12:15 UTC, you would specify: cron(15 12 * * ? *). |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateDataQualityRuleset
**Update data quality ruleset** — Updates the specified data quality ruleset.
- Stability: stable
- Permissions: `glue:UpdateDataQualityRuleset`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the data quality ruleset. |
  | description | string | no | A description of the ruleset. |
  | ruleset | string | no | A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the data quality ruleset. |
  | Description | string | A description of the ruleset. |
  | Ruleset | string | A Data Quality Definition Language (DQDL) ruleset. For more information, see the Glue developer guide. |


## com.datadoghq.aws.glue.updateDatabase
**Update database** — Updates an existing database definition in a Data Catalog.
- Stability: stable
- Permissions: `glue:UpdateDatabase`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog in which the metadata database resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | name | string | yes | The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase. |
  | databaseInput | object | yes | A DatabaseInput object specifying the new definition of the metadata database in the catalog. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateDevEndpoint
**Update dev endpoint** — Updates a specified development endpoint.
- Stability: stable
- Permissions: `glue:UpdateDevEndpoint`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | endpointName | string | yes | The name of the DevEndpoint to be updated. |
  | publicKey | string | no | The public key for the DevEndpoint to use. |
  | addPublicKeys | array<string> | no | The list of public keys for the DevEndpoint to use. |
  | deletePublicKeys | array<string> | no | The list of public keys to be deleted from the DevEndpoint. |
  | customLibraries | object | no | Custom Python or Java libraries to be loaded in the DevEndpoint. |
  | updateEtlLibraries | boolean | no | True if the list of custom libraries to be loaded in the development endpoint needs to be updated, or False if otherwise. |
  | deleteArguments | array<string> | no | The list of argument keys to be deleted from the map of arguments used to configure the DevEndpoint. |
  | addArguments | object | no | The map of arguments to add the map of arguments used to configure the DevEndpoint. Valid arguments are:    "--enable-glue-datacatalog": ""    You can specify a version of Python support for develo... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateJob
**Update job** — Updates an existing job definition. The previous job definition is completely overwritten by this information.
- Stability: stable
- Permissions: `glue:UpdateJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | yes | The name of the job definition to update. |
  | jobUpdate | object | yes | Specifies the values with which to update the job definition. Unspecified configuration is removed or reset to default values. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobName | string | Returns the name of the updated job definition. |


## com.datadoghq.aws.glue.updateJobFromSourceControl
**Update job from source control** — Synchronizes a job from the source control repository. This operation takes the job artifacts that are located in the remote repository and updates the Glue internal stores with these artifacts. This API supports optional parameters which take in the repository information.
- Stability: stable
- Permissions: `glue:UpdateJobFromSourceControl`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | no | The name of the Glue job to be synchronized to or from the remote repository. |
  | provider | string | no | The provider for the remote repository. Possible values: GITHUB, AWS_CODE_COMMIT, GITLAB, BITBUCKET. |
  | repositoryName | string | no | The name of the remote repository that contains the job artifacts. For BitBucket providers, RepositoryName should include WorkspaceName. Use the format <WorkspaceName>/<RepositoryName>. |
  | repositoryOwner | string | no | The owner of the remote repository that contains the job artifacts. |
  | branchName | string | no | An optional branch in the remote repository. |
  | folder | string | no | An optional folder in the remote repository. |
  | commitId | string | no | A commit ID for a commit in the remote repository. |
  | authStrategy | string | no | The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token. |
  | authToken | string | no | The value of the authorization token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobName | string | The name of the Glue job. |


## com.datadoghq.aws.glue.updateMLTransform
**Update mltransform** — Updates an existing machine learning transform. Call this operation to tune the algorithm parameters to achieve better results. After calling this operation, you can call the StartMLEvaluationTaskRun operation to assess how well your new parameters achieved your goals (such as improving the quality of your machine learning transform, or making it more cost-effective).
- Stability: stable
- Permissions: `glue:UpdateMLTransform`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | transformId | string | yes | A unique identifier that was generated when the transform was created. |
  | name | string | no | The unique name that you gave the transform when you created it. |
  | description | string | no | A description of the transform. The default is an empty string. |
  | parameters | object | no | The configuration parameters that are specific to the transform type (algorithm) used. Conditionally dependent on the transform type. |
  | role | string | no | The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. |
  | glueVersion | string | no | This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults ... |
  | maxCapacity | number | no | The number of Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing... |
  | workerType | string | no | The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.   For the Standard worker type, each worker provides 4 vCPU, 16 GB of memory and a 5... |
  | numberOfWorkers | number | no | The number of workers of a defined workerType that are allocated when this task runs. |
  | timeout | number | no | The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters TIMEOUT status. The de... |
  | maxRetries | number | no | The maximum number of times to retry a task for this transform after a task run fails. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransformId | string | The unique identifier for the transform that was updated. |


## com.datadoghq.aws.glue.updatePartition
**Update partition** — Updates a partition.
- Stability: stable
- Permissions: `glue:UpdatePartition`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the partition to be updated resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the table in question resides. |
  | tableName | string | yes | The name of the table in which the partition to be updated is located. |
  | partitionValueList | array<string> | yes | List of partition key values that define the partition to update. |
  | partitionInput | object | yes | The new partition object to update the partition to. The Values property can't be changed. If you want to change the partition key values for a partition, delete and recreate the partition. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateRegistry
**Update registry** — Updates an existing registry which is used to hold a collection of schemas. The updated properties relate to the registry, and do not modify any of the schemas within the registry.
- Stability: stable
- Permissions: `glue:UpdateRegistry`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | object | yes | This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN). |
  | description | string | yes | A description of the registry. If description is not provided, this field will not be updated. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | RegistryName | string | The name of the updated registry. |
  | RegistryArn | string | The Amazon Resource name (ARN) of the updated registry. |


## com.datadoghq.aws.glue.updateSchema
**Update schema** — Updates the description, compatibility setting, or version checkpoint for a schema set. For updating the compatibility setting, the call will not validate compatibility for the entire set of schema versions with the new compatibility setting. If the value for Compatibility is provided, the VersionNumber (a checkpoint) is also required. The API will validate the checkpoint version number for consistency. If the value for the VersionNumber (checkpoint) is provided, Compatibility is optional and this can be used to set or reset a checkpoint for the schema. This update will happen only if the schema is in the AVAILABLE state.
- Stability: stable
- Permissions: `glue:UpdateSchema`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | schemaId | object | yes | This is a wrapper structure to contain schema identity fields. The structure contains:   SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of SchemaArn or SchemaName has to be p... |
  | schemaVersionNumber | object | no | Version number required for check pointing. One of VersionNumber or Compatibility has to be provided. |
  | compatibility | string | no | The new compatibility setting for the schema. |
  | description | string | no | The new description for the schema. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | SchemaArn | string | The Amazon Resource Name (ARN) of the schema. |
  | SchemaName | string | The name of the schema. |
  | RegistryName | string | The name of the registry that contains the schema. |


## com.datadoghq.aws.glue.updateSourceControlFromJob
**Update source control from job** — Synchronizes a job to the source control repository. This operation takes the job artifacts from the Glue internal stores and makes a commit to the remote repository that is configured on the job. This API supports optional parameters which take in the repository information.
- Stability: stable
- Permissions: `glue:UpdateSourceControlFromJob`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | jobName | string | no | The name of the Glue job to be synchronized to or from the remote repository. |
  | provider | string | no | The provider for the remote repository. Possible values: GITHUB, AWS_CODE_COMMIT, GITLAB, BITBUCKET. |
  | repositoryName | string | no | The name of the remote repository that contains the job artifacts. For BitBucket providers, RepositoryName should include WorkspaceName. Use the format <WorkspaceName>/<RepositoryName>. |
  | repositoryOwner | string | no | The owner of the remote repository that contains the job artifacts. |
  | branchName | string | no | An optional branch in the remote repository. |
  | folder | string | no | An optional folder in the remote repository. |
  | commitId | string | no | A commit ID for a commit in the remote repository. |
  | authStrategy | string | no | The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token. |
  | authToken | string | no | The value of the authorization token. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | JobName | string | The name of the Glue job. |


## com.datadoghq.aws.glue.updateTable
**Update table** — Updates a metadata table in the Data Catalog.
- Stability: stable
- Permissions: `glue:UpdateTable`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase. |
  | tableInput | object | yes | An updated TableInput object to define the metadata table in the catalog. |
  | skipArchive | boolean | no | By default, UpdateTable always creates an archived version of the table before updating it. However, if skipArchive is set to true, UpdateTable does not create the archived version. |
  | transactionId | string | no | The transaction ID at which to update the table contents. |
  | versionId | string | no | The version ID at which to update the table contents. |
  | viewUpdateAction | string | no | The operation to be performed when updating the view. |
  | force | boolean | no | A flag that can be set to true to ignore matching storage descriptor and subobject matching requirements. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateTableOptimizer
**Update table optimizer** — Updates the configuration for an existing table optimizer.
- Stability: stable
- Permissions: `glue:UpdateTableOptimizer`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | yes | The Catalog ID of the table. |
  | databaseName | string | yes | The name of the database in the catalog in which the table resides. |
  | tableName | string | yes | The name of the table. |
  | type | string | yes | The type of table optimizer. Currently, the only valid value is compaction. |
  | tableOptimizerConfiguration | object | yes | A TableOptimizerConfiguration object representing the configuration of a table optimizer. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateTrigger
**Update trigger** — Updates a trigger definition.
- Stability: stable
- Permissions: `glue:UpdateTrigger`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the trigger to update. |
  | triggerUpdate | object | yes | The new values with which to update the trigger. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Trigger | object | The resulting trigger definition. |


## com.datadoghq.aws.glue.updateUsageProfile
**Update usage profile** — Update a Glue usage profile.
- Stability: stable
- Permissions: `glue:UpdateUsageProfile`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | The name of the usage profile. |
  | description | string | no | A description of the usage profile. |
  | configuration | object | yes | A ProfileConfiguration object specifying the job and session values for the profile. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the usage profile that was updated. |


## com.datadoghq.aws.glue.updateUserDefinedFunction
**Update user defined function** — Updates an existing function definition in the Data Catalog.
- Stability: stable
- Permissions: `glue:UpdateUserDefinedFunction`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | catalogId | string | no | The ID of the Data Catalog where the function to be updated is located. If none is provided, the Amazon Web Services account ID is used by default. |
  | databaseName | string | yes | The name of the catalog database where the function to be updated is located. |
  | functionName | string | yes | The name of the function. |
  | functionInput | object | yes | A FunctionInput object that redefines the function in the Data Catalog. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.glue.updateWorkflow
**Update workflow** — Updates an existing workflow.
- Stability: stable
- Permissions: `glue:UpdateWorkflow`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | name | string | yes | Name of the workflow to be updated. |
  | description | string | no | The description of the workflow. |
  | defaultRunProperties | object | no | A collection of properties to be used as part of each execution of the workflow. |
  | maxConcurrentRuns | number | no | You can use this parameter to prevent unwanted multiple updates to data, to control costs, or in some cases, to prevent exceeding the maximum number of concurrent runs of any of the component jobs.... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Name | string | The name of the workflow which was specified in input. |

