#!/usr/bin/env python3
"""Extract Datadog action definitions from dd-source manifest files.

Reads manifest.gen.json files from the wf-actions-worker bundles directory,
resolves $ref chains for input/output schemas, and generates:
  - Per-service markdown reference files (e.g., aws-ec2.md)
  - A master index file linking all generated references

Usage:
    python scripts/extract_action_catalog.py \
      --bundles-dir ~/repos/dd-source/.../bundles \
      --output-dir .claude/skills/shared/actions-by-service \
      --index-file .claude/skills/shared/action-catalog-index.md \
      --prefixes com.datadoghq.aws,com.datadoghq.github,com.datadoghq.dd,com.datadoghq.core,com.datadoghq.datatransformation \
      --stability stable,beta
"""

import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


def get_git_short_hash(repo_dir: str) -> str:
    """Get short git commit hash from the given repo directory."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_dir, "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


def resolve_ref(ref: str, defs: dict, depth: int = 0, max_depth: int = 2) -> dict:
    """Resolve a JSON Schema $ref string against the types.$defs map.

    Follows $ref chains up to max_depth levels. Returns the resolved schema
    dict (which may still contain unresolved nested $refs beyond the limit).
    """
    if depth > max_depth:
        return {}

    # ref looks like "#/$defs/SomeName"
    if not ref.startswith("#/$defs/"):
        return {}

    def_name = ref[len("#/$defs/"):]
    schema = defs.get(def_name, {})

    # If the entire schema is just another $ref, follow it
    if "$ref" in schema and len(schema) == 1:
        return resolve_ref(schema["$ref"], defs, depth + 1, max_depth)

    # If schema has a $ref alongside other keys (like description, title),
    # resolve the $ref to get the base type, then overlay local keys
    if "$ref" in schema:
        base = resolve_ref(schema["$ref"], defs, depth + 1, max_depth)
        merged = {**base, **{k: v for k, v in schema.items() if k != "$ref"}}
        return merged

    return schema


def extract_type_string(prop_schema: dict, defs: dict) -> str:
    """Convert a property schema to a human-readable type string."""
    if "anyOf" in prop_schema:
        return "any"
    if "oneOf" in prop_schema:
        return "any"

    typ = prop_schema.get("type", "")

    if typ == "array":
        items = prop_schema.get("items", {})
        if "$ref" in items:
            resolved = resolve_ref(items["$ref"], defs)
            inner = resolved.get("type", "object")
        else:
            inner = items.get("type", "any")
        return f"array<{inner}>"

    if typ:
        return typ

    # No explicit type — check if there's a $ref we can resolve
    if "$ref" in prop_schema:
        resolved = resolve_ref(prop_schema["$ref"], defs)
        return extract_type_string(resolved, defs)

    return "any"


def extract_properties(schema: dict, defs: dict) -> list[dict]:
    """Extract property metadata from an input/output schema.

    Returns a list of dicts with keys: name, type, required, title, description.
    """
    if not schema:
        return []

    # Resolve the schema itself if it's a pure $ref
    if "$ref" in schema and "properties" not in schema:
        schema = resolve_ref(schema["$ref"], defs)

    props = schema.get("properties", {})
    required_set = set(schema.get("required", []))
    result = []

    for name, prop_schema in props.items():
        # Resolve $ref for this property to get type info
        if "$ref" in prop_schema:
            resolved = resolve_ref(prop_schema["$ref"], defs)
            # Local keys override resolved keys
            merged = {**resolved, **{k: v for k, v in prop_schema.items() if k != "$ref"}}
        else:
            merged = prop_schema

        type_str = extract_type_string(merged, defs)
        title = merged.get("title", "")
        description = merged.get("description", "")
        # Truncate long descriptions for readability
        if len(description) > 200:
            description = description[:197] + "..."

        result.append({
            "name": name,
            "type": type_str,
            "required": name in required_set,
            "title": title,
            "description": description,
        })

    return result


def parse_manifest(manifest_path: str) -> dict | None:
    """Parse a manifest.gen.json and extract bundle + action metadata."""
    with open(manifest_path) as f:
        manifest = json.load(f)

    defs = manifest.get("types", {}).get("$defs", {})
    actions_map = manifest.get("actions", {})

    bundle = {
        "name": manifest.get("name", ""),
        "title": manifest.get("title", ""),
        "description": manifest.get("description", ""),
        "stability": manifest.get("stability", ""),
        "actions": [],
    }

    for action_key, action_meta in actions_map.items():
        # Build FQN: bundle_name.action_key
        fqn = f"{bundle['name']}.{action_key}"

        # Resolve input schema
        input_ref = action_meta.get("input", "")
        input_schema = resolve_ref(input_ref, defs) if input_ref else {}
        inputs = extract_properties(input_schema, defs)

        # Resolve output schema
        output_ref = action_meta.get("output", "")
        output_schema = resolve_ref(output_ref, defs) if output_ref else {}
        outputs = extract_properties(output_schema, defs)

        bundle["actions"].append({
            "key": action_key,
            "fqn": fqn,
            "title": action_meta.get("title", action_key),
            "description": action_meta.get("description", ""),
            "stability": action_meta.get("stability", ""),
            "permissions": action_meta.get("permissions", []),
            "accessModes": action_meta.get("accessModes", []),
            "inputs": inputs,
            "outputs": outputs,
        })

    # Sort actions by FQN for consistent output
    bundle["actions"].sort(key=lambda a: a["fqn"])
    return bundle


def bundle_to_file_slug(bundle_name: str) -> str:
    """Convert a bundle name to a filename slug.

    com.datadoghq.aws.ec2 -> aws-ec2
    com.datadoghq.github.issues -> github-issues
    com.datadoghq.dd.cases -> dd-cases
    com.datadoghq.core -> core-workflow
    com.datadoghq.datatransformation -> core-datatransformation
    """
    # Strip the common prefix
    name = bundle_name
    for prefix in ["com.datadoghq."]:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break

    # Special case: core bundle
    if name == "core":
        return "core-workflow"
    if name == "datatransformation":
        return "core-datatransformation"

    # Replace dots with hyphens
    return name.replace(".", "-")


def generate_service_markdown(bundle: dict) -> str:
    """Generate per-service markdown content for a bundle."""
    title = bundle["title"] or bundle["name"]
    action_count = len(bundle["actions"])
    encoded_name = bundle["name"].replace(".", "%2E")

    lines = [
        f"# {title} Actions",
        f"Bundle: `{bundle['name']}` | {action_count} actions | "
        f"[View in Datadog](https://app.datadoghq.com/actions/action-catalog#{encoded_name})",
        "",
    ]

    for action in bundle["actions"]:
        lines.append(f"## {action['fqn']}")
        desc = action["description"] or "No description."
        lines.append(f"**{action['title']}** — {desc}")

        meta_parts = []
        if action["stability"]:
            meta_parts.append(f"Stability: {action['stability']}")
        if action["permissions"]:
            perms = ", ".join(f"`{p}`" for p in action["permissions"])
            meta_parts.append(f"Permissions: {perms}")
        if action["accessModes"]:
            meta_parts.append(f"Access: {', '.join(action['accessModes'])}")

        for part in meta_parts:
            lines.append(f"- {part}")

        # Inputs table
        if action["inputs"]:
            lines.append("- **Inputs**:")
            lines.append("")
            lines.append("  | Name | Type | Required | Description |")
            lines.append("  |------|------|----------|-------------|")
            for inp in action["inputs"]:
                req = "yes" if inp["required"] else "no"
                desc = inp["description"].replace("|", "\\|").replace("\n", " ")
                lines.append(f"  | {inp['name']} | {inp['type']} | {req} | {desc} |")
            lines.append("")

        # Outputs table
        if action["outputs"]:
            lines.append("- **Outputs**:")
            lines.append("")
            lines.append("  | Name | Type | Description |")
            lines.append("  |------|------|-------------|")
            for out in action["outputs"]:
                desc = out["description"].replace("|", "\\|").replace("\n", " ")
                lines.append(f"  | {out['name']} | {out['type']} | {desc} |")
            lines.append("")

        lines.append("")

    return "\n".join(lines)


def categorize_bundle(bundle_name: str) -> str:
    """Assign a bundle to a display category for the index."""
    if bundle_name.startswith("com.datadoghq.aws."):
        return "AWS Services"
    if bundle_name.startswith("com.datadoghq.github"):
        return "GitHub"
    if bundle_name.startswith("com.datadoghq.dd"):
        return "Datadog Native"
    if bundle_name in ("com.datadoghq.core", "com.datadoghq.datatransformation"):
        return "Core Workflow Actions"
    return "Other"


def generate_index_markdown(
    bundles: list[dict], git_hash: str, output_dir_rel: str
) -> str:
    """Generate the master index markdown."""
    today = date.today().isoformat()

    lines = [
        "# Datadog Action Catalog Index",
        f"Generated from dd-source commit: {git_hash} | Date: {today}",
        "",
        "## How to Use",
        f"Read the per-service reference file for the service you need.",
        f"Files are at `{output_dir_rel}/{{service}}.md`",
        "",
    ]

    # Group bundles by category
    categories = defaultdict(list)
    for b in bundles:
        cat = categorize_bundle(b["name"])
        categories[cat].append(b)

    # Define category order
    cat_order = ["AWS Services", "GitHub", "Datadog Native", "Core Workflow Actions", "Other"]

    for cat in cat_order:
        cat_bundles = categories.get(cat, [])
        if not cat_bundles:
            continue

        total_actions = sum(len(b["actions"]) for b in cat_bundles)
        lines.append(f"## {cat} ({len(cat_bundles)} bundles, {total_actions} actions)")
        lines.append("")
        lines.append("| File | Bundle | Title | Actions |")
        lines.append("|------|--------|-------|---------|")

        for b in sorted(cat_bundles, key=lambda x: x["name"]):
            slug = bundle_to_file_slug(b["name"])
            title = b["title"] or b["name"]
            count = len(b["actions"])
            lines.append(f"| {slug}.md | {b['name']} | {title} | {count} |")

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Extract Datadog action catalog from dd-source manifests"
    )
    parser.add_argument(
        "--bundles-dir", required=True,
        help="Path to wf-actions-worker bundles directory",
    )
    parser.add_argument(
        "--output-dir", required=True,
        help="Output directory for per-service markdown files",
    )
    parser.add_argument(
        "--index-file", required=True,
        help="Path for the master index markdown file",
    )
    parser.add_argument(
        "--prefixes", required=True,
        help="Comma-separated bundle name prefixes to include",
    )
    parser.add_argument(
        "--stability", default="stable,beta",
        help="Comma-separated stability levels to include (default: stable,beta)",
    )
    args = parser.parse_args()

    bundles_dir = Path(args.bundles_dir).expanduser().resolve()
    output_dir = Path(args.output_dir)
    index_file = Path(args.index_file)
    prefixes = [p.strip() for p in args.prefixes.split(",")]
    stability_filter = set(s.strip() for s in args.stability.split(","))

    if not bundles_dir.is_dir():
        print(f"Error: bundles directory not found: {bundles_dir}", file=sys.stderr)
        sys.exit(1)

    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    index_file.parent.mkdir(parents=True, exist_ok=True)

    # Find matching bundle directories
    bundle_dirs = sorted(bundles_dir.iterdir())
    matched = []
    for d in bundle_dirs:
        if not d.is_dir():
            continue
        if not any(d.name.startswith(p) or d.name == p for p in prefixes):
            continue
        manifest = d / "manifest.gen.json"
        if manifest.exists():
            matched.append(manifest)

    print(f"Found {len(matched)} matching bundles")

    # Parse all manifests
    all_bundles = []
    skipped = 0
    for manifest_path in matched:
        bundle = parse_manifest(str(manifest_path))
        if bundle is None:
            continue

        # Filter actions by stability
        original_count = len(bundle["actions"])
        bundle["actions"] = [
            a for a in bundle["actions"]
            if a["stability"] in stability_filter
        ]

        if not bundle["actions"]:
            skipped += 1
            continue

        filtered = original_count - len(bundle["actions"])
        if filtered:
            print(f"  {bundle['name']}: {len(bundle['actions'])} actions "
                  f"({filtered} filtered by stability)")
        else:
            print(f"  {bundle['name']}: {len(bundle['actions'])} actions")

        all_bundles.append(bundle)

    print(f"\nProcessing {len(all_bundles)} bundles ({skipped} skipped — no matching actions)")

    # Generate per-service files
    for bundle in all_bundles:
        slug = bundle_to_file_slug(bundle["name"])
        md_content = generate_service_markdown(bundle)
        out_path = output_dir / f"{slug}.md"
        out_path.write_text(md_content)

    total_actions = sum(len(b["actions"]) for b in all_bundles)
    print(f"Wrote {len(all_bundles)} service files to {output_dir}")
    print(f"Total actions: {total_actions}")

    # Generate master index
    git_hash = get_git_short_hash(str(bundles_dir))
    output_dir_rel = str(output_dir)
    # Make path relative if it starts with .claude/
    if ".claude/" in output_dir_rel:
        output_dir_rel = ".claude/" + output_dir_rel.split(".claude/", 1)[1]

    index_content = generate_index_markdown(all_bundles, git_hash, output_dir_rel)
    index_file.write_text(index_content)
    print(f"Wrote index to {index_file}")


if __name__ == "__main__":
    main()
