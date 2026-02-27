# Conventions

## Skill based architecture

Skills-based architecture: each skill is a lean `SKILL.md` playbook + `examples/*.json`. No Python scripts, no sub-agent configs, no local reference docs. Dynamic doc fetching (Datadog `.md` URLs + Terraform MCP server) replaces stored API docs.

### Skill Structure
```
skill-name/
├── SKILL.md              # Playbook + gotchas + doc fetch URLs
└── examples/             # JSON specs only (where applicable)
    └── *.json
```

Emphasize maintainability and readability over complexity. The goal is to be able to easily add new skills and update existing skills without breaking the system. Avoid unneeded verbosity or repetition.

### Output Formats
- `terraform` — Claude queries Terraform MCP for provider docs + generates `.tf`
- `shell` — Claude executes `curl` + `aws cli` directly via Bash (replaces Python)

### External Doc Sources
- **Datadog docs**: `https://docs.datadoghq.com/api/latest/{product}.md` — fetched at runtime
- **Terraform MCP**: `.mcp.json` at project root with `hashicorp/terraform-mcp-server`

## Key Technical Facts
- Datadog's fixed AWS account ID: `464622532012` (US1/US3/US5/EU1)
- External ID path: `data.attributes.integration.credentials.external_id` via `GET /api/v2/actions/connections/{id}`
- App JSON transform: remove `handle`, replace `__CONNECTION_ID__`, wrap in `{"data": {"type": "appDefinitions", "attributes": {...}}}`
- Workflow `connectionLabel` must exactly match (case-sensitive) label in `connectionEnvs`
- `credentials.type`: `"AWSAssumeRole"` (PascalCase); `integration.type`: `"AWS"` (uppercase); `data.type`: `"workflows"` (plural)
- Software catalog v3 uses camelCase (`serviceURL`); Terraform v2.2 uses kebab-case (`service-url`)

## Diagrams
- Use **Mermaid** for all flow diagrams, dependency chains, phase sequences, and DAGs.
- Use `graph TD` for top-down flows (orchestration phases, analysis pipelines).
- Use `graph LR` for left-right dependency chains (skill dependencies, connection wiring).
- **Exception:** Directory/file tree structures stay as ASCII code blocks — Mermaid has no native tree type.
- Wrap Mermaid blocks in triple-backtick fences: ` ```mermaid `

## General
- Placeholder format: `__PLACEHOLDER_NAME__` (e.g., `__CONNECTION_ID__`, `__APP_ID__`)
- Output artifacts: `dd-onboarding-output/{project}-{YYYYMMDD-HHMMSS}-{repo_id}/`
- TF file naming: `shared_role.tf`, `conn_app_*.tf`, `conn_wf_*.tf`, `app_*.tf`, `wf_*.tf`, `catalog.tf`, `dashboard_*.tf`

## File I/O
- **Never write to `/tmp/` or any path outside the repo.** All intermediate files (temp JSON payloads, transform scripts, staging files) must be written inside the active run directory: `dd-onboarding-output/{run_id}/scratch/`.
- Use `dd-onboarding-output/{run_id}/scratch/` for any ephemeral files needed during a run (e.g. dashboard payloads, transformed JSON before POST). Clean up scratch files are not required — they serve as a debug trail.
- Subagents and skills must never read from or write to `/tmp/`, `$TMPDIR`, or any system temp directory.