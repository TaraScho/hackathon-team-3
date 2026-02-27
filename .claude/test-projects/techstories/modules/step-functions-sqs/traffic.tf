# -----------------------------------------------------------------------------
# Traffic Starter Lambda
# -----------------------------------------------------------------------------

data "archive_file" "traffic_starter" {
  type        = "zip"
  source_file = "${path.module}/src/traffic_starter.py"
  output_path = "${path.module}/src/traffic_starter.zip"
}

resource "aws_lambda_function" "traffic_starter" {
  function_name    = "parrot-traffic-starter"
  role             = aws_iam_role.lambda.arn
  handler          = "datadog_lambda.handler.handler"
  runtime          = "python3.12"
  timeout          = 60
  filename         = data.archive_file.traffic_starter.output_path
  source_code_hash = data.archive_file.traffic_starter.output_base64sha256
  layers           = local.dd_layers

  vpc_config {
    subnet_ids         = [var.private_subnet_1_id, var.private_subnet_2_id]
    security_group_ids = [aws_security_group.lambda.id]
  }

  environment {
    variables = merge(local.dd_common_env, {
      DD_LAMBDA_HANDLER  = "traffic_starter.lambda_handler"
      STATE_MACHINE_ARN  = aws_sfn_state_machine.parrot_translation.arn
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

# -----------------------------------------------------------------------------
# IAM — allow traffic-starter to start Step Functions executions
# -----------------------------------------------------------------------------

resource "aws_iam_role_policy" "traffic_starter_sfn" {
  name_prefix = "parrot-traffic-sfn-"
  role        = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "states:StartExecution"
      Resource = aws_sfn_state_machine.parrot_translation.arn
    }]
  })
}

# -----------------------------------------------------------------------------
# EventBridge Rule — triggers every 2 minutes
# -----------------------------------------------------------------------------

resource "aws_cloudwatch_event_rule" "traffic_starter" {
  name                = "parrot-translation-traffic"
  description         = "Triggers parrot translation workflow every 2 minutes"
  schedule_expression = "rate(2 minutes)"

  tags = merge(var.common_tags, {
    service = "techstories-parrot-translator"
  })
}

resource "aws_cloudwatch_event_target" "traffic_starter" {
  rule = aws_cloudwatch_event_rule.traffic_starter.name
  arn  = aws_lambda_function.traffic_starter.arn
}

resource "aws_lambda_permission" "traffic_starter_eventbridge" {
  statement_id  = "AllowEventBridgeInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.traffic_starter.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.traffic_starter.arn
}
