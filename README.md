# IaC Management with Datadog

Manage, observe, and remediate infrastructure-as-code using Datadog as the control plane -- drift detection, security scanning, and automated remediation powered by App Builder, Workflow Automation, and dashboards-as-code.

## Project Goals

- **Hands-on IaC observability** -- prioritize practical experience building drift detection and security pipelines
- **AI-native development** -- structure the codebase for AI agent effectiveness; use Claude Code, Cursor, etc. as primary dev partners
- **Dogfooding Datadog end-to-end** -- dashboards, App Builder, Workflow Automation, monitors as both tools and subjects
- **Boundary exploration** -- push into novel territory; document where it works and where it breaks
- **Failure modes as outcomes** -- treat friction, dead ends, and learnings as first-class deliverables

## Core Workflows

### IaC Drift Detection

Detect configuration drift between declared IaC and actual cloud state, surface findings in Datadog dashboards, and remediate via App Builder apps and Workflow Automation.

**Datadog features:** Dashboards, App Builder, Workflow Automation, Action Connections

### IaC Security

Identify security misconfigurations in IaC templates and running infrastructure, surface findings in dashboards, and trigger automated remediation workflows.

**Datadog features:** Dashboards, Workflow Automation, Monitors

### Monitoring Assets as Code

Deploy Datadog monitors, dashboards, App Builder apps, and workflows via Terraform -- treating observability configuration as version-controlled infrastructure.

**Datadog features:** Terraform provider (`datadog_dashboard_json`, `datadog_monitor`, `datadog_workflow_automation`)

### Remediation from Datadog

Use dashboards as entry points into App Builder apps and Workflow Automation for one-click drift fixes and security remediation.

**Datadog features:** Dashboards (with App Builder widget links), App Builder, Workflow Automation, Action Connections

## Tech Stack

| Component | Role |
|---|---|
| Terraform | IaC for Datadog resources and AWS infrastructure |
| CloudFormation | AWS-native IaC templates |
| Datadog Dashboards | Observability and entry points for remediation |
| Datadog Monitors | Alerting on drift and security findings |
| Datadog App Builder | Interactive remediation UIs |
| Datadog Workflow Automation | Automated remediation pipelines |
| Datadog Action Connections | Secure AWS credential bridging (assume-role) |
| AWS | Cloud infrastructure target |
| Stickerlandia | Microservices demo application (target workload for testing and development) |
| Claude Code / Cursor | AI-assisted development |