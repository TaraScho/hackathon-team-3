"""Tests for Redis queue and async drift detection tasks."""

import pytest
from unittest.mock import Mock, patch
from uuid import uuid4
from app.models import Repository
from app.queue.tasks import enqueue_drift_detection


@pytest.fixture
def mock_repository():
    """Create a mock repository for testing."""
    repo = Mock(spec=Repository)
    repo.id = uuid4()
    repo.git_url = "https://github.com/test/repo.git"
    repo.branch = "main"
    return repo


def test_drift_detection_task_enqueue(mock_repository):
    """Test that drift detection task can be enqueued."""
    with patch("app.queue.tasks.queue") as mock_queue:
        mock_job = Mock()
        mock_job.id = "test-job-123"
        mock_queue.enqueue.return_value = mock_job

        job_id = enqueue_drift_detection(mock_repository.id)

        assert job_id == "test-job-123"
        mock_queue.enqueue.assert_called_once()
