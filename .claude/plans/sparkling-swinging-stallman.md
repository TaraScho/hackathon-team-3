# Plan: Synthesize rearchitecture-plan.md

## Context
The current `rearchitecture-plan.md` reflects iteration 1 ("Eliminate Python, Simplify to Terraform + Direct API Execution"). The conversation evolved the plan into iteration 2 ("Lean Skills + Dynamic Doc Fetching"). Need to merge both into one coherent, updated plan file.

## What changed between iterations

| Aspect | Old Plan | New Plan |
|--------|----------|----------|
| References/ dirs | Keep (11 files) | Delete all (except service-mapping.md) — replaced by Datadog `.md` URLs at runtime |
| .tf examples | Track D: Create 5 new TF modules | Delete all — replaced by Terraform MCP server at runtime |
| html-js examples | Not mentioned | Delete |
| Doc fetching | Not mentioned | New: Datadog `.md` URL convention + Terraform MCP server |
| SKILL.md sections | Output Format Selection | Add "Doc Fetch URLs" section |
| Progressive disclosure | Keep pattern | Pattern changes — no more references/ layer |
| Target structure | SKILL.md + references/ + examples/ | SKILL.md + examples/*.json only |
| scripts/testing/ | Already deleted in prior cleanup | Confirm deleted |
| datadog-resources/python/ | Track B2 | Track B5 |

## Approach
Rewrite `rearchitecture-plan.md` keeping the useful concrete details from the old plan (file paths, task specifics) but restructuring around the new architecture. Key sections to add/change:

1. **New title & overview** — "Lean Skills + Dynamic Doc Fetching"
2. **Target Architecture** section — ideal skill structure, external doc sources, what stays local
3. **Per-Skill Content Audit** — what stays/goes for each of the 6 skills
4. **Restructured tracks**: Remove old Track D (TF modules), add Track C (MCP config), expand Track B (delete refs/, .tf, html-js), rename Track D to SKILL.md rewrites with Doc Fetch URLs
5. **Updated dependency graph**
6. **Updated "What's Changing / Not Changing"**

## File to modify
- `/Users/tara.schoenherr/repos/hackathon-team-3/rearchitecture-plan.md`

## Verification
- Final file reflects dynamic doc fetching strategy
- Concrete file paths and task details preserved from old plan
- No references to keeping references/ directories or creating new .tf modules
