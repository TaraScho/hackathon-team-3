resource "aws_security_group" "db" {
  name_prefix = "techstories-db-"
  description = "Allow DB access from ECS"
  vpc_id      = var.vpc_id

  tags = merge(var.common_tags, {
    Name    = "DBSecurityGroup"
    service = "techstories-database"
  })
}

resource "aws_db_subnet_group" "main" {
  name        = "techstories-db-subnet-group"
  description = "Private subnets for Postgres DB"
  subnet_ids  = [var.private_subnet_1_id, var.private_subnet_2_id]

  tags = merge(var.common_tags, {
    service = "techstories-database"
  })
}

resource "random_password" "db_master" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}|:?"
}

resource "aws_secretsmanager_secret" "db_master" {
  name        = "techstories-postgres-master-secret"
  description = "Master user password for TechStories Postgres DB"

  tags = merge(var.common_tags, {
    service = "techstories-database"
  })
}

resource "aws_secretsmanager_secret_version" "db_master" {
  secret_id = aws_secretsmanager_secret.db_master.id
  secret_string = jsonencode({
    username = "postgres"
    password = random_password.db_master.result
  })
}

resource "aws_db_instance" "main" {
  identifier     = "techstories-postgres-instance"
  engine         = "postgres"
  engine_version = "17.2"
  instance_class = "db.t3.small"

  allocated_storage = 20
  storage_type      = "gp2"

  username = jsondecode(aws_secretsmanager_secret_version.db_master.secret_string)["username"]
  password = jsondecode(aws_secretsmanager_secret_version.db_master.secret_string)["password"]

  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name

  publicly_accessible     = false
  backup_retention_period = 7
  deletion_protection     = false
  multi_az                = false
  skip_final_snapshot     = true

  tags = merge(var.common_tags, {
    Name    = "TechStoriesPostgres DB"
    service = "techstories-database"
  })
}
