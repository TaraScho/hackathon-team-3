#!/usr/bin/env python3
"""
Datadog API helper functions for interacting with Datadog APIs.
Provides modular, reusable functions for teams, services, logs, metrics, and dashboards.
"""

import requests
import time
import os
import boto3
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass


# Constants
DD_SITE = "datadoghq.com"
BASE_URL = f"https://api.{DD_SITE}"
LOGS_ENDPOINT = "https://http-intake.logs.datadoghq.com/v1/input"
DEFAULT_TIMEOUT = 10
DEFAULT_MAX_RETRIES = 1


@dataclass
class DatadogResponse:
    """Structured response from Datadog API operations."""
    success: bool
    status_code: int
    message: str
    data: Optional[Dict] = None


def build_headers(api_key: str, app_key: Optional[str] = None) -> Dict[str, str]:
    """
    Build standard Datadog API headers.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key (optional, required for some endpoints)

    Returns:
        Dict containing the appropriate headers
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
    }

    if app_key:
        headers["DD-APPLICATION-KEY"] = app_key

    return headers


def get_existing_teams(api_key: str, app_key: str) -> Tuple[Set[str], Optional[str]]:
    """
    Fetch existing team handles from Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key

    Returns:
        Tuple of (set of team handles, error message if any)
    """
    headers = build_headers(api_key, app_key)

    try:
        response = requests.get(
            f"{BASE_URL}/api/v2/team",
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 200:
            data = response.json()
            teams = {team["attributes"]["handle"] for team in data.get("data", [])}
            return teams, None
        else:
            return set(), f"Could not fetch existing teams (status {response.status_code})"

    except Exception as e:
        return set(), f"Error fetching existing teams: {e}"


def create_team(
    api_key: str,
    app_key: str,
    team_handle: str,
    team_name: Optional[str] = None,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create a team in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        team_handle: Team handle (unique identifier)
        team_name: Team display name (defaults to formatted team_handle)
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)

    if not team_name:
        team_name = team_handle.replace("-", " ").title()

    payload = {
        "data": {
            "type": "team",
            "attributes": {
                "handle": team_handle,
                "name": team_name
            }
        }
    }

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/team",
                headers=headers,
                json=payload,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code == 201:
                return DatadogResponse(
                    success=True,
                    status_code=201,
                    message=f"Created team: {team_handle}",
                    data=response.json()
                )
            elif response.status_code == 409:
                return DatadogResponse(
                    success=True,
                    status_code=409,
                    message=f"Team already exists: {team_handle}"
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to create team {team_handle}: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error creating team {team_handle}: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to create team {team_handle} after {max_retries} retries"
    )


def create_service_entity(
    api_key: str,
    app_key: str,
    service: Dict,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create or update a service entity using v3 schema in Datadog Software Catalog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        service: Service definition dict with keys: name, description, owner,
                 repo_url, contact_name, contact_email, code_location (optional)
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)
    service_name = service["name"]

    # Build v3 entity definition
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

    # Add additional links if specified
    if "additional_links" in service:
        entity["metadata"]["links"].extend(service["additional_links"])

    # Add tags for code location if available
    if "code_location" in service:
        entity["metadata"]["tags"] = [f"code_location:{service['code_location']}"]

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                f"{BASE_URL}/api/v2/catalog/entity",
                headers=headers,
                json=entity,
                timeout=DEFAULT_TIMEOUT
            )

            if response.status_code in [200, 201, 202]:
                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"Created service entity: {service_name}",
                    data=response.json()
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to create service {service_name}: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error creating service {service_name}: {e}"
            )

    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to create service {service_name} after {max_retries} retries"
    )


def send_logs(api_key: str, logs: List[Dict], endpoint: str = LOGS_ENDPOINT) -> DatadogResponse:
    """
    Send logs to Datadog via the Logs API.

    Args:
        api_key: Datadog API key
        logs: List of log dictionaries with keys: ddsource, ddtags, hostname,
              message, service, status, timestamp
        endpoint: Logs API endpoint (defaults to US intake endpoint)

    Returns:
        DatadogResponse with operation result
    """
    headers = {
        "DD-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            endpoint,
            json=logs,
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code in [200, 202]:
            return DatadogResponse(
                success=True,
                status_code=response.status_code,
                message=f"Successfully sent {len(logs)} logs"
            )
        else:
            return DatadogResponse(
                success=False,
                status_code=response.status_code,
                message=f"Failed to send logs: {response.text}"
            )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error sending logs: {e}"
        )


def send_metrics(api_key: str, app_key: str, series: List[Dict]) -> DatadogResponse:
    """
    Send custom metrics to Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        series: List of metric series dicts with keys: metric, type, points, tags

    Returns:
        DatadogResponse with operation result
    """
    headers = build_headers(api_key, app_key)

    metrics_payload = {"series": series}

    try:
        response = requests.post(
            f"{BASE_URL}/api/v2/series",
            json=metrics_payload,
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 202:
            return DatadogResponse(
                success=True,
                status_code=202,
                message=f"Successfully sent {len(series)} metrics"
            )
        else:
            return DatadogResponse(
                success=False,
                status_code=response.status_code,
                message=f"Failed to send metrics: {response.text}"
            )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error sending metrics: {e}"
        )


def create_dashboard(api_key: str, app_key: str, dashboard_config: Dict) -> DatadogResponse:
    """
    Create a dashboard in Datadog.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        dashboard_config: Dashboard configuration dictionary (JSON)

    Returns:
        DatadogResponse with operation result including dashboard ID and URL
    """
    headers = build_headers(api_key, app_key)

    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/dashboard",
            json=dashboard_config,
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code in [200, 201]:
            response_data = response.json()
            dashboard_id = response_data.get('id', 'unknown')
            # Construct proper dashboard URL instead of using CloudFront URL from API
            dashboard_url = f"https://app.{DD_SITE}/dashboard/{dashboard_id}"

            return DatadogResponse(
                success=True,
                status_code=response.status_code,
                message=f"Successfully created dashboard: {dashboard_id}",
                data={
                    "id": dashboard_id,
                    "url": dashboard_url,
                    "full_response": response_data
                }
            )
        else:
            return DatadogResponse(
                success=False,
                status_code=response.status_code,
                message=f"Failed to create dashboard: {response.text}"
            )

    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error creating dashboard: {e}"
        )


def get_existing_monitors(api_key: str, app_key: str) -> Tuple[Dict[str, int], Optional[str]]:
    """
    Fetch existing monitors from Datadog and return a mapping of monitor names to IDs.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key

    Returns:
        Tuple of (dict mapping monitor names to IDs, error message if any)
    """
    headers = build_headers(api_key, app_key)

    try:
        response = requests.get(
            f"{BASE_URL}/api/v1/monitor",
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )

        if response.status_code == 200:
            monitors = response.json()
            monitor_map = {monitor["name"]: monitor["id"] for monitor in monitors}
            return monitor_map, None
        else:
            return {}, f"Could not fetch existing monitors (status {response.status_code})"

    except Exception as e:
        return {}, f"Error fetching existing monitors: {e}"


def create_or_update_monitor(
    api_key: str,
    app_key: str,
    monitor_config: Dict,
    max_retries: int = DEFAULT_MAX_RETRIES
) -> DatadogResponse:
    """
    Create or update a monitor in Datadog.
    If a monitor with the same name exists, it will be updated.
    Otherwise, a new monitor will be created.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        monitor_config: Monitor configuration dictionary (JSON)
        max_retries: Maximum number of retry attempts

    Returns:
        DatadogResponse with operation result including monitor ID
    """
    headers = build_headers(api_key, app_key)
    monitor_name = monitor_config.get('name', 'unknown')

    # Check if monitor already exists
    existing_monitors, error = get_existing_monitors(api_key, app_key)
    if error:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Failed to check existing monitors: {error}"
        )

    existing_monitor_id = existing_monitors.get(monitor_name)
    is_update = existing_monitor_id is not None

    for attempt in range(max_retries + 1):
        try:
            if is_update:
                # Update existing monitor
                response = requests.put(
                    f"{BASE_URL}/api/v1/monitor/{existing_monitor_id}",
                    json=monitor_config,
                    headers=headers,
                    timeout=DEFAULT_TIMEOUT
                )
            else:
                # Create new monitor
                response = requests.post(
                    f"{BASE_URL}/api/v1/monitor",
                    json=monitor_config,
                    headers=headers,
                    timeout=DEFAULT_TIMEOUT
                )

            if response.status_code in [200, 201]:
                response_data = response.json()
                monitor_id = response_data.get('id', existing_monitor_id if is_update else 'unknown')
                action = "Updated" if is_update else "Created"

                return DatadogResponse(
                    success=True,
                    status_code=response.status_code,
                    message=f"{action} monitor: {monitor_name}",
                    data={
                        "id": monitor_id,
                        "action": action.lower(),
                        "full_response": response_data
                    }
                )
            else:
                error_msg = response.json().get("errors", [response.text]) if response.text else "No error details"

                if attempt < max_retries:
                    time.sleep(1)
                    continue

                action = "update" if is_update else "create"
                return DatadogResponse(
                    success=False,
                    status_code=response.status_code,
                    message=f"Failed to {action} monitor: {error_msg}"
                )

        except Exception as e:
            if attempt < max_retries:
                time.sleep(1)
                continue

            action = "updating" if is_update else "creating"
            return DatadogResponse(
                success=False,
                status_code=0,
                message=f"Error {action} monitor: {e}"
            )

    action = "update" if is_update else "create"
    return DatadogResponse(
        success=False,
        status_code=0,
        message=f"Failed to {action} monitor after {max_retries} retries"
    )


def load_monitors_from_directory(monitors_dir: Optional[str] = None) -> List[Dict]:
    """
    Load all monitor configurations from JSON files in a directory.

    Args:
        monitors_dir: Path to directory containing monitor JSON files. If None, looks for
                     monitors/ subdirectory in the datadog_helpers directory

    Returns:
        List of monitor configuration dicts
    """
    import json
    import glob

    if monitors_dir is None:
        # Default to the monitors/ subdirectory in the same directory as this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        monitors_dir = os.path.join(current_dir, "monitors")

    monitors = []

    try:
        # Find all JSON files in the monitors directory
        json_files = glob.glob(os.path.join(monitors_dir, "*.json"))

        for json_file in json_files:
            try:
                with open(json_file, 'r') as f:
                    monitor_config = json.load(f)
                    monitors.append(monitor_config)
            except json.JSONDecodeError as e:
                print(f"Error: Invalid JSON in monitor file {json_file}: {e}")
            except Exception as e:
                print(f"Error reading monitor file {json_file}: {e}")

        return monitors

    except Exception as e:
        print(f"Error loading monitors from directory {monitors_dir}: {e}")
        return []


def create_dashboard_with_embedded_apps(
    api_key: str,
    app_key: str,
    app_ids: Dict[str, str],
    dashboard_template_path: Optional[str] = None
) -> DatadogResponse:
    """
    Create a dashboard from a template with embedded app IDs.

    Loads dashboard JSON template, replaces app_id placeholders with actual app IDs,
    and creates the dashboard via the Datadog API.

    Args:
        api_key: Datadog API key
        app_key: Datadog application key
        app_ids: Dict mapping placeholder keys to app IDs (e.g., {"dynamodb_manager": "abc-123"})
        dashboard_template_path: Path to dashboard JSON template file. If None, uses
                                techstories-dashboard-full.json in datadog_helpers directory

    Returns:
        DatadogResponse with dashboard ID and URL

    Example:
        app_ids = {"dynamodb_manager": "abc-123"}
        response = create_dashboard_with_embedded_apps(api_key, app_key, app_ids)
        if response.success:
            print(f"Dashboard URL: {response.data['url']}")
    """
    import json

    if dashboard_template_path is None:
        # Default to techstories-dashboard-full.json in the same directory as this file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dashboard_template_path = os.path.join(current_dir, "techstories-dashboard-full.json")

    try:
        # Load dashboard template
        with open(dashboard_template_path, 'r') as f:
            dashboard_config = json.load(f)

        # Convert to JSON string for placeholder replacement
        dashboard_json_str = json.dumps(dashboard_config)

        # Replace all app_id placeholders
        # Format: DYNAMODB_APP_ID_PLACEHOLDER -> actual app_id
        for key, app_id in app_ids.items():
            placeholder = f"{key.upper()}_APP_ID_PLACEHOLDER"
            dashboard_json_str = dashboard_json_str.replace(placeholder, app_id)

        # Convert back to dict
        dashboard_config = json.loads(dashboard_json_str)

        # Create dashboard using existing helper
        return create_dashboard(api_key, app_key, dashboard_config)

    except FileNotFoundError:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Dashboard template file not found: {dashboard_template_path}"
        )
    except json.JSONDecodeError as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Invalid JSON in dashboard template: {e}"
        )
    except Exception as e:
        return DatadogResponse(
            success=False,
            status_code=0,
            message=f"Error creating dashboard from template: {e}"
        )
