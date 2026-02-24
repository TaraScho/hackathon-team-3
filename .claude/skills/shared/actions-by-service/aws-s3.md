# AWS S3 Actions
Bundle: `com.datadoghq.aws.s3` | 22 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Eaws%2Es3)

## com.datadoghq.aws.s3.block_public_access
**Block public access** — Block all public access to an existing S3 bucket and its contents.
- Stability: stable
- Permissions: `s3:PutBucketPublicAccessBlock`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the Amazon S3 bucket on which to set the `PublicAccessBlock` configuration. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | publicAccessBlockConfiguration | object | The `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 conside... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.copyObject
**Copy object** — Create a copy of an object that is already stored in Amazon S3.
- Stability: stable
- Permissions: `s3:GetObject`, `s3:PutObject`, `s3:GetObjectVersion`
- Access: read, create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceBucket | string | yes | Source bucket name of the object to copy. |
  | sourceKey | string | yes | Source key name of the object to copy. |
  | destinationKey | string | yes | Destination key name of the object to copy. |
  | destinationBucket | string | no | Destination bucket name of the object to copy. If not defined, the destination bucket is the same as the source bucket. |
  | expectedSourceBucketOwner | string | no | The account ID of the expected source bucket owner. If the source bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |
  | expectedBucketOwner | string | no | The account ID of the expected destination bucket owner. If the destination bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | copyObjectResult | object | Container for all response elements. |
  | versionId | string | Version ID of the newly created copy.  This functionality is not supported for directory buckets. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.create_s3_bucket
**Create bucket** — Create a new S3 bucket.
- Stability: stable
- Permissions: `s3:CreateBucket`
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket to create.  General purpose buckets - For information about bucket naming restrictions, see Bucket naming rules in the Amazon S3 User Guide.  Directory buckets  - When you us... |
  | cannedAcl | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | location | string | The name of the bucket preceded by a forward slash. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.deleteObject
**Delete object** — Remove the null version (if there is one) of an object and insert a `delete` marker. If there isn't a null version, Amazon S3 does not remove any objects but still responds that the command was successful.
- Stability: stable
- Permissions: `s3:DeleteObject`, `s3:DeleteObjectVersion`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | Bucket name of the object to delete. |
  | key | string | yes | Key name of the object to delete. |
  | versionId | string | no |  |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleteMarker | boolean | Indicates whether the specified object version that was permanently deleted was (true) or was not (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) o... |
  | versionId | string | Returns the version ID of the delete marker created as a result of the DELETE operation.  This functionality is not supported for directory buckets. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.delete_s3_bucket
**Delete bucket** — Delete an S3 bucket.
- Stability: stable
- Permissions: `s3:DeleteBucket`
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | Specifies the bucket being deleted.  Directory buckets  - When you use this operation with a directory bucket, you must use path-style requests in the format https://s3express-control.region_code.a... |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.disableBucketLogging
**Disable bucket logging** — Set the logging parameters for a bucket, and specify permissions for who can view and modify the logging parameters.
- Stability: stable
- Permissions: `s3:PutBucketLogging`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket for which to disable logging. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.enableBucketLogging
**Enable bucket logging** — Set the logging parameters for a bucket, and specify permissions for who can view and modify the logging parameters.
- Stability: stable
- Permissions: `s3:PutBucketLogging`, `s3:GetBucketLogging`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket for which to set the logging parameters. |
  | targetBucket | string | yes | Specifies the bucket where you want Amazon S3 to store server access logs. |
  | targetPrefix | string | yes | A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket. |
  | targetGrants | array<object> | no | Container for [granting](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html) information. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | TargetBucket | string | Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also ... |
  | TargetGrants | array<object> | Container for granting information. Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants. For more information, see [Permissions for server access log... |
  | TargetPrefix | string | A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket. |
  | TargetObjectKeyFormat | object | Amazon S3 key format for log objects. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.enable_default_bucket_encryption
**Enable default bucket encryption** — Configure default encryption and S3 bucket keys for an existing bucket.
- Stability: stable
- Permissions: `s3:PutEncryptionConfiguration`, `s3:GetEncryptionConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | Enable default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3) or customer-managed keys (SSE-KMS). For information about the Amazon S3 default encryption f... |
  | keyType | string | yes | `AES256` or `aws:kms`. Note that for KMS, bucket-level keys are enabled by default for all new objects. |
  | keyName | string | no | (Optional) The name of the key. This is only applicable when the `key_type` is `aws:kms`. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | rules | array<object> | A container for information about a server-side encryption configuration rule. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.enrich_s3_bucket
**List buckets (enrich)** — Return a list of all buckets owned by the authenticated sender of the request.
- Stability: stable
- Permissions: `s3:ListBucket`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | search | string | no | Returns the list of items matching the search criteria. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | options | array<object> | List of results to display in the dropdown. |
  | placeholder | string | Placeholder text to display when the dropdown has no selection |
  | icon | object | Icon to display in the dropdown. |


## com.datadoghq.aws.s3.getBucketLifecycleConfiguration
**Get bucket lifecycle configuration** — Returns the lifecycle configuration information set on the bucket.
- Stability: stable
- Permissions: `s3:GetBucketLifecycleConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket for which to get the lifecycle information. |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code 403 Forbidden (access deni... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | Rules | array<object> | Container for a lifecycle rule. |
  | TransitionDefaultMinimumObjectSize | string | Indicates which default minimum object size behavior is applied to the lifecycle configuration.    all_storage_classes_128K - Objects smaller than 128 KB will not transition to any storage class by... |


## com.datadoghq.aws.s3.getBucketLogging
**Get bucket logging** — Return the logging status of a bucket, and the permissions users have to view and modify that status.
- Stability: stable
- Permissions: `s3:GetBucketLogging`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The bucket name for which to get the logging information. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | TargetBucket | string | Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also ... |
  | TargetGrants | array<object> | Container for granting information. Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants. For more information, see [Permissions for server access log... |
  | TargetPrefix | string | A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket. |
  | TargetObjectKeyFormat | object | Amazon S3 key format for log objects. |


## com.datadoghq.aws.s3.getObject
**Get object** — Retrieve objects from Amazon S3.
- Stability: stable
- Permissions: `s3:GetObject`, `s3:GetObjectVersion`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The bucket name containing the object.   Directory buckets - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format  Bucket_name.s3express-az_... |
  | key | string | yes | Key of the object to get. |
  | versionId | string | no |  |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |
  | responseParsing | string | no | Use if you want to override the default response parsing method which is inferred from the HTTP headers of the object. |
  | responseEncoding | string | no | Use if you want to override the default encoding in response HTTP headers. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | lastModified | string | Date and time when the object was last modified.  General purpose buckets  - When you specify a versionId of the object in your request, if the specified version in the request is a delete marker, ... |
  | contentLength | number | Size of the body in bytes. |
  | eTag | string | An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL. |
  | checksumSHA256 | string | The base64-encoded, 256-bit SHA-256 digest of the object. This will only be present if it was uploaded with the object. With multipart uploads, this may not be a checksum value of the object. For m... |
  | versionId | string | Version ID of the object.  This functionality is not supported for directory buckets. |
  | contentType | string | A standard MIME type describing the format of the object data. |
  | serverSideEncryption | string | The server-side encryption algorithm used when storing this object in Amazon S3 (for example, `AES256`, `aws:kms`). |
  | object | any |  |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.getObjectAttributes
**Get object attributes** — Retrieve all metadata from an object, without returning the object itself.
- Stability: stable
- Permissions: `s3:GetObject`, `s3:GetObjectAttributes`, `s3:GetObjectVersion`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket that contains the object. When using this action with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessP... |
  | key | string | yes | The object key. |
  | versionId | string | no |  |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | deleteMarker | boolean | Specifies whether the object retrieved was (true) or was not (false) a delete marker. If false, this response header does not appear in the response.  This functionality is not supported for direct... |
  | lastModified | string | The creation date of the object. |
  | eTag | string | An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL. |
  | versionId | string | The version ID of the object.  This functionality is not supported for directory buckets. |
  | checksum | object | The checksum or digest of the object. |
  | storageClass | string | Provides the storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects. For more information, see [Storage Classes](https:/... |
  | objectSize | number | The size of the object in bytes. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.getPreSignedURL
**Get pre-signed URL** — Get a pre-signed URL for a given operation name.
- Stability: stable
- Permissions: `depend on the operation`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | operation | any | yes | The operation to perform. See [the docs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_Simple_Storage_Service.html) for a list of the operations. |
  | expiresIn | number | no | The number of seconds to expire the pre-signed URL in. Defaults to 15 minutes. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | url | string |  |


## com.datadoghq.aws.s3.get_s3_bucket_encryption
**Get bucket encryption** — Return the default encryption configuration for an S3 bucket.
- Stability: stable
- Permissions: `s3:GetEncryptionConfiguration`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket from which the server-side encryption configuration is retrieved.  Directory buckets  - When you use this operation with a directory bucket, you must use path-style requests ... |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | rules | array<object> |  |
  | encrypted | boolean |  |


## com.datadoghq.aws.s3.listObjects
**List objects** — Return up to 1,000 objects in a bucket with each request.
- Stability: stable
- Permissions: `s3:ListBucket`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | Directory buckets - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format  Bucket_name.s3express-az_id.region.amazonaws.com. Path-style reque... |
  | prefix | string | no | Limit the response to keys that begin with a prefix. |
  | startAfter | string | no | The point from which Amazon S3 starts listing. `StartAfter` can be any key in the bucket. |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |
  | continuationToken | string | no | ContinuationToken indicates to Amazon S3 that the list is being continued on this bucket with a token. |
  | maxKeys | number | no | Sets the maximum number of keys returned in the response. By default the action returns up to 1,000 key names. The response might contain fewer keys but will never contain more. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | isTruncated | boolean | Set to false if all of the results were returned. Set to true if more keys are available to return. If the number of results exceeds that specified by MaxKeys, all of the results might not be retur... |
  | objects | array<object> | Metadata about each object returned. |
  | keyCount | number | KeyCount is the number of keys returned with this request. KeyCount will always be less than or equal to the MaxKeys field. For example, if you ask for 50 keys, your result will include 50 keys or ... |
  | commonPrefixes | array<object> | All of the keys (up to 1,000) rolled up into a common prefix count as a single return when calculating the number of returns.  A response can contain `CommonPrefixes` only if you specify a delimite... |
  | continuationToken | string | If ContinuationToken was sent with the request, it is included in the response. You can use the returned ContinuationToken for pagination of the list response. You can use this ContinuationToken fo... |
  | nextContinuationToken | string | `NextContinuationToken` is sent when `isTruncated` is `true`, which means there are more keys in the bucket that can be listed. The next list requests to Amazon S3 can be continued with this `NextC... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.list_s3_buckets
**List buckets** — Return a list of all buckets owned by the authenticated sender of the request.
- Stability: stable
- Permissions: `s3:ListBucket`
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | prefix | string | no | Limits the response to bucket names that begin with the specified bucket name prefix. |
  | continuationToken | string | no | ContinuationToken indicates to Amazon S3 that the list is being continued on this bucket with a token. |
  | maxBuckets | number | no | Maximum number of buckets to be returned in response. |
  | bucketRegion | any | no | Limits the response to buckets that are located in the specified Amazon Web Services Region. Requests made to a Regional endpoint that is different from the bucket-region parameter are not supporte... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | buckets | array<object> | The list of buckets owned by the requester. |
  | prefix | string | If Prefix was sent with the request, it is included in the response. All bucket names in the response begin with the specified bucket name prefix. |
  | continuationToken | string | ContinuationToken is included in the response when there are more buckets that can be listed with pagination. The next ListBuckets request to Amazon S3 can be continued with this ContinuationToken.... |
  | owner | object | The owner of the buckets listed. |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.moveObject
**Move object** — Move an object from one bucket to another. To make changes to the key name, use the `Rename` action next.
- Stability: stable
- Permissions: `s3:GetObject`, `s3:PutObject`, `s3:GetObjectVersion`, `s3:DeleteObject`, `s3:DeleteObjectVersion`
- Access: read, create, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | sourceBucket | string | yes | Source bucket name of the object to move. |
  | destinationBucket | string | yes | Destination bucket name of the object to move. |
  | key | string | yes | Key of the object to move. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | copyObjectResult | object | Container for all response elements. |
  | versionId | string | Version ID of the newly created copy.  This functionality is not supported for directory buckets. |


## com.datadoghq.aws.s3.putBucketLifecycleConfiguration
**Put bucket lifecycle configuration** — Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle configuration. Keep in mind that this will overwrite an existing lifecycle configuration, so if you want to retain any configuration details, they must be included in the new lifecycle configuration. This operation is not supported by directory buckets.
- Stability: stable
- Permissions: `s3:PutBucketLifecycleConfiguration`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The name of the bucket for which to set the configuration. |
  | checksumAlgorithm | string | no | Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this heade... |
  | lifecycleConfiguration | object | no | Container for lifecycle rules. You can add as many as 1,000 rules. |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code 403 Forbidden (access deni... |
  | transitionDefaultMinimumObjectSize | string | no | Indicates which default minimum object size behavior is applied to the lifecycle configuration.    all_storage_classes_128K - Objects smaller than 128 KB will not transition to any storage class by... |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |
  | TransitionDefaultMinimumObjectSize | string | Indicates which default minimum object size behavior is applied to the lifecycle configuration.    all_storage_classes_128K - Objects smaller than 128 KB will not transition to any storage class by... |


## com.datadoghq.aws.s3.putObject
**Put object** — Add an object to a bucket. You must have `WRITE` permissions on a bucket to add an object.
- Stability: stable
- Permissions: `s3:PutObject`
- Access: create, update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The bucket name to which the PUT action was initiated.   Directory buckets - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format  Bucket_na... |
  | key | string | yes | Object key for which the `PUT` action was initiated. |
  | body | string | no |  |
  | cannedAcl | string | no |  |
  | contentType | string | no | A standard MIME type describing the format of the contents. |
  | serverSideEncryption | string | no | The server-side encryption algorithm used when storing this object in Amazon S3 (for example, `AES256`, `aws:kms`). |
  | storageClass | string | no | The storage class of the object. By default, Amazon S3 uses the STANDARD Storage Class to store newly created objects. Depending on performance needs, you can specify a different Storage Class. Ama... |
  | expectedBucketOwner | string | no | The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | eTag | string | Entity tag for the uploaded object.  General purpose buckets  - To ensure that data is not corrupted traversing the network, for objects where the ETag is the MD5 digest of the object, you can calc... |
  | serverSideEncryption | string | The server-side encryption algorithm used when you store this object in Amazon S3. |
  | versionId | string | Version ID of the object. If you enable versioning for a bucket, Amazon S3 automatically generates a unique version ID for the object being stored. Amazon S3 returns this ID in the response. When y... |
  | bucketKeyEnabled | boolean | Indicates whether the uploaded object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS). |
  | checksumSHA256 | string | The base64-encoded, 256-bit SHA-256 digest of the object. This will only be present if it was uploaded with the object. With multipart uploads, this may not be a checksum value of the object. For m... |
  | amzRequestId | string | The unique identifier for the request. |


## com.datadoghq.aws.s3.renameObject
**Rename object** — Rename an object's key in a bucket. For cases where users want to make changes across buckets they should use the move action first.
- Stability: stable
- Permissions: `s3:GetObject`, `s3:PutObject`, `s3:GetObjectVersion`, `s3:DeleteObject`, `s3:DeleteObjectVersion`
- Access: read, update, delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | Bucket name of the object to rename. |
  | originalKey | string | yes | Original key of the object to rename. |
  | newKey | string | yes | New key of the object to rename. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | copyObjectResult | object | Container for all response elements. |
  | versionId | string | Version ID of the newly created copy.  This functionality is not supported for directory buckets. |


## com.datadoghq.aws.s3.set_canned_acl
**Set canned ACL** — Set the permissions on an existing bucket using access control lists (ACL).
- Stability: stable
- Permissions: `s3:PutBucketAcl`
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | region | string | yes |  |
  | bucket | string | yes | The bucket to which to apply the ACL. |
  | cannedAcl | string | no |  |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | amzRequestId | string | The unique identifier for the request. |

