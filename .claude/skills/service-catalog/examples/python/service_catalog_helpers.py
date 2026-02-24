"""
Datadog Software Catalog helpers — create teams and register service entities.

Functions:
    build_headers()         — Construct Datadog API auth headers
    get_existing_teams()    — List current team handles
    create_team()           — Idempotent team creation (409 = already exists = success)
    create_service_entity() — Upsert a v3 catalog entity via POST /api/v2/catalog/entity
"""

import requests
import time
from dataclasses import dataclass
from typing import Optional, Dict

BASE_URL = "https://api.datadoghq.com"
DEFAULT_TIMEOUT = 10


@dataclass
class DatadogResponse:
    success: bool
    status_code: int
    message: str
    data: Optional[Dict] = None


def build_headers(api_key: str, app_key: str) -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
    }


def get_existing_teams(api_key: str, app_key: str) -> set:
    """Return a set of existing team handles (for skip-if-exists logic)."""
    resp = requests.get(f"{BASE_URL}/api/v2/team",
                        headers=build_headers(api_key, app_key),
                        timeout=DEFAULT_TIMEOUT)
    if resp.status_code == 200:
        return {t["attributes"]["handle"] for t in resp.json().get("data", [])}
    return set()


def create_team(api_key: str, app_key: str, team_handle: str,
                team_name: str = None) -> DatadogResponse:
    """
    Create a Datadog team. Returns success on 201 (created) or 409 (already exists).
    team_name defaults to title-cased team_handle if not provided.
    """
    if not team_name:
        team_name = team_handle.replace("-", " ").title()

    payload = {
        "data": {
            "type": "team",
            "attributes": {"handle": team_handle, "name": team_name}
        }
    }
    resp = requests.post(f"{BASE_URL}/api/v2/team",
                         headers=build_headers(api_key, app_key),
                         json=payload, timeout=DEFAULT_TIMEOUT)

    if resp.status_code == 201:
        return DatadogResponse(True, 201, f"Created team: {team_handle}", resp.json())
    elif resp.status_code == 409:
        return DatadogResponse(True, 409, f"Team already exists: {team_handle}")
    else:
        errors = resp.json().get("errors", [resp.text]) if resp.text else "No details"
        return DatadogResponse(False, resp.status_code,
                               f"Failed to create team {team_handle}: {errors}")


def create_service_entity(api_key: str, app_key: str, service: dict,
                          max_retries: int = 1) -> DatadogResponse:
    """
    Create or update a service entity in the Datadog Software Catalog using v3 schema.

    service dict keys:
        Required: name, description, owner, repo_url, contact_name, contact_email
        Optional: code_location (str glob), additional_links (list of link dicts),
                  depends_on (list of entity ref strings e.g. "service:foo"),
                  component_of (list of system ref strings e.g. "system:my-platform"),
                  extensions (dict of custom metadata)
    """
    service_name = service["name"]

    entity = {
        "apiVersion": "v3",
        "kind": "service",
        "metadata": {
            "name": service_name,
            "displayName": service_name.replace("-", " ").title(),
            "owner": service["owner"],
            "description": service["description"],
            "contacts": [
                {
                    "type": "email",
                    "name": service["contact_name"],
                    "contact": service["contact_email"]
                }
            ],
            "links": [
                {
                    "name": "Repository",
                    "type": "repo",
                    "url": f"https://github.com/{service['repo_url']}"
                }
            ]
        },
        "spec": {
            "lifecycle": "production"
        }
    }

    # Extend links with any additional_links defined on the service
    if "additional_links" in service:
        entity["metadata"]["links"].extend(service["additional_links"])

    # v3 preferred: datadog.codeLocations (first-class field)
    if "code_location" in service:
        entity["datadog"] = {
            "codeLocations": [
                {
                    "repositoryURL": f"https://github.com/{service['repo_url']}",
                    "paths": [service["code_location"]]
                }
            ]
        }

    # Service dependency graph: outbound dependencies
    if "depends_on" in service:
        entity["spec"]["dependsOn"] = service["depends_on"]

    # System membership: which system(s) this service belongs to
    if "component_of" in service:
        entity["spec"]["componentOf"] = service["component_of"]

    # Custom metadata (no effect on Datadog features; useful for cost-center, compliance, SLA)
    if "extensions" in service:
        entity["extensions"] = service["extensions"]

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{BASE_URL}/api/v2/catalog/entity",
                headers=build_headers(api_key, app_key),
                json=entity,
                timeout=DEFAULT_TIMEOUT
            )
            if resp.status_code in [200, 201, 202]:
                return DatadogResponse(True, resp.status_code,
                                       f"Registered service: {service_name}", resp.json())

            errors = resp.json().get("errors", [resp.text]) if resp.text else "No details"
            if attempt < max_retries:
                time.sleep(1)
                continue
            return DatadogResponse(False, resp.status_code,
                                   f"Failed to register {service_name}: {errors}")
        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue
            return DatadogResponse(False, 0, f"Error registering {service_name}: {e}")

    return DatadogResponse(False, 0,
                           f"Failed to register {service_name} after {max_retries} retries")
