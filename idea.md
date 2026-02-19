# Terraform State Alerting — Research & Build Plan

> Next steps for setting up drift detection and state change alerts using GitHub Actions and Datadog.

---

## Option 1: GitHub Actions — Drift Detection on a Schedule

The core trick is `terraform plan -detailed-exitcode`. It returns:
- **Exit 0** = no changes (state matches reality)
- **Exit 1** = error
- **Exit 2** = drift detected (changes needed)

A scheduled workflow that runs `plan`, checks that exit code, and creates a GitHub Issue or Slack alert when it hits `2`:

```yaml
name: Terraform Drift Detection

on:
  schedule:
    - cron: "0 8 * * *"  # daily at 8 AM UTC
  workflow_dispatch:

jobs:
  drift-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.9.0

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan (drift check)
        id: plan
        run: terraform plan -detailed-exitcode -no-color
        continue-on-error: true

      - name: Create issue on drift
        if: steps.plan.outcome == 'failure' && steps.plan.outputs.exitcode == '2'
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: '⚠️ Terraform drift detected',
              body: 'Scheduled drift check found changes. Run `terraform plan` to review.',
              labels: ['drift', 'infrastructure']
            });
```

### Ready-Made Actions to Evaluate

| Action | What It Does | Link |
|--------|-------------|------|
| dflook/terraform-check | Runs plan, fails the build on drift | https://github.com/dflook/terraform-check |
| cloudposse/atmos-terraform-drift-detection | Creates GitHub Issues per workspace | https://github.com/cloudposse/github-action-atmos-terraform-drift-detection |
| snyk/driftctl | Measures IaC coverage, detects unmanaged resources beyond state drift | https://github.com/snyk/driftctl |

### Research TODOs

- [ ] Decide on schedule frequency (daily, hourly, etc.)
- [ ] Determine which workspaces/environments to monitor
- [ ] Choose between raw `terraform plan` vs a pre-built action
- [ ] Decide alert target: GitHub Issues, Slack webhook, or both
- [ ] Evaluate driftctl for catching unmanaged resources (things created outside Terraform)
- [ ] Set up state backend access (S3 + DynamoDB credentials) for the CI runner

---

## Option 2: Datadog — Metrics + Monitors

### A. Push Custom Metrics from CI Pipeline

After your scheduled `terraform plan`, push a custom metric to Datadog via their API:

```yaml
      - name: Report drift metric to Datadog
        if: always()
        run: |
          DRIFT_STATUS=${{ steps.plan.outputs.exitcode == '2' && '1' || '0' }}
          curl -X POST "https://api.datadoghq.com/api/v1/series" \
            -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "series": [{
                "metric": "terraform.drift.detected",
                "points": [["'"$(date +%s)"'", '"$DRIFT_STATUS"']],
                "type": "gauge",
                "tags": ["env:production", "workspace:default"]
              }]
            }'
```

Then in Datadog, create a **Monitor** that alerts when `terraform.drift.detected >= 1`:

```hcl
resource "datadog_monitor" "terraform_drift" {
  name    = "Terraform Drift Detected"
  type    = "metric alert"
  message = "Drift detected in Terraform state. @slack-infra-alerts @pagerduty"

  query = "max(last_1h):max:terraform.drift.detected{env:production} >= 1"

  monitor_thresholds {
    critical = 1
  }

  notify_no_data    = true
  no_data_timeframe = 1440  # alert if no data for 24h (pipeline didn't run)
}
```

### Research TODOs

- [ ] Store `DD_API_KEY` in GitHub Secrets
- [ ] Decide on metric naming convention (`terraform.drift.*` vs custom namespace)
- [ ] Define tags to slice by (env, workspace, region, team)
- [ ] Build a Datadog dashboard for drift history over time
- [ ] Set up alert routing (@slack, @pagerduty, @email)
- [ ] Consider adding a `terraform.plan.resource_count` gauge for tracking state size

---

### B. HCP Terraform (Terraform Cloud) Native Integration

If you use Terraform Cloud / HCP Terraform, it has built-in **health checks** that run drift detection automatically. HCP exposes drift metrics showing which workspaces have drifted.

Steps:
1. Enable health assessments on your workspaces
2. Use the Datadog Terraform integration to pull those metrics
3. Build monitors and dashboards on top of them

### Research TODOs

- [ ] Check if current Terraform Cloud tier supports health assessments (Plus tier required)
- [ ] Review Datadog's Terraform Cloud integration setup: https://docs.datadoghq.com/integrations/terraform/
- [ ] Evaluate cost of health check runs against workspace count

---

### C. Webhooks for Real-Time Alerts

Use Terraform Cloud run notifications to send webhooks to Datadog on state changes, then build monitors on the incoming events.

### Research TODOs

- [ ] Set up Terraform Cloud notification configuration: https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/notifications
- [ ] Create a Datadog webhook endpoint to receive payloads
- [ ] Map run notification events (started, completed, errored, needs_attention) to Datadog events
- [ ] Build monitors on webhook events for failed applies and drift

---

## Decision Matrix

| Approach | Best For | Complexity | Prerequisites |
|----------|----------|------------|---------------|
| GitHub Actions + Issues | Small teams, GitHub-centric workflows | Low | State backend access from CI |
| GitHub Actions + Datadog metrics | Teams already using Datadog for observability | Medium | DD API key + state backend access |
| HCP Terraform + Datadog integration | Terraform Cloud users who want hands-off drift detection | Low | TFC Plus tier |
| driftctl | Catching unmanaged resources outside of state | Medium | Cloud provider read-only credentials |

---

## Build Order (Suggested)

1. **Start with GitHub Actions drift detection** — lowest barrier, fits existing repo patterns
2. **Add Datadog custom metrics** — once the pipeline works, bolt on the `curl` step
3. **Build the Datadog monitor and dashboard** — alert routing + visibility
4. **Evaluate driftctl** — for catching shadow infrastructure not in state
5. **Explore HCP Terraform health checks** — if/when migrating to Terraform Cloud

---

## Reference Links

- Terrateam: Terraform Drift Detection with GitHub Actions — https://terrateam.io/blog/terraform-drift-detection-github-actions
- Taccoform: Drift Detection with GitHub Actions — https://www.taccoform.com/posts/tfg_p3/
- Firefly: Continuous Drift Detection in CI/CD — https://www.firefly.ai/academy/implementing-continuous-drift-detection-in-ci-cd-pipelines-with-github-actions-workflow
- dflook/terraform-check — https://github.com/dflook/terraform-check
- snyk/driftctl — https://github.com/snyk/driftctl
- Datadog Terraform Integration Docs — https://docs.datadoghq.com/integrations/terraform/
- HashiCorp: Automate Monitoring with Datadog Provider — https://developer.hashicorp.com/terraform/tutorials/applications/datadog-provider
- RapDev: Enhancing Terraform with Datadog Metrics — https://www.rapdev.io/blog/enhancing-terraform-with-datadog-new-metrics-improvements-and-more
- Datadog Webhooks Guide — https://docs.datadoghq.com/developers/guide/calling-on-datadog-s-api-with-the-webhooks-integration/
- Datadog Monitor Terraform Resource — https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/monitor

