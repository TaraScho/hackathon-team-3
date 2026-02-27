terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = {
      Project = "tf-simple"
    }
  }
}

variable "region" {
  default = "us-east-1"
}

data "aws_caller_identity" "current" {}

# --- Lambda Function (minimal, no-op) ---
resource "aws_iam_role" "lambda_role" {
  name = "tf-simple-lambda-role"

  tags = {
    Team    = "compute"
    Service = "order-processor"
  }

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_lambda_function" "test" {
  function_name = "tf-simple-test-fn"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.12"
  handler       = "index.handler"
  filename      = "${path.module}/lambda.zip"

  environment {
    variables = {
      ENV = "test"
    }
  }

  tags = {
    Team    = "compute"
    Service = "order-processor"
  }
}

# --- Step Functions State Machine ---
resource "aws_iam_role" "sfn_role" {
  name = "tf-simple-sfn-role"

  tags = {
    Team    = "data-engineering"
    Service = "pipeline-orchestrator"
  }

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "states.amazonaws.com" }
    }]
  })
}

resource "aws_sfn_state_machine" "test" {
  name     = "tf-simple-test-sfn"
  role_arn = aws_iam_role.sfn_role.arn

  definition = jsonencode({
    StartAt = "Pass"
    States = {
      Pass = {
        Type = "Pass"
        End  = true
      }
    }
  })

  tags = {
    Team    = "data-engineering"
    Service = "pipeline-orchestrator"
  }
}

# --- EventBridge Rule ---
resource "aws_cloudwatch_event_rule" "test" {
  name                = "tf-simple-test-rule"
  schedule_expression = "rate(1 day)"
  state               = "DISABLED"

  tags = {
    Team    = "platform-engineering"
    Service = "scheduler"
  }
}

# --- Secrets Manager Secret ---
resource "aws_secretsmanager_secret" "test" {
  name                    = "tf-simple/test-secret"
  recovery_window_in_days = 0

  tags = {
    Team    = "security"
    Service = "secrets-manager"
  }
}

# --- Kinesis Stream ---
resource "aws_kinesis_stream" "test" {
  name        = "tf-simple-test-stream"
  shard_count = 1

  tags = {
    Team    = "data-engineering"
    Service = "event-ingestion"
  }
}

output "lambda_arn" {
  value = aws_lambda_function.test.arn
}

output "state_machine_arn" {
  value = aws_sfn_state_machine.test.arn
}

output "event_rule_arn" {
  value = aws_cloudwatch_event_rule.test.arn
}

output "secret_arn" {
  value = aws_secretsmanager_secret.test.arn
}

output "stream_arn" {
  value = aws_kinesis_stream.test.arn
}
