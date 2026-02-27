# Datadog GCP Integration Actions
Bundle: `com.datadoghq.dd.integration.gcp` | 5 actions | [View in Datadog](https://app.datadoghq.com/actions/action-catalog#com%2Edatadoghq%2Edd%2Eintegration%2Egcp)

## com.datadoghq.dd.integration.gcp.createGCPSTSAccount
**Create GCP STS account** — Create a new entry within Datadog for your STS-enabled service account.
- Stability: stable
- Access: create
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_tags | array<string> | no | Tags to be associated with GCP metrics and service checks from your account. |
  | automute | boolean | no | Silence monitors for expected GCE instance shutdowns. |
  | client_email | string | no | Your service account email address. |
  | cloud_run_revision_filters | array<string> | no | List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. |
  | host_filters | array<string> | no | List of filters to limit the VM instances that are pulled into Datadog by using tags. |
  | is_cspm_enabled | boolean | no | When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. |
  | is_per_project_quota_enabled | boolean | no | When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project. |
  | is_resource_change_collection_enabled | boolean | no | When enabled, Datadog scans for all resource change data in your Google Cloud environment. |
  | is_security_command_center_enabled | boolean | no | When enabled, Datadog will attempt to collect Security Command Center Findings. |
  | metric_namespace_configs | array<object> | no | Configurations for GCP metric namespaces. |
  | monitored_resource_configs | array<object> | no | Configurations for GCP monitored resources. |
  | resource_collection_enabled | boolean | no | When enabled, Datadog scans for all resources in your GCP environment. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Info on your service account. |


## com.datadoghq.dd.integration.gcp.deleteGCPSTSAccount
**Delete GCP STS account** — Delete an STS-enabled service account.
- Stability: stable
- Access: delete
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your GCP STS enabled service account's unique ID. |


## com.datadoghq.dd.integration.gcp.getGCPSTSDelegate
**Get GCP STS delegate** — List your Datadog-GCP STS delegate account configured in your Datadog account.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Datadog principal service account info. |


## com.datadoghq.dd.integration.gcp.listGCPSTSAccounts
**List GCP STS accounts** — List all GCP STS-enabled service accounts configured in your Datadog account.
- Stability: stable
- Access: read
- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | array<object> | Array of GCP STS enabled service accounts. |


## com.datadoghq.dd.integration.gcp.updateGCPSTSAccount
**Update GCP STS account** — Update an STS-enabled service account.
- Stability: stable
- Access: update
- **Inputs**:

  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | account_id | string | yes | Your GCP STS enabled service account's unique ID. |
  | account_tags | array<string> | no | Tags to be associated with GCP metrics and service checks from your account. |
  | automute | boolean | no | Silence monitors for expected GCE instance shutdowns. |
  | client_email | string | no | Your service account email address. |
  | cloud_run_revision_filters | array<string> | no | List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags. |
  | host_filters | array<string> | no | List of filters to limit the VM instances that are pulled into Datadog by using tags. |
  | is_cspm_enabled | boolean | no | When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. |
  | is_per_project_quota_enabled | boolean | no | When enabled, Datadog applies the `X-Goog-User-Project` header, attributing Google Cloud billing and quota usage to the project being monitored rather than the default service account project. |
  | is_resource_change_collection_enabled | boolean | no | When enabled, Datadog scans for all resource change data in your Google Cloud environment. |
  | is_security_command_center_enabled | boolean | no | When enabled, Datadog will attempt to collect Security Command Center Findings. |
  | metric_namespace_configs | array<object> | no | Configurations for GCP metric namespaces. |
  | monitored_resource_configs | array<object> | no | Configurations for GCP monitored resources. |
  | resource_collection_enabled | boolean | no | When enabled, Datadog scans for all resources in your GCP environment. |
  | id | string | no | Your service account's unique ID. |

- **Outputs**:

  | Name | Type | Description |
  |------|------|-------------|
  | data | object | Info on your service account. |

