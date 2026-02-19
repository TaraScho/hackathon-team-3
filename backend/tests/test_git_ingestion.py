import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from app.services.git_ingestion import GitIngestionService


@pytest.fixture
def git_service(tmp_path):
    """Create GitIngestionService with temporary workspace."""
    return GitIngestionService(workspace_dir=tmp_path)


@pytest.fixture
def mock_repository():
    """Create mock git repository."""
    mock_repo = Mock()
    mock_repo.working_dir = "/tmp/test-repo"
    return mock_repo


def test_clone_repository(git_service, mock_repository):
    """Test cloning a git repository."""
    with patch('app.services.git_ingestion.git.Repo.clone_from') as mock_clone:
        mock_clone.return_value = mock_repository

        repo_url = "https://github.com/test/repo.git"
        result = git_service.clone_repository(repo_url)

        assert result == Path(mock_repository.working_dir)
        mock_clone.assert_called_once()


def test_find_config_files(git_service):
    """Test discovering configuration files."""
    # Create test directory structure
    test_dir = git_service.workspace_dir / "test-repo"
    test_dir.mkdir()

    (test_dir / "main.tf").write_text("resource \"aws_instance\" \"test\" {}")
    (test_dir / "docker-compose.yml").write_text("version: '3'")

    nested = test_dir / "k8s"
    nested.mkdir()
    (nested / "deployment.yaml").write_text("apiVersion: apps/v1")

    files = git_service.find_config_files(test_dir)

    assert len(files) == 3
    assert any(f.name == "main.tf" for f in files)
    assert any(f.name == "docker-compose.yml" for f in files)
    assert any(f.name == "deployment.yaml" for f in files)
