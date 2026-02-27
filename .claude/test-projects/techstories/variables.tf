variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "datadog_api_key" {
  description = "Datadog API key for EC2 user data .env"
  type        = string
  sensitive   = true
}

variable "datadog_app_key" {
  description = "Datadog APP key for EC2 user data .env"
  type        = string
  sensitive   = true
}

variable "datadog_api_key_secret_arn" {
  description = "Existing Secrets Manager ARN for Datadog API key (used by Lambda)"
  type        = string
}

variable "assets_bucket_name" {
  description = "S3 bucket name for CloudFormation/deployment assets"
  type        = string
}

variable "db_name" {
  description = "Name of the Postgres database"
  type        = string
  default     = "TechStoriesDB"
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

variable "keyword_insights_queue_name" {
  description = "Name of the SQS queue for keyword insights"
  type        = string
  default     = "keyword-insights-queue"
}
