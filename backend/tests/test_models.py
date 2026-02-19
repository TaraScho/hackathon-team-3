import pytest
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Repository, ConfigResource, DriftReport, RemediationHistory
from app.models import ResourceType, DriftStatus, Severity, RemediationStatus, RemediationType, RemediationOutcome


@pytest.fixture
def db_session():
    """Create test database session."""
    engine = create_engine("postgresql://driftguard:driftguard@localhost:5432/driftguard")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(engine)


def test_repository_model(db_session):
    """Test Repository model creation and persistence."""
    repo = Repository(
        id=uuid4(),
        git_url="https://github.com/example/repo.git",
        branch="main",
        credentials_ref="secret/github/token",
        last_sync_timestamp=datetime.now(timezone.utc)
    )
    db_session.add(repo)
    db_session.commit()

    retrieved = db_session.query(Repository).filter_by(git_url=repo.git_url).first()
    assert retrieved is not None
    assert retrieved.branch == "main"
