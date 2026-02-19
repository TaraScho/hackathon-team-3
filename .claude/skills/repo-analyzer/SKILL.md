---
name: repo-analyzer
description: >
  Analyzes a repository's infrastructure-as-code files to produce a prioritized
  Datadog resource recommendations report. Use this skill when you need to:
  determine what Datadog resources to build for an existing repo, audit a codebase
  for Datadog observability gaps, generate an actionable build list for subagents,
  map AWS services to App Builder apps and Workflow Automations, or onboard a new
  service onto Datadog. Outputs a tiered datadog-recommendations.md file with
  must-haves, nice-to-haves, and stretch goals. Trigger phrases: "analyze my repo
  for Datadog", "what Datadog resources should I build", "scan my repo for Datadog",
  "generate Datadog recommendations", "what should I build in Datadog for this codebase",
  "audit repo for Datadog", "Datadog onboarding for my repo", "map my AWS services to Datadog".
metadata:
  author: hackathon-team-3
  version: 1.0.0
  tags: [repo-analysis, recommendations, planning, aws, iac, app-builder, workflows, dashboards]
  category: planning
---

# Repo Analyzer Skill

## Overview

This skill scans a repository's IaC and infrastructure files to detect the AWS services in use, identify microservice boundaries, and map findings to concrete Datadog resources. The output is a tiered `datadog-recommendations.md` report that a human or subagent can act on directly.

```
repo (IaC files)
      │
      ▼
repo-analyzer ──► datadog-recommendations.md
                        │
                        ├──► action-connections skill
                        ├──► app-builder skill
                        ├──► workflow-automation skill
                        └──► dashboards skill
```

Each recommendation in the report names the skill to invoke and the trigger phrase to use, so subagents can act without further interpretation.

### Dependency Diagram

```
repo-analyzer (planning)
      │
      ▼
action-connections ──► workflow-automation
        │
        └──────────► app-builder ──► dashboards
```

This skill is the planning step. The four peer skills execute the plan.

---

## When to Use

- Onboarding a new service onto Datadog and unsure where to start
- Deciding which App Builder templates are relevant to the repo's AWS footprint
- Planning which remediation workflows to create based on detected risk patterns
- Generating an actionable queue for CI/CD automation or a subagent pipeline
- Assessing observability coverage before going to production
- Building a comprehensive IaC-driven Datadog setup from scratch

---

## Analysis Playbook (5-Step Process)

Follow these five steps in order whenever this skill is invoked.

### Step 1 — Inventory the Repo

Scan for the following file patterns to understand the IaC tooling and project structure:

| Pattern | What it tells you |
|---|---|
| `**/*.tf`, `**/*.tfvars` | Terraform — service names in resource blocks |
| `**/cdk.json`, `**/lib/**/*.ts` | AWS CDK — construct names map to services |
| `**/cloudformation/**/*.yaml`, `**/template.yaml` | CloudFormation / SAM |
| `Dockerfile*`, `docker-compose*.yml` | Runtime / container info |
| `**/k8s/**/*.yaml` | Kubernetes workloads |
| `**/.terraform.lock.hcl`, `**/terraform.tfstate` | Terraform state (suggests drift detection is relevant) |
| `**/otel*.yaml`, `**/opentelemetry*.yaml` | OTel collector config (Tier 3 dashboard candidate) |

Also look at the top-level directory layout — directory names often map directly to microservice names (e.g., `services/payments/`, `apps/api/`).

Extract from each file:
- Languages and runtimes (from Dockerfiles, `package.json`, `requirements.txt`)
- Deployment targets (ECS, EC2, Lambda, EKS)
- Any explicit AWS account IDs or region references

### Step 2 — Identify AWS Services

Use these patterns to build a deduplicated list of AWS services present:

**Terraform** — search for `resource "aws_<service>"` blocks:
```
resource "aws_ecs_service"           → ecs
resource "aws_ecs_task_definition"   → ecs
resource "aws_instance"              → ec2
resource "aws_security_group"        → ec2 (also flag for ingress risk)
resource "aws_iam_role"              → iam
resource "aws_iam_policy"            → iam
resource "aws_s3_bucket"             → s3
resource "aws_dynamodb_table"        → dynamodb
resource "aws_sqs_queue"             → sqs
resource "aws_lambda_function"       → lambda
resource "aws_sfn_state_machine"     → step-functions
resource "aws_autoscaling_group"     → autoscaling
resource "aws_db_instance"           → rds
```

**CDK TypeScript** — search for imports from `aws-cdk-lib/aws-<service>` or `new <Service>` constructs:
```typescript
import { Cluster, FargateService } from 'aws-cdk-lib/aws-ecs'  → ecs
import { Instance, SecurityGroup }  from 'aws-cdk-lib/aws-ec2'  → ec2
import { Function }                 from 'aws-cdk-lib/aws-lambda' → lambda
```

**CloudFormation / SAM** — search for `Type: AWS::<Service>::`:
```yaml
Type: AWS::ECS::Service         → ecs
Type: AWS::EC2::Instance        → ec2
Type: AWS::IAM::Role            → iam
Type: AWS::Serverless::Function → lambda
```

**Dockerfile / compose** — look at `ENV` vars and entrypoints for AWS service SDK references (e.g., `AWS_DYNAMODB_TABLE`, `SQS_QUEUE_URL`, `S3_BUCKET`).

### Step 3 — Map AWS Services to App Builder Templates

Use this table to select the applicable app definitions:

| AWS Service Found | App Builder Template | Notes |
|---|---|---|
| EC2 | `ec2-management-console.json` | Primary compute; always Tier 1 if present |
| ECS | `manage-ecs-tasks.json` | Primary compute; always Tier 1 if present |
| S3 | `explore-s3.json` | Storage visibility |
| DynamoDB | `manage-dynamodb.json` | NoSQL management console |
| SQS | `manage-sqs.json` | Queue inspection and management |
| Lambda | `lambda-function-manager.json` | Invoke, configure, view functions |
| Step Functions | `manage-step-functions.json` | State machine management |
| Auto Scaling | `manage-autoscaling.json` | Group capacity management |
| Multiple services | `aws-quick-review.json` | Read-only cross-service overview (always useful as a complement) |

If both EC2 and ECS are found, recommend both templates as separate Tier 1 items.

### Step 4 — Identify Security and Operational Risk Areas

Flag these patterns and pair each with the appropriate workflow:

| Pattern Found | Risk | Recommended Workflow |
|---|---|---|
| `aws_iam_role` or `aws_iam_policy` with `"*"` resource | Broad IAM permissions | IAM disable user workflow (`com.datadoghq.aws.iam.disable_user`) |
| `aws_security_group` with `ingress` blocks | Open network exposure | Revoke ingress workflow (`com.datadoghq.aws.ec2.revoke_security_group_ingress`) |
| `aws_ecs_service` or `aws_ecs_task_definition` | Deployment risk | ECS rollback workflow (4-step chain via `ecs.registerTaskDefinition` + `ecs.updateEcsService`) |
| `.terraform.tfstate` or remote state config | IaC drift possible | IaC drift detection workflow (monitor trigger → remediate) |
| Any deployment pipeline (CI YAML, `buildspec.yml`) | Drift between deployed and repo state | IaC drift detection dashboard + workflow |

### Step 5 — Assess Observability Gaps and Assign Tiers

Apply these criteria:

**Tier 1 — Foundation (build first, blocks everything else)**
- Action connection — always present regardless of what services are found; prerequisite for all other items
- App Builder app for primary compute (EC2, ECS, or both if both detected)
- SRE golden signals dashboard (`dd101-sre-dashboard.json`) — universally applicable

**Tier 2 — Operational Tooling (build after Tier 1)**
- App Builder apps for non-compute AWS services found (S3, DynamoDB, SQS, Lambda, Step Functions, Auto Scaling)
- Workflow automations tied to detected risk patterns (IAM breadth, EC2 security groups, ECS deployments)
- `aws-quick-review.json` app if 3+ distinct services found

**Tier 3 — Advanced Automation (stretch goals)**
- Composite dashboard with embedded App Builder app widgets (requires Tier 1/2 app IDs; use `techstories-dashboard-full.json` as base)
- Multi-step workflow chains (e.g., security signal → disable user → create case)
- OTel collector health dashboard (`otel-collector-health-dashboard.json`) — only if OTel config files detected
- IaC drift detection dashboard + workflow pair — only if Terraform state files detected

---

## AWS Service → Datadog Resource Mapping (Full Reference)

| AWS Service | App Builder Template | Workflow | Dashboard |
|---|---|---|---|
| EC2 | `ec2-management-console.json` | Revoke ingress (if SG ingress found) | SRE golden signals |
| ECS | `manage-ecs-tasks.json` | ECS rollback workflow | SRE golden signals |
| S3 | `explore-s3.json` | — | IaC visibility |
| DynamoDB | `manage-dynamodb.json` | — | SRE golden signals |
| SQS | `manage-sqs.json` | — | SRE golden signals |
| Lambda | `lambda-function-manager.json` | — | SRE golden signals |
| Step Functions | `manage-step-functions.json` | — | IaC visibility |
| Auto Scaling | `manage-autoscaling.json` | — | SRE golden signals |
| IAM (any role/policy) | (any of the above) | IAM disable user workflow | Security posture |
| Multi-service (3+) | `aws-quick-review.json` | — | Composite dashboard |
| OTel config detected | — | — | `otel-collector-health-dashboard.json` |

Action connection is **always** a Tier 1 item regardless of services found.

---

## Output Report Template

Write the following structure to `datadog-recommendations.md` at the root of the analyzed repo. Replace all `{placeholders}`.

```markdown
# Datadog Resources Recommendations
> Repo: {path} | Generated: {date} | Skill: repo-analyzer v1.0.0

## Findings Summary

- **AWS services detected:** {comma-separated list, e.g., ecs, iam, s3, sqs}
- **Microservices / service directories:** {list of top-level directories that map to services}
- **IaC tooling:** {Terraform / CDK TypeScript / CloudFormation / SAM — list all detected}
- **Risk areas:** {e.g., "broad IAM role in iam.tf:12", "EC2 SG with ingress 0.0.0.0/0 in security-groups.tf:34"}
- **OTel detected:** {Yes / No}
- **Terraform state detected:** {Yes / No}

---

## Tier 1: Foundation (Build These First)

### 1. AWS Action Connection
- **Skill to invoke:** `action-connections`
- **Trigger phrase:** "set up action connection for account {aws_account_id} with role DatadogActionRole"
- **Why:** Prerequisite for all App Builder apps and Workflow Automations below. Nothing else works without this.
- **Inputs required:** AWS account ID, IAM role name (`DatadogActionRole` recommended)
- **Output:** Connection UUID — save this; it is input to all items below

### 2. {Primary Compute App Builder App — EC2 and/or ECS}
- **Skill to invoke:** `app-builder`
- **Trigger phrase:** "create App Builder app from {template-name}.json with connection {connection_id}"
- **Template:** `{ec2-management-console.json | manage-ecs-tasks.json}`
- **Why:** {service} found in {file(s)}
- **Depends on:** Action connection from #1
- **Output:** App UUID — save this; it is input to Tier 3 composite dashboard

### 3. SRE Golden Signals Dashboard
- **Skill to invoke:** `dashboards`
- **Trigger phrase:** "create dashboard from dd101-sre-dashboard.json"
- **Template:** `dd101-sre-dashboard.json`
- **Why:** Core operational visibility (latency, traffic, errors, saturation) — applicable to all services found
- **Depends on:** Nothing (standalone template, no app IDs needed)

---

## Tier 2: Operational Tooling

### {N}. {App Builder App for Additional Service}
- **Skill to invoke:** `app-builder`
- **Trigger phrase:** "create App Builder app from {template-name}.json with connection {connection_id}"
- **Template:** `{template-name}.json`
- **Why:** {service} found in {file(s)}
- **Depends on:** Action connection from Tier 1 #1

### {N}. {Workflow Automation — one per risk area detected}
- **Skill to invoke:** `workflow-automation`
- **Trigger phrase:** "{e.g., 'create IAM disable user workflow' | 'create ECS rollback workflow' | 'create revoke ingress workflow'}"
- **Why:** {risk pattern} detected in {file(s)}
- **Key action IDs:**
  - IAM disable user: `com.datadoghq.aws.iam.disable_user`
  - Revoke SG ingress: `com.datadoghq.aws.ec2.revoke_security_group_ingress`
  - ECS rollback: `com.datadoghq.aws.ecs.updateEcsService` (4-step chain)
- **Depends on:** Action connection from Tier 1 #1

---

## Tier 3: Advanced Automation

### {N}. Composite Dashboard with Embedded Apps
- **Skill to invoke:** `dashboards`
- **Trigger phrase:** "create composite dashboard from techstories-dashboard-full.json with app IDs {id_map}"
- **Template:** `techstories-dashboard-full.json`
- **Why:** Embeds all Tier 1/2 App Builder apps into a single operations control plane
- **Depends on:** All app IDs from Tier 1 and Tier 2 app-builder items

### {N}. OTel Collector Health Dashboard (if OTel detected)
- **Skill to invoke:** `dashboards`
- **Trigger phrase:** "create dashboard from otel-collector-health-dashboard.json"
- **Template:** `otel-collector-health-dashboard.json`
- **Condition:** Only include if OTel config files were found in Step 1

### {N}. IaC Drift Detection (if Terraform state detected)
- **Skill to invoke:** `workflow-automation` + `dashboards`
- **Trigger phrase:** "create IaC drift detection workflow and dashboard"
- **Why:** Terraform state files detected — drift between deployed and repo state is a risk
- **Condition:** Only include if `.terraform.tfstate` or remote state config found

---

## Dependency Build Order

```
action-connections (Tier 1 #1)
  ├──► {primary compute app} (Tier 1 #2) ──► composite dashboard (Tier 3)
  ├──► {additional apps}     (Tier 2)     ──► composite dashboard (Tier 3)
  └──► {workflow automations}(Tier 2)
dashboards - SRE golden signals (Tier 1 #3, standalone)
```

## Invoke Sequence for Subagents

1. **action-connections skill** → creates connection, returns connection UUID
2. **app-builder skill** → deploys Tier 1 + Tier 2 apps using connection UUID, returns app UUIDs
3. **workflow-automation skill** → creates workflows using connection UUID
4. **dashboards skill** → creates standalone dashboards; then creates composite dashboard using app UUIDs from step 2
```

---

## Where to Write the Report

- **Default:** Save as `datadog-recommendations.md` at the root of the analyzed repo path
- **Fallback:** If the repo path is read-only or the user prefers a different location, save to the current working directory
- Always state the full output path explicitly in the final response message

---

## Cross-Skill Notes

This skill produces the planning artifact; the other four skills execute it.

| Skill | Role in pipeline | Key input | Key output |
|---|---|---|---|
| `action-connections` | Always first; enables all AWS actions | AWS account ID, role name | Connection UUID |
| `app-builder` | Deploys management UIs | Connection UUID | App UUIDs |
| `workflow-automation` | Automated remediation | Connection UUID | Workflow UUIDs |
| `dashboards` | Final visualization layer | App UUIDs (for composite), standalone templates need nothing | Dashboard URLs |

**Connection UUID** flows from `action-connections` into both `app-builder` (as `connectionId` in app JSON or `action_query_names_to_connection_ids` in Terraform) and `workflow-automation` (as `connectionId` in `connectionEnvs`).

**App UUIDs** flow from `app-builder` into `dashboards` for placeholder substitution in composite dashboard templates.

**Monitor IDs** created in `dashboards` can be passed back to `workflow-automation` as `monitorTrigger` sources.

---

## Level 3 References

- `../action-connections/SKILL.md` — 5-step connection setup; external ID retrieval; IAM trust policy pattern
- `../app-builder/SKILL.md` — full template list; `transform_app_json_for_api()` transformation; publish flow
- `../workflow-automation/SKILL.md` — all action IDs; ECS rollback walk-through; Terraform `spec_json` pattern
- `../dashboards/SKILL.md` — available dashboard templates; composite dashboard embedding; monitor management
