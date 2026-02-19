# Taco Fiesta - Infrastructure Drift Detection Tool

## Project Overview

**Purpose**: Build a tool that detects drift between infrastructure and configs for CI/CD deployment, using Datadog for observability and showcasing Datadog's cross-app detection capabilities.

**Team**: Hackathon Team 3 (aka Taco Fiesta)

---

## Key Architectural Decisions

### 1. Observability Platform: Datadog
- **Instrumentation**: Using Datadog APIs for comprehensive observability
- **MCP Server**: Leveraging Datadog's official MCP (Model Context Protocol) server
  - Access to logs, traces, and incident context via AI agents
  - Currently in preview/allowlist (team member has employee access)
  - Official documentation: https://docs.datadoghq.com/bits_ai/mcp_server/

### 2. Core Capabilities

#### Drift Detection
- **Continuous Monitoring**: Track configuration drift in live infrastructure environments
- **Policy-Based Evaluation**: Define best practices for reliability, security, cost optimization, and tagging
- **Real-time Alerting**: Proactive detection of configuration issues
- Based on Datadog Infrastructure Management: https://www.datadoghq.com/blog/automate-infrastructure-operations-with-datadog-infrastructure-management/

#### Cross-Application Monitoring
- **Unified Observability**: Correlate across applications, networks, devices, and infrastructure
- **Intelligent Insights**: Datadog's cross-app correlation capabilities
- **Full API Access**: Bring observability to all apps and infrastructure

### 3. Technical Approach

#### Infrastructure Monitoring
- Monitor CI/CD configuration files vs. actual deployed infrastructure
- Detect discrepancies between declared state and live state
- Group and filter drift reports for teams and leadership

#### Integration Points
- **Datadog APIs**: For instrumentation and data collection
- **Datadog MCP Server**: For AI-assisted incident response and troubleshooting
  - Retrieve logs, traces, incident context
  - Root cause analysis capabilities
  - Requires Datadog "Incidents Read" permission

#### Model Drift (Extended Capability)
- Track AI/ML model drift using Datadog's LLM Observability
- Monitor model performance degradation
- Detect toxic or hallucinated content in AI outputs
- Reference: https://uptimerobot.com/knowledge-hub/observability/ai-observability-the-complete-guide/

---

## Research Findings

### Datadog Infrastructure Management
- Continuously evaluates deployed resources for configuration drift
- Built-in grouping and filtering for team-specific views
- Unified platform for detecting drift from best practices

### Datadog MCP Server Status
- **Availability**: Preview/allowlisted access only
- **Features**: Logs, traces, incident context retrieval
- **Use Cases**: Troubleshooting, root cause analysis, incident response
- **Alternative**: Community open-source implementations available on GitHub if needed

### 2026 Trends
- AI observability becoming critical for enterprise deployments
- Cross-platform monitoring and drift detection expanding to ML workloads
- DASH conference (June 9-10, 2026 in NYC) focusing on observability, security, AI

---

## Implementation Status

### Completed
- [x] Research Datadog's infrastructure drift detection capabilities
- [x] Explore existing codebase structure
- [x] Research Datadog MCP server integration
- [x] Design initial architecture
- [x] Set up Datadog MCP server configuration
- [x] Document drift detection engine architecture
- [x] Create DriftGuard branding and UI design
- [x] Define data model and technology stack

### In Progress
- [ ] Create detailed implementation plan

### Pending
- [ ] Set up project structure (Python 3.13, FastAPI, React/Vite)
- [ ] Implement Config Ingestion Service (Terraform, Docker Compose, K8s parsers)
- [ ] Build Drift Detection Engine with Datadog API integration
- [ ] Implement event queue with Redis/RQ
- [ ] Create Web API and dashboard
- [ ] Add remediation workflows (view, one-click, auto)
- [ ] Implement sensitive data redaction
- [ ] Set up Datadog observability (metrics, events, monitors)
- [ ] Build alerting and incident integration
- [ ] Add policy-based evaluation (post-MVP)

---

## Sources & References

### Datadog Documentation
- [Datadog MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server/)
- [Infrastructure Monitoring](https://docs.datadoghq.com/infrastructure/)
- [Automate Infrastructure Operations](https://www.datadoghq.com/blog/automate-infrastructure-operations-with-datadog-infrastructure-management/)
- [Datadog Remote MCP Server Blog](https://www.datadoghq.com/blog/datadog-remote-mcp-server/)

### Integration Examples
- [AWS DevOps Agent with Datadog MCP](https://aws.amazon.com/blogs/devops/accelerate-autonomous-incident-resolutions-using-the-datadog-mcp-server-and-aws-devops-agent-in-preview/)
- [What is Datadog MCP?](https://www.getguru.com/reference/datadog-mcp)

### Community Implementations
- [shelfio/datadog-mcp](https://github.com/shelfio/datadog-mcp)
- [GeLi2001/datadog-mcp-server](https://github.com/GeLi2001/datadog-mcp-server)
- [brukhabtu/datadog-mcp](https://github.com/brukhabtu/datadog-mcp)

### AI Observability
- [AI Observability Complete Guide 2026](https://uptimerobot.com/knowledge-hub/observability/ai-observability-the-complete-guide/)
- [Top 5 AI Agent Observability Platforms 2026](https://o-mega.ai/articles/top-5-ai-agent-observability-platforms-the-ultimate-2026-guide)

---

## Next Steps

1. **MCP Server Setup**: Complete Datadog MCP server configuration and authentication
2. **Project Structure**: Define application architecture and file structure
3. **API Integration**: Implement Datadog API client for metrics and logs
4. **Drift Detection Logic**: Build core comparison and detection algorithms
5. **Cross-App Features**: Implement multi-application correlation and monitoring

---

*Last Updated*: 2026-02-19
*Branch*: taco-fiesta
