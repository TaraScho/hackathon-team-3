data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

# --- Shared resources ---

resource "aws_security_group" "fargate" {
  name_prefix = "techstories-fargate-"
  description = "Allow web server access to the quotes API"
  vpc_id      = var.vpc_id

  tags = merge(var.common_tags, {
    service = "ecs-shared-services"
  })
}

resource "aws_vpc_security_group_egress_rule" "fargate_all" {
  security_group_id = aws_security_group.fargate.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_ecs_cluster" "main" {
  name = "TechStoriesCluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  tags = merge(var.common_tags, {})
}

resource "aws_service_discovery_private_dns_namespace" "main" {
  name        = "techstories.local"
  vpc         = var.vpc_id
  description = "Service discovery for TechStories services"

  tags = merge(var.common_tags, {
    service = "ecs-shared-services"
  })
}

# --- IAM: shared execution role ---

resource "aws_iam_role" "fargate_execution" {
  name_prefix = "techstories-ecs-exec-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "ecs-shared-services"
  })
}

resource "aws_iam_role_policy_attachment" "fargate_execution" {
  role       = aws_iam_role.fargate_execution.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy" "fargate_execution_dynamo" {
  name = "ReferralsServiceDynamoPolicy"
  role = aws_iam_role.fargate_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:Scan",
        "dynamodb:UpdateItem",
      ]
      Resource = [
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_points_table_name}",
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_submission_table_name}",
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_submission_table_name}/index/RefereeEmailIndex",
      ]
    }]
  })
}

resource "aws_iam_role_policy" "fargate_execution_secrets" {
  name = "DatadogSecretsAccess"
  role = aws_iam_role.fargate_execution.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "secretsmanager:GetSecretValue"
      Resource = var.datadog_api_key_secret_arn
    }]
  })
}

# --- Quotes API ---

resource "aws_iam_role" "quotes_api_task" {
  name_prefix = "techstories-quotes-task-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-quotes-api"
  })
}

resource "aws_iam_role_policy_attachment" "quotes_api_task" {
  role       = aws_iam_role.quotes_api_task.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_cloudwatch_log_group" "quotes_api" {
  name = "/ecs/techstories-quotes-api"

  tags = merge(var.common_tags, {
    service = "techstories-quotes-api"
  })
}

resource "aws_ecs_task_definition" "quotes_api" {
  family                   = "techstories-quotes-api"
  cpu                      = "1024"
  memory                   = "2048"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.fargate_execution.arn
  task_role_arn            = aws_iam_role.quotes_api_task.arn

  container_definitions = jsonencode([
    {
      name         = "quotes-api"
      image        = "europe-west1-docker.pkg.dev/datadog-community/training-images-docker/aws-techstories-quotes-api:1.0.0"
      essential    = true
      portMappings = [{ containerPort = 3001 }]
      command      = ["npm", "run", "start"]
      environment = [
        { name = "PORT", value = "3001" },
        { name = "DD_ENV", value = "monitoring-aws-lab" },
        { name = "DD_SERVICE", value = "techstories-quotes-api" },
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
        "com.datadoghq.tags.service" = "techstories-quotes-api"
        "com.datadoghq.tags.version" = "1.0.0"
      }
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.quotes_api.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "quotes-api"
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
          "awslogs-group"         = aws_cloudwatch_log_group.quotes_api.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "datadog-agent"
        }
      }
    },
  ])

  tags = merge(var.common_tags, {
    service = "techstories-quotes-api"
  })
}

resource "aws_service_discovery_service" "quotes_api" {
  name = "techstories-quotes-api"

  dns_config {
    namespace_id = aws_service_discovery_private_dns_namespace.main.id
    dns_records {
      type = "A"
      ttl  = 60
    }
  }

  health_check_custom_config {
    failure_threshold = 1
  }

  tags = merge(var.common_tags, {
    service = "techstories-quotes-api"
  })
}

resource "aws_ecs_service" "quotes_api" {
  name            = "techstories-quotes-api"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.quotes_api.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    assign_public_ip = false
    security_groups  = [aws_security_group.fargate.id]
    subnets          = [var.private_subnet_1_id, var.private_subnet_2_id]
  }

  service_registries {
    registry_arn = aws_service_discovery_service.quotes_api.arn
  }

  tags = merge(var.common_tags, {
    service = "techstories-quotes-api"
  })
}

# --- Generate Posts API ---

resource "aws_iam_role" "generate_posts_task" {
  name_prefix = "techstories-genposts-task-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-generate-posts-api"
  })
}

resource "aws_iam_role_policy_attachment" "generate_posts_task" {
  role       = aws_iam_role.generate_posts_task.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_cloudwatch_log_group" "generate_posts_api" {
  name = "/ecs/techstories-generate-posts-api"

  tags = merge(var.common_tags, {
    service = "techstories-generate-posts-api"
  })
}

resource "aws_ecs_task_definition" "generate_posts_api" {
  family                   = "techstories-generate-posts-api"
  cpu                      = "1024"
  memory                   = "2048"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.fargate_execution.arn
  task_role_arn            = aws_iam_role.generate_posts_task.arn

  container_definitions = jsonencode([
    {
      name         = "generate-posts-api"
      image        = "europe-west1-docker.pkg.dev/datadog-community/training-images-docker/aws-techstories-generate-post-api:1.0.0"
      essential    = true
      portMappings = [{ containerPort = 3002 }]
      command      = ["npm", "run", "start"]
      environment = [
        { name = "PORT", value = "3002" },
        { name = "DD_ENV", value = "monitoring-aws-lab" },
        { name = "DD_SERVICE", value = "techstories-generate-posts-api" },
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
        "com.datadoghq.tags.service" = "techstories-generate-posts-api"
        "com.datadoghq.tags.version" = "1.0.0"
      }
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.generate_posts_api.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "generate-posts-api"
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
          "awslogs-group"         = aws_cloudwatch_log_group.generate_posts_api.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "datadog-agent"
        }
      }
    },
  ])

  tags = merge(var.common_tags, {
    service = "techstories-generate-posts-api"
  })
}

resource "aws_service_discovery_service" "generate_posts_api" {
  name = "techstories-generate-posts-api"

  dns_config {
    namespace_id = aws_service_discovery_private_dns_namespace.main.id
    dns_records {
      type = "A"
      ttl  = 60
    }
  }

  health_check_custom_config {
    failure_threshold = 1
  }

  tags = merge(var.common_tags, {
    service = "techstories-generate-posts-api"
  })
}

resource "aws_ecs_service" "generate_posts_api" {
  name            = "techstories-generate-posts-api"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.generate_posts_api.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    assign_public_ip = false
    security_groups  = [aws_security_group.fargate.id]
    subnets          = [var.private_subnet_1_id, var.private_subnet_2_id]
  }

  service_registries {
    registry_arn = aws_service_discovery_service.generate_posts_api.arn
  }

  tags = merge(var.common_tags, {
    service = "techstories-generate-posts-api"
  })
}

# --- Referrals Service ---

resource "aws_iam_role" "referrals_task" {
  name_prefix = "techstories-referrals-task-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-referrals-service"
  })
}

resource "aws_iam_role_policy_attachment" "referrals_task" {
  role       = aws_iam_role.referrals_task.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy" "referrals_task_dynamo" {
  name = "ReferralsServiceDynamoPolicy"
  role = aws_iam_role.referrals_task.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:Scan",
        "dynamodb:UpdateItem",
      ]
      Resource = [
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_points_table_name}",
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_submission_table_name}",
        "arn:aws:dynamodb:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:table/${var.referral_submission_table_name}/index/RefereeEmailIndex",
      ]
    }]
  })
}

resource "aws_cloudwatch_log_group" "referrals_service" {
  name = "/ecs/techstories-referrals-service"

  tags = merge(var.common_tags, {
    service = "techstories-referrals-service"
  })
}

resource "aws_ecs_task_definition" "referrals_service" {
  family                   = "techstories-referrals-service"
  cpu                      = "1024"
  memory                   = "2048"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.fargate_execution.arn
  task_role_arn            = aws_iam_role.referrals_task.arn

  container_definitions = jsonencode([
    {
      name         = "referrals-service"
      image        = "europe-west1-docker.pkg.dev/datadog-community/training-images-docker/aws-techstories-referrals-service:1.0.0"
      essential    = true
      portMappings = [{ containerPort = 3003 }]
      command      = ["ddtrace-run", "flask", "run", "--host=0.0.0.0", "--port=3003"]
      environment = [
        { name = "PORT", value = "3003" },
        { name = "FLASK_APP", value = "referrals.py" },
        { name = "DD_ENV", value = "monitoring-aws-lab" },
        { name = "DD_SERVICE", value = "techstories-referrals-service" },
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
        "com.datadoghq.tags.service" = "techstories-referrals-service"
        "com.datadoghq.tags.version" = "1.0.0"
      }
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.referrals_service.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "referrals-service"
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
          "awslogs-group"         = aws_cloudwatch_log_group.referrals_service.name
          "awslogs-region"        = data.aws_region.current.name
          "awslogs-stream-prefix" = "datadog-agent"
        }
      }
    },
  ])

  tags = merge(var.common_tags, {
    service = "techstories-referrals-service"
  })
}

resource "aws_service_discovery_service" "referrals_service" {
  name = "techstories-referrals-service"

  dns_config {
    namespace_id = aws_service_discovery_private_dns_namespace.main.id
    dns_records {
      type = "A"
      ttl  = 60
    }
  }

  health_check_custom_config {
    failure_threshold = 1
  }

  tags = merge(var.common_tags, {
    service = "techstories-referrals-service"
  })
}

resource "aws_ecs_service" "referrals_service" {
  name            = "techstories-referrals-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.referrals_service.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    assign_public_ip = false
    security_groups  = [aws_security_group.fargate.id]
    subnets          = [var.private_subnet_1_id, var.private_subnet_2_id]
  }

  service_registries {
    registry_arn = aws_service_discovery_service.referrals_service.arn
  }

  tags = merge(var.common_tags, {
    service = "techstories-referrals-service"
  })
}
