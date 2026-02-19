# DriftGuard

**Keep Your Infrastructure in Check**

Infrastructure drift detection tool for DevOps teams, built by Hackathon Team 3 (Taco Fiesta).

---

## What is DriftGuard?

DriftGuard continuously monitors configuration drift between your declared infrastructure configs (Terraform, Docker Compose, Kubernetes) and actual deployed state via Datadog monitoring APIs. It provides:

- **Automatic Drift Detection**: Git-triggered and periodic checks (5-minute intervals)
- **Multi-Tier Remediation**: View details, one-click fixes, or automated remediation with approvals
- **Full Observability**: Native Datadog integration for metrics, events, alerts, and incidents
- **Security-First**: Automatic redaction of secrets and sensitive data
- **Cloud-Agnostic**: Normalized config format works across cloud providers

---

## Quick Start

### Prerequisites
- Python 3.13+
- PostgreSQL
- Redis
- Node.js 18+ (for frontend)
- Datadog account with API access

### Installation
```bash
# Clone the repository
git clone https://github.com/TaraScho/hackathon-team-3.git
cd hackathon-team-3

# Backend setup
cd backend
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Start services (using docker-compose)
docker-compose up -d
```

### Configuration
1. Set up Datadog API credentials in `.env`
2. Configure git repository connections
3. Run database migrations
4. Start the web dashboard

See `docs/plans/` for detailed design documentation.

---

## Architecture

DriftGuard uses an **event-driven architecture** with:

- **Config Ingestion Service**: Parses Terraform, Docker Compose, K8s manifests from git
- **Drift Detection Engine**: Compares expected vs. actual state from Datadog
- **Event Queue (Redis)**: Handles async jobs and scheduling
- **Web Dashboard (React/TypeScript)**: Provides UI with DriftGuard design system
- **Datadog Integration**: Full observability with metrics, events, and alerting

See `docs/plans/2026-02-19-drift-detection-engine-design.md` for complete architecture details.

---

## Documentation

- [Drift Detection Engine Design](docs/plans/2026-02-19-drift-detection-engine-design.md)
- [DriftGuard Branding & UI Design](docs/plans/2026-02-19-driftguard-design.md)
- [Project Overview](claude.md)

---

## Team

**Hackathon Team 3 (Taco Fiesta)**

Datadog Internal Hackathon 2026 
