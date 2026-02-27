variable "vpc_id" {
  description = "ID of the VPC"
  type        = string
}

variable "public_subnet_1_id" {
  description = "ID of public subnet 1"
  type        = string
}

variable "public_subnet_2_id" {
  description = "ID of public subnet 2"
  type        = string
}

variable "db_security_group_id" {
  description = "Security group ID for the database"
  type        = string
}

variable "db_endpoint" {
  description = "Endpoint of the database"
  type        = string
}

variable "db_port" {
  description = "Port for the database"
  type        = number
  default     = 5432
}

variable "db_secret_arn" {
  description = "ARN of the database secret in Secrets Manager"
  type        = string
}

variable "fargate_security_group_id" {
  description = "Security group ID for the Fargate services"
  type        = string
}

variable "datadog_api_key" {
  description = "Datadog API key"
  type        = string
  sensitive   = true
}

variable "datadog_app_key" {
  description = "Datadog APP key"
  type        = string
  sensitive   = true
}

variable "assets_bucket_name" {
  description = "S3 bucket name for assets"
  type        = string
}

variable "keyword_insights_queue_name" {
  description = "Name of the SQS queue for keyword insights"
  type        = string
  default     = "keyword-insights-queue"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.small"
}

variable "common_tags" {
  description = "Common tags applied to all resources"
  type        = map(string)
  default     = {}
}
