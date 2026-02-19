"""
Kubernetes YAML configuration parser.
"""
from pathlib import Path
from typing import List, Dict, Any
import yaml
from app.parsers.base import BaseParser, NormalizedResource, ResourceType


class KubernetesParser(BaseParser):
    """Parser for Kubernetes YAML manifests."""

    SUPPORTED_KINDS = {
        "Pod", "Deployment", "Service", "ConfigMap", "Secret",
        "StatefulSet", "DaemonSet", "Job", "CronJob", "Ingress",
        "PersistentVolume", "PersistentVolumeClaim", "ServiceAccount",
        "Role", "RoleBinding", "ClusterRole", "ClusterRoleBinding",
        "Namespace", "ResourceQuota", "LimitRange", "NetworkPolicy"
    }

    def validate_syntax(self, file_path: Path) -> bool:
        """
        Validate YAML syntax of Kubernetes manifest.

        Args:
            file_path: Path to the YAML file

        Returns:
            True if valid YAML, False otherwise
        """
        try:
            with open(file_path, 'r') as f:
                list(yaml.safe_load_all(f))
            return True
        except yaml.YAMLError:
            return False
        except Exception:
            return False

    def parse_file(self, file_path: Path) -> List[NormalizedResource]:
        """
        Parse a Kubernetes YAML file and return normalized resources.

        Args:
            file_path: Path to the YAML file

        Returns:
            List of NormalizedResource objects
        """
        resources = []

        try:
            with open(file_path, 'r') as f:
                # Support multi-document YAML files
                documents = list(yaml.safe_load_all(f))

            for doc in documents:
                if not doc or not isinstance(doc, dict):
                    continue

                kind = doc.get('kind')
                if not kind or kind not in self.SUPPORTED_KINDS:
                    continue

                metadata = doc.get('metadata', {})
                name = metadata.get('name', 'unnamed')
                namespace = metadata.get('namespace', 'default')
                labels = metadata.get('labels', {})
                annotations = metadata.get('annotations', {})

                # Create unique resource ID
                resource_id = f"{kind.lower()}/{namespace}/{name}"

                # Normalize the resource
                normalized = NormalizedResource(
                    resource_id=resource_id,
                    resource_type=ResourceType.KUBERNETES,
                    properties=self._extract_properties(doc),
                    metadata={
                        "kind": kind,
                        "namespace": namespace,
                        "labels": labels,
                        "annotations": annotations,
                        "source_format": "kubernetes"
                    },
                    source_file=str(file_path)
                )

                resources.append(normalized)

        except yaml.YAMLError as e:
            # Log error but don't fail the entire parse
            print(f"YAML parsing error in {file_path}: {e}")
        except Exception as e:
            print(f"Error parsing Kubernetes file {file_path}: {e}")

        return resources

    def _extract_properties(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract relevant properties from Kubernetes resource.

        Args:
            doc: Kubernetes resource document

        Returns:
            Dictionary of normalized properties
        """
        kind = doc.get('kind')
        spec = doc.get('spec', {})
        metadata = doc.get('metadata', {})

        properties = {
            "name": metadata.get('name'),
            "namespace": metadata.get('namespace', 'default'),
        }

        # Extract kind-specific properties
        if kind in ["Deployment", "StatefulSet", "DaemonSet"]:
            properties.update({
                "replicas": spec.get('replicas', 1),
                "selector": spec.get('selector'),
                "template": spec.get('template', {}).get('spec', {}),
            })
        elif kind == "Service":
            properties.update({
                "type": spec.get('type', 'ClusterIP'),
                "ports": spec.get('ports', []),
                "selector": spec.get('selector'),
            })
        elif kind == "Pod":
            properties.update({
                "containers": spec.get('containers', []),
                "volumes": spec.get('volumes', []),
            })
        elif kind == "Ingress":
            properties.update({
                "rules": spec.get('rules', []),
                "tls": spec.get('tls', []),
            })
        elif kind in ["PersistentVolume", "PersistentVolumeClaim"]:
            properties.update({
                "capacity": spec.get('capacity', {}),
                "access_modes": spec.get('accessModes', []),
                "storage_class": spec.get('storageClassName'),
            })
        elif kind == "ConfigMap":
            properties.update({
                "data": doc.get('data', {}),
                "binary_data": doc.get('binaryData', {}),
            })
        elif kind == "Secret":
            # Don't store actual secret values
            properties.update({
                "type": doc.get('type', 'Opaque'),
                "data_keys": list(doc.get('data', {}).keys()),
            })
        elif kind in ["Role", "ClusterRole"]:
            properties.update({
                "rules": spec.get('rules', []),
            })
        elif kind in ["RoleBinding", "ClusterRoleBinding"]:
            properties.update({
                "subjects": spec.get('subjects', []),
                "role_ref": spec.get('roleRef', {}),
            })

        return properties
