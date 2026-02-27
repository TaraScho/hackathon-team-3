output "keyword_insights_queue_arn" {
  description = "ARN of the Keyword Insights SQS Queue"
  value       = aws_sqs_queue.keyword_insights.arn
}

output "keyword_insights_queue_url" {
  description = "URL of the Keyword Insights SQS Queue"
  value       = aws_sqs_queue.keyword_insights.url
}
