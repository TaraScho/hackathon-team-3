"""
Batch registration script for Datadog Software Catalog.

Orchestration order: teams first (idempotent), then service entities (upsert).
Can be run standalone or embedded in a Lambda handler.
"""

import os
from service_data import ALL_SERVICES, get_unique_teams
from service_catalog_helpers import create_team, create_service_entity


def register_all_services(api_key: str, app_key: str) -> dict:
    """
    Full bootstrap: create all teams, then register all service entities.
    Returns a summary dict with counts of successes and failures.
    """
    results = {"teams": {"ok": 0, "fail": 0}, "services": {"ok": 0, "fail": 0}}

    # Step 1: Create teams (idempotent — 409 = already exists)
    for team_handle in get_unique_teams():
        resp = create_team(api_key, app_key, team_handle)
        print(f"  Team: {resp.message}")
        if resp.success:
            results["teams"]["ok"] += 1
        else:
            results["teams"]["fail"] += 1

    # Step 2: Register service entities (upsert — 200/201/202 all = success)
    for service in ALL_SERVICES:
        resp = create_service_entity(api_key, app_key, service)
        print(f"  Service: {resp.message}")
        if resp.success:
            results["services"]["ok"] += 1
        else:
            results["services"]["fail"] += 1

    return results


# --- Lambda integration pattern ---
# def _configure_datadog_catalog(self):
#     api_key = self._get_datadog_api_key()    # from SSM/Secrets Manager
#     app_key = self._get_datadog_app_key()
#     for team_handle in get_unique_teams():
#         create_team(api_key, app_key, team_handle)
#     for service in ALL_SERVICES:
#         create_service_entity(api_key, app_key, service)


if __name__ == "__main__":
    api_key = os.environ["DD_API_KEY"]
    app_key = os.environ["DD_APP_KEY"]
    summary = register_all_services(api_key, app_key)
    print(f"\nSummary: {summary}")
