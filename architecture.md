# Architecture Overview

This project uses Claude Code skills and agents to automate Datadog onboarding for infrastructure repositories. The process is organized into three phases.

---

## Phase 1: Prerequisites

Before onboarding, the following must be in place:

```mermaid
flowchart LR
    AWS["AWS Account"] <-->|Integration| DD["Datadog Org"]
    DD --> API["API Key + APP Key"]
    API --> WF["APP Key registered with\nWorkflow Automation Actions API"]
```

- **AWS ↔ Datadog Integration** — bidirectional trust between your AWS account and Datadog
- **API Key + APP Key** — generated in your Datadog organization
- **Workflow Actions registration** — APP Key must be registered with the Workflow Automation Actions API

---

## Phase 2: Onboarding Your Project

The `onboard-repository` skill orchestrates everything in three stages:

```mermaid
flowchart TD
    subgraph Stage1["1 · Repo Analysis"]
        RA["Repo Analyzer\nscans IaC → recommendations"]
    end

    subgraph Stage2["2 · Parallel Fan-Out"]
        SC["Software Catalog\nregister teams + services"]
        AB["App Builder\ncreate management UIs"]
        WA["Workflow Automation\ncreate remediation workflows"]
        AC1["Action Connection\n(1:1 per app)"]
        AC2["Action Connection\n(1:1 per workflow)"]
        AB --- AC1
        WA --- AC2
    end

    subgraph Stage3["3 · Composite Dashboard"]
        DB["Dashboard\nassembles monitors, apps,\nand workflows into one view"]
    end

    RA --> SC
    RA --> AB
    RA --> WA
    SC --> DB
    AB --> DB
    WA --> DB
```

1. **Repo Analysis** — scans IaC files, identifies services, and produces a tiered recommendation plan
2. **Parallel fan-out** — three skills run concurrently:
   - **Software Catalog** — registers teams and services in Datadog
   - **App Builder** — creates management UIs, each with its own dedicated Action Connection
   - **Workflow Automation** — creates remediation workflows, each with its own dedicated Action Connection
3. **Composite Dashboard** — pulls everything together into a single operational dashboard

---

## Phase 3: Ongoing / Maintenance

> _This phase is planned but not yet implemented._

```mermaid
flowchart LR
    DS["Drift Scanning\n(TBD)"]
    style DS stroke-dasharray: 5 5
```

- **Drift scanning** — detect when deployed resources diverge from IaC definitions
- Additional maintenance workflows to be defined
