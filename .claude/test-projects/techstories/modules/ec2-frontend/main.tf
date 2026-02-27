data "aws_region" "current" {}
data "aws_caller_identity" "current" {}

data "aws_ssm_parameter" "al2023_ami" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64"
}

# --- Security groups ---

resource "aws_security_group" "alb" {
  name_prefix = "techstories-alb-"
  description = "Allow HTTP access to the ALB"
  vpc_id      = var.vpc_id

  tags = merge(var.common_tags, {
    Name    = "techstories-frontend-alb-sg"
    service = "techstories-frontend"
  })
}

resource "aws_vpc_security_group_ingress_rule" "alb_http" {
  security_group_id = aws_security_group.alb.id
  from_port         = 80
  to_port           = 80
  ip_protocol       = "tcp"
  cidr_ipv4         = "10.0.0.0/16"
}

resource "aws_vpc_security_group_egress_rule" "alb_all" {
  security_group_id = aws_security_group.alb.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

resource "aws_security_group" "ec2" {
  name_prefix = "techstories-ec2-"
  description = "Security group for EC2 server"
  vpc_id      = var.vpc_id

  tags = merge(var.common_tags, {
    service = "techstories-frontend"
  })
}

resource "aws_vpc_security_group_ingress_rule" "ec2_from_alb" {
  security_group_id            = aws_security_group.ec2.id
  from_port                    = 3000
  to_port                      = 3000
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.alb.id
  description                  = "Allow HTTP from ALB"
}

resource "aws_vpc_security_group_egress_rule" "ec2_all" {
  security_group_id = aws_security_group.ec2.id
  ip_protocol       = "-1"
  cidr_ipv4         = "0.0.0.0/0"
}

# --- Cross-stack security group rules ---

resource "aws_vpc_security_group_ingress_rule" "db_from_ec2" {
  security_group_id            = var.db_security_group_id
  from_port                    = var.db_port
  to_port                      = var.db_port
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.ec2.id
}

resource "aws_vpc_security_group_ingress_rule" "fargate_quotes" {
  security_group_id            = var.fargate_security_group_id
  from_port                    = 3001
  to_port                      = 3001
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.ec2.id
}

resource "aws_vpc_security_group_ingress_rule" "fargate_generate_posts" {
  security_group_id            = var.fargate_security_group_id
  from_port                    = 3002
  to_port                      = 3002
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.ec2.id
}

resource "aws_vpc_security_group_ingress_rule" "fargate_referrals" {
  security_group_id            = var.fargate_security_group_id
  from_port                    = 3003
  to_port                      = 3003
  ip_protocol                  = "tcp"
  referenced_security_group_id = aws_security_group.ec2.id
}

# --- IAM ---

resource "aws_iam_role" "ec2" {
  name_prefix = "techstories-web-"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = merge(var.common_tags, {
    service = "techstories-frontend"
  })
}

resource "aws_iam_role_policy_attachment" "ec2_ssm" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_role_policy_attachment" "ec2_cloudwatch" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"
}

resource "aws_iam_role_policy" "ec2_s3" {
  name = "EC2S3Access"
  role = aws_iam_role.ec2.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = "s3:*"
      Resource = [
        "arn:aws:s3:::${var.assets_bucket_name}",
        "arn:aws:s3:::${var.assets_bucket_name}/*",
      ]
    }]
  })
}

resource "aws_iam_role_policy" "ec2_secrets" {
  name = "EC2SecretsManagerAccess"
  role = aws_iam_role.ec2.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "secretsmanager:GetSecretValue"
      Resource = var.db_secret_arn
    }]
  })
}

resource "aws_iam_role_policy" "ec2_sqs" {
  name = "EC2SQSAccess"
  role = aws_iam_role.ec2.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "sqs:SendMessage"
      Resource = "arn:aws:sqs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:${var.keyword_insights_queue_name}"
    }]
  })
}

resource "aws_iam_instance_profile" "ec2" {
  name_prefix = "techstories-web-"
  role        = aws_iam_role.ec2.name
}

# --- ALB ---

resource "aws_lb" "frontend" {
  name               = "techstories-frontend-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = [var.public_subnet_1_id, var.public_subnet_2_id]
  security_groups    = [aws_security_group.alb.id]

  tags = merge(var.common_tags, {
    service = "techstories-frontend"
  })
}

resource "aws_lb_target_group" "frontend" {
  name_prefix = "ts-fe-"
  port        = 3000
  protocol    = "HTTP"
  target_type = "instance"
  vpc_id      = var.vpc_id

  health_check {
    path     = "/"
    protocol = "HTTP"
    matcher  = "200"
  }

  tags = merge(var.common_tags, {
    service = "techstories-frontend"
  })
}

resource "aws_lb_listener" "frontend" {
  load_balancer_arn = aws_lb.frontend.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.frontend.arn
  }
}

# --- Launch template + ASG ---

resource "aws_launch_template" "frontend" {
  name = "techstories-frontend-launch-template"

  instance_type = var.instance_type
  image_id      = data.aws_ssm_parameter.al2023_ami.value

  vpc_security_group_ids = [aws_security_group.ec2.id]

  iam_instance_profile {
    name = aws_iam_instance_profile.ec2.name
  }

  metadata_options {
    http_tokens = "required"
  }

  user_data = base64encode(templatefile("${path.module}/templates/userdata.sh.tpl", {
    db_secret_arn               = var.db_secret_arn
    db_host                     = var.db_endpoint
    db_port                     = var.db_port
    dd_api_key                  = var.datadog_api_key
    dd_app_key                  = var.datadog_app_key
    alb_dns_name                = aws_lb.frontend.dns_name
    aws_region                  = data.aws_region.current.name
    aws_account_id              = data.aws_caller_identity.current.account_id
    keyword_insights_queue_name = var.keyword_insights_queue_name
  }))

  tag_specifications {
    resource_type = "instance"
    tags = merge(var.common_tags, {
      Name    = "TechStories-Web-Server"
      service = "techstories-frontend"
    })
  }

  tag_specifications {
    resource_type = "volume"
    tags = merge(var.common_tags, {
      service = "techstories-frontend"
    })
  }

  tags = merge(var.common_tags, {
    service = "techstories-frontend"
  })
}

resource "aws_autoscaling_group" "frontend" {
  name_prefix      = "techstories-web-"
  min_size         = 1
  max_size         = 1
  desired_capacity = 1

  launch_template {
    id      = aws_launch_template.frontend.id
    version = aws_launch_template.frontend.latest_version
  }

  vpc_zone_identifier = [var.public_subnet_1_id, var.public_subnet_2_id]
  target_group_arns   = [aws_lb_target_group.frontend.arn]

  health_check_type         = "ELB"
  health_check_grace_period = 300

  tag {
    key                 = "Name"
    value               = "TechStories-Web-Server"
    propagate_at_launch = true
  }
}
