# `.claude/context/` — Inter-Agent Shared State

This directory holds project-level shared state that downstream agents can read without needing an explicit handoff from an orchestrator.

## Convention

Files here represent the **latest known state** for the current project. They are overwritten on each analysis run (single-repo-at-a-time assumption).

## Files

| File | Written by | Read by | Contents |
|---|---|---|---|
| `repo-analysis.json` | `repo-analyzer` skill | `app-builder`, `workflow-automation`, `dashboards` agents | Latest structured repo analysis: detected AWS services, microservices, risk patterns, app candidates, workflow candidates |

## How It Works

- **repo-analyzer** writes `repo-analysis.json` here (in addition to the analyzed repo root and any run-scoped directory)
- **Downstream agents** check this file if the user does not explicitly specify what to build — they announce what they found before proceeding
- **test-orchestrator** also copies `repo-analysis.json` here after Phase 1 so the well-known path stays current for orchestrated runs

## Lifecycle

Files in this directory are transient session state. They are not committed to version control (add `.claude/context/*.json` to `.gitignore` if needed). The markdown `README.md` is the only file that should be committed.
