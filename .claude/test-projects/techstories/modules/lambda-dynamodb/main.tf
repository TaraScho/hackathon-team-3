data "aws_region" "current" {}

# --- SQS ---

resource "aws_sqs_queue" "keyword_insights" {
  name = var.keyword_insights_queue_name

  tags = merge(var.common_tags, {
    service = "techstories-keyword-insights"
  })
}

resource "aws_sqs_queue_policy" "keyword_insights" {
  queue_url = aws_sqs_queue.keyword_insights.id

  policy = jsonencode({
    Version = "2012-10-17"
    Id      = "QueuePolicy"
    Statement = [{
      Sid       = "OnlyAllowEC2InstanceToSendMessages"
      Effect    = "Allow"
      Principal = { AWS = var.ec2_instance_role_arn }
      Action    = "sqs:SendMessage"
      Resource  = aws_sqs_queue.keyword_insights.arn
    }]
  })
}

# --- DynamoDB tables ---

resource "aws_dynamodb_table" "keyword_insights" {
  name         = "keyword-insights-tracker"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "keyword"

  attribute {
    name = "keyword"
    type = "S"
  }

  tags = merge(var.common_tags, {
    service = "techstories-keyword-insights"
  })
}

resource "aws_dynamodb_table" "referral_points" {
  name         = var.referral_points_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "email"

  attribute {
    name = "email"
    type = "S"
  }

  tags = merge(var.common_tags, {
    service = "techstories-referrals"
  })
}

resource "aws_dynamodb_table" "referral_submissions" {
  name         = var.referral_submission_table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "referrer_email"
  range_key    = "referee_email"

  attribute {
    name = "referrer_email"
    type = "S"
  }

  attribute {
    name = "referee_email"
    type = "S"
  }

  global_secondary_index {
    name            = "RefereeEmailIndex"
    hash_key        = "referee_email"
    projection_type = "ALL"
  }

  tags = merge(var.common_tags, {
    service = "techstories-referrals"
  })
}

# --- Lambda ---

data "archive_file" "keyword_insights" {
  type        = "zip"
  source_file = "${path.module}/src/keyword-insights-lambda.py"
  output_path = "${path.module}/src/keyword-insights-lambda.zip"
}

resource "aws_iam_role" "lambda" {
  name_prefix = "keyword-insights-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-keyword-insights"
  })
}

resource "aws_iam_role_policy" "lambda" {
  name = "allow-dynamodb-sqs-logs"
  role = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["dynamodb:UpdateItem"]
        Resource = aws_dynamodb_table.keyword_insights.arn
      },
      {
        Effect = "Allow"
        Action = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes",
        ]
        Resource = aws_sqs_queue.keyword_insights.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
        ]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["secretsmanager:GetSecretValue"]
        Resource = var.datadog_api_key_secret_arn
      },
    ]
  })
}

resource "aws_lambda_function" "keyword_insights" {
  function_name = "keyword-insights-processor"
  runtime       = "python3.12"
  handler       = "datadog_lambda.handler.handler"
  role          = aws_iam_role.lambda.arn
  timeout       = 60

  filename         = data.archive_file.keyword_insights.output_path
  source_code_hash = data.archive_file.keyword_insights.output_base64sha256

  layers = [
    "arn:aws:lambda:${data.aws_region.current.name}:464622532012:layer:Datadog-Python312:109",
    "arn:aws:lambda:${data.aws_region.current.name}:464622532012:layer:Datadog-Extension:78",
  ]

  environment {
    variables = {
      TABLE_NAME                                        = aws_dynamodb_table.keyword_insights.name
      DD_LAMBDA_HANDLER                                 = "keyword-insights-lambda.lambda_handler"
      DD_SITE                                           = "datadoghq.com"
      DD_ENV                                            = "monitoring-aws-lab"
      DD_SERVICE                                        = "techstories-keyword-insights"
      DD_VERSION                                        = "1.0.0"
      DD_TRACE_ENABLED                                  = "true"
      DD_SERVERLESS_LOGS_ENABLED                        = "true"
      DD_CAPTURE_LAMBDA_PAYLOAD                         = "true"
      DD_SERVERLESS_APPSEC_ENABLED                      = "true"
      DD_LOGS_INJECTION                                 = "true"
      DD_PROFILING_ENABLED                              = "true"
      DD_API_KEY_SECRET_ARN                             = var.datadog_api_key_secret_arn
      DD_DATA_STREAMS_ENABLED                           = "true"
      DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED = "true"
    }
  }

  tags = merge(var.common_tags, {
    service = "techstories-keyword-insights"
  })
}

resource "aws_lambda_event_source_mapping" "keyword_insights" {
  event_source_arn = aws_sqs_queue.keyword_insights.arn
  function_name    = aws_lambda_function.keyword_insights.arn
  batch_size       = 5
  enabled          = true
}
