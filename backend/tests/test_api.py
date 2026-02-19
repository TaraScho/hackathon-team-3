"""
Tests for FastAPI REST API endpoints.
"""
import pytest
from unittest.mock import patch, MagicMock, Mock
from fastapi.testclient import TestClient


@pytest.fixture
def mock_db_session():
    """Create a mock database session."""
    return MagicMock()


@pytest.fixture
def client(mock_db_session):
    """Create a test client with mocked dependencies."""
    from app.main import app
    from app.database import get_db

    # Override the database dependency
    def override_get_db():
        yield mock_db_session

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    # Clean up
    app.dependency_overrides.clear()


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@patch('app.api.repositories.enqueue_drift_detection')
def test_create_repository(mock_enqueue, client, mock_db_session):
    """Test creating a repository."""
    from uuid import uuid4
    from datetime import datetime, timezone

    # Mock the enqueue function
    mock_enqueue.return_value = "test-job-id"

    # Mock database operations - no existing repository
    mock_db_session.query.return_value.filter.return_value.first.return_value = None

    # Create mock repository that will be returned after refresh
    repo_id = uuid4()
    created_at = datetime.now(timezone.utc)

    def mock_refresh(obj):
        obj.id = repo_id
        obj.created_at = created_at
        obj.last_sync_timestamp = None

    mock_db_session.refresh.side_effect = mock_refresh

    repo_data = {
        "name": "test-repo",
        "url": "https://github.com/test/repo.git",
        "branch": "main"
    }
    response = client.post("/api/repositories", json=repo_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "test-repo"
    assert data["url"] == "https://github.com/test/repo.git"
    assert data["branch"] == "main"
    assert "id" in data
    assert "created_at" in data


def test_list_repositories(client, mock_db_session):
    """Test listing repositories."""
    # Mock empty repository list
    mock_db_session.query.return_value.all.return_value = []

    response = client.get("/api/repositories")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
