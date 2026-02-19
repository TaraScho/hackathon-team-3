# DriftGuard MVP Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the core DriftGuard drift detection engine with Terraform config support, Datadog integration, and basic web dashboard.

**Architecture:** Event-driven system with FastAPI backend, Redis queue for async processing, PostgreSQL for persistence, and React frontend. Config ingestion parses Terraform files from git, detection engine compares against Datadog infrastructure state, and web API exposes drift reports with remediation actions.

**Tech Stack:** Python 3.13, FastAPI, PostgreSQL, Redis/RQ, GitPython, python-hcl2, datadog-api-client, React, TypeScript, Vite

---

## Phase 1: Project Setup & Database Schema

### Task 1: Initialize Project Structure

**Files:**
- Create: `backend/requirements.txt`
- Create: `backend/app/__init__.py`
- Create: `backend/app/config.py`
- Create: `backend/tests/__init__.py`
- Create: `.env.example`
- Create: `.gitignore`
- Create: `docker-compose.yml`

**Step 1: Create backend directory structure**

```bash
mkdir -p backend/app backend/tests
touch backend/requirements.txt
touch backend/app/__init__.py
touch backend/app/config.py
touch backend/tests/__init__.py
```

**Step 2: Write requirements.txt**

Create `backend/requirements.txt`:
```txt
fastapi==0.115.0
uvicorn[standard]==0.32.0
sqlalchemy==2.0.36
alembic==1.14.0
psycopg2-binary==2.9.10
redis==5.2.0
rq==2.0.0
gitpython==3.1.43
python-hcl2==4.3.5
pyyaml==6.0.2
datadog-api-client==2.30.0
pydantic==2.10.3
pydantic-settings==2.6.1
python-dotenv==1.0.1
pytest==8.3.4
pytest-asyncio==0.24.0
httpx==0.28.1
```

**Step 3: Create .env.example**

```env
# Database
DATABASE_URL=postgresql://driftguard:driftguard@localhost:5432/driftguard

# Redis
REDIS_URL=redis://localhost:6379/0

# Datadog
DATADOG_API_KEY=your_api_key_here
DATADOG_APP_KEY=your_app_key_here
DATADOG_SITE=datadoghq.com

# Application
APP_ENV=development
LOG_LEVEL=INFO
SECRET_KEY=change_this_in_production
```

**Step 4: Create .gitignore**

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv

# Environment
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Database
*.db
*.sqlite3

# Logs
*.log

# OS
.DS_Store
Thumbs.db

# Frontend
node_modules/
dist/
build/
.cache/
```

**Step 5: Create docker-compose.yml**

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: driftguard
      POSTGRES_PASSWORD: driftguard
      POSTGRES_DB: driftguard
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U driftguard"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
  redis_data:
```

**Step 6: Commit project setup**

```bash
git add backend/ .env.example .gitignore docker-compose.yml
git commit -m "feat: initialize DriftGuard project structure

- Add backend directory with Python dependencies
- Configure PostgreSQL and Redis with docker-compose
- Add environment configuration template
- Set up project .gitignore

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 2: Database Models & Migrations

**Files:**
- Create: `backend/app/models.py`
- Create: `backend/app/database.py`
- Create: `backend/alembic.ini`
- Create: `backend/alembic/env.py`
- Create: `backend/alembic/versions/001_initial_schema.py`

**Step 1: Write database configuration test**

Create `backend/tests/test_database.py`:
```python
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db


def test_database_connection():
    """Test database connection is established."""
    engine = create_engine("postgresql://driftguard:driftguard@localhost:5432/driftguard")
    connection = engine.connect()
    result = connection.execute(text("SELECT 1"))
    assert result.fetchone()[0] == 1
    connection.close()
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_database.py::test_database_connection -v`

Expected: FAIL - ImportError or module not found

**Step 3: Create database.py**

Create `backend/app/database.py`:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Dependency for getting database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Step 4: Create config.py**

Create `backend/app/config.py`:
```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    REDIS_URL: str
    DATADOG_API_KEY: str
    DATADOG_APP_KEY: str
    DATADOG_SITE: str = "datadoghq.com"
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    SECRET_KEY: str


settings = Settings()
```

**Step 5: Write models test**

Create `backend/tests/test_models.py`:
```python
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
```

**Step 6: Run test to verify it fails**

Run: `cd backend && pytest tests/test_models.py::test_repository_model -v`

Expected: FAIL - models not defined

**Step 7: Create models.py with database schema**

Create `backend/app/models.py`:
```python
import enum
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base


class ResourceType(str, enum.Enum):
    TERRAFORM = "terraform"
    DOCKER = "docker"
    KUBERNETES = "kubernetes"


class DriftStatus(str, enum.Enum):
    NONE = "none"
    WARNING = "warning"
    CRITICAL = "critical"


class Severity(str, enum.Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class RemediationStatus(str, enum.Enum):
    NONE = "none"
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class RemediationType(str, enum.Enum):
    MANUAL = "manual"
    ONE_CLICK = "one_click"
    AUTOMATED = "automated"


class RemediationOutcome(str, enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    ROLLED_BACK = "rolled_back"


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    git_url = Column(String, nullable=False, unique=True)
    branch = Column(String, nullable=False, default="main")
    credentials_ref = Column(String, nullable=True)
    last_sync_timestamp = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    config_resources = relationship("ConfigResource", back_populates="repository")
    drift_reports = relationship("DriftReport", back_populates="repository")


class ConfigResource(Base):
    __tablename__ = "config_resources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"), nullable=False)
    resource_type = Column(Enum(ResourceType), nullable=False)
    resource_identifier = Column(String, nullable=False)
    expected_config = Column(JSON, nullable=False)
    source_file_path = Column(String, nullable=False)
    tags = Column(JSON, nullable=True)
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    repository = relationship("Repository", back_populates="config_resources")
    drift_reports = relationship("DriftReport", back_populates="config_resource")


class DriftReport(Base):
    __tablename__ = "drift_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    check_timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"), nullable=False)
    config_resource_id = Column(UUID(as_uuid=True), ForeignKey("config_resources.id"), nullable=False)
    drift_status = Column(Enum(DriftStatus), nullable=False)
    diff_details = Column(JSON, nullable=True)
    actual_state = Column(JSON, nullable=True)
    severity = Column(Enum(Severity), nullable=False)
    remediation_status = Column(Enum(RemediationStatus), nullable=False, default=RemediationStatus.NONE)
    error_message = Column(Text, nullable=True)
    datadog_event_id = Column(String, nullable=True)

    repository = relationship("Repository", back_populates="drift_reports")
    config_resource = relationship("ConfigResource", back_populates="drift_reports")
    remediation_history = relationship("RemediationHistory", back_populates="drift_report")


class RemediationHistory(Base):
    __tablename__ = "remediation_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    drift_report_id = Column(UUID(as_uuid=True), ForeignKey("drift_reports.id"), nullable=False)
    triggered_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    triggered_by = Column(String, nullable=False)
    remediation_type = Column(Enum(RemediationType), nullable=False)
    action_taken = Column(Text, nullable=False)
    outcome = Column(Enum(RemediationOutcome), nullable=False)
    error_details = Column(Text, nullable=True)

    drift_report = relationship("DriftReport", back_populates="remediation_history")
```

**Step 8: Run test to verify it passes**

Run: `cd backend && pytest tests/test_models.py::test_repository_model -v`

Expected: PASS

**Step 9: Commit database models**

```bash
git add backend/app/models.py backend/app/database.py backend/app/config.py backend/tests/
git commit -m "feat: add database models and configuration

- Define SQLAlchemy models for repositories, configs, drift reports, remediation history
- Add database connection management with connection pooling
- Create pydantic settings for environment configuration
- Add tests for database connection and model persistence

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 2: Config Ingestion Service

### Task 3: Terraform Parser

**Files:**
- Create: `backend/app/parsers/__init__.py`
- Create: `backend/app/parsers/terraform.py`
- Create: `backend/app/parsers/base.py`
- Create: `backend/tests/test_terraform_parser.py`
- Create: `backend/tests/fixtures/terraform/main.tf`

**Step 1: Write terraform parser test**

Create `backend/tests/fixtures/terraform/main.tf`:
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name        = "web-server"
    Environment = "production"
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
  acl    = "private"

  tags = {
    Name        = "data-bucket"
    Environment = "production"
  }
}
```

Create `backend/tests/test_terraform_parser.py`:
```python
import pytest
from pathlib import Path
from app.parsers.terraform import TerraformParser
from app.parsers.base import NormalizedResource
from app.models import ResourceType


@pytest.fixture
def terraform_parser():
    return TerraformParser()


@pytest.fixture
def sample_terraform_file():
    return Path(__file__).parent / "fixtures" / "terraform" / "main.tf"


def test_parse_terraform_file(terraform_parser, sample_terraform_file):
    """Test parsing Terraform file into normalized resources."""
    resources = terraform_parser.parse_file(sample_terraform_file)

    assert len(resources) == 2
    assert all(isinstance(r, NormalizedResource) for r in resources)

    web_instance = next(r for r in resources if r.resource_id == "aws_instance.web")
    assert web_instance.resource_type == ResourceType.TERRAFORM
    assert web_instance.properties["ami"] == "ami-0c55b159cbfafe1f0"
    assert web_instance.properties["instance_type"] == "t2.micro"
    assert web_instance.metadata["tags"]["Name"] == "web-server"
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_terraform_parser.py::test_parse_terraform_file -v`

Expected: FAIL - parser not implemented

**Step 3: Create base parser interface**

Create `backend/app/parsers/__init__.py`:
```python
from app.parsers.base import BaseParser, NormalizedResource
from app.parsers.terraform import TerraformParser

__all__ = ["BaseParser", "NormalizedResource", "TerraformParser"]
```

Create `backend/app/parsers/base.py`:
```python
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
```

**Step 4: Implement Terraform parser**

Create `backend/app/parsers/terraform.py`:
```python
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

    def _parse_resource_block(self, resource_block: List[Dict[str, Any]], source_file: str) -> List[NormalizedResource]:
        """Parse individual resource block."""
        normalized_resources = []

        for resource_type_dict in resource_block:
            for resource_type, resources_dict in resource_type_dict.items():
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
```

**Step 5: Run test to verify it passes**

Run: `cd backend && pytest tests/test_terraform_parser.py::test_parse_terraform_file -v`

Expected: PASS

**Step 6: Add validation test**

Add to `backend/tests/test_terraform_parser.py`:
```python
def test_validate_terraform_syntax(terraform_parser, sample_terraform_file):
    """Test Terraform syntax validation."""
    assert terraform_parser.validate_syntax(sample_terraform_file) is True

    # Test invalid file
    invalid_file = Path(__file__).parent / "fixtures" / "terraform" / "invalid.tf"
    invalid_file.parent.mkdir(parents=True, exist_ok=True)
    with open(invalid_file, 'w') as f:
        f.write("invalid { syntax")

    assert terraform_parser.validate_syntax(invalid_file) is False
```

**Step 7: Run validation test**

Run: `cd backend && pytest tests/test_terraform_parser.py::test_validate_terraform_syntax -v`

Expected: PASS

**Step 8: Commit Terraform parser**

```bash
git add backend/app/parsers/ backend/tests/
git commit -m "feat: add Terraform config parser

- Implement BaseParser interface for config parsers
- Add TerraformParser with HCL2 parsing
- Normalize Terraform resources into cloud-agnostic format
- Extract tags/labels as metadata
- Add syntax validation
- Include test fixtures and comprehensive tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 4: Git Repository Ingestion Service

**Files:**
- Create: `backend/app/services/__init__.py`
- Create: `backend/app/services/git_ingestion.py`
- Create: `backend/tests/test_git_ingestion.py`

**Step 1: Write git ingestion test**

Create `backend/tests/test_git_ingestion.py`:
```python
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from app.services.git_ingestion import GitIngestionService
from app.models import Repository, ResourceType
from app.parsers.terraform import TerraformParser


@pytest.fixture
def git_service():
    return GitIngestionService()


@pytest.fixture
def mock_repository():
    repo = Mock(spec=Repository)
    repo.git_url = "https://github.com/example/repo.git"
    repo.branch = "main"
    repo.credentials_ref = None
    return repo


def test_clone_repository(git_service, mock_repository, tmp_path):
    """Test cloning a git repository."""
    with patch('git.Repo.clone_from') as mock_clone:
        mock_repo = MagicMock()
        mock_clone.return_value = mock_repo

        cloned_path = git_service.clone_repository(mock_repository, str(tmp_path))

        assert cloned_path.exists()
        mock_clone.assert_called_once()


def test_find_config_files(git_service, tmp_path):
    """Test finding config files in repository."""
    # Create test structure
    terraform_dir = tmp_path / "terraform"
    terraform_dir.mkdir()
    (terraform_dir / "main.tf").touch()
    (terraform_dir / "variables.tf").touch()

    config_files = git_service.find_config_files(tmp_path)

    assert len(config_files) >= 2
    assert any(f.name == "main.tf" for f in config_files)
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_git_ingestion.py::test_clone_repository -v`

Expected: FAIL - service not implemented

**Step 3: Implement GitIngestionService**

Create `backend/app/services/__init__.py`:
```python
from app.services.git_ingestion import GitIngestionService

__all__ = ["GitIngestionService"]
```

Create `backend/app/services/git_ingestion.py`:
```python
import shutil
from pathlib import Path
from typing import List, Optional
from git import Repo
from app.models import Repository, ResourceType
from app.parsers import TerraformParser, NormalizedResource


class GitIngestionService:
    """Service for ingesting configs from git repositories."""

    def __init__(self, workspace_dir: str = "/tmp/driftguard"):
        self.workspace_dir = Path(workspace_dir)
        self.workspace_dir.mkdir(parents=True, exist_ok=True)
        self.terraform_parser = TerraformParser()

    def clone_repository(self, repository: Repository, target_dir: Optional[str] = None) -> Path:
        """Clone git repository to local workspace."""
        if target_dir is None:
            # Use repository ID as subdirectory
            target_dir = self.workspace_dir / str(repository.id)
        else:
            target_dir = Path(target_dir)

        # Remove existing directory if present
        if target_dir.exists():
            shutil.rmtree(target_dir)

        target_dir.mkdir(parents=True, exist_ok=True)

        # Clone repository
        Repo.clone_from(
            repository.git_url,
            target_dir,
            branch=repository.branch,
            depth=1  # Shallow clone for efficiency
        )

        return target_dir

    def find_config_files(self, repo_path: Path) -> List[Path]:
        """Find all config files in repository."""
        config_files = []

        # Find Terraform files
        config_files.extend(repo_path.rglob("*.tf"))

        # Find Docker Compose files
        config_files.extend(repo_path.rglob("docker-compose.yml"))
        config_files.extend(repo_path.rglob("docker-compose.yaml"))

        # Find Kubernetes manifests
        k8s_patterns = ["deployment.yml", "deployment.yaml", "service.yml", "service.yaml"]
        for pattern in k8s_patterns:
            config_files.extend(repo_path.rglob(pattern))

        return config_files

    def ingest_repository(self, repository: Repository) -> List[NormalizedResource]:
        """Clone repository and parse all config files."""
        # Clone repository
        repo_path = self.clone_repository(repository)

        # Find config files
        config_files = self.find_config_files(repo_path)

        # Parse config files
        all_resources = []
        for config_file in config_files:
            try:
                if config_file.suffix == ".tf":
                    resources = self.terraform_parser.parse_file(config_file)
                    all_resources.extend(resources)
                # TODO: Add Docker Compose and Kubernetes parsers
            except Exception as e:
                # Log error but continue processing other files
                print(f"Error parsing {config_file}: {e}")

        return all_resources

    def cleanup_workspace(self, repository: Repository):
        """Remove cloned repository from workspace."""
        target_dir = self.workspace_dir / str(repository.id)
        if target_dir.exists():
            shutil.rmtree(target_dir)
```

**Step 4: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_git_ingestion.py -v`

Expected: PASS

**Step 5: Commit git ingestion service**

```bash
git add backend/app/services/ backend/tests/test_git_ingestion.py
git commit -m "feat: add git repository ingestion service

- Implement GitIngestionService for cloning repositories
- Add config file discovery (Terraform, Docker Compose, K8s)
- Integrate with TerraformParser for resource extraction
- Include workspace management and cleanup
- Add comprehensive tests with mocking

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 3: Datadog Integration & Drift Detection

### Task 5: Datadog Client Wrapper

**Files:**
- Create: `backend/app/services/datadog_client.py`
- Create: `backend/tests/test_datadog_client.py`

**Step 1: Write Datadog client test**

Create `backend/tests/test_datadog_client.py`:
```python
import pytest
from unittest.mock import Mock, patch
from app.services.datadog_client import DatadogClient


@pytest.fixture
def datadog_client():
    return DatadogClient(api_key="test_key", app_key="test_app_key")


def test_get_infrastructure_list(datadog_client):
    """Test fetching infrastructure list from Datadog."""
    with patch('datadog_api_client.v1.api.hosts_api.HostsApi.list_hosts') as mock_list:
        mock_response = Mock()
        mock_response.host_list = [
            Mock(name="web-server-1", tags=["env:production", "team:backend"]),
            Mock(name="web-server-2", tags=["env:production", "team:backend"])
        ]
        mock_list.return_value = mock_response

        hosts = datadog_client.get_infrastructure_list()

        assert len(hosts) == 2
        assert hosts[0]["name"] == "web-server-1"
        assert "env:production" in hosts[0]["tags"]


def test_get_host_by_name(datadog_client):
    """Test fetching specific host by name."""
    with patch('datadog_api_client.v1.api.hosts_api.HostsApi.list_hosts') as mock_list:
        mock_response = Mock()
        mock_response.host_list = [
            Mock(name="web-server-1", tags=["env:production"], meta=Mock(agent_version="7.0.0"))
        ]
        mock_list.return_value = mock_response

        host = datadog_client.get_host_by_name("web-server-1")

        assert host is not None
        assert host["name"] == "web-server-1"
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_datadog_client.py::test_get_infrastructure_list -v`

Expected: FAIL - client not implemented

**Step 3: Implement DatadogClient**

Create `backend/app/services/datadog_client.py`:
```python
from typing import List, Dict, Any, Optional
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datadog_api_client.v1.api.events_api import EventsApi
from app.config import settings


class DatadogClient:
    """Wrapper for Datadog API client."""

    def __init__(self, api_key: Optional[str] = None, app_key: Optional[str] = None):
        self.api_key = api_key or settings.DATADOG_API_KEY
        self.app_key = app_key or settings.DATADOG_APP_KEY

        configuration = Configuration()
        configuration.api_key['apiKeyAuth'] = self.api_key
        configuration.api_key['appKeyAuth'] = self.app_key
        configuration.server_variables['site'] = settings.DATADOG_SITE

        self.api_client = ApiClient(configuration)
        self.hosts_api = HostsApi(self.api_client)
        self.metrics_api = MetricsApi(self.api_client)
        self.events_api = EventsApi(self.api_client)

    def get_infrastructure_list(self, filter_tags: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Fetch list of infrastructure hosts from Datadog."""
        try:
            response = self.hosts_api.list_hosts(filter=",".join(filter_tags) if filter_tags else None)

            hosts = []
            for host in response.host_list:
                hosts.append({
                    "name": host.name,
                    "tags": host.tags or [],
                    "meta": host.meta.to_dict() if host.meta else {},
                    "host_name": host.host_name,
                    "up": host.up
                })

            return hosts
        except Exception as e:
            raise Exception(f"Failed to fetch infrastructure list from Datadog: {e}")

    def get_host_by_name(self, host_name: str) -> Optional[Dict[str, Any]]:
        """Fetch specific host by name."""
        hosts = self.get_infrastructure_list()
        return next((h for h in hosts if h["name"] == host_name), None)

    def send_event(self, title: str, text: str, tags: Optional[List[str]] = None, alert_type: str = "info") -> str:
        """Send event to Datadog."""
        from datadog_api_client.v1.model.event_create_request import EventCreateRequest

        event = EventCreateRequest(
            title=title,
            text=text,
            tags=tags or [],
            alert_type=alert_type
        )

        response = self.events_api.create_event(body=event)
        return response.event.id

    def send_metric(self, metric_name: str, value: float, tags: Optional[List[str]] = None):
        """Send custom metric to Datadog."""
        from datadog_api_client.v1.model.metrics_payload import MetricsPayload
        from datadog_api_client.v1.model.series import Series
        import time

        series = Series(
            metric=metric_name,
            type="gauge",
            points=[[int(time.time()), value]],
            tags=tags or []
        )

        payload = MetricsPayload(series=[series])
        self.metrics_api.submit_metrics(body=payload)
```

**Step 4: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_datadog_client.py -v`

Expected: PASS

**Step 5: Commit Datadog client**

```bash
git add backend/app/services/datadog_client.py backend/tests/test_datadog_client.py
git commit -m "feat: add Datadog API client wrapper

- Implement DatadogClient for infrastructure monitoring
- Add methods for fetching hosts, sending events, and metrics
- Configure API client with credentials from environment
- Include comprehensive tests with API mocking

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### Task 6: Drift Detection Engine

**Files:**
- Create: `backend/app/services/drift_detector.py`
- Create: `backend/app/services/sensitive_data.py`
- Create: `backend/tests/test_drift_detector.py`

**Step 1: Write drift detector test**

Create `backend/tests/test_drift_detector.py`:
```python
import pytest
from app.services.drift_detector import DriftDetector, DriftResult
from app.parsers.base import NormalizedResource
from app.models import ResourceType, Severity


@pytest.fixture
def drift_detector():
    return DriftDetector()


def test_compare_resources_no_drift():
    """Test comparing resources with no drift."""
    expected = NormalizedResource(
        resource_id="aws_instance.web",
        resource_type=ResourceType.TERRAFORM,
        properties={"instance_type": "t2.micro", "ami": "ami-12345"},
        metadata={"tags": {"Name": "web-server"}},
        source_file="main.tf"
    )

    actual = {
        "instance_type": "t2.micro",
        "ami": "ami-12345",
        "tags": {"Name": "web-server"}
    }

    detector = DriftDetector()
    result = detector.compare_resources(expected, actual)

    assert result.has_drift is False
    assert result.severity == Severity.INFO
    assert len(result.diffs) == 0


def test_compare_resources_with_drift():
    """Test comparing resources with configuration drift."""
    expected = NormalizedResource(
        resource_id="aws_instance.web",
        resource_type=ResourceType.TERRAFORM,
        properties={"instance_type": "t2.micro", "ami": "ami-12345"},
        metadata={"tags": {"Name": "web-server"}},
        source_file="main.tf"
    )

    actual = {
        "instance_type": "t2.small",  # Drift detected
        "ami": "ami-12345",
        "tags": {"Name": "web-server"}
    }

    detector = DriftDetector()
    result = detector.compare_resources(expected, actual)

    assert result.has_drift is True
    assert result.severity == Severity.WARNING
    assert len(result.diffs) == 1
    assert result.diffs[0]["property_path"] == "instance_type"
    assert result.diffs[0]["expected_value"] == "t2.micro"
    assert result.diffs[0]["actual_value"] == "t2.small"
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_drift_detector.py::test_compare_resources_no_drift -v`

Expected: FAIL - detector not implemented

**Step 3: Implement sensitive data redactor**

Create `backend/app/services/sensitive_data.py`:
```python
import re
from typing import Dict, Any


class SensitiveDataRedactor:
    """Redact sensitive data from configs and diffs."""

    # Patterns for common secrets
    PATTERNS = {
        "aws_access_key": re.compile(r'AKIA[0-9A-Z]{16}'),
        "aws_secret_key": re.compile(r'[A-Za-z0-9/+=]{40}'),
        "api_key": re.compile(r'(?i)(api[_-]?key|apikey)["\']?\s*[:=]\s*["\']?([A-Za-z0-9_\-]+)["\']?'),
        "password": re.compile(r'(?i)(password|passwd|pwd)["\']?\s*[:=]\s*["\']?([^"\'\s]+)["\']?'),
        "token": re.compile(r'(?i)(token|bearer)["\']?\s*[:=]\s*["\']?([A-Za-z0-9_\-\.]+)["\']?'),
        "private_key": re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    }

    REDACTED_VALUE = "***REDACTED***"

    @classmethod
    def redact_dict(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively redact sensitive data from dictionary."""
        redacted = {}

        for key, value in data.items():
            if isinstance(value, dict):
                redacted[key] = cls.redact_dict(value)
            elif isinstance(value, str):
                redacted[key] = cls.redact_string(value)
            else:
                redacted[key] = value

        return redacted

    @classmethod
    def redact_string(cls, text: str) -> str:
        """Redact sensitive patterns from string."""
        for pattern_name, pattern in cls.PATTERNS.items():
            if pattern.search(text):
                return cls.REDACTED_VALUE
        return text
```

**Step 4: Implement DriftDetector**

Create `backend/app/services/drift_detector.py`:
```python
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
from app.parsers.base import NormalizedResource
from app.models import Severity
from app.services.sensitive_data import SensitiveDataRedactor


@dataclass
class DriftDiff:
    """Represents a single drift difference."""
    property_path: str
    expected_value: Any
    actual_value: Any
    drift_type: str
    suggested_action: str


@dataclass
class DriftResult:
    """Result of drift detection."""
    resource_id: str
    has_drift: bool
    severity: Severity
    diffs: List[Dict[str, Any]]
    actual_state: Dict[str, Any]
    error: Optional[str] = None


class DriftDetector:
    """Engine for detecting configuration drift."""

    def __init__(self):
        self.redactor = SensitiveDataRedactor()

    def compare_resources(self, expected: NormalizedResource, actual: Dict[str, Any]) -> DriftResult:
        """Compare expected config against actual state."""
        diffs = []

        # Compare all expected properties
        for key, expected_value in expected.properties.items():
            actual_value = actual.get(key)

            if actual_value != expected_value:
                diffs.append({
                    "property_path": key,
                    "expected_value": expected_value,
                    "actual_value": actual_value,
                    "drift_type": "value_mismatch" if actual_value is not None else "missing_property",
                    "suggested_action": "Update config to match actual state" if actual_value is not None else "Add missing property"
                })

        # Check for extra properties in actual state
        for key in actual.keys():
            if key not in expected.properties and key not in ["tags", "labels"]:
                diffs.append({
                    "property_path": key,
                    "expected_value": None,
                    "actual_value": actual[key],
                    "drift_type": "extra_property",
                    "suggested_action": "Remove undeclared property or add to config"
                })

        # Determine severity
        severity = self._classify_severity(diffs, expected)

        # Redact sensitive data
        redacted_actual = self.redactor.redact_dict(actual)
        redacted_diffs = [self.redactor.redact_dict(d) for d in diffs]

        return DriftResult(
            resource_id=expected.resource_id,
            has_drift=len(diffs) > 0,
            severity=severity,
            diffs=redacted_diffs,
            actual_state=redacted_actual
        )

    def _classify_severity(self, diffs: List[Dict[str, Any]], resource: NormalizedResource) -> Severity:
        """Classify drift severity based on changes."""
        if not diffs:
            return Severity.INFO

        # Check for security-related changes
        security_keywords = ["security", "encryption", "ssl", "tls", "password", "key", "secret"]
        for diff in diffs:
            prop_path = diff["property_path"].lower()
            if any(keyword in prop_path for keyword in security_keywords):
                return Severity.CRITICAL

        # Check for missing properties
        if any(d["drift_type"] == "missing_property" for d in diffs):
            return Severity.CRITICAL

        # Default to warning for value mismatches
        return Severity.WARNING

    def detect_missing_resources(self, expected_resources: List[NormalizedResource], actual_resources: List[Dict[str, Any]]) -> List[DriftResult]:
        """Detect resources that exist in config but not in actual infrastructure."""
        actual_ids = {r.get("resource_id") for r in actual_resources}
        missing = []

        for expected in expected_resources:
            if expected.resource_id not in actual_ids:
                missing.append(DriftResult(
                    resource_id=expected.resource_id,
                    has_drift=True,
                    severity=Severity.CRITICAL,
                    diffs=[{
                        "property_path": "resource",
                        "expected_value": "exists",
                        "actual_value": "missing",
                        "drift_type": "missing_resource",
                        "suggested_action": "Deploy missing resource or remove from config"
                    }],
                    actual_state={}
                ))

        return missing
```

**Step 5: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_drift_detector.py -v`

Expected: PASS

**Step 6: Add sensitive data redaction test**

Add to `backend/tests/test_drift_detector.py`:
```python
def test_sensitive_data_redaction():
    """Test that sensitive data is redacted in diffs."""
    from app.services.sensitive_data import SensitiveDataRedactor

    data = {
        "database_url": "postgresql://user:secret_password@localhost:5432/db",
        "api_key": "AKIAIOSFODNN7EXAMPLE",
        "normal_config": "safe_value"
    }

    redactor = SensitiveDataRedactor()
    redacted = redactor.redact_dict(data)

    assert redacted["database_url"] == SensitiveDataRedactor.REDACTED_VALUE
    assert redacted["api_key"] == SensitiveDataRedactor.REDACTED_VALUE
    assert redacted["normal_config"] == "safe_value"
```

**Step 7: Run redaction test**

Run: `cd backend && pytest tests/test_drift_detector.py::test_sensitive_data_redaction -v`

Expected: PASS

**Step 8: Commit drift detection engine**

```bash
git add backend/app/services/drift_detector.py backend/app/services/sensitive_data.py backend/tests/test_drift_detector.py
git commit -m "feat: add drift detection engine with sensitive data redaction

- Implement DriftDetector for comparing expected vs actual configs
- Add severity classification (info, warning, critical)
- Implement SensitiveDataRedactor for security
- Detect missing resources, value mismatches, extra properties
- Generate actionable diff suggestions
- Include comprehensive tests

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 4: Event Queue & Workers

### Task 7: Redis Queue Setup

**Files:**
- Create: `backend/app/queue/__init__.py`
- Create: `backend/app/queue/tasks.py`
- Create: `backend/app/queue/worker.py`
- Create: `backend/tests/test_queue.py`

**Step 1: Write queue task test**

Create `backend/tests/test_queue.py`:
```python
import pytest
from unittest.mock import Mock, patch
from app.queue.tasks import run_drift_detection_job
from app.models import Repository, ResourceType


@pytest.fixture
def mock_repository():
    repo = Mock(spec=Repository)
    repo.id = "test-repo-id"
    repo.git_url = "https://github.com/example/repo.git"
    repo.branch = "main"
    return repo


def test_drift_detection_task_enqueue():
    """Test enqueueing drift detection task."""
    from app.queue.tasks import enqueue_drift_detection

    with patch('rq.Queue.enqueue') as mock_enqueue:
        repository_id = "test-repo-id"
        job = enqueue_drift_detection(repository_id)

        mock_enqueue.assert_called_once()
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_queue.py::test_drift_detection_task_enqueue -v`

Expected: FAIL - queue tasks not implemented

**Step 3: Implement queue tasks**

Create `backend/app/queue/__init__.py`:
```python
from app.queue.tasks import enqueue_drift_detection, run_drift_detection_job
from app.queue.worker import start_worker

__all__ = ["enqueue_drift_detection", "run_drift_detection_job", "start_worker"]
```

Create `backend/app/queue/tasks.py`:
```python
import redis
from rq import Queue
from typing import Optional
from app.config import settings
from app.models import Repository, ConfigResource, DriftReport, DriftStatus, RemediationStatus
from app.services.git_ingestion import GitIngestionService
from app.services.drift_detector import DriftDetector
from app.services.datadog_client import DatadogClient
from app.database import SessionLocal


# Initialize Redis connection
redis_conn = redis.from_url(settings.REDIS_URL)
drift_queue = Queue('drift_detection', connection=redis_conn)


def enqueue_drift_detection(repository_id: str, priority: str = "normal") -> str:
    """Enqueue a drift detection job for a repository."""
    job = drift_queue.enqueue(
        run_drift_detection_job,
        repository_id,
        job_timeout='10m'
    )
    return job.id


def run_drift_detection_job(repository_id: str):
    """Execute drift detection for a repository."""
    db = SessionLocal()

    try:
        # Fetch repository
        repository = db.query(Repository).filter_by(id=repository_id).first()
        if not repository:
            raise ValueError(f"Repository {repository_id} not found")

        # Initialize services
        git_service = GitIngestionService()
        detector = DriftDetector()
        datadog_client = DatadogClient()

        # Ingest configs from git
        normalized_resources = git_service.ingest_repository(repository)

        # Store configs in database
        for resource in normalized_resources:
            config_resource = ConfigResource(
                repository_id=repository.id,
                resource_type=resource.resource_type,
                resource_identifier=resource.resource_id,
                expected_config={"properties": resource.properties},
                source_file_path=resource.source_file,
                tags=resource.metadata
            )
            db.add(config_resource)

        db.commit()

        # Fetch actual state from Datadog
        actual_hosts = datadog_client.get_infrastructure_list()

        # Run drift detection
        drift_results = []
        for resource in normalized_resources:
            # Map resource to Datadog host (simplified for MVP)
            actual_state = {}
            for host in actual_hosts:
                if resource.resource_id in host.get("name", ""):
                    actual_state = host
                    break

            result = detector.compare_resources(resource, actual_state)
            drift_results.append(result)

            # Store drift report
            config_resource = db.query(ConfigResource).filter_by(
                resource_identifier=resource.resource_id
            ).first()

            if config_resource:
                drift_report = DriftReport(
                    repository_id=repository.id,
                    config_resource_id=config_resource.id,
                    drift_status=DriftStatus.CRITICAL if result.has_drift else DriftStatus.NONE,
                    diff_details=result.diffs,
                    actual_state=result.actual_state,
                    severity=result.severity,
                    remediation_status=RemediationStatus.NONE
                )
                db.add(drift_report)

        db.commit()

        # Send Datadog event for drift detection
        drift_count = sum(1 for r in drift_results if r.has_drift)
        if drift_count > 0:
            datadog_client.send_event(
                title=f"Drift Detected: {repository.git_url}",
                text=f"Found {drift_count} resources with configuration drift",
                tags=[f"repository:{repository.git_url}", "service:driftguard"],
                alert_type="warning"
            )

        # Send metrics
        datadog_client.send_metric(
            "driftguard.drift.count",
            float(drift_count),
            tags=[f"repository:{repository.id}", "severity:warning"]
        )

        # Cleanup workspace
        git_service.cleanup_workspace(repository)

        return {"drift_count": drift_count, "total_resources": len(normalized_resources)}

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
```

**Step 4: Implement worker process**

Create `backend/app/queue/worker.py`:
```python
import redis
from rq import Worker
from app.config import settings


def start_worker():
    """Start RQ worker for processing drift detection jobs."""
    redis_conn = redis.from_url(settings.REDIS_URL)

    worker = Worker(['drift_detection'], connection=redis_conn)
    worker.work()


if __name__ == '__main__':
    start_worker()
```

**Step 5: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_queue.py -v`

Expected: PASS

**Step 6: Commit queue implementation**

```bash
git add backend/app/queue/ backend/tests/test_queue.py
git commit -m "feat: add Redis queue for async drift detection

- Implement RQ-based task queue with Redis backend
- Add drift detection job that orchestrates full pipeline
- Integrate git ingestion, parsing, Datadog API, and drift detection
- Store results in database and send Datadog events/metrics
- Include worker process for job execution
- Add tests for task enqueueing

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 5: FastAPI Web API

### Task 8: REST API Endpoints

**Files:**
- Create: `backend/app/main.py`
- Create: `backend/app/api/__init__.py`
- Create: `backend/app/api/repositories.py`
- Create: `backend/app/api/drift.py`
- Create: `backend/tests/test_api.py`

**Step 1: Write API endpoint test**

Create `backend/tests/test_api.py`:
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_repository(client):
    """Test creating a repository."""
    payload = {
        "git_url": "https://github.com/example/repo.git",
        "branch": "main"
    }

    response = client.post("/api/v1/repositories", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["git_url"] == payload["git_url"]


def test_list_repositories(client):
    """Test listing repositories."""
    response = client.get("/api/v1/repositories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

**Step 2: Run test to verify it fails**

Run: `cd backend && pytest tests/test_api.py::test_health_check -v`

Expected: FAIL - API not implemented

**Step 3: Create FastAPI main application**

Create `backend/app/main.py`:
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import repositories, drift
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DriftGuard API",
    description="Infrastructure drift detection API",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(repositories.router, prefix="/api/v1", tags=["repositories"])
app.include_router(drift.router, prefix="/api/v1", tags=["drift"])


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "driftguard"}
```

**Step 4: Implement repositories API**

Create `backend/app/api/__init__.py`:
```python
# API module initialization
```

Create `backend/app/api/repositories.py`:
```python
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Repository
from app.queue.tasks import enqueue_drift_detection


router = APIRouter()


class RepositoryCreate(BaseModel):
    git_url: str
    branch: str = "main"
    credentials_ref: str = None


class RepositoryResponse(BaseModel):
    id: UUID
    git_url: str
    branch: str
    last_sync_timestamp: str = None

    class Config:
        from_attributes = True


@router.post("/repositories", response_model=RepositoryResponse, status_code=201)
async def create_repository(repository: RepositoryCreate, db: Session = Depends(get_db)):
    """Create a new repository for monitoring."""
    db_repository = Repository(
        git_url=repository.git_url,
        branch=repository.branch,
        credentials_ref=repository.credentials_ref
    )
    db.add(db_repository)
    db.commit()
    db.refresh(db_repository)

    # Trigger initial drift detection
    enqueue_drift_detection(str(db_repository.id))

    return db_repository


@router.get("/repositories", response_model=List[RepositoryResponse])
async def list_repositories(db: Session = Depends(get_db)):
    """List all monitored repositories."""
    repositories = db.query(Repository).all()
    return repositories


@router.get("/repositories/{repository_id}", response_model=RepositoryResponse)
async def get_repository(repository_id: UUID, db: Session = Depends(get_db)):
    """Get a specific repository by ID."""
    repository = db.query(Repository).filter_by(id=repository_id).first()
    if not repository:
        raise HTTPException(status_code=404, detail="Repository not found")
    return repository


@router.post("/repositories/{repository_id}/scan")
async def trigger_scan(repository_id: UUID, db: Session = Depends(get_db)):
    """Trigger drift detection scan for a repository."""
    repository = db.query(Repository).filter_by(id=repository_id).first()
    if not repository:
        raise HTTPException(status_code=404, detail="Repository not found")

    job_id = enqueue_drift_detection(str(repository_id))
    return {"job_id": job_id, "status": "queued"}
```

**Step 5: Implement drift API**

Create `backend/app/api/drift.py`:
```python
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DriftReport, DriftStatus, Severity


router = APIRouter()


class DriftReportResponse(BaseModel):
    id: UUID
    check_timestamp: str
    repository_id: UUID
    config_resource_id: UUID
    drift_status: DriftStatus
    severity: Severity
    diff_details: dict = None
    remediation_status: str

    class Config:
        from_attributes = True


@router.get("/drift", response_model=List[DriftReportResponse])
async def list_drift_reports(
    repository_id: UUID = None,
    severity: Severity = None,
    drift_status: DriftStatus = None,
    limit: int = Query(default=100, le=1000),
    db: Session = Depends(get_db)
):
    """List drift reports with optional filtering."""
    query = db.query(DriftReport)

    if repository_id:
        query = query.filter(DriftReport.repository_id == repository_id)
    if severity:
        query = query.filter(DriftReport.severity == severity)
    if drift_status:
        query = query.filter(DriftReport.drift_status == drift_status)

    reports = query.order_by(DriftReport.check_timestamp.desc()).limit(limit).all()
    return reports


@router.get("/drift/{drift_id}", response_model=DriftReportResponse)
async def get_drift_report(drift_id: UUID, db: Session = Depends(get_db)):
    """Get a specific drift report by ID."""
    report = db.query(DriftReport).filter_by(id=drift_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Drift report not found")
    return report
```

**Step 6: Run tests to verify they pass**

Run: `cd backend && pytest tests/test_api.py -v`

Expected: PASS

**Step 7: Commit FastAPI implementation**

```bash
git add backend/app/main.py backend/app/api/ backend/tests/test_api.py
git commit -m "feat: add FastAPI REST API for DriftGuard

- Implement health check and API routing
- Add repositories endpoints (create, list, get, trigger scan)
- Add drift reports endpoints with filtering
- Integrate with queue for async drift detection
- Include comprehensive API tests
- Add CORS middleware for frontend integration

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 6: Frontend Dashboard (Simplified MVP)

### Task 9: React Dashboard Setup

**Files:**
- Create: `frontend/package.json`
- Create: `frontend/vite.config.ts`
- Create: `frontend/tsconfig.json`
- Create: `frontend/index.html`
- Create: `frontend/src/main.tsx`
- Create: `frontend/src/App.tsx`

**Step 1: Initialize frontend structure**

```bash
mkdir -p frontend/src/components frontend/src/services frontend/src/types
```

**Step 2: Create package.json**

Create `frontend/package.json`:
```json
{
  "name": "driftguard-frontend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext ts,tsx"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.28.0",
    "axios": "^1.7.9"
  },
  "devDependencies": {
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.3.4",
    "typescript": "^5.7.2",
    "vite": "^6.0.5"
  }
}
```

**Step 3: Create Vite config**

Create `frontend/vite.config.ts`:
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

**Step 4: Create TypeScript config**

Create `frontend/tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

**Step 5: Create index.html**

Create `frontend/index.html`:
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DriftGuard - Keep Your Infrastructure in Check</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

**Step 6: Create main.tsx**

Create `frontend/src/main.tsx`:
```typescript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
```

**Step 7: Create App.tsx**

Create `frontend/src/App.tsx`:
```typescript
import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <header className="app-header">
          <h1>DriftGuard</h1>
          <p>Keep Your Infrastructure in Check</p>
        </header>
        <main className="app-main">
          <Routes>
            <Route path="/" element={<Dashboard />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
```

**Step 8: Create basic dashboard component**

Create `frontend/src/components/Dashboard.tsx`:
```typescript
import React, { useEffect, useState } from 'react'
import { apiClient } from '../services/api'
import { DriftReport } from '../types'

const Dashboard: React.FC = () => {
  const [driftReports, setDriftReports] = useState<DriftReport[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchDriftReports()
  }, [])

  const fetchDriftReports = async () => {
    try {
      const reports = await apiClient.listDriftReports()
      setDriftReports(reports)
    } catch (error) {
      console.error('Failed to fetch drift reports:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Loading drift reports...</div>
  }

  return (
    <div className="dashboard">
      <h2>Drift Reports</h2>
      <div className="drift-reports">
        {driftReports.length === 0 ? (
          <p>No drift reports found</p>
        ) : (
          driftReports.map(report => (
            <div key={report.id} className={`drift-card drift-${report.severity}`}>
              <h3>Resource: {report.config_resource_id}</h3>
              <p>Status: {report.drift_status}</p>
              <p>Severity: {report.severity}</p>
              <p>Checked: {new Date(report.check_timestamp).toLocaleString()}</p>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default Dashboard
```

**Step 9: Create API client service**

Create `frontend/src/services/api.ts`:
```typescript
import axios from 'axios'
import { DriftReport, Repository } from '../types'

const API_BASE_URL = '/api/v1'

const axiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const apiClient = {
  listDriftReports: async (): Promise<DriftReport[]> => {
    const response = await axiosInstance.get('/drift')
    return response.data
  },

  listRepositories: async (): Promise<Repository[]> => {
    const response = await axiosInstance.get('/repositories')
    return response.data
  },

  createRepository: async (gitUrl: string, branch: string): Promise<Repository> => {
    const response = await axiosInstance.post('/repositories', { git_url: gitUrl, branch })
    return response.data
  }
}
```

**Step 10: Create TypeScript types**

Create `frontend/src/types/index.ts`:
```typescript
export interface DriftReport {
  id: string
  check_timestamp: string
  repository_id: string
  config_resource_id: string
  drift_status: 'none' | 'warning' | 'critical'
  severity: 'info' | 'warning' | 'critical'
  diff_details: any
  remediation_status: string
}

export interface Repository {
  id: string
  git_url: string
  branch: string
  last_sync_timestamp: string | null
}
```

**Step 11: Create basic CSS**

Create `frontend/src/App.css`:
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'IBM Plex Sans', sans-serif;
  background: #F9FAFB;
  color: #1F2937;
}

.app {
  min-height: 100vh;
}

.app-header {
  background: linear-gradient(135deg, #632CA6 0%, #4B2283 100%);
  color: white;
  padding: 2rem;
  text-align: center;
}

.app-header h1 {
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.app-main {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 2rem;
}

.dashboard h2 {
  font-size: 1.75rem;
  margin-bottom: 1.5rem;
  color: #632CA6;
}

.drift-reports {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.drift-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-left: 4px solid;
}

.drift-card.drift-info {
  border-left-color: #0066FF;
}

.drift-card.drift-warning {
  border-left-color: #FBBF24;
}

.drift-card.drift-critical {
  border-left-color: #EF4444;
}

.drift-card h3 {
  font-size: 1.125rem;
  margin-bottom: 0.75rem;
  font-weight: 600;
}

.drift-card p {
  margin-bottom: 0.5rem;
  color: #6B7280;
}

.loading {
  text-align: center;
  padding: 4rem;
  font-size: 1.25rem;
  color: #6B7280;
}
```

Create `frontend/src/index.css`:
```css
:root {
  font-family: 'IBM Plex Sans', sans-serif;
  line-height: 1.5;
  font-weight: 400;
}
```

**Step 12: Commit frontend implementation**

```bash
git add frontend/
git commit -m "feat: add React frontend dashboard with Vite

- Initialize React + TypeScript project with Vite
- Implement DriftGuard design system (Datadog purple theme, IBM Plex fonts)
- Add dashboard component for viewing drift reports
- Create API client service for backend integration
- Add TypeScript types for type safety
- Include responsive card-based layout
- Proxy API requests through Vite dev server

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Phase 7: Deployment & Documentation

### Task 10: Docker Deployment Setup

**Files:**
- Create: `backend/Dockerfile`
- Create: `frontend/Dockerfile`
- Update: `docker-compose.yml`
- Create: `docs/DEPLOYMENT.md`

**Step 1: Create backend Dockerfile**

Create `backend/Dockerfile`:
```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Expose port
EXPOSE 8000

# Run migrations and start server
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Step 2: Create frontend Dockerfile**

Create `frontend/Dockerfile`:
```dockerfile
FROM node:20-alpine as builder

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built files
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Step 3: Create nginx config**

Create `frontend/nginx.conf`:
```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Step 4: Update docker-compose.yml**

Update `docker-compose.yml`:
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: driftguard
      POSTGRES_PASSWORD: driftguard
      POSTGRES_DB: driftguard
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U driftguard"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      DATABASE_URL: postgresql://driftguard:driftguard@postgres:5432/driftguard
      REDIS_URL: redis://redis:6379/0
      DATADOG_API_KEY: ${DATADOG_API_KEY}
      DATADOG_APP_KEY: ${DATADOG_APP_KEY}
      DATADOG_SITE: ${DATADOG_SITE:-datadoghq.com}
      APP_ENV: ${APP_ENV:-development}
      LOG_LEVEL: ${LOG_LEVEL:-INFO}
      SECRET_KEY: ${SECRET_KEY}
    ports:
      - "8000:8000"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./backend/app:/app/app

  worker:
    build:
      context: ./backend
      dockerfile: Dockerfile
    command: python -m app.queue.worker
    environment:
      DATABASE_URL: postgresql://driftguard:driftguard@postgres:5432/driftguard
      REDIS_URL: redis://redis:6379/0
      DATADOG_API_KEY: ${DATADOG_API_KEY}
      DATADOG_APP_KEY: ${DATADOG_APP_KEY}
      DATADOG_SITE: ${DATADOG_SITE:-datadoghq.com}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  postgres_data:
  redis_data:
```

**Step 5: Create deployment documentation**

Create `docs/DEPLOYMENT.md`:
```markdown
# DriftGuard Deployment Guide

## Prerequisites

- Docker and Docker Compose
- Datadog API credentials
- Git repositories to monitor

## Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/TaraScho/hackathon-team-3.git
   cd hackathon-team-3
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Datadog credentials
   ```

3. **Start services**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Production Deployment

### Kubernetes Deployment

1. **Create secrets**
   ```bash
   kubectl create secret generic driftguard-secrets \
     --from-literal=database-url=<your-db-url> \
     --from-literal=datadog-api-key=<your-api-key> \
     --from-literal=datadog-app-key=<your-app-key>
   ```

2. **Apply manifests**
   ```bash
   kubectl apply -f k8s/
   ```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| DATABASE_URL | PostgreSQL connection string | Yes |
| REDIS_URL | Redis connection string | Yes |
| DATADOG_API_KEY | Datadog API key | Yes |
| DATADOG_APP_KEY | Datadog application key | Yes |
| DATADOG_SITE | Datadog site (default: datadoghq.com) | No |
| SECRET_KEY | Application secret key | Yes |
| APP_ENV | Environment (development/production) | No |
| LOG_LEVEL | Logging level | No |

## Monitoring

DriftGuard automatically sends metrics and events to Datadog:

- **Metrics**: `driftguard.drift.count`, `driftguard.detection.duration_ms`
- **Events**: Drift detection alerts
- **Logs**: Structured application logs

## Troubleshooting

### Worker not processing jobs

Check worker logs:
```bash
docker-compose logs worker
```

Verify Redis connection:
```bash
docker-compose exec redis redis-cli ping
```

### Database migration issues

Run migrations manually:
```bash
docker-compose exec backend alembic upgrade head
```
```

**Step 6: Commit deployment setup**

```bash
git add backend/Dockerfile frontend/Dockerfile frontend/nginx.conf docker-compose.yml docs/DEPLOYMENT.md
git commit -m "feat: add Docker deployment configuration

- Create Dockerfiles for backend and frontend
- Update docker-compose with all services (postgres, redis, backend, worker, frontend)
- Add nginx configuration for frontend proxy
- Include deployment documentation
- Configure health checks and dependencies
- Add environment variable documentation

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Summary

This implementation plan covers:

1. **Project Setup**: Database schema, models, configuration
2. **Config Ingestion**: Terraform parser, git repository ingestion
3. **Drift Detection**: Datadog client, drift detection engine, sensitive data redaction
4. **Event Queue**: Redis queue, async workers, job orchestration
5. **Web API**: FastAPI REST endpoints for repositories and drift reports
6. **Frontend**: React dashboard with DriftGuard design system
7. **Deployment**: Docker containers, docker-compose orchestration

**MVP Features Delivered:**
- Terraform config parsing and normalization
- Git repository ingestion
- Datadog infrastructure state retrieval
- Drift detection with severity classification
- Sensitive data redaction
- Async job processing with Redis/RQ
- REST API for repositories and drift reports
- React dashboard for viewing drift
- Docker deployment setup

**Future Enhancements (Post-MVP):**
- Docker Compose and Kubernetes parsers
- Remediation workflows (view, one-click, auto)
- Git webhook integration
- Scheduler for periodic checks
- Policy-based evaluation
- Advanced UI features (filtering, search, charts)
- Datadog app integration

---

## Execution Options

Plan complete and saved to `docs/plans/2026-02-19-driftguard-mvp-implementation.md`.

**Two execution options:**

1. **Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

2. **Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?**
