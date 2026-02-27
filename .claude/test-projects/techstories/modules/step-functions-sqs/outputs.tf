output "state_machine_arn" {
  description = "ARN of the Parrot Translation Workflow state machine"
  value       = aws_sfn_state_machine.parrot_translation.arn
}

output "delivery_queue_url" {
  description = "URL of the translation delivery SQS queue"
  value       = aws_sqs_queue.translation_delivery.url
}

output "delivery_queue_arn" {
  description = "ARN of the translation delivery SQS queue"
  value       = aws_sqs_queue.translation_delivery.arn
}

output "dlq_url" {
  description = "URL of the translation delivery dead letter queue"
  value       = aws_sqs_queue.translation_delivery_dlq.url
}
