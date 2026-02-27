---
name: action-catalog-extractor
description: >-
  Extracts Datadog Workflow Automation action definitions from the dd-source
  repository and generates per-service markdown reference files plus a master
  index. Use when refreshing the shared action catalog that workflow-automation
  and other skills depend on.
---

# Action Catalog Extractor

Parses `manifest.gen.json` files from the `wf-actions-worker` bundles directory in `dd-source`, resolves JSON Schema `$ref` chains for input/output schemas, and produces:

- **Per-service markdown files** (e.g., `aws-ec2.md`, `github-issues.md`) with action FQNs, inputs, outputs, permissions
- **Master index** linking all generated references by category (AWS, GitHub, Datadog Native, Core)

## When to Use

- The shared action catalog at `.claude/skills/shared/actions-by-service/` is stale or missing actions
- A new Datadog service bundle has been added to dd-source and you need its action definitions
- You want to regenerate the catalog from a specific dd-source commit

## Prerequisites

- **Local clone of `dd-source`** — the script reads from its `wf-actions-worker` bundles directory
- **Python 3.10+** — uses `argparse`, `json`, `pathlib` (stdlib only, no pip dependencies)

## Core Workflow

### Step 1 — Locate the bundles directory

The bundles live inside dd-source at a path like:

```
~/repos/dd-source/domains/workflow/apps/wf-actions-worker/bundles/
```

Each subdirectory is a bundle (e.g., `com.datadoghq.aws.ec2/`) containing a `manifest.gen.json`.

### Step 2 — Run the extractor

```bash
python .claude/skills/action-catalog-extractor/examples/python/extract_action_catalog.py \
  --bundles-dir ~/repos/dd-source/domains/workflow/apps/wf-actions-worker/bundles \
  --output-dir .claude/skills/shared/actions-by-service \
  --index-file .claude/skills/shared/action-catalog-index.md \
  --prefixes com.datadoghq.aws,com.datadoghq.github,com.datadoghq.dd,com.datadoghq.core,com.datadoghq.datatransformation \
  --stability stable,beta
```

### Arguments

| Flag | Required | Description |
|------|----------|-------------|
| `--bundles-dir` | Yes | Path to `wf-actions-worker/bundles/` in dd-source |
| `--output-dir` | Yes | Where to write per-service `.md` files |
| `--index-file` | Yes | Path for the master index markdown |
| `--prefixes` | Yes | Comma-separated bundle name prefixes to include |
| `--stability` | No | Stability levels to include (default: `stable,beta`) |

### Step 3 — Verify output

After running, check:
- `--output-dir` has one `.md` file per service (e.g., `aws-ec2.md`, `aws-s3.md`)
- `--index-file` has a categorized table of all bundles with action counts
- The index header shows the dd-source commit hash and generation date

## Output Structure

```
.claude/skills/shared/
├── action-catalog-index.md              # Master index with categories
└── actions-by-service/
    ├── aws-ec2.md                       # Per-service action reference
    ├── aws-s3.md
    ├── aws-lambda.md
    ├── github-issues.md
    ├── dd-monitor.md
    └── ...                              # ~130 files across AWS/GitHub/DD/Core
```

Each per-service file contains:
- Bundle metadata (name, title, link to Datadog action catalog UI)
- Per-action sections with: FQN, title, description, stability, permissions
- Input parameters table (name, type, required, description)
- Output parameters table (name, type, description)

## How the Script Works

1. **Discovery** — walks `--bundles-dir`, matches directories against `--prefixes`
2. **Parsing** — reads each `manifest.gen.json`, extracts `types.$defs` and `actions` maps
3. **Schema resolution** — follows `$ref` chains (up to depth 2) to resolve input/output types
4. **Filtering** — drops actions whose stability level doesn't match `--stability`
5. **Generation** — produces per-service markdown with tables for inputs/outputs
6. **Indexing** — groups bundles by category (AWS, GitHub, Datadog Native, Core) and writes the master index

## Cross-Skill Notes

- **workflow-automation** reads the generated action catalog to look up correct action FQNs and input schemas when authoring workflow specs
- The catalog is a **read-only reference** — it documents what actions exist, it does not create or modify them
- Bundle naming convention: `com.datadoghq.{provider}.{service}` → file slug `{provider}-{service}.md`
