# AWS Service to Datadog Resource Mapping

> Full reference for the repo-analyzer skill. This document expands on the condensed tables in SKILL.md with complete mappings, tier criteria, and workflow trigger types.

---

## AWS Service to App Builder Template Mapping

| AWS Service | App Builder Template | Service Catalog Entity Type | Notes |
|---|---|---|---|
| EC2 | `ec2-management-console.json` | `service` | Primary compute; always Tier 1 if present |
| ECS | `manage-ecs-tasks.json` | `service` | Primary compute; always Tier 1 if present |
| S3 | `explore-s3.json` | `service` | Storage visibility |
| DynamoDB | `manage-dynamodb.json` | `service` | NoSQL management console |
| SQS | `manage-sqs.json` | `service` | Queue inspection and management |
| Lambda | `lambda-function-manager.json` | `service` | Invoke, configure, view functions |
| Step Functions | `manage-step-functions.json` | `service` | State machine management |
| Auto Scaling | `manage-autoscaling.json` | `service` | Group capacity management |
| Multiple services (3+) | `aws-quick-review.json` | — | Read-only cross-service overview; always useful as a complement |
| CloudFront | _(no template yet)_ | `service` | CDN edge distribution — candidate for future template |
| RDS | _(no template yet)_ | `service` | Relational database — candidate for future template |
| ElastiCache | _(no template yet)_ | `service` | Cache cluster management — candidate for future template |
| SNS | _(no template yet)_ | `service` | Notification topic management — candidate for future template |
| API Gateway | _(no template yet)_ | `service` | REST/HTTP API management — candidate for future template |

### Service Catalog Entity Types

When registering discovered services with the `software-catalog` skill, use these entity types:

| Entity Type | When to Use | Example |
|---|---|---|
| `service` | Backend services, APIs, workers, data stores — any AWS resource that serves traffic or processes data | ECS task, Lambda function, RDS instance |
| `frontend` | Web UIs, SPAs, static sites — anything that serves end-user browser content | CloudFront + S3 static hosting, Amplify app |
| `library` | Shared modules, CDK constructs, Terraform modules, internal packages consumed by other services | A shared `cdk-constructs/` directory, a `modules/` Terraform folder |
| `custom` | Infrastructure-only resources that don't fit service/frontend/library — networking, security, CI/CD tooling | VPC definitions, IAM baseline stacks, CodePipeline definitions |

---

## Output Format Derivation

The `preferred_output_format` field in `repo-analysis.json` tells downstream skills whether to generate Terraform (`.tf`) or Python API scripts. It is derived from the detected IaC tooling in Step 1b.

### Derivation Rules

| Detected `iac_tooling` | `preferred_output_format` | Output Style |
|---|---|---|
| `Terraform` | `terraform` | `.tf` files using `datadog_*` Terraform provider resources |
| `CloudFormation` | `python` | Python scripts calling Datadog REST API via `requests` |
| `CDK TypeScript` | `python` | Python scripts calling Datadog REST API via `requests` |
| `SAM` | `python` | Python scripts calling Datadog REST API via `requests` |
| Unknown / not detected | `python` | Python scripts (safe default — no provider config needed) |

### Mixed IaC Edge Cases

When a repo contains multiple IaC frameworks:

| Scenario | Resolution | Example |
|---|---|---|
| More `.tf` files than CFN/CDK templates | `terraform` | 15 `.tf` files, 3 CloudFormation YAML → `terraform` |
| More CFN/CDK templates than `.tf` files | `python` | 2 `.tf` files, 10 CloudFormation YAML → `python` |
| Equal count | `terraform` | 5 `.tf` files, 5 CloudFormation YAML → `terraform` (tiebreaker) |
| Only CDK with no CFN | `python` | `cdk.json` present, TypeScript constructs → `python` |

**Counting rules:**
- Terraform: count files matching `**/*.tf` (exclude `.terraform/` directories)
- CloudFormation: count files matching `**/*.yaml` and `**/*.json` inside `cloudformation/` directories, plus `template.yaml`/`template.json` at any level
- CDK: count `.ts` files inside `lib/` directories where `cdk.json` exists at the project root

### Downstream Impact

All five product skills read `preferred_output_format` from `.claude/context/repo-analysis.json`:

| Skill | `terraform` output | `python` output |
|---|---|---|
| action-connections | `datadog_action_connection` + `aws_iam_role` resources | `setup_action_connection.py` API script |
| app-builder | `datadog_app_builder_app` with `file()` | `app_builder_helpers.py` create flow |
| dashboards | `datadog_dashboard_json` with `file()` | `create_dashboard()` API script |
| workflow-automation | `datadog_workflow_automation` with `spec_json` | `create_workflows.py` API script |
| software-catalog | `datadog_service_definition` (v2.2 YAML schema) | `POST /api/v2/catalog/entity` (v3 JSON) |

---

## Risk Pattern to Workflow Mapping

| Pattern Found | Risk | Recommended Workflow | Action ID / Approach | Trigger Type |
|---|---|---|---|---|
| `aws_iam_role` or `aws_iam_policy` with `"*"` resource | Broad IAM permissions | IAM disable user | `com.datadoghq.aws.iam.disable_user` | Security signal |
| `aws_security_group` with `ingress` from `0.0.0.0/0` | Open network exposure | Revoke ingress | `com.datadoghq.aws.ec2.revoke_security_group_ingress` | Security signal |
| `aws_ecs_service` or `aws_ecs_task_definition` | Deployment risk | ECS rollback | 4-step chain: `ecs.registerTaskDefinition` + `ecs.updateEcsService` | Monitor alert |
| `.terraform.tfstate` or remote state config | IaC drift possible | IaC drift detection | Monitor trigger then remediate | Scheduled (cron) |
| CI YAML, `buildspec.yml`, deployment pipeline | Drift between deployed and repo state | Deployment drift alert | Dashboard + workflow pair | Scheduled (cron) |
| `aws_s3_bucket` without `block_public_access` | S3 public access risk | S3 public access remediation | `com.datadoghq.aws.s3.putPublicAccessBlock` | Security signal |
| `aws_lambda_function` with `timeout` > 300 or missing | Lambda timeout risk | Lambda timeout remediation | `com.datadoghq.aws.lambda.updateFunctionConfiguration` | Monitor alert |
| `aws_db_instance` with `publicly_accessible = true` | RDS public exposure | RDS public access remediation | `com.datadoghq.aws.rds.modifyDBInstance` | Security signal |
| No `aws_cloudtrail` resource in account-level IaC | CloudTrail logging disabled | Enable CloudTrail logging | `com.datadoghq.aws.cloudtrail.createTrail` + `startLogging` | Incident |

---

## Tier Assignment Criteria

### Tier 1 — Foundation (build first; blocks everything else)

A recommendation is Tier 1 if **any** of these are true:

1. **It is the action connection.** Every Datadog-to-AWS integration requires this. It is always Tier 1 regardless of what services the repo uses.
2. **It covers primary compute.** If the repo deploys workloads to EC2 or ECS, the corresponding App Builder app is Tier 1 because it provides the core operational control plane.
3. **It is the SRE golden signals dashboard.** The `dd101-sre-dashboard.json` template covers latency, traffic, errors, and saturation — universally applicable to any service.

Tier 1 items have **zero optional dependencies** on other Datadog resources (except the action connection itself, which is always first).

### Tier 2 — Operational Tooling (build after Tier 1)

A recommendation is Tier 2 if:

1. **It is an App Builder app for a non-compute AWS service** (S3, DynamoDB, SQS, Lambda, Step Functions, Auto Scaling). These provide operational visibility but are not the primary control plane.
2. **It is a workflow automation tied to a detected risk pattern.** Risk-based workflows need the action connection from Tier 1 but are otherwise independent.
3. **It is the `aws-quick-review.json` app** when 3 or more distinct services are found — useful as a cross-service overview but not essential for day-one operations.

Tier 2 items depend only on the Tier 1 action connection. They can be built in parallel with each other.

### Tier 3 — Advanced Automation (stretch goals)

A recommendation is Tier 3 if:

1. **It requires outputs from Tier 1 and Tier 2.** The composite dashboard (`techstories-dashboard-full.json`) needs app UUIDs from deployed App Builder apps.
2. **It chains multiple workflows.** Multi-step chains (e.g., security signal triggers user disable triggers case creation) are higher complexity.
3. **It is conditional on specialized tooling.** The OTel collector health dashboard is only relevant if OTel config files are detected. IaC drift detection is only relevant if Terraform state files are present.
4. **It involves cross-skill orchestration.** Items that require coordinating outputs from 2+ other skills are Tier 3 by default.

---

## Workflow Trigger Types

Workflows are not limited to security signals. Use the appropriate trigger type based on the risk pattern:

| Trigger Type | When to Use | Example |
|---|---|---|
| **Security signal** | Datadog Cloud SIEM detects a real-time security event | IAM credential compromise, S3 bucket made public, security group opened |
| **Monitor alert** | A Datadog monitor threshold is breached | ECS task CPU > 90%, Lambda error rate > 5%, RDS connection count spike |
| **Scheduled (cron)** | Periodic checks that don't map to a single monitor | IaC drift detection (run every 6h), compliance posture scan (daily), cost anomaly check (weekly) |
| **Incident** | A Datadog incident is created or escalated | CloudTrail logging found disabled during incident triage, broad IAM role discovered during IR |
| **Manual** | Operator-initiated via App Builder button or workflow UI | Ad-hoc ECS rollback, force S3 public access block, rotate credentials |

When populating `workflow_candidates` in the JSON output, include a `trigger` field alongside `type` and `risk` to indicate the recommended trigger type.

---

## Future App Template Candidates

These AWS services are commonly found in IaC repos but do not yet have App Builder templates. They are candidates for custom app development:

| AWS Service | Proposed App Name | Key Actions | Priority |
|---|---|---|---|
| RDS | `manage-rds.json` | Instance status, failover, snapshot, parameter groups | High — very common in production repos |
| CloudFront | `manage-cloudfront.json` | Distribution status, invalidation, origin config | Medium — relevant for frontend-heavy repos |
| ElastiCache | `manage-elasticache.json` | Cluster status, node groups, replication | Medium — common caching layer |
| SNS | `manage-sns.json` | Topic listing, subscription management, publish test message | Medium — notification backbone |
| API Gateway | `manage-apigateway.json` | Stage management, deployment history, throttling config | High — very common for serverless repos |
| EKS | `manage-eks.json` | Cluster status, node groups, addon management | High — growing Kubernetes adoption |
| Kinesis | `manage-kinesis.json` | Stream status, shard management, consumer listing | Low — niche data streaming |
| CodePipeline | `manage-codepipeline.json` | Pipeline status, stage actions, manual approvals | Low — CI/CD visibility |

---

## Full Cross-Reference: AWS Service to All Datadog Resources

| AWS Service | App Builder Template | Workflow | Dashboard | Service Catalog Type |
|---|---|---|---|---|
| EC2 | `ec2-management-console.json` | Revoke ingress (if SG ingress found) | SRE golden signals | `service` |
| ECS | `manage-ecs-tasks.json` | ECS rollback workflow | SRE golden signals | `service` |
| S3 | `explore-s3.json` | S3 public access remediation | IaC visibility | `service` |
| DynamoDB | `manage-dynamodb.json` | — | SRE golden signals | `service` |
| SQS | `manage-sqs.json` | — | SRE golden signals | `service` |
| Lambda | `lambda-function-manager.json` | Lambda timeout remediation | SRE golden signals | `service` |
| Step Functions | `manage-step-functions.json` | — | IaC visibility | `service` |
| Auto Scaling | `manage-autoscaling.json` | — | SRE golden signals | `service` |
| RDS | _(no template yet)_ | RDS public access remediation | SRE golden signals | `service` |
| IAM (any role/policy) | (any of the above) | IAM disable user workflow | Security posture | `custom` |
| CloudTrail | — | Enable CloudTrail logging | Security posture | `custom` |
| Multi-service (3+) | `aws-quick-review.json` | — | Composite dashboard | — |
| OTel config detected | — | — | `otel-collector-health-dashboard.json` | — |
| CloudFront | _(no template yet)_ | — | SRE golden signals | `frontend` |
| CDK constructs dir | — | — | — | `library` |
| Terraform modules dir | — | — | — | `library` |
| VPC / networking-only | — | — | — | `custom` |

Action connection is **always** a Tier 1 item regardless of services found.
