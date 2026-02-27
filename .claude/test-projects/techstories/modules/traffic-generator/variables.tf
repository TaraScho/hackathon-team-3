variable "vpc_id" {
  type = string
}

variable "private_subnet_1_id" {
  type = string
}

variable "private_subnet_2_id" {
  type = string
}

variable "ecs_cluster_id" {
  type = string
}

variable "techstories_url" {
  type = string
}

variable "datadog_api_key_secret_arn" {
  description = "ARN of the Datadog API key secret in Secrets Manager"
  type        = string
}

variable "common_tags" {
  type    = map(string)
  default = {}
}
