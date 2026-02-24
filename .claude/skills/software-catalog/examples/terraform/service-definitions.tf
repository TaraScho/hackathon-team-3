# Datadog Service Catalog — Terraform v2.2 pattern
#
# Uses datadog_service_definition with schema-version "v2.2".
# Note: Terraform uses v2.2 YAML-style schema; POST /api/v2/catalog/entity
# uses v3 JSON — both populate the same catalog.
#
# v2.2 adds: application (grouping), OpsGenie region, ci-pipeline-fingerprints, extensions.
# v2.2 integrations use kebab-case (service-url) unlike v3 (camelCase serviceURL).

resource "datadog_service_definition" "island_mail" {
  service_definition = jsonencode({
    schema-version = "v2.2"
    dd-service      = "island-mail"
    team            = "backend-services-team"
    application     = "techstories-platform"   # logical grouping (v2.2+)
    description     = "Private messaging service for premium users"
    tier            = "High"
    lifecycle       = "production"
    type            = "web"                     # web | db | cache | function | browser | mobile | custom
    languages       = ["python"]
    contacts = [
      {type = "email", name = "Island Mail Support", contact = "support@example.com"},
      {type = "slack", name = "Oncall", contact = "https://my-org.slack.com/archives/C123"}
    ]
    links = [
      {name = "Repository", type = "repo",    url = "https://github.com/my-org/my-repo"},
      {name = "Runbook",    type = "runbook", url = "https://wiki.example.com/runbooks/island-mail"}
    ]
    tags = ["env:production", "team:backend-services-team"]
    integrations = {
      pagerduty = {service-url = "https://my-org.pagerduty.com/service-directory/P123"}
      opsgenie  = {service-url = "https://my-org.opsgenie.com/service/abc", region = "US"}
    }
    extensions = {cost-center = "eng-1234", compliance = "SOC2"}
  })
}

# Bulk pattern using for_each
locals {
  services = {
    "island-mail"       = {team = "backend-services-team", app = "techstories-platform", desc = "Private messaging"}
    "quotes-api"        = {team = "frontend-team",         app = "techstories-platform", desc = "Quotes microservice"}
    "parrot-translator" = {team = "backend-services-team", app = "techstories-platform", desc = "Language translation"}
  }
}

resource "datadog_service_definition" "all" {
  for_each = local.services

  service_definition = jsonencode({
    schema-version = "v2.2"
    dd-service      = each.key
    team            = each.value.team
    application     = each.value.app
    description     = each.value.desc
    lifecycle       = "production"
  })
}
