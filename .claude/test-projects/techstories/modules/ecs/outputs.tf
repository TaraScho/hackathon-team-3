output "fargate_security_group_id" {
  description = "Security group ID for the Fargate services"
  value       = aws_security_group.fargate.id
}

output "cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.main.name
}

output "cluster_id" {
  description = "ID of the ECS cluster"
  value       = aws_ecs_cluster.main.id
}
