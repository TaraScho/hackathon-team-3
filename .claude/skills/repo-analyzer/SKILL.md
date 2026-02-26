---
name: repo-analyzer
description: >
  Scans a repo's IaC files to produce a tiered Datadog resource recommendations
  report (datadog-recommendations.md + repo-analysis.json). Maps AWS services
  to App Builder templates and infrastructure patterns to Workflow Automations.
  Trigger phrases: "analyze my repo for Datadog", "what Datadog resources should I build",
  "scan my repo", "generate Datadog recommendations", "audit repo for Datadog",
  "Datadog onboarding for my repo", "map AWS services to Datadog".
  Do NOT use to execute recommendations — use action-connections, app-builder,
  workflow-automation, dashboards, or software-catalog to act on them.
metadata:
  author: hackathon-team-3
  tags: [repo-analysis, recommendations, planning, aws, iac, app-builder, workflows, dashboards]
  category: planning
---

# Repo Analyzer Skill

## Overview

Scans a repository's IaC and infrastructure files to detect AWS services, identify microservice boundaries, and map findings to concrete Datadog resources. Outputs a tiered `datadog-recommendations.md` report and a machine-parseable `repo-analysis.json`.

The focus is **infrastructure criticality** — what AWS services are most critical to monitor and manage for this project's operations. The output answers: "what Datadog resources should we build and in what order of importance?"

```
repo (IaC files)
      |
      v
repo-analyzer --> datadog-recommendations.md (human-readable)
              \-> repo-analysis.json         (machine-parseable)
                        |
                        v
              onboard-repository skill
              (executes the plan)
```

---

## When to Use

- Onboarding a new service onto Datadog and unsure where to start
- Deciding which App Builder templates are relevant to a repo's AWS footprint
- Planning which remediation workflows to create based on detected infrastructure patterns
- Generating an actionable queue for skill pipelines or CI/CD automation
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

Check top-level directory layout for microservice names. Extract languages from `Dockerfile`/`package.json`/`requirements.txt` and deployment targets (ECS, EC2, Lambda, EKS).

### Step 1b — Derive Output Format Preference

Based on detected IaC tooling:

| Detected IaC Tooling | `preferred_output_format` | Rationale |
|---|---|---|
| Terraform | `terraform` | Generate `.tf` files using Datadog Terraform provider |
| CloudFormation | `shell` | Execute `curl` + `aws cli` commands directly |
| CDK | `shell` | Execute `curl` + `aws cli` commands directly |
| Unknown / mixed | `shell` | Shell commands are the safe default |

**Edge case — mixed IaC:** Count files for each tooling:
- More `.tf` files → `terraform`
- More CFN/CDK files → `shell`
- Tie → `terraform` (Terraform provider coverage is broader)

See `references/service-mapping.md` for the full derivation table.

### Step 2 — Identify AWS Services

Build a deduplicated list from IaC resource declarations:

```
resource "aws_ecs_service"         -> ecs
resource "aws_instance"            -> ec2
resource "aws_security_group"      -> ec2 (flag for ingress pattern)
resource "aws_s3_bucket"           -> s3
resource "aws_dynamodb_table"      -> dynamodb
resource "aws_sqs_queue"           -> sqs
resource "aws_lambda_function"     -> lambda
resource "aws_sfn_state_machine"   -> step-functions
resource "aws_autoscaling_group"   -> autoscaling
resource "aws_db_instance"         -> rds
resource "aws_iam_role"            -> iam
```

For CDK: search `aws-cdk-lib/aws-<service>` imports. For CloudFormation: search `Type: AWS::<Service>::*`.

### Step 3 — Map to App Builder Templates

Select applicable templates (see `references/service-mapping.md` for full table):

| AWS Service | Template | Tier |
|---|---|---|
| EC2 | `ec2-management-console.json` | 1 |
| ECS | `manage-ecs-tasks.json` | 1 |
| S3 | `explore-s3.json` | 2 |
| Lambda | `lambda-function-manager.json` | 2 |
| Multiple (3+) | `aws-quick-review.json` | 2 |

### Step 4 — Identify Infrastructure Patterns

Flag patterns that indicate operational criticality and pair with workflows:

| Pattern | Criticality | Workflow |
|---|---|---|
| IAM role/policy with `"*"` resource | Broad permissions need governance | IAM disable user |
| Security group with `0.0.0.0/0` ingress | Open exposure needs remediation | Revoke ingress |
| ECS service/task definition | Deployment operations need rollback capability | ECS rollback |
| S3 bucket without `block_public_access` | Data exposure needs access control | S3 public access block |

Additional patterns (Lambda timeout, RDS public access, CloudTrail logging) in `references/service-mapping.md`.

### Step 5 — Assign Tiers

- **Tier 1 (Foundation):** Action connection (always), primary compute app (EC2/ECS), SRE golden signals dashboard
- **Tier 2 (Operational):** Non-compute app builder apps, infrastructure-pattern workflows, `aws-quick-review.json` if 3+ services
- **Tier 3 (Advanced):** Composite dashboard with embedded apps, multi-step workflow chains, OTel dashboard (if detected)

---

## Output Report Template

Write to `datadog-recommendations.md` at the analyzed repo root:

```markdown
# Datadog Resources Recommendations
> Repo: {path} | Generated: {date} | Skill: repo-analyzer

## Findings Summary

- **AWS services detected:** {comma-separated list}
- **Microservices / service directories:** {list}
- **IaC tooling:** {Terraform / CDK / CloudFormation / SAM}
- **Preferred output format:** {terraform | shell}
- **Infrastructure patterns:** {e.g., "broad IAM in iam.tf:12", "open SG in security-groups.tf:34"}
- **OTel detected:** {Yes / No}
- **Terraform state detected:** {Yes / No}

---

## Tier 1: Foundation (Build These First)

### 1. AWS Action Connection
- **Skill:** `action-connections`
- **Why:** Prerequisite for all App Builder apps and Workflow Automations
- **Output:** Connection UUID

### 2. {Primary Compute App}
- **Skill:** `app-builder`
- **Template:** `{ec2-management-console.json | manage-ecs-tasks.json}`
- **Why:** {service} found in {file(s)} — critical compute management
- **Depends on:** Action connection from #1

### 3. SRE Golden Signals Dashboard
- **Skill:** `dashboards`
- **Template:** `dd101-sre-dashboard.json`
- **Why:** Core operational visibility

---

## Tier 2: Operational Tooling

### {N}. {App / Workflow per detected pattern}
...

---

## Tier 3: Advanced Automation

### {N}. Composite Dashboard with Embedded Apps
...
```

---

## Structured Output (JSON)

Produce `repo-analysis.json`:

```json
{
  "repo_path": "<analyzed path>",
  "iac_tooling": "<Terraform | CloudFormation | CDK TypeScript>",
  "preferred_output_format": "<terraform | shell>",
  "aws_services": ["ecs", "sqs", "iam", "s3"],
  "microservices": ["<service boundaries>"],
  "infrastructure_patterns": [
    {
      "type": "<iam_broad_permissions | open_security_groups | ecs_deployment | ...>",
      "files": ["<files where detected>"]
    }
  ],
  "app_candidates": [
    {
      "template": "<template filename>",
      "service": "<AWS service>",
      "tier": 1,
      "short_label": "<PascalCase>"
    }
  ],
  "workflow_candidates": [
    {
      "type": "<ecs_rollback | iam_disable_user | revoke_ingress | ...>",
      "infrastructure_pattern": "<matched pattern type>",
      "trigger": "<security_signal | monitor_alert | scheduled | manual>",
      "tier": 2,
      "short_label": "<PascalCase>"
    }
  ]
}
```

NOTE: The field names are `infrastructure_patterns` and `infrastructure_pattern` — these replaced the legacy field names from earlier versions.

### `short_label` Derivation Rule

1. **Apps:** strip `.json`, strip prefixes/suffixes, PascalCase.
   - `manage-ecs-tasks.json` → `EcsTasks` | `explore-s3.json` → `S3`
2. **Workflows:** PascalCase the type.
   - `ecs_rollback` → `EcsRollback` | `iam_disable_user` → `IamDisableUser`

---

## Where to Write

| Location | File | Purpose |
|---|---|---|
| Analyzed repo root | `{repo_path}/datadog-recommendations.md` | Human report |
| Analyzed repo root | `{repo_path}/repo-analysis.json` | Machine output |
| Well-known handoff | `.claude/context/repo-analysis.json` | Fixed path downstream skills check |

The `.claude/context/` write is always required.

---

## Additional Resources

- `references/service-mapping.md` — Full AWS→Datadog mapping tables, infrastructure pattern details, tier criteria

---

## Cross-Skill Notes

| Skill | Role | Key Input | Key Output |
|---|---|---|---|
| `onboard-repository` | Executes this plan | `repo-analysis.json` | All Datadog resources |
| `action-connections` | Prerequisite per app/workflow | AWS account ID, role name | Connection UUID |
| `app-builder` | Management UIs | Connection UUID | App UUIDs |
| `workflow-automation` | Automated remediation | Connection UUID | Workflow UUIDs |
| `dashboards` | Visualization layer | App UUIDs (composite) | Dashboard URLs |
