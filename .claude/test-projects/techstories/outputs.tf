output "techstories_url" {
  description = "URL of the TechStories application"
  value       = module.ec2_frontend.techstories_url
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.vpc_id
}

output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = module.ecs.cluster_name
}

output "db_endpoint" {
  description = "Postgres database endpoint"
  value       = module.rds.db_endpoint
}

output "keyword_insights_queue_url" {
  description = "URL of the keyword insights SQS queue"
  value       = module.lambda_dynamodb.keyword_insights_queue_url
}

output "state_machine_arn" {
  description = "ARN of the Parrot Translation Workflow state machine"
  value       = module.step_functions_sqs.state_machine_arn
}

output "translation_delivery_queue_url" {
  description = "URL of the translation delivery SQS queue"
  value       = module.step_functions_sqs.delivery_queue_url
}
