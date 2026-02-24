"""Shared IAM permissions utility for Datadog action catalog.

Pure data transformation — no AWS/Datadog API calls. Parses action catalog
markdown files to map Datadog action FQNs to required IAM permissions, then
extracts actions from app/workflow JSON definitions to compute least-privilege
IAM policy documents.

Usage:
    from iam_permissions import (
        load_action_catalog,
        extract_actions_from_app_json,
        extract_actions_from_workflow_json,
        resolve_permissions,
        generate_iam_policy_document,
    )

    catalog = load_action_catalog(".claude/skills/shared/actions-by-service")
    actions = extract_actions_from_app_json("path/to/app.json")
    permissions = resolve_permissions(actions, catalog)
    policy = generate_iam_policy_document(permissions)
"""

import json
import os
import re
import sys
from typing import Union


def load_action_catalog(catalog_dir: str) -> dict:
    """Parse aws-*.md files from the action catalog directory.

    Each file contains action entries in this format:
        ## com.datadoghq.aws.ec2.describe_ec2_instances
        ...
        - Permissions: `ec2:DescribeInstances`
        ...

    Args:
        catalog_dir: Path to the actions-by-service directory.

    Returns:
        Dict mapping FQN to list of IAM permissions, e.g.:
        {"com.datadoghq.aws.ec2.describe_ec2_instances": ["ec2:DescribeInstances"]}
    """
    catalog = {}
    fqn_re = re.compile(r"^## (com\.datadoghq\.\S+)")
    perm_re = re.compile(r"^- Permissions:\s*(.+)")
    perm_value_re = re.compile(r"`([^`]+)`")

    for filename in sorted(os.listdir(catalog_dir)):
        if not filename.startswith("aws-") or not filename.endswith(".md"):
            continue

        filepath = os.path.join(catalog_dir, filename)
        current_fqn = None

        with open(filepath, "r") as f:
            for line in f:
                line = line.rstrip()

                fqn_match = fqn_re.match(line)
                if fqn_match:
                    current_fqn = fqn_match.group(1)
                    if current_fqn not in catalog:
                        catalog[current_fqn] = []
                    continue

                if current_fqn:
                    perm_match = perm_re.match(line)
                    if perm_match:
                        perms_str = perm_match.group(1)
                        perms = perm_value_re.findall(perms_str)
                        catalog[current_fqn].extend(perms)

    return catalog


def extract_actions_from_app_json(path_or_dict: Union[str, dict]) -> list:
    """Extract AWS action FQNs from an App Builder app JSON definition.

    Looks for FQNs at: queries[].properties.spec.fqn

    Args:
        path_or_dict: Path to app JSON file, or already-parsed dict.

    Returns:
        Sorted, deduplicated list of com.datadoghq.aws.* FQNs.
    """
    if isinstance(path_or_dict, str):
        with open(path_or_dict, "r") as f:
            app = json.load(f)
    else:
        app = path_or_dict

    fqns = set()
    for query in app.get("queries", []):
        # Primary path: queries[].properties.spec.fqn
        fqn = (query.get("properties", {})
               .get("spec", {})
               .get("fqn", ""))
        if fqn and fqn.startswith("com.datadoghq.aws."):
            fqns.add(fqn)

        # Fallback: queries[].fqn (simplified format)
        fqn = query.get("fqn", "")
        if fqn and fqn.startswith("com.datadoghq.aws."):
            fqns.add(fqn)

        # Fallback: queries[].actionId
        fqn = query.get("actionId", "")
        if fqn and fqn.startswith("com.datadoghq.aws."):
            fqns.add(fqn)

    return sorted(fqns)


def extract_actions_from_workflow_json(path_or_dict: Union[str, dict]) -> list:
    """Extract AWS action FQNs from a Workflow Automation JSON spec.

    Checks multiple paths since workflow JSON can be nested differently:
    - spec.steps[].actionId  (standard spec structure)
    - steps[].actionId       (flat spec)
    - data.attributes.spec.steps[].actionId  (API response wrapper)

    Args:
        path_or_dict: Path to workflow JSON file, or already-parsed dict.

    Returns:
        Sorted, deduplicated list of com.datadoghq.aws.* FQNs.
    """
    if isinstance(path_or_dict, str):
        with open(path_or_dict, "r") as f:
            workflow = json.load(f)
    else:
        workflow = path_or_dict

    fqns = set()

    def _extract_from_steps(steps):
        for step in steps:
            action_id = step.get("actionId", "")
            if action_id.startswith("com.datadoghq.aws."):
                fqns.add(action_id)

    # Path 1: spec.steps[]
    spec = workflow.get("spec", {})
    if isinstance(spec, dict):
        _extract_from_steps(spec.get("steps", []))

    # Path 2: steps[] (flat)
    _extract_from_steps(workflow.get("steps", []))

    # Path 3: data.attributes.spec.steps[] (API response wrapper)
    data_spec = (workflow.get("data", {})
                 .get("attributes", {})
                 .get("spec", {}))
    if isinstance(data_spec, dict):
        _extract_from_steps(data_spec.get("steps", []))

    return sorted(fqns)


def resolve_permissions(action_fqns: list, catalog: dict) -> list:
    """Map action FQNs to IAM permissions via the catalog.

    Args:
        action_fqns: List of com.datadoghq.aws.* FQNs.
        catalog: Dict from load_action_catalog().

    Returns:
        Sorted, deduplicated list of IAM permission strings.
        Warns to stderr for any FQN not found in the catalog (non-fatal).
    """
    permissions = set()
    for fqn in action_fqns:
        if fqn in catalog:
            permissions.update(catalog[fqn])
        else:
            print(f"Warning: action FQN not found in catalog: {fqn}", file=sys.stderr)
    return sorted(permissions)


def generate_iam_policy_document(permissions: list) -> dict:
    """Generate an IAM policy document from a list of permissions.

    Args:
        permissions: List of IAM permission strings (e.g., ["ec2:DescribeInstances"]).

    Returns:
        IAM policy document dict ready for json.dumps() or boto3 put_role_policy().
    """
    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": sorted(permissions),
                "Resource": "*"
            }
        ]
    }
