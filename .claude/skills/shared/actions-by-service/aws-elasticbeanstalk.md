# AWS Elastic Beanstalk Actions
Bundle: `com.datadoghq.aws.elasticbeanstalk` | 8 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eelasticbeanstalk)

## com.datadoghq.aws.elasticbeanstalk.describeApplication
**Describe application** — Describe an existing application.
- Stability: stable
- Permissions: `elasticbeanstalk:DescribeApplications`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | applicationName | string | yes | Name of the Elastic Beanstalk application. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | application | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.describeConfigurationOptions
**Describe configuration options** — Describe the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines.
- Stability: stable
- Permissions: `elasticbeanstalk:DescribeConfigurationOptions`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | configurationIdentification | any | yes | Select your configuration either through the environment name, the solution stack name or the template stack name. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | options | array<object> |  |
  | platformArn | string |  |
  | solutionStackName | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.describeEnvironment
**Describe environment** — Return description of an existing environment.
- Stability: stable
- Permissions: `elasticbeanstalk:DescribeEnvironments`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | environmentId | string | yes | ID of the AWS Elastic Beanstalk application environment. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | environment | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.listApplications
**List applications** — List the descriptions of existing applications that you have access to. Returns an empty array if they don’t exist or if you don’t have the right permissions.
- Stability: stable
- Permissions: `elasticbeanstalk:DescribeApplications`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | applicationNames | array<string> | no | If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | applications | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.listEnvironments
**List environments** — Return descriptions for existing environments that you have access to. Returns an empty array if they don’t exist or if you don’t have the right permissions.
- Stability: stable
- Permissions: `elasticbeanstalk:DescribeEnvironments`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | applicationName | string | no | If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application. |
  | environmentIds | array<string> | no | If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs. |
  | environmentNames | array<string> | no | If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | environments | array<object> |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.rebuildEnvironment
**Rebuild environment** — Delete and recreate all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and force a restart.
- Stability: stable
- Permissions: `elasticbeanstalk:RebuildEnvironment`, `autoscaling:*`, `elasticloadbalancing:*`, `ec2:*`
- Access: update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | environmentId | string | yes | The ID of the environment to rebuild. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.restartAppServer
**Restart app server** — Restart the application container server running on each Amazon EC2 instance in the specified environment.
- Stability: stable
- Permissions: `elasticbeanstalk:RestartAppServer`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | environmentId | string | yes | The ID of the environment to restart the server for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.elasticbeanstalk.updateEnvironment
**Update environment** — Update the environment description, deploy a new application version, update the configuration settings to an entirely new configuration template, or update select configuration option values in the running environment.
- Stability: stable
- Permissions: `elasticbeanstalk:UpdateEnvironment`, `cloudwatch:*`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | environmentId | string | yes | The ID of the environment to update. |
  | applicationName | string | no | The name of the application with which the environment is associated. |
  | description | string | no | If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment. |
  | optionSettings | array<object> | no | If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value. |
  | optionsToRemove | array<object> | no | A list of custom user-defined configuration options to remove from the configuration set for this environment. |
  | solutionStackName | string | no | This specifies the platform version that the environment will run after the environment is updated. |
  | templateName | string | no | If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. |
  | versionLabel | string | no | If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | environment | object |  |
  | amzRequestId | string | The unique identifier for the request. |

