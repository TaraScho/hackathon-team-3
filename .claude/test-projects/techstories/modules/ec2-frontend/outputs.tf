output "techstories_url" {
  description = "URL of the TechStories application"
  value       = "http://${aws_lb.frontend.dns_name}"
}

output "ec2_role_arn" {
  description = "ARN of the EC2 instance role"
  value       = aws_iam_role.ec2.arn
}

output "ec2_security_group_id" {
  description = "Security group ID for the web server"
  value       = aws_security_group.ec2.id
}

output "alb_security_group_id" {
  description = "Security group ID for the ALB"
  value       = aws_security_group.alb.id
}
