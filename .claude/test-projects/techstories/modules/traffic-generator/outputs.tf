output "security_group_id" {
  description = "Security group ID for the traffic generator"
  value       = aws_security_group.traffic_generator.id
}

output "service_name" {
  description = "Name of the traffic generator ECS service"
  value       = aws_ecs_service.traffic_generator.name
}

output "task_definition_arn" {
  description = "ARN of the traffic generator task definition"
  value       = aws_ecs_task_definition.traffic_generator.arn
}
