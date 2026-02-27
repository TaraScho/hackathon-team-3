variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "private_subnet_1_id" {
  description = "ID of private subnet 1"
  type        = string
}

variable "private_subnet_2_id" {
  description = "ID of private subnet 2"
  type        = string
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

variable "datadog_api_key_secret_arn" {
  description = "ARN of the Datadog API key secret in Secrets Manager"
  type        = string
}

variable "common_tags" {
  description = "Common tags applied to all resources"
  type        = map(string)
  default     = {}
}
