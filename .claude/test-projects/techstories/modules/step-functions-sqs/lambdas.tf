# -----------------------------------------------------------------------------
# Shared Lambda IAM Role
# -----------------------------------------------------------------------------

resource "aws_iam_role" "lambda" {
  name_prefix = "parrot-translation-lambda-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_iam_role_policy" "lambda" {
  name_prefix = "parrot-translation-lambda-"
  role        = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
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
        Action   = "secretsmanager:GetSecretValue"
        Resource = var.datadog_api_key_secret_arn
      },
      {
        Effect = "Allow"
        Action = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes",
        ]
        Resource = aws_sqs_queue.translation_delivery.arn
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_vpc" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

# -----------------------------------------------------------------------------
# Lambda Security Group
# -----------------------------------------------------------------------------

resource "aws_security_group" "lambda" {
  name_prefix = "parrot-translation-lambda-"
  description = "Security group for Parrot Translation Lambda functions"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

# -----------------------------------------------------------------------------
# Datadog Lambda Layers
# -----------------------------------------------------------------------------

locals {
  dd_python_layer    = "arn:aws:lambda:${data.aws_region.current.name}:464622532012:layer:Datadog-Python312:109"
  dd_extension_layer = "arn:aws:lambda:${data.aws_region.current.name}:464622532012:layer:Datadog-Extension:78"
  dd_layers          = [local.dd_python_layer, local.dd_extension_layer]

  dd_common_env = {
    DD_SITE                        = "datadoghq.com"
    DD_ENV                         = "monitoring-aws-lab"
    DD_SERVICE                     = "techstories-parrot-translator"
    DD_VERSION                     = "1.0.0"
    DD_TRACE_ENABLED               = "true"
    DD_SERVERLESS_LOGS_ENABLED     = "true"
    DD_CAPTURE_LAMBDA_PAYLOAD      = "true"
    DD_SERVERLESS_APPSEC_ENABLED   = "true"
    DD_LOGS_INJECTION              = "true"
    DD_PROFILING_ENABLED           = "true"
    DD_API_KEY_SECRET_ARN          = var.datadog_api_key_secret_arn
  }
}

# -----------------------------------------------------------------------------
# Archive files for Lambda source code
# -----------------------------------------------------------------------------

data "archive_file" "validate_request" {
  type        = "zip"
  source_file = "${path.module}/src/validate_request.py"
  output_path = "${path.module}/src/validate_request.zip"
}

data "archive_file" "perform_translation" {
  type        = "zip"
  source_file = "${path.module}/src/perform_translation.py"
  output_path = "${path.module}/src/perform_translation.zip"
}

data "archive_file" "archive_result" {
  type        = "zip"
  source_file = "${path.module}/src/archive_result.py"
  output_path = "${path.module}/src/archive_result.zip"
}

data "archive_file" "mark_complete" {
  type        = "zip"
  source_file = "${path.module}/src/mark_complete.py"
  output_path = "${path.module}/src/mark_complete.zip"
}

data "archive_file" "webhook_delivery" {
  type        = "zip"
  source_file = "${path.module}/src/webhook_delivery.py"
  output_path = "${path.module}/src/webhook_delivery.zip"
}

# -----------------------------------------------------------------------------
# Lambda Functions — Step Functions tasks
# -----------------------------------------------------------------------------

resource "aws_lambda_function" "validate_request" {
  function_name    = "parrot-validate-request"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.validate_request.output_path
  source_code_hash = data.archive_file.validate_request.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER = "validate_request.lambda_handler"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_lambda_function" "perform_translation" {
  function_name    = "parrot-perform-translation"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.perform_translation.output_path
  source_code_hash = data.archive_file.perform_translation.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER = "perform_translation.lambda_handler"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_lambda_function" "archive_result" {
  function_name    = "parrot-archive-result"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.archive_result.output_path
  source_code_hash = data.archive_file.archive_result.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER = "archive_result.lambda_handler"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_lambda_function" "mark_complete" {
  function_name    = "parrot-mark-complete"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.mark_complete.output_path
  source_code_hash = data.archive_file.mark_complete.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER = "mark_complete.lambda_handler"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

# -----------------------------------------------------------------------------
# Lambda Function — SQS consumer with Data Streams Monitoring
# -----------------------------------------------------------------------------

resource "aws_lambda_function" "webhook_delivery" {
  function_name    = "parrot-webhook-delivery"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.webhook_delivery.output_path
  source_code_hash = data.archive_file.webhook_delivery.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER                              = "webhook_delivery.lambda_handler"
      DD_DATA_STREAMS_ENABLED                        = "true"
      DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED = "true"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_lambda_event_source_mapping" "webhook_delivery" {
  event_source_arn = aws_sqs_queue.translation_delivery.arn
  function_name    = aws_lambda_function.webhook_delivery.arn
  batch_size       = 10
}
