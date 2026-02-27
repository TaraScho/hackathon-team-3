# AWS ECR Actions
Bundle: `com.datadoghq.aws.ecr` | 37 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Eecr)

## com.datadoghq.aws.ecr.batchCheckLayerAvailability
**Batch check layer availability** — Checks the availability of one or more image layers in a repository. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.  This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.
- Stability: stable
- Permissions: `ecr:BatchCheckLayerAvailability`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository that is associated with the image layers to check. |
  | layerDigests | array<string> | yes | The digests of the image layers to check. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | layers | array<object> | A list of image layer objects corresponding to the image layer references in the request. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecr.batchDeleteImage
**Batch delete image** — Deletes a list of specified images within a repository. Images are specified with either an imageTag or imageDigest. You can remove a tag from an image by specifying the image&#x27;s tag in your request. When you remove the last tag from an image, the image is deleted from your repository. You can completely delete an image (and all of its tags) by specifying the image&#x27;s digest in your request.
- Stability: stable
- Permissions: `ecr:BatchDeleteImage`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The repository that contains the image to delete. |
  | imageIds | array<object> | yes | A list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | imageIds | array<object> | The image IDs of the deleted images. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecr.batchGetImage
**Batch get image** — Gets detailed information for an image. Images are specified with either an imageTag or imageDigest. When an image is pulled, the BatchGetImage API is called once to retrieve the image manifest.
- Stability: stable
- Permissions: `ecr:BatchGetImage`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The repository that contains the images to describe. |
  | imageIds | array<object> | yes | A list of image ID references that correspond to images to describe. The format of the imageIds reference is imageTag=tag or imageDigest=digest. |
  | acceptedMediaTypes | array<string> | no | The accepted media types for the request. Valid values: application/vnd.docker.distribution.manifest.v1+json \| application/vnd.docker.distribution.manifest.v2+json \| application/vnd.oci.image.manif... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | images | array<object> | A list of image objects corresponding to the image references in the request. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecr.batchGetRepositoryScanningConfiguration
**Batch get repository scanning configuration** — Gets the scanning configuration for one or more repositories.
- Stability: stable
- Permissions: `ecr:BatchGetRepositoryScanningConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | repositoryNames | array<string> | yes | One or more repository names to get the scanning configuration for. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | scanningConfigurations | array<object> | The scanning configuration for the requested repositories. |
  | failures | array<object> | Any failures associated with the call. |


## com.datadoghq.aws.ecr.createPullThroughCacheRule
**Create pull through cache rule** — Creates a pull through cache rule. A pull through cache rule provides a way to cache images from an upstream registry source in your Amazon ECR private registry. For more information, see Using pull through cache rules in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:CreatePullThroughCacheRule`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ecrRepositoryPrefix | string | yes | The repository name prefix to use when caching images from the source registry. |
  | upstreamRegistryUrl | string | yes | The registry URL of the upstream public registry to use as the source for the pull through cache rule. The following is the syntax to use for each supported upstream registry.   Amazon ECR Public (... |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry to create the pull through cache rule for. If you do not specify a registry, the default registry is assumed. |
  | upstreamRegistry | string | no | The name of the upstream registry. |
  | credentialArn | string | no | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ecrRepositoryPrefix | string | The Amazon ECR repository prefix associated with the pull through cache rule. |
  | upstreamRegistryUrl | string | The upstream registry URL associated with the pull through cache rule. |
  | createdAt | string | The date and time, in JavaScript date format, when the pull through cache rule was created. |
  | registryId | string | The registry ID associated with the request. |
  | upstreamRegistry | string | The name of the upstream registry associated with the pull through cache rule. |
  | credentialArn | string | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule. |


## com.datadoghq.aws.ecr.createRepository
**Create repository** — Creates a repository. For more information, see Amazon ECR repositories in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:CreateRepository`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry to create the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as ... |
  | tags | any | no | The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum chara... |
  | imageTagMutability | string | no | The tag mutability setting for the repository. If this parameter is omitted, the default setting of MUTABLE will be used which will allow image tags to be overwritten. If IMMUTABLE is specified, al... |
  | imageScanningConfiguration | object | no | The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository. |
  | encryptionConfiguration | object | no | The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | repository | object | The repository that was created. |


## com.datadoghq.aws.ecr.deleteLifecyclePolicy
**Delete lifecycle policy** — Deletes the lifecycle policy associated with the specified repository.
- Stability: stable
- Permissions: `ecr:DeleteLifecyclePolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | lifecyclePolicyText | string | The JSON lifecycle policy text. |
  | lastEvaluatedAt | string | The time stamp of the last time that the lifecycle policy was run. |


## com.datadoghq.aws.ecr.deletePullThroughCacheRule
**Delete pull through cache rule** — Deletes a pull through cache rule.
- Stability: stable
- Permissions: `ecr:DeletePullThroughCacheRule`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ecrRepositoryPrefix | string | yes | The Amazon ECR repository prefix associated with the pull through cache rule to delete. |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the pull through cache rule. If you do not specify a registry, the default registry is assumed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ecrRepositoryPrefix | string | The Amazon ECR repository prefix associated with the request. |
  | upstreamRegistryUrl | string | The upstream registry URL associated with the pull through cache rule. |
  | createdAt | string | The timestamp associated with the pull through cache rule. |
  | registryId | string | The registry ID associated with the request. |
  | credentialArn | string | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule. |


## com.datadoghq.aws.ecr.deleteRegistryPolicy
**Delete registry policy** — Deletes the registry permissions policy.
- Stability: stable
- Permissions: `ecr:DeleteRegistryPolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | policyText | string | The contents of the registry permissions policy that was deleted. |


## com.datadoghq.aws.ecr.deleteRepository
**Delete repository** — Deletes a repository. If the repository isn&#x27;t empty, you must either delete the contents of the repository or use the force option to delete the repository and have Amazon ECR delete all of its contents on your behalf.
- Stability: stable
- Permissions: `ecr:DeleteRepository`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository to delete. |
  | force | boolean | no | If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | repository | object | The repository that was deleted. |


## com.datadoghq.aws.ecr.deleteRepositoryPolicy
**Delete repository policy** — Deletes the repository policy associated with the specified repository.
- Stability: stable
- Permissions: `ecr:DeleteRepositoryPolicy`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository that is associated with the repository policy to delete. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | policyText | string | The JSON repository policy that was deleted from the repository. |


## com.datadoghq.aws.ecr.describeImageReplicationStatus
**Describe image replication status** — Returns the replication status for a specified image.
- Stability: stable
- Permissions: `ecr:DescribeImageReplicationStatus`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | repositoryName | string | yes | The name of the repository that the image is in. |
  | imageId | object | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry. If you do not specify a registry, the default registry is assumed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | repositoryName | string | The repository name associated with the request. |
  | imageId | object |  |
  | replicationStatuses | array<object> | The replication status details for the images in the specified repository. |


## com.datadoghq.aws.ecr.describeImageScanFindings
**Describe image scan findings** — Returns the scan findings for the specified image.
- Stability: stable
- Permissions: `ecr:DescribeImageScanFindings`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to describe the image scan findings for. If you do not specify a registry, the default registry... |
  | repositoryName | string | yes | The repository for the image for which to describe the scan findings. |
  | imageId | object | yes |  |
  | nextToken | string | no | The nextToken value returned from a previous paginated DescribeImageScanFindings request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from th... |
  | maxResults | number | no | The maximum number of image scan results returned by DescribeImageScanFindings in paginated output. When this parameter is used, DescribeImageScanFindings only returns maxResults results in a singl... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | imageId | object |  |
  | imageScanStatus | object | The current state of the scan. |
  | imageScanFindings | object | The information contained in the image scan findings. |
  | nextToken | string | The nextToken value to include in a future DescribeImageScanFindings request. When the results of a DescribeImageScanFindings request exceed maxResults, this value can be used to retrieve the next ... |


## com.datadoghq.aws.ecr.describeImages
**Describe images** — Returns metadata about the images in a repository.  Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the docker images command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by DescribeImages.
- Stability: stable
- Permissions: `ecr:DescribeImages`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The repository that contains the images to describe. |
  | imageIds | array<object> | no | The list of image IDs for the requested repository. |
  | nextToken | string | no | The nextToken value returned from a previous paginated DescribeImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of th... |
  | maxResults | number | no | The maximum number of repository results returned by DescribeImages in paginated output. When this parameter is used, DescribeImages only returns maxResults results in a single page along with a ne... |
  | filter | object | no | The filter key and value with which to filter your DescribeImages results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | imageDetails | array<object> | A list of ImageDetail objects that contain data about the image. |
  | nextToken | string | The nextToken value to include in a future DescribeImages request. When the results of a DescribeImages request exceed maxResults, this value can be used to retrieve the next page of results. This ... |


## com.datadoghq.aws.ecr.describePullThroughCacheRules
**Describe pull through cache rules** — Returns the pull through cache rules for a registry.
- Stability: stable
- Permissions: `ecr:DescribePullThroughCacheRules`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry to return the pull through cache rules for. If you do not specify a registry, the default registry is assumed. |
  | ecrRepositoryPrefixes | array<string> | no | The Amazon ECR repository prefixes associated with the pull through cache rules to return. If no repository prefix value is specified, all pull through cache rules are returned. |
  | nextToken | string | no | The nextToken value returned from a previous paginated DescribePullThroughCacheRulesRequest request where maxResults was used and the results exceeded the value of that parameter. Pagination contin... |
  | maxResults | number | no | The maximum number of pull through cache rules returned by DescribePullThroughCacheRulesRequest in paginated output. When this parameter is used, DescribePullThroughCacheRulesRequest only returns m... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | pullThroughCacheRules | array<object> | The details of the pull through cache rules. |
  | nextToken | string | The nextToken value to include in a future DescribePullThroughCacheRulesRequest request. When the results of a DescribePullThroughCacheRulesRequest request exceed maxResults, this value can be used... |


## com.datadoghq.aws.ecr.describeRegistry
**Describe registry** — Describes the settings for a registry. The replication configuration for a repository can be created or updated with the PutReplicationConfiguration API action.
- Stability: stable
- Permissions: `ecr:DescribeRegistry`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | replicationConfiguration | object | The replication configuration for the registry. |


## com.datadoghq.aws.ecr.describeRepositories
**Describe repositories** — Describes image repositories in a registry.
- Stability: stable
- Permissions: `ecr:DescribeRepositories`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed. |
  | repositoryNames | array<string> | no | A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described. |
  | nextToken | string | no | The nextToken value returned from a previous paginated DescribeRepositories request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end... |
  | maxResults | number | no | The maximum number of repository results returned by DescribeRepositories in paginated output. When this parameter is used, DescribeRepositories only returns maxResults results in a single page alo... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | repositories | array<object> | A list of repository objects corresponding to valid repositories. |
  | nextToken | string | The nextToken value to include in a future DescribeRepositories request. When the results of a DescribeRepositories request exceed maxResults, this value can be used to retrieve the next page of re... |


## com.datadoghq.aws.ecr.getLifecyclePolicy
**Get lifecycle policy** — Retrieves the lifecycle policy for the specified repository.
- Stability: stable
- Permissions: `ecr:GetLifecyclePolicy`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | lifecyclePolicyText | string | The JSON lifecycle policy text. |
  | lastEvaluatedAt | string | The time stamp of the last time that the lifecycle policy was run. |


## com.datadoghq.aws.ecr.getLifecyclePolicyPreview
**Get lifecycle policy preview** — Retrieves the results of the lifecycle policy preview request for the specified repository.
- Stability: stable
- Permissions: `ecr:GetLifecyclePolicyPreview`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository. |
  | imageIds | array<object> | no | The list of imageIDs to be included. |
  | nextToken | string | no | The nextToken value returned from a previous paginated  GetLifecyclePolicyPreviewRequest request where maxResults was used and the  results exceeded the value of that parameter. Pagination continue... |
  | maxResults | number | no | The maximum number of repository results returned by GetLifecyclePolicyPreviewRequest in  paginated output. When this parameter is used, GetLifecyclePolicyPreviewRequest only returns  maxResults re... |
  | filter | object | no | An optional parameter that filters results based on image tag status and all tags, if tagged. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | lifecyclePolicyText | string | The JSON lifecycle policy text. |
  | status | string | The status of the lifecycle policy preview request. |
  | nextToken | string | The nextToken value to include in a future GetLifecyclePolicyPreview request. When the results of a GetLifecyclePolicyPreview request exceed maxResults, this value can be used to retrieve the next ... |
  | previewResults | array<object> | The results of the lifecycle policy preview request. |
  | summary | object | The list of images that is returned as a result of the action. |


## com.datadoghq.aws.ecr.getRegistryPolicy
**Get registry policy** — Retrieves the permissions policy for a registry.
- Stability: stable
- Permissions: `ecr:GetRegistryPolicy`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | policyText | string | The JSON text of the permissions policy for a registry. |


## com.datadoghq.aws.ecr.getRegistryScanningConfiguration
**Get registry scanning configuration** — Retrieves the scanning configuration for a registry.
- Stability: stable
- Permissions: `ecr:GetRegistryScanningConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | scanningConfiguration | object | The scanning configuration for the registry. |


## com.datadoghq.aws.ecr.getRepositoryPolicy
**Get repository policy** — Retrieves the repository policy for the specified repository.
- Stability: stable
- Permissions: `ecr:GetRepositoryPolicy`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository with the policy to retrieve. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | policyText | string | The JSON repository policy text associated with the repository. |


## com.datadoghq.aws.ecr.listImages
**List images** — Lists image IDs for the specified repository. You can filter images based on whether or not they are tagged by using the tagStatus filter and specifying either TAGGED, UNTAGGED, or ANY. For example, you can filter your results to return only UNTAGGED images, and then pipe that result to a BatchDeleteImage operation to delete them. You can also filter your results to return only TAGGED images to list all of the tags in your repository.
- Stability: stable
- Permissions: `ecr:ListImages`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The repository with image IDs to be listed. |
  | nextToken | string | no | The nextToken value returned from a previous paginated ListImages request where maxResults was used and the results exceeded the value of that parameter. Pagination continues from the end of the pr... |
  | maxResults | number | no | The maximum number of image results returned by ListImages in paginated output. When this parameter is used, ListImages only returns maxResults results in a single page along with a nextToken respo... |
  | filter | object | no | The filter key and value with which to filter your ListImages results. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | imageIds | array<object> | The list of image IDs for the requested repository. |
  | nextToken | string | The nextToken value to include in a future ListImages request. When the results of a ListImages request exceed maxResults, this value can be used to retrieve the next page of results. This value is... |


## com.datadoghq.aws.ecr.listTagsForResource
**List tags for resource** — List the tags for an Amazon ECR resource.
- Stability: stable
- Permissions: `ecr:ListTagsForResource`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon ECR repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | tags | array<object> | The tags for the resource. |


## com.datadoghq.aws.ecr.putImageScanningConfiguration
**Put image scanning configuration** — The PutImageScanningConfiguration API is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see PutRegistryScanningConfiguration.  Updates the image scanning configuration for the specified repository.
- Stability: stable
- Permissions: `ecr:PutImageScanningConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image scanning configuration setting. If you do not specify a registry, the defau... |
  | repositoryName | string | yes | The name of the repository in which to update the image scanning configuration setting. |
  | imageScanningConfiguration | object | yes | The image scanning configuration for the repository. This setting determines whether images are scanned for known vulnerabilities after being pushed to the repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | imageScanningConfiguration | object | The image scanning configuration setting for the repository. |


## com.datadoghq.aws.ecr.putImageTagMutability
**Put image tag mutability** — Updates the image tag mutability settings for the specified repository. For more information, see Image tag mutability in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:PutImageTagMutability`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to update the image tag mutability settings. If you do not specify a registry, the default regi... |
  | repositoryName | string | yes | The name of the repository in which to update the image tag mutability settings. |
  | imageTagMutability | string | yes | The tag mutability setting for the repository. If MUTABLE is specified, image tags can be overwritten. If IMMUTABLE is specified, all image tags within the repository will be immutable which will p... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | imageTagMutability | string | The image tag mutability setting for the repository. |


## com.datadoghq.aws.ecr.putLifecyclePolicy
**Put lifecycle policy** — Creates or updates the lifecycle policy for the specified repository. For more information, see Lifecycle policy template.
- Stability: stable
- Permissions: `ecr:PutLifecyclePolicy`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do  not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository to receive the policy. |
  | lifecyclePolicyText | string | yes | The JSON repository policy text to apply to the repository. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | lifecyclePolicyText | string | The JSON repository policy text. |


## com.datadoghq.aws.ecr.putRegistryPolicy
**Put registry policy** — Creates or updates the permissions policy for your registry. A registry policy is used to specify permissions for another Amazon Web Services account and is used when configuring cross-account replication. For more information, see Registry permissions in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:PutRegistryPolicy`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | policyText | string | yes | The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions in the Amazon Elastic Container Registry U... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | policyText | string | The JSON policy text for your registry. |


## com.datadoghq.aws.ecr.putRegistryScanningConfiguration
**Put registry scanning configuration** — Creates or updates the scanning configuration for your private registry.
- Stability: stable
- Permissions: `ecr:PutRegistryScanningConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | scanType | string | no | The scanning type to set for the registry. When a registry scanning configuration is not defined, by default the BASIC scan type is used. When basic scanning is used, you may specify filters to det... |
  | rules | array<object> | no | The scanning rules to use for the registry. A scanning rule is used to determine which repository filters are used and at what frequency scanning will occur. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryScanningConfiguration | object | The scanning configuration for your registry. |


## com.datadoghq.aws.ecr.putReplicationConfiguration
**Put replication configuration** — Creates or updates the replication configuration for a registry. The existing replication configuration for a repository can be retrieved with the DescribeRegistry API action. The first time the PutReplicationConfiguration API is called, a service-linked IAM role is created in your account for the replication process. For more information, see [Using service-linked roles for Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/using-service-linked-roles.html) in the Amazon Elastic Container Registry User Guide. For more information on the custom role for replication, see [Creating an IAM role for replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).
- Stability: stable
- Permissions: `ecr:PutReplicationConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | replicationConfiguration | object | yes | An object representing the replication configuration for a registry. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | replicationConfiguration | object | The contents of the replication configuration for the registry. |


## com.datadoghq.aws.ecr.setRepositoryPolicy
**Set repository policy** — Applies a repository policy to the specified repository to control access permissions. For more information, see Amazon ECR Repository policies in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:SetRepositoryPolicy`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository to receive the policy. |
  | policyText | string | yes | The JSON repository policy text to apply to the repository. For more information, see Amazon ECR repository policies in the Amazon Elastic Container Registry User Guide. |
  | force | boolean | no | If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to pre... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | policyText | string | The JSON repository policy text applied to the repository. |


## com.datadoghq.aws.ecr.startImageScan
**Start image scan** — Starts an image vulnerability scan. An image scan can only be started once per 24 hours on an individual image. This limit includes if an image was scanned on initial push. For more information, see Image scanning in the Amazon Elastic Container Registry User Guide.
- Stability: stable
- Permissions: `ecr:StartImageScan`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository in which to start an image scan request. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository that contains the images to scan. |
  | imageId | object | yes |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | imageId | object |  |
  | imageScanStatus | object | The current state of the scan. |


## com.datadoghq.aws.ecr.startLifecyclePolicyPreview
**Start lifecycle policy preview** — Starts a preview of a lifecycle policy for the specified repository. This allows you to see the results before associating the lifecycle policy with the repository.
- Stability: stable
- Permissions: `ecr:StartLifecyclePolicyPreview`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed. |
  | repositoryName | string | yes | The name of the repository to be evaluated. |
  | lifecyclePolicyText | string | no | The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | registryId | string | The registry ID associated with the request. |
  | repositoryName | string | The repository name associated with the request. |
  | lifecyclePolicyText | string | The JSON repository policy text. |
  | status | string | The status of the lifecycle policy preview request. |


## com.datadoghq.aws.ecr.tagResource
**Tag resource** — Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.
- Stability: stable
- Permissions: `ecr:TagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository. |
  | tags | any | yes | The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecr.untagResource
**Untag resource** — Deletes specified tags from a resource.
- Stability: stable
- Permissions: `ecr:UntagResource`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | resourceArn | string | yes | The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository. |
  | tagKeys | array<string> | yes | The keys of the tags to be removed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.ecr.updatePullThroughCacheRule
**Update pull through cache rule** — Updates an existing pull through cache rule.
- Stability: stable
- Permissions: `ecr:UpdatePullThroughCacheRule`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | registryId | string | no | The Amazon Web Services account ID associated with the registry associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed. |
  | ecrRepositoryPrefix | string | yes | The repository name prefix to use when caching images from the source registry. |
  | credentialArn | string | yes | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that identifies the credentials to authenticate to the upstream registry. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ecrRepositoryPrefix | string | The Amazon ECR repository prefix associated with the pull through cache rule. |
  | registryId | string | The registry ID associated with the request. |
  | updatedAt | string | The date and time, in JavaScript date format, when the pull through cache rule was updated. |
  | credentialArn | string | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule. |


## com.datadoghq.aws.ecr.validatePullThroughCacheRule
**Validate pull through cache rule** — Validates an existing pull through cache rule for an upstream registry that requires authentication. This rule retrieves the contents of the Amazon Web Services Secrets Manager secret, verifies the syntax, and then validates that authentication to the upstream registry is successful.
- Stability: stable
- Permissions: `ecr:ValidatePullThroughCacheRule`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | ecrRepositoryPrefix | string | yes | The repository name prefix associated with the pull through cache rule. |
  | registryId | string | no | The registry ID associated with the pull through cache rule. If you do not specify a registry, the default registry is assumed. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | ecrRepositoryPrefix | string | The Amazon ECR repository prefix associated with the pull through cache rule. |
  | registryId | string | The registry ID associated with the request. |
  | upstreamRegistryUrl | string | The upstream registry URL associated with the pull through cache rule. |
  | credentialArn | string | The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret associated with the pull through cache rule. |
  | isValid | boolean | Whether or not the pull through cache rule was validated. If true, Amazon ECR was able to reach the upstream registry and authentication was successful. If false, there was an issue and validation ... |
  | failure | string | The reason the validation failed. For more details about possible causes and how to address them, see Using pull through cache rules in the Amazon Elastic Container Registry User Guide. |

