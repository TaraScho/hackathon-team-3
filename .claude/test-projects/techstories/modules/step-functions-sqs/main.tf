data "aws_region" "current" {}

# -----------------------------------------------------------------------------
# CloudWatch Log Group for Step Functions
# -----------------------------------------------------------------------------

resource "aws_cloudwatch_log_group" "state_machine" {
  name              = "/aws/states/parrot-translation-workflow"
  retention_in_days = 7

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

# -----------------------------------------------------------------------------
# SQS Queues
# -----------------------------------------------------------------------------

resource "aws_sqs_queue" "translation_delivery_dlq" {
  name                      = "translation-delivery-dlq"
  message_retention_seconds = 1209600 # 14 days

  tags = merge(var.common_tags, {
    service = "techstories-translation-delivery"
  })
}

resource "aws_sqs_queue" "translation_delivery" {
  name                       = "translation-delivery-queue"
  visibility_timeout_seconds = 60

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.translation_delivery_dlq.arn
    maxReceiveCount     = 3
  })

  tags = merge(var.common_tags, {
    service = "techstories-translation-delivery"
  })
}

# -----------------------------------------------------------------------------
# Step Functions IAM Role
# -----------------------------------------------------------------------------

resource "aws_iam_role" "state_machine" {
  name_prefix = "parrot-translation-sfn-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "states.amazonaws.com"
      }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_iam_role_policy" "state_machine" {
  name_prefix = "parrot-translation-sfn-"
  role        = aws_iam_role.state_machine.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "lambda:InvokeFunction"
        Resource = [
          aws_lambda_function.validate_request.arn,
          aws_lambda_function.perform_translation.arn,
          aws_lambda_function.archive_result.arn,
          aws_lambda_function.mark_complete.arn,
        ]
      },
      {
        Effect   = "Allow"
        Action   = "sqs:SendMessage"
        Resource = aws_sqs_queue.translation_delivery.arn
      },
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogDelivery",
          "logs:GetLogDelivery",
          "logs:UpdateLogDelivery",
          "logs:DeleteLogDelivery",
          "logs:ListLogDeliveries",
          "logs:PutResourcePolicy",
          "logs:DescribeResourcePolicies",
          "logs:DescribeLogGroups",
        ]
        Resource = "*"
      },
    ]
  })
}

# -----------------------------------------------------------------------------
# Step Functions State Machine
# -----------------------------------------------------------------------------

resource "aws_sfn_state_machine" "parrot_translation" {
  name     = "ParrotTranslationWorkflow"
  role_arn = aws_iam_role.state_machine.arn

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.state_machine.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }

  definition = jsonencode({
    Comment = "Parrot Translation Workflow — validates, translates, queues delivery, archives, and completes."
    StartAt = "ValidateRequest"
    States = {
      ValidateRequest = {
        Type     = "Task"
        Resource = aws_lambda_function.validate_request.arn
        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 2
          MaxAttempts     = 2
          BackoffRate     = 1.5
        }]
        Next = "PerformTranslation"
        Catch = [{
          ErrorEquals = ["ValidationError"]
          Next        = "ValidationFailed"
        }]
      }

      PerformTranslation = {
        Type     = "Task"
        Resource = aws_lambda_function.perform_translation.arn
        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 2
          MaxAttempts     = 2
          BackoffRate     = 1.5
        }]
        Next = "SendToQueue"
      }

      SendToQueue = {
        Type     = "Task"
        Resource = "arn:aws:states:::sqs:sendMessage"
        Parameters = {
          QueueUrl    = aws_sqs_queue.translation_delivery.url
          "MessageBody.$" = "$.translatedText"
        }
        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 2
          MaxAttempts     = 2
          BackoffRate     = 1.5
        }]
        ResultPath = "$.sqsResult"
        Next       = "ArchiveResult"
      }

      ArchiveResult = {
        Type     = "Task"
        Resource = aws_lambda_function.archive_result.arn
        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 2
          MaxAttempts     = 2
          BackoffRate     = 1.5
        }]
        Catch = [{
          ErrorEquals = ["States.ALL"]
          ResultPath  = "$.archiveError"
          Next        = "MarkComplete"
        }]
        Next = "MarkComplete"
      }

      MarkComplete = {
        Type     = "Task"
        Resource = aws_lambda_function.mark_complete.arn
        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 2
          MaxAttempts     = 2
          BackoffRate     = 1.5
        }]
        End = true
      }

      ValidationFailed = {
        Type  = "Fail"
        Error = "ValidationError"
        Cause = "Request failed validation checks"
      }
    }
  })

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}
