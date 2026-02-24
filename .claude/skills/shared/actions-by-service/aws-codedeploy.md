# AWS CodeDeploy Actions
Bundle: `com.datadoghq.aws.codedeploy` | 4 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Ecodedeploy)

## com.datadoghq.aws.codedeploy.createDeployment
**Create deployment** — Deploy an application revision through the specified deployment group.
- Stability: stable
- Permissions: `codedeploy:CreateDeployment`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | applicationName | string | yes | The name of an AWS CodeDeploy application associated with the IAM user or AWS account. |
  | autoRollbackConfiguration | object | no | [Configuration information](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AutoRollbackConfiguration.html) for an automatic rollback that is added when a deployment is created. |
  | deploymentConfigName | string | no | The name of a deployment configuration associated with the IAM user or AWS account. |
  | deploymentGroupName | string | no | The name of the deployment group. |
  | fileExistsBehavior | string | no | Information about how AWS CodeDeploy handles files that already exist in a deployment target location but weren't part of the previous successful deployment. Defaults to `DISALLOW`. |
  | ignoreApplicationStopFailures | boolean | no | If `true`, then if an `ApplicationStop`, `BeforeBlockTraffic`, or `AfterBlockTraffic` deployment lifecycle event to an instance fails, the deployment continues to the next deployment lifecycle event. |
  | revision | object | no | The type and [location](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RevisionLocation.html) of the revision to deploy. |
  | targetInstances | object | no | [Information about the instances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetInstances.html) that belong to the replacement environment in a blue/green deployment. |
  | updateOutdatedInstancesOnly | boolean | no | Indicates whether to deploy to all instances or only to instances that are not running the latest application revision. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deploymentId | string |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codedeploy.getDeployment
**Get deployment** — Get information about an AWS CodeDeploy deployment.
- Stability: stable
- Permissions: `codedeploy:GetDeployment`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | deploymentId | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deploymentInfo | object |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codedeploy.registerApplicationRevision
**Register application revision** — Register a revision for the specified application with AWS CodeDeploy.
- Stability: stable
- Permissions: `codedeploy:RegisterApplicationRevision`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | applicationName | string | yes |  |
  | description | string | no |  |
  | revisionType | string | no |  |
  | s3Location | object | no | Information about the [location](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_S3Location.html) of a revision stored in Amazon S3. |
  | appSpecContent | object | no | [The content](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AppSpecContent.html) of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or ... |
  | gitHubLocation | object | no | Information about the [location](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GitHubLocation.html) of application artifacts stored in GitHub. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.codedeploy.stopDeployment
**Stop deployment** — Attempt to stop an ongoing deployment.
- Stability: stable
- Permissions: `codedeploy:StopDeployment`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | deploymentId | string | yes |  |
  | autoRollbackEnabled | boolean | no | Indicates, when a deployment is stopped, whether instances that have been updated should be rolled back to the previous version of the application revision. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | status | string |  |
  | statusMessage | string |  |
  | amzRequestId | string | The unique identifier for the request. |

