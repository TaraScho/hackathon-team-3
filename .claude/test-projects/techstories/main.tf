locals {
  common_tags = {
    application = "techstories"
    team        = "techstories"
    Env         = "monitoring-aws-lab"
    Version     = "1.0.0"
    project     = "techstories"
  }
}

module "vpc" {
  source      = "./modules/vpc"
  common_tags = local.common_tags
}

module "rds" {
  source              = "./modules/rds"
  vpc_id              = module.vpc.vpc_id
  private_subnet_1_id = module.vpc.private_subnet_1_id
  private_subnet_2_id = module.vpc.private_subnet_2_id
  db_name             = var.db_name
  common_tags         = local.common_tags
}

module "ecs" {
  source                         = "./modules/ecs"
  vpc_id                         = module.vpc.vpc_id
  private_subnet_1_id            = module.vpc.private_subnet_1_id
  private_subnet_2_id            = module.vpc.private_subnet_2_id
  referral_points_table_name     = var.referral_points_table_name
  referral_submission_table_name = var.referral_submission_table_name
  datadog_api_key_secret_arn     = var.datadog_api_key_secret_arn
  common_tags                    = local.common_tags
}

module "ec2_frontend" {
  source                      = "./modules/ec2-frontend"
  vpc_id                      = module.vpc.vpc_id
  public_subnet_1_id          = module.vpc.public_subnet_1_id
  public_subnet_2_id          = module.vpc.public_subnet_2_id
  db_security_group_id        = module.rds.db_security_group_id
  db_endpoint                 = module.rds.db_endpoint
  db_secret_arn               = module.rds.db_master_secret_arn
  fargate_security_group_id   = module.ecs.fargate_security_group_id
  datadog_api_key             = var.datadog_api_key
  datadog_app_key             = var.datadog_app_key
  assets_bucket_name          = var.assets_bucket_name
  keyword_insights_queue_name = var.keyword_insights_queue_name
  common_tags                 = local.common_tags
}

module "traffic_generator" {
  source                     = "./modules/traffic-generator"
  vpc_id                     = module.vpc.vpc_id
  private_subnet_1_id        = module.vpc.private_subnet_1_id
  private_subnet_2_id        = module.vpc.private_subnet_2_id
  ecs_cluster_id             = module.ecs.cluster_id
  techstories_url            = module.ec2_frontend.techstories_url
  datadog_api_key_secret_arn = var.datadog_api_key_secret_arn
  common_tags                = local.common_tags
}

resource "aws_vpc_security_group_ingress_rule" "alb_from_nat_gateway" {
  security_group_id = module.ec2_frontend.alb_security_group_id
  from_port         = 80
  to_port           = 80
  ip_protocol       = "tcp"
  cidr_ipv4         = "${module.vpc.nat_gateway_public_ip}/32"
  description       = "Allow HTTP from NAT gateway (traffic generator)"
}

module "lambda_dynamodb" {
  source                         = "./modules/lambda-dynamodb"
  keyword_insights_queue_name    = var.keyword_insights_queue_name
  referral_points_table_name     = var.referral_points_table_name
  referral_submission_table_name = var.referral_submission_table_name
  ec2_instance_role_arn          = module.ec2_frontend.ec2_role_arn
  datadog_api_key_secret_arn     = var.datadog_api_key_secret_arn
  common_tags                    = local.common_tags
}

module "step_functions_sqs" {
  source                     = "./modules/step-functions-sqs"
  vpc_id                     = module.vpc.vpc_id
  private_subnet_1_id        = module.vpc.private_subnet_1_id
  private_subnet_2_id        = module.vpc.private_subnet_2_id
  datadog_api_key_secret_arn = var.datadog_api_key_secret_arn
  common_tags                = local.common_tags
}
