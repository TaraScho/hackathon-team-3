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

variable "db_name" {
  description = "Name of the database"
  type        = string
  default     = "TechStoriesDB"
}

variable "common_tags" {
  description = "Common tags applied to all resources"
  type        = map(string)
  default     = {}
}
