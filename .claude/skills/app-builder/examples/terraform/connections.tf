#=============================================================================
# DATADOG ACTION CONNECTIONS
# Creates connections for workflow automation to interact with AWS services
#=============================================================================

# AWS EC2 Connection for Workflow Automation
# This connection allows workflows to manage EC2 instances and security groups
resource "datadog_action_connection" "aws_ec2_workflow" {
  count    = var.create_workflows ? 1 : 0
  name     = "workflow-ec2"

  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = "datadog-workflow-ec2" # This role was created in aws-infrastructure module
    }
  }
}

# AWS EC2 Connection for App Builder
# This connection allows App Builder apps to manage EC2 resources
resource "datadog_action_connection" "aws_ec2_appbuilder" {
  count    = var.create_workflows ? 1 : 0
  name     = "appbuilder-ec2"

  aws {
    assume_role {
      account_id = var.aws_account_id
      role       = "datadog-appbuilder-ec2" # This role was created in aws-infrastructure module
    }
  }
}

# Get the external IDs from the connections to update IAM trust policies
# Note: External IDs are only available after the connection resources are created
# During plan phase, these will be empty/unknown
locals {
  workflow_connection_external_id   = var.create_workflows && length(datadog_action_connection.aws_ec2_workflow) > 0 ? try(datadog_action_connection.aws_ec2_workflow[0].id, "") : ""
  appbuilder_connection_external_id = var.create_workflows && length(datadog_action_connection.aws_ec2_appbuilder) > 0 ? try(datadog_action_connection.aws_ec2_appbuilder[0].id, "") : ""
}
