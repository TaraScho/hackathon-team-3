variable "vpc_id" {
  description = "VPC ID for Lambda security group"
  type        = string
}

variable "private_subnet_1_id" {
  description = "First private subnet ID for Lambda functions"
  type        = string
}

variable "private_subnet_2_id" {
  description = "Second private subnet ID for Lambda functions"
  type        = string
}

variable "datadog_api_key_secret_arn" {
  description = "ARN of the Secrets Manager secret containing the Datadog API key"
  type        = string
}

variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default     = {}
}
