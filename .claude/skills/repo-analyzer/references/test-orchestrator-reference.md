# Test Orchestrator Reference

## Manifest Format

After each phase, update `scripts/testing/generated/{run_id}/manifest.json`. The manifest tracks **all** created resources using arrays (multiple of each type):

```json
{
  "run_id": "<run_id>",
  "timestamp": "<ISO 8601 timestamp>",
  "phases": {
    "repo_analysis": {"status": "passed|failed|skipped", "output_files": ["datadog-recommendations.md", "repo-analysis.json"]},
    "selection": {"status": "passed|failed|skipped", "output_file": "selection.json"},
    "apps": {"status": "passed|failed|skipped"},
    "workflows": {"status": "passed|failed|skipped"},
    "dashboard": {"status": "passed|failed|skipped"},
    "service_catalog": {"status": "passed|failed|skipped"},
    "cleanup": {"status": "pending|passed|failed"}
  },
  "iam_roles": [
    {"name": "DatadogAction-TestApp-{short_label}-{run_id}", "source": "app-builder", "app_label": "<short_label>"},
    {"name": "DatadogAction-TestWF-{short_label}-{run_id}", "source": "workflow-automation", "wf_label": "<short_label>"}
  ],
  "connections": [
    {"id": "<uuid>", "name": "TestConn-App-{short_label}-{run_id}"},
    {"id": "<uuid>", "name": "TestConn-WF-{short_label}-{run_id}"}
  ],
  "app_keys": [
    {"id": "<uuid>", "name": "TestKey-App-{short_label}-{run_id}"},
    {"id": "<uuid>", "name": "TestKey-WF-{short_label}-{run_id}"}
  ],
  "apps": [
    {"id": "<uuid>", "name": "TestApp-{short_label}-{run_id}", "template": "<selected template>"}
  ],
  "workflows": [
    {"id": "<uuid>", "name": "TestWF-{short_label}-{run_id}", "type": "<selected workflow type>"}
  ],
  "dashboards": [{"id": "<id>", "name": "TestDash-{run_id}"}],
  "monitors": [{"id": "<id>", "name": "TestMon-CPU-{run_id}"}],
  "teams": [{"id": "<uuid>", "handle": "<team handle>", "name": "<team name>"}],
  "catalog_entities": [{"name": "<entity name>", "kind": "service"}]
}
```

All resource names are populated from Phase 2 `selection.json`, which derives them from Phase 1's `repo-analysis.json`. Arrays contain 2 entries each for apps/workflows/connections/keys/roles (one per selected resource).

---

## Failure Analysis

When a phase or sub-step fails, diagnose the error using these known patterns:

| Error | Likely Cause | Suggested Fix |
|---|---|---|
| 403 on `/api/v2/actions/connections` | App key missing `connections_write` scope | Update action-connections skill scope list |
| 403 on `/api/v2/app-builder/apps` | App key missing `apps_write` scope | Update app-builder skill scope list |
| 400 on app creation with "handle already exists" | JSON transform still contains `handle` field | Update app-builder skill transform logic to strip `handle` |
| 400 on app creation with "invalid payload" | Missing `{"data": {"type": "appDefinitions", "attributes": {...}}}` envelope | Update app-builder skill API envelope docs |
| Connection not ready after 60s | External ID not applied to IAM trust policy | Check action-connections IAM trust policy step |
| 409 on workflow creation | Handle collision | Skill should use unique handles |
| 422 on catalog entity | Team doesn't exist yet | Skill's team-first flow not followed |
| 429 on any endpoint | Rate limited | Add retry with exponential backoff |
| `ConnectionError` or `Timeout` | Network issue or wrong DD_SITE | Check DD_SITE env var |
| 403 on `/api/v2/workflows` | App key missing `workflows_write` scope | Check scoped key creation |
| Multiple apps fail with same IAM error | IAM rate limiting on role creation | Add delay between app builds |
| Connection 1 ready but Connection 2 times out | Trust policy updated for wrong role | Check role name matches connection |
| Phase 1 finds 0 AWS services | Wrong repo path or unsupported IaC format | Verify target repo path exists and contains supported IaC files |
| Phase 2 selects <2 apps or <2 workflows | Not enough candidates from repo analysis | Relax selection to accept fewer candidates, log warning |

For unknown errors: include the full API response body, status code, and the request that caused it. Suggest which section of which skill file likely needs updating.

---

## Partial Runs

The user may request:
- **Test specific phases only:** `"Run just Phase 3 and Phase 5"` — run only those phases, use provided IDs for dependencies.
- **Test a single app or workflow:** `"Test just the <short_label> app"` — run Phase 3 for that one app only.
- **Re-test with existing resources:** `"Re-test dashboard using app IDs abc-123 and def-456"` — skip Phases 1-4, use provided IDs, run only Phase 5.
- **Resume from a failure:** `"Continue from Phase 4, app IDs are abc-123 and def-456"` — skip already-passed phases, use provided IDs for dependencies.
- **Skip repo analysis:** `"Test all skills using <app1> and <app2> apps, <wf1> and <wf2> workflows"` — skip Phases 1-2, use the specified selections directly.

In partial runs, still generate a manifest and report, and still clean up only the resources created in this run.
