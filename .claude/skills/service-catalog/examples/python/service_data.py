"""
Service data definitions for Datadog Software Catalog registration.

Define all services as a Python list of dicts. This makes the data portable
and testable independent of API calls.

Required fields: name, description, owner, repo_url, contact_name, contact_email
Optional fields: code_location, additional_links, depends_on, component_of, extensions
"""

ALL_SERVICES = [
    {
        # Required
        "name": "island-mail",                       # kebab-case
        "description": "Private messaging service for premium users",
        "owner": "backend-services-team",            # Datadog team handle
        "repo_url": "my-org/my-repo",                # appended to https://github.com/
        "contact_name": "Island Mail Support",
        "contact_email": "island-mail-support@example.com",
        # Optional
        "code_location": "services/messaging_api/**",  # maps to datadog.codeLocations
        "depends_on": ["datastore:postgres-main", "queue:email-queue"],  # entity refs
        "component_of": ["system:techstories-platform"],                 # system membership
        "extensions": {"cost-center": "eng-1234", "compliance": "SOC2"},
        "additional_links": [
            {"name": "Runbook", "type": "doc",
             "url": "https://wiki.example.com/runbooks/island-mail"}
        ]
    },
    {
        "name": "quotes-api",
        "description": "Next.js microservice that serves inspirational quotes",
        "owner": "frontend-team",
        "repo_url": "my-org/my-repo",
        "contact_name": "Frontend Support",
        "contact_email": "frontend-support@example.com",
        "code_location": "services/quotes_api/**"
    },
    {
        "name": "parrot-translator",
        "description": "Translates content between languages",
        "owner": "backend-services-team",
        "repo_url": "my-org/my-repo",
        "contact_name": "Internal Support",
        "contact_email": "support@example.com",
        "code_location": "services/parrot_translator/**",
        "depends_on": ["service:quotes-api"]
    }
]


def get_unique_teams() -> list:
    """Extract unique owner handles from ALL_SERVICES."""
    return list({s["owner"] for s in ALL_SERVICES})


def get_services_by_team(team_handle: str) -> list:
    """Return all services owned by the given team handle."""
    return [s for s in ALL_SERVICES if s["owner"] == team_handle]
