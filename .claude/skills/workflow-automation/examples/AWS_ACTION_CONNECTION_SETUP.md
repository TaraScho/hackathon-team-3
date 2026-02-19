# AWS Action Connection Setup for Datadog Workflow Automation

This document describes the implementation of Datadog AWS action connection setup for the Stickerlandia quest, enabling Datadog workflows to perform automated actions in AWS.

## Overview

The implementation creates an AWS IAM role that Datadog workflow automation can assume, sets up an action connection in Datadog, and configures the necessary trust policies with external IDs for secure cross-account access.

## Components

### 1. Standalone Script: `setup_aws_action_connection.py`

**Purpose**: Local testing and manual setup of the AWS action connection.

**Location**: `walkup-quest-2026/setup_aws_action_connection.py`

**Usage**:
```bash
# Set environment variables
export DD_API_KEY="your-api-key"
export DD_APP_KEY="your-app-key"  # Must have actions API access enabled
export AWS_PROFILE="gameday"

# Run the script
python walkup-quest-2026/setup_aws_action_connection.py
```

**Prerequisites**:
- `DD_APP_KEY` must have actions API access enabled (workflow automation scopes)

**What it does**:
1. Creates an AWS action connection in Datadog (named "DatadogWorkflowAutomationConnection")
2. Retrieves the external ID from Datadog
3. Updates the IAM role trust policy to allow Datadog's AWS account (464622532012) to assume the role

### 2. CloudFormation Resources

**Location**: `walkup-quest-2026/team_enable_cfn.yaml`

#### DatadogActionRole

IAM role that Datadog workflows can assume to perform actions in AWS.

**Permissions**:
- `IAMFullAccess` managed policy - Full IAM access (users, roles, policies, permissions)
- `AmazonEventBridgeFullAccess` managed policy - Full EventBridge access (rules, event buses, schedules)

**Trust Policy**:
- Initial placeholder external ID: `placeholder-will-be-updated`
- Updated by the ConfigureDatadog Lambda with the real external ID from Datadog
- Principal: `arn:aws:iam::464622532012:root` (Datadog's AWS account)

#### ConfigureDatadogLambdaRole (Updated)

Added IAM permissions for the Lambda to update the DatadogActionRole trust policy:
- `iam:UpdateAssumeRolePolicy`
- `iam:GetRole`
- `sts:GetCallerIdentity`

#### ConfigureDatadog Custom Resource (Updated)

Now receives the `DatadogActionRoleArn` as a property and triggers AWS action connection setup during stack creation/update.

### 3. Integration in `configure_datadog.py`

**Location**: `walkup-quest-2026/team_lambda_source/configure_datadog.py`

**New Functions**:
- `create_aws_action_connection()` - Creates AWS action connection in Datadog using DD_APP_KEY
- `update_role_trust_policy()` - Updates IAM role trust policy with external ID
- `setup_aws_action_connection()` - Orchestrates the complete workflow

**Integration Point**: Called from `configure_stickerlandia()` if `role_arn` is provided.

**Local Testing**:
```bash
source .env
python walkup-quest-2026/team_lambda_source/configure_datadog.py
```

The script automatically looks for the `DatadogActionRole` and sets up the connection if found.

## Workflow

### CloudFormation Deployment

```
1. CloudFormation creates DatadogActionRole
   └─ Initial trust policy with placeholder external ID

2. CloudFormation invokes ConfigureDatadog Lambda
   └─ Lambda receives DatadogActionRoleArn

3. Lambda executes setup_aws_action_connection()
   ├─ Creates AWS action connection in Datadog (using DD_APP_KEY)
   │  └─ Datadog generates external ID
   ├─ Retrieves external ID from Datadog
   └─ Updates DatadogActionRole trust policy
      └─ Principal: arn:aws:iam::464622532012:root
      └─ Condition: sts:ExternalId = <external-id-from-datadog>

4. Datadog workflows can now assume DatadogActionRole
```

### Local Testing Workflow

```
1. Ensure DatadogActionRole exists in AWS
   └─ Deploy CloudFormation stack OR create role manually

2. Ensure DD_APP_KEY has actions API access enabled

3. Run standalone script
   └─ python walkup-quest-2026/setup_aws_action_connection.py

4. Script orchestrates the 2-step workflow:
   ├─ Create AWS action connection (using existing DD_APP_KEY)
   └─ Update role trust policy
```

## Architecture Pattern

This implementation follows the pattern from `gameday-reinvent-2025`, specifically:
- `central_lambda_source/datadog_helpers/setup_action_connection.py`
- `central_lambda_source/datadog_helpers/datadog_helpers.py`

Key differences:
- Uses `urllib3` instead of `requests` (for Lambda compatibility)
- Integrated into existing `configure_datadog.py` Lambda
- Role name: `DatadogActionRole` (same as reinvent-2025)
- Connection name: `DatadogWorkflowAutomationConnection` (more descriptive)
- Uses existing DD_APP_KEY instead of creating a new application key

## Security

- **External ID**: Prevents confused deputy attacks by requiring Datadog to provide a unique external ID
- **Scoped Permissions**: Role has IAM and EventBridge full access only (not broad PowerUserAccess)
- **Trust Policy**: Only Datadog's AWS account (464622532012) can assume the role
- **Condition**: Role assumption requires the correct external ID from Datadog

## Testing

### Validate CloudFormation
```bash
aws cloudformation validate-template \
  --template-body file://walkup-quest-2026/team_enable_cfn.yaml \
  --profile gameday --region us-east-1
```

### Test Standalone Script
```bash
source .env
python walkup-quest-2026/setup_aws_action_connection.py
```

### Test configure_datadog.py Locally
```bash
source .env
python walkup-quest-2026/team_lambda_source/configure_datadog.py
```

### Verify Role Trust Policy
```bash
aws iam get-role --role-name DatadogActionRole --profile gameday
```

Look for:
- Principal: `arn:aws:iam::464622532012:root`
- Condition with `sts:ExternalId`

### Verify Datadog Connection
1. Log in to Datadog
2. Navigate to: **Workflow Automation** → **Connections**
3. Look for: `DatadogWorkflowAutomationConnection`
4. Verify: Status should be "Connected" or "Ready"

## Deployment

### Initial Deployment
```bash
# 1. Validate template
aws cloudformation validate-template \
  --template-body file://walkup-quest-2026/team_enable_cfn.yaml

# 2. Deploy via QDK pipeline
cd walkup-quest-2026
./deploy.sh

# 3. Monitor stack
aws cloudformation describe-stacks \
  --stack-name gdQuests-2ae222a2-a6dc-4fc0-a797-3f4a7bbd1d63-TeamEnable \
  --profile gameday --region us-east-1
```

### Verify ConfigureDatadog Lambda Logs
```bash
aws logs tail /aws/lambda/stickerlandia-configure-datadog \
  --follow --profile gameday --region us-east-1
```

Look for:
```
--- Setting up AWS Action Connection ---
Step 1: Creating AWS action connection...
✓ Created action connection: DatadogWorkflowAutomationConnection (ID: ..., External ID: ...)
Step 2: Updating IAM role trust policy...
✓ Updated trust policy for role: DatadogActionRole with external ID: ...
✓ AWS action connection setup completed successfully
```

## Troubleshooting

### Error: "Failed to create action connection: 403 Forbidden"
- **Cause**: DD_APP_KEY lacks actions API access (workflow automation scopes)
- **Fix**: Ensure the application key has actions API access enabled in Datadog (Organization Settings → Application Keys → Enable actions API access)

### Error: "Failed to get AWS account ID"
- **Cause**: Missing AWS credentials or STS permissions
- **Fix**: Check `AWS_PROFILE` / credentials, ensure role has `sts:GetCallerIdentity`

### Error: "Connection already exists but could not retrieve external_id"
- **Cause**: Connection exists but external ID retrieval failed
- **Fix**: Manually retrieve external ID from Datadog UI or delete the connection and re-run

### Error: "Error updating role trust policy"
- **Cause**: Lambda lacks `iam:UpdateAssumeRolePolicy` permission
- **Fix**: Ensure ConfigureDatadogLambdaRole has the IAMRoleTrustPolicyUpdate policy

## References

- **Datadog Workflow Automation**: https://docs.datadoghq.com/service_management/workflows/
- **AWS Action Connections**: https://docs.datadoghq.com/service_management/workflows/connections/
- **Datadog AWS Account ID**: 464622532012
- **Source Pattern**: `gameday-reinvent-2025/central_lambda_source/datadog_helpers/setup_action_connection.py`
