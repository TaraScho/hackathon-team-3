import hcl2
from pathlib import Path
from typing import List, Dict, Any
from app.parsers.base import BaseParser, NormalizedResource
from app.models import ResourceType


class TerraformParser(BaseParser):
    """Parser for Terraform HCL configuration files."""

    def parse_file(self, file_path: Path) -> List[NormalizedResource]:
        """Parse Terraform file into normalized resources."""
        with open(file_path, 'r') as f:
            try:
                hcl_dict = hcl2.load(f)
            except Exception as e:
                raise ValueError(f"Failed to parse Terraform file {file_path}: {e}")

        resources = []

        # Parse resource blocks
        if 'resource' in hcl_dict:
            for resource_block in hcl_dict['resource']:
                resources.extend(self._parse_resource_block(resource_block, str(file_path)))

        return resources

    def _parse_resource_block(self, resource_block: Dict[str, Any], source_file: str) -> List[NormalizedResource]:
        """Parse individual resource block."""
        normalized_resources = []

        for resource_type, resources_dict in resource_block.items():
            for resource_name, resource_config in resources_dict.items():
                resource_id = f"{resource_type}.{resource_name}"

                # Extract tags/labels as metadata
                metadata = {
                    "tags": resource_config.get("tags", {}),
                    "labels": resource_config.get("labels", {})
                }

                # Properties are all config values except metadata
                properties = {k: v for k, v in resource_config.items() if k not in ["tags", "labels"]}

                normalized_resources.append(NormalizedResource(
                    resource_id=resource_id,
                    resource_type=ResourceType.TERRAFORM,
                    properties=properties,
                    metadata=metadata,
                    source_file=source_file
                ))

        return normalized_resources

    def validate_syntax(self, file_path: Path) -> bool:
        """Validate Terraform file syntax."""
        try:
            with open(file_path, 'r') as f:
                hcl2.load(f)
            return True
        except Exception:
            return False
