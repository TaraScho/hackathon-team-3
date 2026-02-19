# Datadog Dashboards

# Sample Apps KPI Dashboard (from workshop)
# This dashboard provides insights into Datadog Log Management estimated usage metrics
resource "datadog_dashboard_json" "sample_apps_kpi" {
  count = var.create_dashboards ? 1 : 0

  dashboard = file("${path.module}/estimated-usage-dashboard.json")
}
