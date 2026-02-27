data "aws_region" "current" {}

# --- CloudWatch log group ---

resource "aws_cloudwatch_log_group" "traffic_generator" {
  name = "/ecs/techstories-traffic-generator"

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}

# --- IAM: execution role ---

resource "aws_iam_role" "execution" {
  name_prefix = "techstories-trafgen-exec-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}

resource "aws_iam_role_policy_attachment" "execution" {
  role       = aws_iam_role.execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy" "execution_secrets" {
  name = "DatadogSecretsAccess"
  role = aws_iam_role.execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "secretsmanager:GetSecretValue"
      Resource = var.datadog_api_key_secret_arn
    }]
  })
}

# --- IAM: task role ---

resource "aws_iam_role" "task" {
  name_prefix = "techstories-trafgen-task-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}

# --- Security group (egress-only) ---

resource "aws_security_group" "traffic_generator" {
  name_prefix = "techstories-trafgen-"
  description = "Traffic generator - egress only"
  vpc_id      = var.vpc_id

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}

resource "aws_vpc_security_group_egress_rule" "traffic_generator_all" {
  security_group_id = aws_security_group.traffic_generator.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

# --- Task definition ---

resource "aws_ecs_task_definition" "traffic_generator" {
  family                   = "techstories-traffic-generator"
  cpu                      = "512"
  memory                   = "1024"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.execution.arn
  task_role_arn            = aws_iam_role.task.arn

  container_definitions = jsonencode([
    {
      name      = "traffic-generator"
      image     = "europe-west1-docker.pkg.dev/datadog-community/training-images-docker/techstories-aws-traffic-generator:1.0.0"
      essential = true
      environment = [
        { name = "TECHSTORIES_URL", value = var.techstories_url },
        { name = "PYTHONUNBUFFERED", value = "1" },
        { name = "DD_ENV", value = "monitoring-aws-lab" },
        { name = "DD_SERVICE", value = "techstories-traffic-generator" },
        { name = "DD_VERSION", value = "1.0.0" },
        { name = "DD_SITE", value = "datadoghq.com" },
        { name = "DD_TRACE_ENABLED", value = "true" },
        { name = "DD_LOGS_INJECTION", value = "true" },
        { name = "DD_PROFILING_ENABLED", value = "true" },
        { name = "DD_APPSEC_ENABLED", value = "true" },
        { name = "DD_DATA_STREAMS_ENABLED", value = "true" },
        { name = "DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED", value = "true" },
        { name = "DD_AGENT_HOST", value = "localhost" },
      ]
      secrets = [{ name = "DD_API_KEY", valueFrom = var.datadog_api_key_secret_arn }]
      dockerLabels = {
        "com.datadoghq.tags.env"     = "monitoring-aws-lab"
        "com.datadoghq.tags.service" = "techstories-traffic-generator"
        "com.datadoghq.tags.version" = "1.0.0"
      }
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.traffic_generator.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "traffic-generator"
        }
      }
    },
    {
      name      = "datadog-agent"
      image     = "public.ecr.aws/datadog/agent:latest"
      essential = true
      portMappings = [
        { containerPort = 8126, hostPort = 8126, protocol = "tcp" },
        { containerPort = 8125, hostPort = 8125, protocol = "udp" },
      ]
      secrets = [{ name = "DD_API_KEY", valueFrom = var.datadog_api_key_secret_arn }]
      environment = [
        { name = "DD_SITE", value = "datadoghq.com" },
        { name = "DD_ENV", value = "monitoring-aws-lab" },
        { name = "DD_APM_ENABLED", value = "true" },
        { name = "DD_LOGS_ENABLED", value = "true" },
        { name = "DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL", value = "true" },
        { name = "DD_PROCESS_AGENT_ENABLED", value = "true" },
        { name = "DD_DOGSTATSD_NON_LOCAL_TRAFFIC", value = "true" },
        { name = "DD_APM_NON_LOCAL_TRAFFIC", value = "true" },
        { name = "ECS_FARGATE", value = "true" },
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.traffic_generator.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "datadog-agent"
        }
      }
    },
  ])

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}

# --- ECS service ---

resource "aws_ecs_service" "traffic_generator" {
  name            = "techstories-traffic-generator"
  cluster         = var.ecs_cluster_id
  task_definition = aws_ecs_task_definition.traffic_generator.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    assign_public_ip = false
    security_groups  = [aws_security_group.traffic_generator.id]
    subnets          = [var.private_subnet_1_id, var.private_subnet_2_id]
  }

  tags = merge(var.common_tags, {
    service = "techstories-traffic-generator"
  })
}
