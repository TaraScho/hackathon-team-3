# Datadog CCM Actions
Bundle: `com.datadoghq.dd.cloudcostmanagement` | 11 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Ecloudcostmanagement)

## com.datadoghq.dd.cloudcostmanagement.createCostAWSCURConfig
**Create AWS CUR config** — Create a Cloud Cost Management account for an AWS CUR config.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_filters | object | no | The account filtering configuration. |
  | account_id | string | yes | The AWS account ID. |
  | bucket_name | string | yes | The AWS bucket name used to store the Cost and Usage Report. |
  | bucket_region | string | no | The region the bucket is located in. |
  | months | number | no | The month of the report. |
  | report_name | string | yes | The name of the Cost and Usage Report. |
  | report_prefix | string | yes | The report prefix used for the Cost and Usage Report. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | The definition of `AwsCurConfigResponseData` object. |


## com.datadoghq.dd.cloudcostmanagement.createCostAzureUCConfigs
**Create Azure UC configs** — Create a Cloud Cost Management account for an Azure config.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | The tenant ID of the Azure account. |
  | actual_bill_config | object | yes | Bill config. |
  | amortized_bill_config | object | yes | Bill config. |
  | client_id | string | yes | The client ID of the Azure account. |
  | scope | string | yes | The scope of your observed subscription. |
  | is_enabled | boolean | no | Whether or not the Cloud Cost Management account is enabled. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Azure config pair. |


## com.datadoghq.dd.cloudcostmanagement.deleteCostAWSCURConfig
**Delete AWS CUR config** — Archive a Cloud Cost Management Account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | cloud_account_id | number | yes | Cloud Account id. |


## com.datadoghq.dd.cloudcostmanagement.deleteCostAzureUCConfig
**Delete Azure UC config** — Archive a Cloud Cost Management Account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | cloud_account_id | number | yes | Cloud Account id. |


## com.datadoghq.dd.cloudcostmanagement.deleteCustomCostsFile
**Delete custom costs file** — Delete the specified Custom Costs file.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | file_id | string | yes | File ID. |


## com.datadoghq.dd.cloudcostmanagement.getCustomCostsFile
**Get custom costs file** — Fetch the specified Custom Costs file.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | file_id | string | yes | File ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | JSON API format of for a Custom Costs file with content. |
  | meta | object | Meta for the response from the Get Custom Costs endpoints. |


## com.datadoghq.dd.cloudcostmanagement.listCostAWSCURConfigs
**List AWS CUR configs** — List the AWS CUR configs.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An AWS CUR config. |


## com.datadoghq.dd.cloudcostmanagement.listCostAzureUCConfigs
**List Azure UC configs** — List the Azure configs.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An Azure config pair. |


## com.datadoghq.dd.cloudcostmanagement.listCustomCostsFiles
**List custom costs files** — List the Custom Costs files.
- Stability: stable
- Access: read
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | page_number | number | no | Page number for pagination. |
  | page_size | number | no | Page size for pagination. |
  | filter_status | string | no | Filter by file status. |
  | sort | string | no | Sort key with optional descending prefix. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | List of Custom Costs files. |
  | meta | object | Meta for the response from the List Custom Costs endpoints. |


## com.datadoghq.dd.cloudcostmanagement.updateCostAWSCURConfig
**Update AWS CUR config** — Update the status (active/archived) or account filtering configuration of an AWS CUR config.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | cloud_account_id | number | yes | Cloud Account id. |
  | account_filters | object | no | The account filtering configuration. |
  | is_enabled | boolean | no | Whether or not the Cloud Cost Management account is enabled. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | An AWS CUR config. |


## com.datadoghq.dd.cloudcostmanagement.updateCostAzureUCConfigs
**Update Azure UC configs** — Update the status of an  Azure config (active/archived).
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | cloud_account_id | number | yes | Cloud Account id. |
  | is_enabled | boolean | yes | Whether or not the Cloud Cost Management account is enabled. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Azure config pair. |

