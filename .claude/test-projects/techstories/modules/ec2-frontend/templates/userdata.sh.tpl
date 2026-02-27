#!/bin/bash -xe
echo "Running user data script..."

dnf makecache --refresh
dnf install -y python3 unzip aws-cli nodejs git jq
npm install -g yarn

# --- Install Datadog Agent ---
DD_API_KEY="${dd_api_key}" DD_SITE="datadoghq.com" DD_ENV="monitoring-aws-lab" \
  DD_HOST_TAGS="service:techstories-frontend,env:monitoring-aws-lab,version:1.0.0" \
  bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"

cat <<'DDCONF' >> /etc/datadog-agent/datadog.yaml
apm_config:
  enabled: true
logs_enabled: true
process_config:
  process_collection:
    enabled: true
data_streams_config:
  enabled: true
DDCONF

systemctl restart datadog-agent

echo "Cloning TechStories release for Intro to AWS course..."
mkdir -p /root/lab
git clone https://github.com/DataDog/techstories-demo-app.git /root/lab/techstories
cd /root/lab/techstories
git checkout template/aws_techstories_05_06

DATABASE_SECRET_ARN="${db_secret_arn}"

secret=$(aws secretsmanager get-secret-value --secret-id "$DATABASE_SECRET_ARN" --query SecretString --output text)
db_user=$(echo "$secret" | jq -r .username)
db_password_raw=$(echo "$secret" | jq -r .password)

db_password_encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$db_password_raw'''))")

export DB_USER="$db_user"
export DB_PASSWORD_ENCODED="$db_password_encoded"
export DB_HOST=${db_host}
export DB_PORT=${db_port}
export DB_NAME="db"
export DB_SCHEMA="techstories"

export DATABASE_URL="postgresql://$DB_USER:$DB_PASSWORD_ENCODED@$DB_HOST:$DB_PORT/$DB_NAME?schema=$DB_SCHEMA"
export DD_API_KEY="${dd_api_key}"
export DD_APP_KEY="${dd_app_key}"
export ALB_URL="http://${alb_dns_name}"

cat <<EOF > /root/lab/techstories/.env
NEXTAUTH_SECRET="secret"
NEXTAUTH_URL="$ALB_URL"

DATABASE_URL="$DATABASE_URL"

DD_API_KEY="$DD_API_KEY"
DD_APP_KEY="$DD_APP_KEY"

NEXT_PUBLIC_DD_SERVICE_NAME="techstories-frontend"
NEXT_PUBLIC_DD_ENV="monitoring-aws-lab"
NEXT_PUBLIC_DD_VERSION="1.0.0"
NEXT_PUBLIC_DD_SITE="datadoghq.com"

# Private DNS names for services in ECS Fargate
INTERNAL_QUOTES_API_URL="http://techstories-quotes-api.techstories.local:3001"
INTERNAL_GENERATE_POSTS_API_URL="http://techstories-generate-posts-api.techstories.local:3002"
INTERNAL_REFERRALS_API_URL="http://techstories-referrals-service.techstories.local:3003"

DD_ENV="monitoring-aws-lab"
DD_SERVICE="techstories-frontend"
DD_VERSION="1.0.0"
DD_TRACE_ENABLED="true"
DD_LOGS_INJECTION="true"
DD_PROFILING_ENABLED="true"
DD_DATA_STREAMS_ENABLED="true"
DD_TRACE_REMOVE_INTEGRATION_SERVICE_NAMES_ENABLED="true"

# URL for keyword insights SQS queue
INTERNAL_KEYWORD_INSIGHTS_QUEUE_URL="https://sqs.${aws_region}.amazonaws.com/${aws_account_id}/${keyword_insights_queue_name}"

EOF

npm install
npm run db-prep
npm run build
npm run start
