variable "keyword_insights_queue_name" {
  description = "Name of the SQS queue for keyword insights"
  type        = string
  default     = "keyword-insights-queue"
}

variable "referral_points_table_name" {
  description = "DynamoDB table name for referral user points"
  type        = string
  default     = "techstories-referral-users"
}

variable "referral_submission_table_name" {
  description = "DynamoDB table name for referral submissions"
  type        = string
  default     = "techstories-referral-records"
}

variable "ec2_instance_role_arn" {
  description = "IAM role ARN for the EC2 instance that sends SQS messages"
  type        = string
}

variable "datadog_api_key_secret_arn" {
  description = "ARN of the Datadog API key secret in Secrets Manager"
  type        = string
}

variable "common_tags" {
  description = "Common tags applied to all resources"
  type        = map(string)
  default     = {}
}
