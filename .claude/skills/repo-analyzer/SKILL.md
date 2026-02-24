---
name: repo-analyzer
description: >
  Scans a repo's IaC files to produce a tiered Datadog resource recommendations
  report (datadog-recommendations.md + repo-analysis.json). Maps AWS services
  to App Builder templates and risk patterns to Workflow Automations.
  Trigger phrases: "analyze my repo for Datadog", "what Datadog resources should I build",
  "scan my repo", "generate Datadog recommendations", "audit repo for Datadog",
  "Datadog onboarding for my repo", "map AWS services to Datadog".
  Do NOT use to execute recommendations — use action-connections, app-builder,
  workflow-automation, dashboards, or software-catalog to act on them.
compatibility: >
  Read-only analysis — no API keys or external dependencies required.
  Needs file system access to scan repository IaC files.
metadata:
  author: hackathon-team-3
  version: 1.1.0
  tags: [repo-analysis, recommendations, planning, aws, iac, app-builder, workflows, dashboards]
  category: planning
---

# Repo Analyzer Skill

## Overview

Scans a repository's IaC and infrastructure files to detect AWS services, identify microservice boundaries, and map findings to concrete Datadog resources. Outputs a tiered `datadog-recommendations.md` report and a machine-parseable `repo-analysis.json`.

```
repo (IaC files)
      |
      v
repo-analyzer --> datadog-recommendations.md (human-readable)
              \-> repo-analysis.json         (machine-parseable)
                        |
                        |---> action-connections skill
                        |---> app-builder skill
                        |---> workflow-automation skill
                        \---> dashboards skill
```

Each recommendation names the skill to invoke and the trigger phrase to use.

### Dependency Diagram

```
repo-analyzer (planning)
      |
      v
action-connections --> workflow-automation
        |
        \----------> app-builder --> dashboards
```

---

## When to Use

- Onboarding a new service onto Datadog and unsure where to start
- Deciding which App Builder templates are relevant to a repo's AWS footprint
- Planning which remediation workflows to create based on detected risk patterns
- Generating an actionable queue for subagent pipelines or CI/CD automation
- Assessing observability coverage before going to production

---

## Analysis Playbook (5-Step Process)

### Step 1 — Inventory the Repo

Scan for IaC file patterns to identify tooling and project structure:

- **Terraform:** `**/*.tf`, `**/*.tfvars`, `**/.terraform.lock.hcl`
- **CDK:** `**/cdk.json`, `**/lib/**/*.ts`
- **CloudFormation / SAM:** `**/cloudformation/**/*.yaml`, `**/template.yaml`
- **Containers:** `Dockerfile*`, `docker-compose*.yml`, `**/k8s/**/*.yaml`
- **OTel:** `**/otel*.yaml`, `**/opentelemetry*.yaml`

Check top-level directory layout for microservice names (e.g., `services/payments/`). Extract languages from `Dockerfile`/`package.json`/`requirements.txt` and deployment targets (ECS, EC2, Lambda, EKS).

### Step 2 — Identify AWS Services

Build a deduplicated list via Terraform `resource "aws_<service>"` blocks:

```
resource "aws_ecs_service"         -> ecs
resource "aws_instance"            -> ec2
resource "aws_security_group"      -> ec2 (flag for ingress risk)
resource "aws_s3_bucket"           -> s3
resource "aws_dynamodb_table"      -> dynamodb
resource "aws_sqs_queue"           -> sqs
resource "aws_lambda_function"     -> lambda
resource "aws_sfn_state_machine"   -> step-functions
resource "aws_autoscaling_group"   -> autoscaling
resource "aws_db_instance"         -> rds
resource "aws_iam_role"            -> iam
```

For CDK, search `aws-cdk-lib/aws-<service>` imports. For CloudFormation, search `Type: AWS::<Service>::*`. For Docker, check `ENV` vars (`AWS_DYNAMODB_TABLE`, `SQS_QUEUE_URL`).

### Step 3 — Map to App Builder Templates

Select applicable app definitions (see `references/service-mapping.md` for the full table):

| AWS Service | Template | Tier |
|---|---|---|
| EC2 | `ec2-management-console.json` | 1 |
| ECS | `manage-ecs-tasks.json` | 1 |
| S3 | `explore-s3.json` | 2 |
| Lambda | `lambda-function-manager.json` | 2 |
| Multiple (3+) | `aws-quick-review.json` | 2 |

If both EC2 and ECS are found, recommend both as Tier 1. Full mapping (DynamoDB, SQS, Step Functions, Auto Scaling, future candidates) in `references/service-mapping.md`.

### Step 4 — Identify Risk Patterns

Flag patterns and pair with workflows (see `references/service-mapping.md` for full risk table):

| Pattern | Risk | Workflow |
|---|---|---|
| IAM role/policy with `"*"` resource | Broad permissions | IAM disable user |
| Security group with `0.0.0.0/0` ingress | Open exposure | Revoke ingress |
| ECS service/task definition | Deployment risk | ECS rollback |
| S3 bucket without `block_public_access` | Public access risk | S3 public access block |

Additional patterns (Lambda timeout, RDS public access, CloudTrail logging) are documented in `references/service-mapping.md`.

### Step 5 — Assign Tiers

- **Tier 1 (Foundation):** Action connection (always), primary compute app (EC2/ECS), SRE golden signals dashboard
- **Tier 2 (Operational):** Non-compute app builder apps, risk-pattern workflows, `aws-quick-review.json` if 3+ services
- **Tier 3 (Advanced):** Composite dashboard with embedded apps, multi-step workflow chains, OTel dashboard (if detected), IaC drift detection (if Terraform state found)

Detailed tier assignment criteria are in `references/service-mapping.md`.

---

## Output Report Template

Write the following structure to `datadog-recommendations.md` at the root of the analyzed repo. Replace all `{placeholders}`.

```markdown
# Datadog Resources Recommendations
> Repo: {path} | Generated: {date} | Skill: repo-analyzer v1.1.0

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
- **Condition:** Only include if OTel config files were found in Step 1

### {N}. IaC Drift Detection (if Terraform state detected)
- **Skill to invoke:** `workflow-automation` + `dashboards`
- **Trigger phrase:** "create IaC drift detection workflow and dashboard"
- **Condition:** Only include if `.terraform.tfstate` or remote state config found

---

## Dependency Build Order

```
action-connections (Tier 1 #1)
  |---> {primary compute app} (Tier 1 #2) --> composite dashboard (Tier 3)
  |---> {additional apps}     (Tier 2)     --> composite dashboard (Tier 3)
  \---> {workflow automations} (Tier 2)
dashboards - SRE golden signals (Tier 1 #3, standalone)
```

## Invoke Sequence for Subagents

1. **action-connections skill** -> creates connection, returns connection UUID
2. **app-builder skill** -> deploys Tier 1 + Tier 2 apps using connection UUID, returns app UUIDs
3. **workflow-automation skill** -> creates workflows using connection UUID
4. **dashboards skill** -> creates standalone dashboards; then creates composite dashboard using app UUIDs from step 2
```

---

## Structured Output (JSON)

Produce a machine-parseable `repo-analysis.json` alongside the markdown report.

### Schema

```json
{
  "repo_path": "<analyzed path>",
  "iac_tooling": "<Terraform | CloudFormation | CDK TypeScript>",
  "aws_services": ["<ecs, sqs, iam, s3, ...>"],
  "microservices": ["<service boundaries from directory layout or stack names>"],
  "risk_patterns": [
    {
      "type": "<iam_broad_permissions | open_security_groups | ecs_deployment | iac_drift | s3_public_access | lambda_timeout | rds_public_access | cloudtrail_disabled>",
      "files": ["<files where detected>"]
    }
  ],
  "app_candidates": [
    {
      "template": "<template filename, e.g. manage-ecs-tasks.json>",
      "service": "<matched AWS service name>",
      "tier": 1,
      "short_label": "<PascalCase — see derivation rule below>"
    }
  ],
  "workflow_candidates": [
    {
      "type": "<ecs_rollback | iam_disable_user | revoke_ingress | iac_drift_detection | s3_public_access_block | lambda_timeout_remediation | rds_public_access_remediation | cloudtrail_enable>",
      "risk": "<matched risk pattern type>",
      "trigger": "<security_signal | monitor_alert | scheduled | incident | manual>",
      "tier": 2,
      "short_label": "<PascalCase — see derivation rule below>"
    }
  ]
}
```

### `short_label` Derivation Rule

1. **App candidates:** strip `.json`, strip prefixes (`manage-`, `explore-`) and suffixes (`-manager`, `-console`), PascalCase the remainder.
   - `manage-ecs-tasks.json` -> `EcsTasks` | `explore-s3.json` -> `S3` | `ec2-management-console.json` -> `Ec2Management`
   - `lambda-function-manager.json` -> `LambdaFunction` | `aws-quick-review.json` -> `AwsQuickReview`
2. **Workflow candidates:** PascalCase the workflow type.
   - `ecs_rollback` -> `EcsRollback` | `iam_disable_user` -> `IamDisableUser` | `revoke_ingress` -> `RevokeIngress`

### Population Rules

- `app_candidates` — from Step 3 mapping: for each detected AWS service, include the corresponding template.
- `workflow_candidates` — from Step 4 risk patterns: for each detected risk, include the corresponding workflow type and recommended trigger.
- `tier` values — per Step 5 criteria (1 = foundation, 2 = operational, 3 = advanced).
- Arrays may be empty if no matches are found.

---

## Where to Write the Report

- **Default:** Save `datadog-recommendations.md` and `repo-analysis.json` at the root of the analyzed repo
- **Fallback:** If the repo path is read-only, save to the current working directory
- Always state full output paths in the final response

---

## Additional Resources

- `references/service-mapping.md` — Full AWS service to Datadog resource mapping tables, expanded risk patterns, tier criteria details, workflow trigger types, future template candidates, and service catalog entity type guidance

---

## Cross-Skill Notes

This skill produces the planning artifact; the other four skills execute it.

| Skill | Role | Key Input | Key Output |
|---|---|---|---|
| `action-connections` | Always first; enables AWS actions | AWS account ID, role name | Connection UUID |
| `app-builder` | Deploys management UIs | Connection UUID | App UUIDs |
| `workflow-automation` | Automated remediation | Connection UUID | Workflow UUIDs |
| `dashboards` | Final visualization layer | App UUIDs (for composite) | Dashboard URLs |

**Connection UUID** flows into `app-builder` (as `connectionId`) and `workflow-automation` (as `connectionId` in `connectionEnvs`). **App UUIDs** flow into `dashboards` for composite templates. **Monitor IDs** from `dashboards` can feed back to `workflow-automation` as `monitorTrigger` sources.

---

## Level 3 References

- `../action-connections/SKILL.md` — 5-step connection setup; external ID retrieval; IAM trust policy pattern
- `../app-builder/SKILL.md` — full template list; `transform_app_json_for_api()` transformation; publish flow
- `../workflow-automation/SKILL.md` — all action IDs; ECS rollback walk-through; Terraform `spec_json` pattern
- `../dashboards/SKILL.md` — available dashboard templates; composite dashboard embedding; monitor management
