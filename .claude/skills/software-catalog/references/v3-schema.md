# v3 Entity Schema Reference

Complete reference for the Datadog Software Catalog v3 entity schema. Covers all 8 entity kinds, metadata structure, spec fields per kind, integrations, the datadog block, and extensions.

Official schema source: `https://github.com/DataDog/schema/tree/main/software-catalog/v3`

---

## Top-Level Structure

Every v3 entity follows the same top-level shape:

```yaml
apiVersion: v3          # always "v3"
kind: <kind>            # one of: service, system, datastore, queue, api, frontend, library, custom
metadata: { ... }       # identity, ownership, contacts, links, tags
spec: { ... }           # kind-specific fields
integrations: { ... }   # optional PagerDuty/OpsGenie
datadog: { ... }        # optional code locations, events, logs, pipelines, performance data
extensions: { ... }     # optional free-form custom metadata
```

---

## EntityV3Metadata (All Kinds)

```yaml
metadata:
  name: my-entity               # REQUIRED. Kebab-case. Used as entity ref (e.g., service:my-entity)
  displayName: My Entity        # Optional human-readable name
  namespace: default            # Optional namespace for multi-tenant orgs (default: "default")
  owner: my-team                # REQUIRED. Datadog team handle (case-sensitive, must exist)
  description: "..."            # Optional text description

  contacts:                     # Optional list of contact channels
    - type: email               # email | slack | microsoft-teams
      name: "Support inbox"
      contact: "support@example.com"
    - type: slack
      name: "#my-service-alerts"
      contact: "https://my-org.slack.com/archives/C123ABC"

  links:                        # Optional list of related links
    - name: Repository
      type: repo                # repo | runbook | doc | dashboard | other
      url: "https://github.com/my-org/my-repo"
      provider: github          # Optional hint for UI icon

  tags:                         # Optional Datadog tags
    - "env:production"
    - "region:us-east-1"

  inheritFrom: service:base-service   # Optional. Inherit metadata fields from another entity ref

  additionalOwners:             # Optional. Declare multiple ownership for cross-team services
    - name: sre-team
      type: team                # team | operator
    - name: platform-team
      type: operator
      managed: true             # Optional boolean. If true, team manages but does not own the entity
```

### Key Metadata Notes

- `name` must be unique within its kind+namespace. Kebab-case is enforced (no uppercase, no spaces).
- `owner` must reference an existing Datadog team handle. If the team does not exist, the entity POST returns a `400`.
- `inheritFrom` lets you define a base entity (e.g., `service:base-service`) with shared metadata and have other entities inherit contacts, links, and tags from it.
- `additionalOwners` enables multi-ownership patterns: the primary `owner` field is still required, but additional teams can be listed with `type` and optional `managed` flag.

---

## Spec Fields Per Kind

### service

```yaml
spec:
  lifecycle: production         # production | staging | experimental | deprecated | sandbox
  tier: "High"                  # Free-form string (no enforced enum). Common: "High", "critical", "1"
  type: web                     # web | grpc | http | rest | graphql | worker | background | cron
  languages:
    - python
    - go
  dependsOn:                    # Outbound dependencies (entity refs)
    - service:auth-service
    - datastore:postgres-main
    - queue:payment-queue
  componentOf:                  # Parent systems this service belongs to
    - system:payments-platform
```

### system

```yaml
spec:
  lifecycle: production
  tier: "High"
  components:                   # Entity refs of entities belonging to this system
    - service:order-service
    - service:payment-service
    - datastore:orders-db
    - queue:order-events
```

### datastore

```yaml
spec:
  lifecycle: production
  tier: "High"
  type: postgres                # postgres | mysql | redis | cassandra | mongodb | dynamodb | elasticsearch
  dependencyOf:                 # Reverse direction: which services depend on this datastore
    - service:order-service
```

### queue

```yaml
spec:
  lifecycle: production
  tier: "Medium"
  type: kafka                   # kafka | rabbitmq | sqs | sns | kinesis
  dependencyOf:
    - service:order-processor
```

### api

```yaml
spec:
  lifecycle: production
  tier: "High"
  type: openapi                 # openapi | grpc | graphql | soap
  interface:
    fileRef: "https://github.com/my-org/my-repo/blob/main/openapi.yaml"   # URI to spec file
    # OR inline definition:
    # definition: |
    #   openapi: "3.0.0"
    #   ...
  implementedBy:                # Which service(s) implement this API
    - service:order-service
```

### frontend

```yaml
spec:
  lifecycle: production
  tier: "High"
  type: web-app                 # web-app | mobile-app | desktop-app
  languages:
    - typescript
    - javascript
  dependsOn:
    - api:orders-api
    - service:auth-service
  componentOf:
    - system:customer-portal
```

### library

```yaml
spec:
  lifecycle: production
  tier: "Medium"
  type: library                 # library | sdk | module | package
  languages:
    - python
  dependencyOf:                 # Which services consume this library
    - service:order-service
    - service:payment-service
```

### custom

The `custom` kind allows registering any entity type not covered by the built-in kinds. It uses the `spec` block freely.

```yaml
apiVersion: v3
kind: custom
metadata:
  name: ml-model-fraud-detection
  owner: ml-team
  description: "Fraud detection ML model"
  tags:
    - "domain:fraud"
spec:
  lifecycle: production
  tier: "High"
  type: ml-model
  framework: pytorch
  version: "2.1.0"
  dependsOn:
    - datastore:feature-store
    - service:model-serving
```

---

## Integrations Block

The integrations block connects the catalog entity to external incident management tools. In v3, all keys use **camelCase** (unlike v2.2 which uses kebab-case).

```yaml
integrations:
  pagerduty:
    serviceURL: "https://my-org.pagerduty.com/service-directory/P123ABC"  # camelCase!
  opsgenie:
    serviceURL: "https://my-org.opsgenie.com/service/abc-123-def"         # camelCase!
    region: US                  # US | EU
```

**v3 vs v2.2 key difference:** v3 uses `serviceURL`, v2.2 uses `service-url`. Do not mix them.

---

## Datadog Block

The `datadog` block provides first-class integration with Datadog features. All fields are optional.

```yaml
datadog:
  codeLocations:                # Link entity to source code
    - repositoryURL: "https://github.com/my-org/my-repo"
      paths:
        - "services/my_service/**"
        - "libs/shared/**"

  events:                       # Associate entity with event sources
    - name: deployment
      query: "source:github tags:service:my-service"

  logs:                         # Define log pipelines associated with this entity
    - name: app-logs
      query: "service:my-service"
      source: python

  pipelines:                    # CI/CD pipeline associations
    fingerprints:
      - fp-abc123

  performanceData:              # Link to APM/tracing data
    tags:
      - "service:my-service"
      - "env:production"
```

### Code Locations Notes

- `codeLocations` is the v3 first-class way to link an entity to source code. It replaces the legacy `code_location:<glob>` tag from v2.x.
- `repositoryURL` must match a repository connected to Datadog via the GitHub or GitLab integration.
- `paths` supports glob patterns relative to the repository root.

---

## Extensions Block

The `extensions` block is a free-form object for custom metadata. Datadog does not use or validate its contents. It will not affect any Datadog features, dashboards, or alerts.

```yaml
extensions:
  cost-center: "eng-1234"
  compliance: "SOC2"
  runbook-tier: "P1"
  team-slack: "#my-team"
  custom:
    deployment-strategy: "blue-green"
    max-replicas: 10
```

---

## Full YAML Examples

### Service

```yaml
apiVersion: v3
kind: service
metadata:
  name: order-service
  displayName: Order Service
  owner: commerce-team
  description: "Handles order creation, updates, and fulfillment"
  contacts:
    - type: email
      name: "Commerce Support"
      contact: "commerce@example.com"
    - type: slack
      name: "#commerce-alerts"
      contact: "https://org.slack.com/archives/C999"
  links:
    - name: Repository
      type: repo
      url: "https://github.com/my-org/order-service"
    - name: Runbook
      type: runbook
      url: "https://wiki.example.com/order-service-runbook"
  tags:
    - "env:production"
    - "region:us-east-1"
  additionalOwners:
    - name: sre-team
      type: operator
spec:
  lifecycle: production
  tier: "High"
  type: web
  languages:
    - python
  dependsOn:
    - service:auth-service
    - datastore:orders-db
    - queue:order-events
  componentOf:
    - system:commerce-platform
integrations:
  pagerduty:
    serviceURL: "https://my-org.pagerduty.com/service-directory/P123"
datadog:
  codeLocations:
    - repositoryURL: "https://github.com/my-org/order-service"
      paths:
        - "src/**"
  performanceData:
    tags:
      - "service:order-service"
extensions:
  cost-center: "eng-commerce"
```

### System

```yaml
apiVersion: v3
kind: system
metadata:
  name: commerce-platform
  owner: commerce-team
  description: "End-to-end commerce platform including ordering, payment, and fulfillment"
  tags:
    - "domain:commerce"
spec:
  lifecycle: production
  tier: "High"
  components:
    - service:order-service
    - service:payment-service
    - service:fulfillment-service
    - datastore:orders-db
    - queue:order-events
```

### Datastore

```yaml
apiVersion: v3
kind: datastore
metadata:
  name: orders-db
  owner: platform-team
  description: "Primary PostgreSQL database for order data"
  tags:
    - "env:production"
spec:
  lifecycle: production
  tier: "High"
  type: postgres
  dependencyOf:
    - service:order-service
    - service:fulfillment-service
```

### Queue

```yaml
apiVersion: v3
kind: queue
metadata:
  name: order-events
  owner: platform-team
  description: "Kafka topic for order lifecycle events"
  tags:
    - "env:production"
spec:
  lifecycle: production
  tier: "High"
  type: kafka
  dependencyOf:
    - service:order-service
    - service:order-processor
```

### API

```yaml
apiVersion: v3
kind: api
metadata:
  name: orders-api
  owner: commerce-team
  description: "Public-facing Orders REST API"
  links:
    - name: API Docs
      type: doc
      url: "https://docs.example.com/orders-api"
spec:
  lifecycle: production
  tier: "High"
  type: openapi
  interface:
    fileRef: "https://github.com/my-org/order-service/blob/main/openapi.yaml"
  implementedBy:
    - service:order-service
```

### Frontend

```yaml
apiVersion: v3
kind: frontend
metadata:
  name: storefront-web
  owner: frontend-team
  description: "Customer-facing storefront web application"
  tags:
    - "env:production"
spec:
  lifecycle: production
  tier: "High"
  type: web-app
  languages:
    - typescript
  dependsOn:
    - api:orders-api
    - service:auth-service
  componentOf:
    - system:customer-portal
datadog:
  codeLocations:
    - repositoryURL: "https://github.com/my-org/storefront-web"
      paths:
        - "src/**"
```

### Library

```yaml
apiVersion: v3
kind: library
metadata:
  name: auth-sdk
  owner: platform-team
  description: "Shared authentication SDK used by all backend services"
  tags:
    - "language:python"
spec:
  lifecycle: production
  tier: "Medium"
  type: library
  languages:
    - python
  dependencyOf:
    - service:order-service
    - service:payment-service
    - service:fulfillment-service
datadog:
  codeLocations:
    - repositoryURL: "https://github.com/my-org/auth-sdk"
      paths:
        - "src/**"
```

### Custom

```yaml
apiVersion: v3
kind: custom
metadata:
  name: fraud-model-v2
  owner: ml-team
  description: "Production fraud detection ML model"
  contacts:
    - type: slack
      name: "#ml-oncall"
      contact: "https://org.slack.com/archives/C456"
  tags:
    - "domain:fraud"
    - "env:production"
spec:
  lifecycle: production
  tier: "High"
  type: ml-model
  framework: pytorch
  version: "2.1.0"
  dependsOn:
    - datastore:feature-store
    - service:model-serving
extensions:
  model-registry: "https://mlflow.internal/models/fraud-v2"
  training-cadence: weekly
```
