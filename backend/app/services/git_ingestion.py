import git
import shutil
from pathlib import Path
from typing import List, Dict, Any
from app.parsers.terraform import TerraformParser
from app.parsers.kubernetes import KubernetesParser


class GitIngestionService:
    """Service for ingesting git repositories and extracting configuration files."""

    # Supported configuration file patterns
    CONFIG_PATTERNS = {
        'terraform': ['*.tf', '*.tfvars'],
        'docker': ['docker-compose.yml', 'docker-compose.yaml', 'Dockerfile'],
        'kubernetes': ['*.yaml', '*.yml']
    }

    def __init__(self, workspace_dir: Path = None):
        """
        Initialize Git Ingestion Service.

        Args:
            workspace_dir: Directory for cloning repositories (default: ./workspace)
        """
        self.workspace_dir = workspace_dir or Path("./workspace")
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        self.terraform_parser = TerraformParser()
        self.kubernetes_parser = KubernetesParser()

    def clone_repository(self, repo_url: str, branch: str = None) -> Path:
        """
        Clone a git repository.

        Args:
            repo_url: Git repository URL
            branch: Optional branch name (default: default branch)

        Returns:
            Path to cloned repository

        Raises:
            git.GitCommandError: If cloning fails
        """
        repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')
        target_path = self.workspace_dir / repo_name

        # Remove existing directory if it exists
        if target_path.exists():
            shutil.rmtree(target_path)

        # Clone repository
        if branch:
            repo = git.Repo.clone_from(repo_url, target_path, branch=branch)
        else:
            repo = git.Repo.clone_from(repo_url, target_path)

        return Path(repo.working_dir)

    def find_config_files(self, directory: Path) -> List[Path]:
        """
        Find all configuration files in a directory.

        Args:
            directory: Directory to search

        Returns:
            List of configuration file paths
        """
        config_files = []

        # Find Terraform files
        for pattern in self.CONFIG_PATTERNS['terraform']:
            config_files.extend(directory.rglob(pattern))

        # Find Docker files
        for pattern in self.CONFIG_PATTERNS['docker']:
            config_files.extend(directory.rglob(pattern))

        # Find all Kubernetes YAML files
        # Check all YAML files, parser will filter by kind
        for pattern in self.CONFIG_PATTERNS['kubernetes']:
            config_files.extend(directory.rglob(pattern))

        return config_files

    def ingest_repository(self, repo_url: str, branch: str = None) -> Dict[str, Any]:
        """
        Ingest a repository: clone, discover configs, and parse.

        Args:
            repo_url: Git repository URL
            branch: Optional branch name

        Returns:
            Dictionary with ingestion results:
            {
                'repo_path': Path,
                'config_files': List[Path],
                'resources': List[NormalizedResource]
            }
        """
        # Clone repository
        repo_path = self.clone_repository(repo_url, branch)

        # Find configuration files
        config_files = self.find_config_files(repo_path)

        # Parse configuration files
        resources = []
        for config_file in config_files:
            if config_file.suffix in ['.tf', '.tfvars']:
                try:
                    parsed_resources = self.terraform_parser.parse_file(config_file)
                    resources.extend(parsed_resources)
                except Exception as e:
                    print(f"Error parsing Terraform file {config_file}: {e}")
            elif config_file.suffix in ['.yaml', '.yml']:
                try:
                    parsed_resources = self.kubernetes_parser.parse_file(config_file)
                    resources.extend(parsed_resources)
                except Exception as e:
                    # Log error but continue processing other files
                    print(f"Error parsing {config_file}: {e}")

        return {
            'repo_path': repo_path,
            'config_files': config_files,
            'resources': resources
        }

    def cleanup_workspace(self):
        """Remove all cloned repositories from workspace."""
        if self.workspace_dir.exists():
            shutil.rmtree(self.workspace_dir)
            self.workspace_dir.mkdir(parents=True, exist_ok=True)
