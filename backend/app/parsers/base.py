from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List
from app.models import ResourceType


@dataclass
class NormalizedResource:
    """Normalized representation of infrastructure resource."""
    resource_id: str
    resource_type: ResourceType
    properties: Dict[str, Any]
    metadata: Dict[str, Any]
    source_file: str


class BaseParser(ABC):
    """Abstract base class for config parsers."""

    @abstractmethod
    def parse_file(self, file_path: Path) -> List[NormalizedResource]:
        """Parse config file and return normalized resources."""
        pass

    @abstractmethod
    def validate_syntax(self, file_path: Path) -> bool:
        """Validate config file syntax."""
        pass
