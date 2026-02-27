output "db_endpoint" {
  description = "Hostname for PostgreSQL DB instance"
  value       = aws_db_instance.main.address
}

output "db_security_group_id" {
  description = "Security group ID for the Postgres DB"
  value       = aws_security_group.db.id
}

output "db_master_secret_arn" {
  description = "ARN of the Secrets Manager secret for the Postgres master user"
  value       = aws_secretsmanager_secret.db_master.arn
}
