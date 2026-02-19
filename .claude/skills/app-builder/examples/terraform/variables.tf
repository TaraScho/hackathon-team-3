# Variables for Datadog Workflows Module

variable "aws_account_id" {
  description = "AWS account ID for IAM role ARNs"
  type        = string
}

variable "aws_region" {
  description = "AWS region for workflow actions"
  type        = string
  default     = "us-east-1"
}

variable "workflow_iam_role_arn" {
  description = "IAM role ARN for workflow EC2 actions"
  type        = string
}

variable "appbuilder_iam_role_arn" {
  description = "IAM role ARN for App Builder EC2 actions"
  type        = string
}

variable "datadog_api_key" {
  description = "Datadog API key"
  type        = string
  sensitive   = true
  default     = ""
}

variable "create_workflows" {
  description = "Whether to create workflows and connections"
  type        = bool
  default     = false
}

variable "datadog_app_key" {
  description = "Datadog application key"
  type        = string
  sensitive   = true
  default     = ""
}

variable "aws_profile" {
  description = "AWS profile to use for IAM operations"
  type        = string
  default     = "lab-aws-account-admin"
}

variable "ec2_scorecard_rule_id" {
  description = "ID of the EC2 scorecard rule for workflow to update"
  type        = string
  default     = ""
}
