# Rearchitecture Plan: Lean Skills + Dynamic Doc Fetching

## Guiding Principle

**Simple, modular, repeatable.** Every design decision should be evaluated against this standard:
- **Simple** — fewer moving parts, no indirection layers that don't earn their keep, no scaffolding for hypothetical future needs
- **Modular** — skills are self-contained units that work independently or compose; no hidden dependencies between skills
- **Repeatable** — any skill invoked on any repo should produce consistent, predictable results without manual setup

When in doubt, remove rather than add. Complexity is a liability.

---

## Overview

Two output paths, no Python (except `extract_action_catalog.py`):
1. **Terraform repos** → Claude uses Terraform MCP server for provider docs + executes `terraform` commands
2. **Non-Terraform repos** → Claude executes `curl` + `aws cli` directly. No scripts generated.

The skill IS the deployment playbook. JSON resource definitions are the content layer. API + provider docs are fetched at runtime from authoritative external sources — not stored locally.

---

## Target Architecture

### Ideal Skill Structure
```
skill-name/
├── SKILL.md              # Playbook + gotchas + doc fetch URLs
└── examples/             # JSON specs (where applicable)
    └── *.json
```

No `references/` directory. No `.tf` examples. No Python.

### External Doc Sources (Project-Level)
1. **Datadog docs via `.md` URLs** — API refs are full-featured (schemas, curl, 6-language examples).
   - API pattern: `https://docs.datadoghq.com/api/latest/{product}.md`
   - Product pattern: `https://docs.datadoghq.com/actions/app_builder/{page}.md`
2. **Terraform MCP server** — Provides real-time Datadog provider resource docs via `search_providers` + `get_provider_details` tools.
   - Config: `.mcp.json` at project root

### What Stays Local (Proprietary Content)
- **SKILL.md playbooks** — Workflow steps, gotchas not in official docs, decision logic
- **JSON example specs** — App definitions, workflow specs, dashboard templates, service entities
- **Action catalog** (`shared/actions-by-service/`, 129 files) — Extracted from dd-source, not available via llms.txt
- **Service mapping** (`repo-analyzer/references/service-mapping.md`) — Proprietary AWS→Datadog mapping

---

## Per-Skill Content Audit

### action-connections
- **SKILL.md keeps**: 6-step flow, external ID path gotcha, fixed account ID `464622532012`, `AWSAssumeRole` PascalCase, `"workflows"` plural
- **JSON examples**: None (procedural, not template-based)
- **Doc fetch URLs**: `api/latest/action-connection.md`, TF MCP → `datadog_action_connection`
- **Delete**: `examples/python/`, `examples/terraform/`, `references/api-reference.md`, `references/advanced-patterns.md`

### app-builder
- **SKILL.md keeps**: Create→Restrict→Publish flow, JSON transform gotchas (remove `handle`, replace `__CONNECTION_ID__`, wrap in API envelope), connection wiring
- **JSON examples**: 9 app definitions (move from `examples/python/app-definitions/` → `examples/app-definitions/`)
- **Doc fetch URLs**: `api/latest/app-builder.md`, product pages (components, queries, events, expressions), TF MCP → `datadog_app_builder_app`
- **Delete**: `examples/python/app_builder_helpers.py`, `examples/terraform/`, `examples/html-js/`, `references/` (4 files)

### workflow-automation
- **SKILL.md keeps**: Spec authoring + submission flow, `connectionLabel` case-sensitivity gotcha, wrapped format requirement, `connectionEnvs` structure
- **JSON examples**: 6 workflow specs (standardize placeholders + wrap format)
- **Doc fetch URLs**: `api/latest/workflow-automation.md`, product pages (triggers, build, actions, expressions), TF MCP → `datadog_workflow_automation`
- **Delete**: `examples/terraform/` (7 files), `references/` (4 files)

### dashboards
- **SKILL.md keeps**: JSON POST flow, composite pattern (app ID substitution), jq substitution gotcha
- **JSON examples**: 7 dashboard templates
- **Doc fetch URLs**: `api/latest/dashboards.md`, product pages (template variables, guides), TF MCP → `datadog_dashboard_json`
- **Delete**: `examples/python/`, `examples/terraform/` (5 files), `references/` (3 files)

### software-catalog
- **SKILL.md keeps**: Teams-first ordering, v3 schema gotchas (camelCase fields), entity kinds, `componentOf`/`dependsOn`
- **Examples**: `services.yaml` (converted from `service_data.py`)
- **Doc fetch URLs**: `api/latest/software-catalog.md`, product pages (entity model, setup), TF MCP → `datadog_software_catalog`
- **Delete**: `examples/python/` (3 files), `examples/terraform/`, `references/` (3 files)

### repo-analyzer
- **SKILL.md keeps**: Scan + recommend flow, format derivation (`terraform` | `shell`), infrastructure criticality framing (replaces risk/security framing — the question is "what is most critical to monitor in this project" not "what are the security risks")
- **Local references**: `service-mapping.md` (proprietary, stays)
- **Doc fetch URLs**: None needed (reads-only, no API calls)
- **Delete**: `references/onboard-repository-dry-run-reference.md`

---

## Task Breakdown

### Track A: JSON Content Cleanup

#### A1. Standardize placeholder syntax across all JSON definitions
**Files:** ~15 JSON files across 3 skill directories
**What:** Replace inconsistent placeholders with `__PLACEHOLDER_NAME__` pattern
- App Builder: `"REPLACE_WITH_CONNECTION_ID"` → `__CONNECTION_ID__`
- Dashboards: `"APP_ID_PLACEHOLDER"` / `"APP_ID_ECS"` → `__APP_ID_ECS_TASKS__` etc.
- Workflows: hardcoded UUIDs → `__CONNECTION_ID__`
**Locations:**
- `.claude/skills/app-builder/examples/python/app-definitions/*.json` (9 files)
- `.claude/skills/dashboards/examples/json/techstories-dashboard-demo.json`
- `.claude/skills/dashboards/examples/json/techstories-dashboard-full.json`
- `.claude/skills/workflow-automation/examples/json/*.json` (6 files)

#### A2. Standardize workflow spec format to wrapped format
**Files:** 3 legacy-format workflow specs
**What:** Migrate bare specs to wrapped format: `{ "name": "...", "spec": { "triggers": [...], "steps": [...], "connectionEnvs": [...] } }`
**Files to convert:**
- `.claude/skills/workflow-automation/examples/json/AWS-IAM-Disable-User.json`
- `.claude/skills/workflow-automation/examples/json/AWS-EC2-Require-IMDS-v2_spec.json`
- `.claude/skills/workflow-automation/examples/json/AWS-IAM-Revoke-Permissions.json`

#### A3. Move app definitions to format-agnostic location
**What:** Move from `examples/python/app-definitions/` → `examples/app-definitions/` (they're JSON, not Python)
**From:** `.claude/skills/app-builder/examples/python/app-definitions/`
**To:** `.claude/skills/app-builder/examples/app-definitions/`
**Also update:** Any SKILL.md or reference file paths that reference the old location

#### A4. Convert `service_data.py` → `services.yaml`
**What:** Static service metadata should be a config file, not Python code
**From:** `.claude/skills/software-catalog/examples/python/service_data.py`
**To:** `.claude/skills/software-catalog/examples/services.yaml`

---

### Track B: Delete Non-Proprietary Content

#### B1. Delete Python files from skills
**Files:**
- `.claude/skills/action-connections/examples/python/` (entire dir)
- `.claude/skills/app-builder/examples/python/app_builder_helpers.py`
- `.claude/skills/dashboards/examples/python/` (entire dir)
- `.claude/skills/software-catalog/examples/python/` (entire dir — after A4 converts service_data.py)
- `.claude/skills/shared/iam_permissions.py`

#### B2. Delete Terraform example files from skills
**Directories:**
- `.claude/skills/action-connections/examples/terraform/` (entire dir)
- `.claude/skills/app-builder/examples/terraform/` (entire dir)
- `.claude/skills/workflow-automation/examples/terraform/` (entire dir)
- `.claude/skills/dashboards/examples/terraform/` (entire dir)
- `.claude/skills/software-catalog/examples/terraform/` (entire dir)

#### B3. Delete hand-written references/ directories
**What:** Audit each file for genuine gotchas not covered by official docs → merge anything worth keeping into the corresponding SKILL.md → then delete the file.
**Directories:**
- `.claude/skills/action-connections/references/` (api-reference.md, advanced-patterns.md)
- `.claude/skills/app-builder/references/` (4 files)
- `.claude/skills/dashboards/references/` (3 files)
- `.claude/skills/workflow-automation/references/` (4 files)
- `.claude/skills/software-catalog/references/` (3 files)
- `.claude/skills/repo-analyzer/references/onboard-repository-dry-run-reference.md` (keep `service-mapping.md`)

#### B4. Delete html-js examples
- `.claude/skills/app-builder/examples/html-js/` (entire dir)

#### B5. Delete generated Python deployment scripts
- `datadog-resources/python/` (entire directory — generated output, not source)

#### B6. Delete scripts/testing/ directory
- `scripts/testing/` (entire directory including setup_wizard.py, dd_cleanup.py, dd_verify.py, lib/, generated/)

#### B7. Delete cleanup_stickerlandia.py
- Find and delete `cleanup_stickerlandia.py` wherever it lives

#### B8. Clean up empty directories
- Remove any empty `examples/python/`, `examples/terraform/`, `references/` dirs after B1–B7

---

### Track C: Add Terraform MCP Server

#### C1. Create `.mcp.json` at project root
```json
{
  "mcpServers": {
    "terraform": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "hashicorp/terraform-mcp-server"]
    }
  }
}
```

---

### Track D: Rewrite SKILL.md Files

Each SKILL.md gets rewritten with this structure:
1. Frontmatter (name, description, metadata)
2. Overview (what this skill does)
3. **Doc Fetch URLs** (new section — tells agent what to WebFetch/MCP-query before acting)
4. Output Format Selection (`terraform` via TF MCP | `shell` via curl+aws cli)
5. Core Workflow (step-by-step playbook)
6. Gotchas & Patterns (hard-won lessons only — audited from existing references/)
7. JSON Examples (what's in examples/ and how to use them)

#### D1. action-connections/SKILL.md
- Replace Python workflow with explicit `curl` + `aws cli` commands Claude executes directly
- Add Doc Fetch URLs section
- Merge genuine gotchas from references/ (external ID path, fixed account ID, PascalCase quirks)

Key commands:
- `aws iam create-role` / `aws iam get-role`
- `curl -X POST .../api/v2/actions/connections`
- `curl .../api/v2/connection/custom_connections/{id}` (for external ID)
- `aws iam update-assume-role-policy`
- `aws iam put-role-policy`
- `curl -X POST .../api/v2/restriction_policy/connection:{id}`

#### D2. app-builder/SKILL.md
- Document `jq` transformation pattern + `curl` API calls
- Add Doc Fetch URLs section (API + components + queries + events + expressions pages)
- Merge genuine gotchas from references/

Key commands:
- `jq` to transform app JSON (remove `handle`, replace `__CONNECTION_ID__`, wrap in API envelope)
- `curl -X POST .../api/v2/app-builder/apps`
- `curl -X POST .../api/v2/restriction_policy/app-builder-app:{id}`
- `curl -X POST .../api/v2/app-builder/apps/{id}/deployment`

#### D3. workflow-automation/SKILL.md
- Document workflow spec submission via `curl`
- Add Doc Fetch URLs section (API + triggers + build + actions pages)
- Merge genuine gotchas from references/

Key commands:
- `curl -X POST .../api/v2/workflows` with spec envelope
- `connectionLabel` must exactly match `connectionEnvs[].connections[].label` (case-sensitive)

#### D4. dashboards/SKILL.md
- Document curl dashboard POST + jq substitution
- Add Doc Fetch URLs section (API + template variables + guides)
- Merge genuine gotchas from references/

Key commands:
- `curl -X POST .../api/v1/dashboard -d @dashboard.json`
- `jq` for app ID placeholder substitution in composite dashboards
- `curl -X POST .../api/v1/monitor` for monitor creation

#### D5. software-catalog/SKILL.md
- Document team creation + entity upsert via `curl`
- Add Doc Fetch URLs section (API + entity model + setup pages)
- Merge genuine gotchas from references/

Key commands:
- `curl -X POST .../api/v2/team`
- `curl -X POST .../api/v2/catalog/entity` (v3 JSON, camelCase fields)

#### D6. repo-analyzer/SKILL.md
- Change format derivation: `preferred_output_format: python` → `preferred_output_format: shell`
- Logic: Terraform detected → `terraform`; CloudFormation/CDK/other → `shell`
- Replace "risk/security" framing with "infrastructure criticality" framing throughout
  - Old: tiers based on security risk (overly permissive IAM, exposed ports, etc.)
  - New: prioritization based on what AWS services are most critical to monitor for this project's operations
  - The output answers: "what Datadog resources should we build and in what order of importance"
- No Doc Fetch URLs needed (reads-only, no API calls)

#### D7. Update "Output Format Selection" in all 5 product SKILL.md files

| `preferred_output_format` | What happens |
|---|---|
| `terraform` | Claude queries Terraform MCP for provider docs + generates `.tf` modules in `datadog-resources/terraform/` |
| `shell` | Claude executes `curl` + `aws cli` commands directly via Bash tool |

---

### Track E: Remove Sub-Agents + Simplify Orchestration

#### E1. Delete all agent config files
**What:** The `.claude/agents/` directory and all its contents are deleted. Sub-agent spawning behavior is delegated to the orchestrating Claude Code agent, which reads SKILL.md files directly via the Read tool and spawns sub-agents as it sees fit.
**Delete:**
- `.claude/agents/action-connections.md`
- `.claude/agents/app-builder.md`
- `.claude/agents/dashboards.md`
- `.claude/agents/software-catalog.md`
- `.claude/agents/workflow-automation.md`
- `.claude/agents/onboard-repository-dry-run.md`
- (any other files in `.claude/agents/`)

#### E2. Simplify onboard-repository/SKILL.md
- Remove all references to spawning named sub-agents
- Let app-builder and workflow-automation skills handle their own connections (no separate action-connections spawn)
- The orchestrating agent reads SKILL.md files and decides how to sequence work

#### E3. Add structured Phase 2→3 handoff
- Document `.claude/context/onboarding-uuids.json` as the handoff contract for app/workflow UUIDs → dashboards
```json
{
  "app_ids": { "EcsTasks": "uuid", "S3": "uuid" },
  "workflow_ids": { "IamDisableUser": "uuid", "EcsRollback": "uuid" }
}
```

---

### Track F: Update Dry-Run

#### F1. Update dry-run SKILL.md
**What:** The dry-run produces a **conceptual report** of what would be created — no scripts, no Terraform files, no actual API calls. This works identically for Terraform repos and CloudFormation repos because it's reporting on Datadog resources, not the customer's IaC.

The report answers:
- What Datadog resources would be created (apps, workflows, dashboards, catalog entries, action connections)
- What parameters would be needed (connection IDs, app IDs, team names, etc.)
- What dependencies exist between resources
- What order they'd be created in

Format: structured markdown report with sections per Datadog resource type. No execution, no validation, just a human-readable plan.

Remove all references to: `terraform validate`, `py_compile`, script generation, file creation.

#### F2. Delete dry-run agent config
- `.claude/agents/onboard-repository-dry-run.md` is deleted in E1 above
- The dry-run skill (`onboard-repository-dry-run/SKILL.md`) remains — it's invoked directly by the orchestrating agent

---

### Track G: Cleanup & Verification

#### G1. Grep and remove all Python references from SKILL.md files
`grep -r 'python\|py_compile\|\.py\|pip\|requests\|boto3' .claude/skills/`

#### G2. Delete `.claude/context/README.md`
- This file is no longer needed; the skills are self-documenting

#### G3. Update root `README.md`
- Rewrite to reflect current architecture: skills-based, no Python, no sub-agent configs
- Remove any references to generated scripts, test orchestrator, or Python workflow

#### G4. Update memory files
`/Users/tara.schoenherr/.claude/projects/-Users-tara-schoenherr-repos-hackathon-team-3/memory/MEMORY.md`
- Update to reflect new architecture (shell + Terraform MCP, no Python, no references/ dirs, no .tf examples, no sub-agents)
- Update `preferred_output_format` values: `python` → `shell`

#### G5. Verification checklist
- [ ] `find .claude/skills -name "*.py" -not -path "*/action-catalog-extractor/*"` returns nothing
- [ ] `find .claude/skills -name "*.tf"` returns nothing
- [ ] `find .claude/agents -type f` returns nothing (agents dir empty or gone)
- [ ] No `references/` directories remain (except `repo-analyzer/references/service-mapping.md`)
- [ ] No `examples/python/` directories remain (except action-catalog-extractor)
- [ ] `jq . < file.json` passes for all JSON resource definitions
- [ ] All placeholders use `__PLACEHOLDER_NAME__` format
- [ ] `.mcp.json` exists with Terraform MCP config
- [ ] Each of the 5 product SKILL.md files has a "Doc Fetch URLs" section
- [ ] `grep -r 'preferred_output_format.*python' .claude/skills/` returns nothing
- [ ] repo-analyzer output uses "criticality" not "risk" framing
- [ ] Dry-run against stickerlandia produces a conceptual markdown report (no files created, no API calls)
- [ ] Invoke app-builder skill against stickerlandia → Claude fetches docs via WebFetch + MCP → creates app via curl

---

## Dependency Graph

```
A1-A4 (JSON cleanup) ──┐
                        ├─→ D1-D7 (rewrite SKILL.md) ─→ E2-E3 (simplify orchestration)
B1-B8 (delete files) ──┘                               ─→ F1-F2 (dry-run update)
                                                        ─→ G1-G5 (cleanup + verification)
C1 (MCP config) — independent, can run anytime
E1 (delete agents) — independent, can run anytime
```

**Safe to parallelize:**
- Track A + Track B + Track C + E1 (all independent)
- Track D (after Track A — needs standardized placeholders and moved files)
- Track E2-E3 + Track F + Track G (after Track D)

---

## What We're NOT Changing

- The 3-phase orchestration model (analyze → fan-out → aggregate) — it's sound
- The 1:1 connection-to-resource model — it's sound
- The `extract_action_catalog.py` script — stays as Python
- The action catalog (`shared/actions-by-service/`, 129 files) — stays
- The `service-mapping.md` in repo-analyzer — stays (proprietary)
- The JSON resource definitions themselves — content stays, format gets standardized
- The SKILL.md files as the primary knowledge carrier

## What IS Changing

- **No more Python** — skills teach agents to run `curl`/`aws cli` directly
- **No more `.tf` examples** — Terraform MCP provides provider docs at runtime
- **No more hand-written `references/`** — Datadog `.md` URLs provide API + product docs at runtime
- **No more sub-agent configs** — `.claude/agents/` deleted; orchestrating agent reads skills directly and spawns sub-agents as it sees fit
- **Skills become lean** — SKILL.md (playbook + gotchas + doc fetch URLs) + JSON examples only
- **New SKILL.md section** — "Doc Fetch URLs" tells agents where to get docs dynamically
- **New infrastructure** — `.mcp.json` with Terraform MCP server at project root
- **Output format vocabulary** — `python` → `shell` everywhere (`preferred_output_format: shell`)
- **Dry-run = conceptual report** — markdown preview of what would be created, no files generated, works for any IaC flavor
- **Repo-analyzer framing** — "infrastructure criticality" replaces "security risk" — focus on what to monitor, not what's dangerous
- **`cleanup_stickerlandia.py` deleted** — no longer needed
- **`.claude/context/README.md` deleted** — no longer needed
- **Root `README.md` updated** — reflects current architecture
