# IaC Management with Datadog

Manage, observe, and remediate infrastructure-as-code using Datadog as the control plane — App Builder, Workflow Automation, Software Catalog, and dashboards-as-code.

## Architecture

Skills-based architecture where each Claude Code skill is a self-contained playbook for creating Datadog resources. No Python scripts, no sub-agent configs — skills teach Claude to execute `curl`/`aws cli` directly or generate Terraform via MCP.

### Skill Structure

```
skill-name/
├── SKILL.md              # Playbook + gotchas + doc fetch URLs
└── examples/             # JSON specs (where applicable)
    └── *.json
```

### Skills

| Skill | Purpose |
|---|---|
| `repo-analyzer` | Scan IaC repos → tiered Datadog resource recommendations |
| `action-connections` | Create Datadog Action Connections (AWS IAM trust) |
| `app-builder` | Deploy App Builder apps (9 AWS management templates) |
| `workflow-automation` | Create automated remediation workflows |
| `dashboards` | Create dashboards (7 templates, composite embedding) |
| `software-catalog` | Register teams + service entities in Software Catalog |
| `onboard-repository` | End-to-end orchestration (Phase 1→2→3) |
| `onboard-repository-dry-run` | Conceptual preview of what onboarding would create |
| `action-catalog-extractor` | Extract action definitions from dd-source |

### Output Formats

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP server for provider docs + generates `.tf` modules |
| `shell` | Claude executes `curl` + `aws cli` commands directly via Bash |

### External Doc Sources

- **Datadog docs** via `.md` URLs — fetched at runtime by Claude (API refs, product pages)
- **Terraform MCP server** — provides Datadog provider resource docs via `.mcp.json`

## Orchestration Model

```
[Phase 1] repo-analyzer → recommendations + repo-analysis.json
[Phase 2] parallel fan-out:
  ├─ software-catalog (teams → entities)
  ├─ (action-connections → app-builder) × N apps
  ├─ (action-connections → workflow-automation) × M workflows
[Phase 3] composite dashboard (embeds all app + workflow UUIDs)
```

## Test Projects

| Directory | Contents |
|---|---|
| `test-projects/stickerlandia/` | Microservices CloudFormation templates |
| `test-projects/cfn-simple/` | Simple CloudFormation stack |
| `test-projects/tf-simple/` | Simple Terraform configuration |

## Tech Stack

| Component | Role |
|---|---|
| Terraform | IaC for Datadog resources and AWS infrastructure |
| CloudFormation | AWS-native IaC templates |
| Datadog App Builder | Interactive AWS management UIs |
| Datadog Workflow Automation | Automated remediation pipelines |
| Datadog Dashboards | Observability + embedded app widgets |
| Datadog Software Catalog | Service registry + dependency mapping |
| Datadog Action Connections | Secure AWS credential bridging (assume-role) |
| Terraform MCP Server | Runtime provider docs for Claude |
| Claude Code | AI-assisted development + execution |
