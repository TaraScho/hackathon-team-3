"""
Repository management API endpoints.
"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models import Repository
from app.database import get_db
from app.queue.tasks import enqueue_drift_detection

router = APIRouter()


class RepositoryCreate(BaseModel):
    """Schema for creating a repository."""
    name: str
    url: str
    branch: str = "main"


class RepositoryResponse(BaseModel):
    """Schema for repository response."""
    id: str
    name: str
    url: str
    branch: str
    created_at: datetime
    last_scan_at: Optional[datetime] = None

    class Config:
        from_attributes = True


@router.post("", response_model=RepositoryResponse, status_code=201)
async def create_repository(
    repo: RepositoryCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new repository and trigger initial drift scan.
    """
    # Check if repository already exists
    existing = db.query(Repository).filter(
        Repository.git_url == repo.url,
        Repository.branch == repo.branch
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Repository already exists")

    # Create repository
    db_repo = Repository(
        git_url=repo.url,
        branch=repo.branch
    )
    db.add(db_repo)
    db.commit()
    db.refresh(db_repo)

    # Enqueue drift detection job
    enqueue_drift_detection(db_repo.id)

    # Return response with mapped fields
    return {
        "id": str(db_repo.id),
        "name": repo.name,  # Store name in response but not DB for now
        "url": db_repo.git_url,
        "branch": db_repo.branch,
        "created_at": db_repo.created_at,
        "last_scan_at": db_repo.last_sync_timestamp
    }


@router.get("", response_model=List[RepositoryResponse])
async def list_repositories(db: Session = Depends(get_db)):
    """
    List all repositories.
    """
    repositories = db.query(Repository).all()
    # Map database fields to response fields
    return [
        {
            "id": str(repo.id),
            "name": repo.git_url.split('/')[-1].replace('.git', ''),  # Extract name from URL
            "url": repo.git_url,
            "branch": repo.branch,
            "created_at": repo.created_at,
            "last_scan_at": repo.last_sync_timestamp
        }
        for repo in repositories
    ]


@router.get("/{repo_id}", response_model=RepositoryResponse)
async def get_repository(repo_id: str, db: Session = Depends(get_db)):
    """
    Get a specific repository by ID.
    """
    try:
        repo_uuid = UUID(repo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid repository ID format")

    repo = db.query(Repository).filter(Repository.id == repo_uuid).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")

    return {
        "id": str(repo.id),
        "name": repo.git_url.split('/')[-1].replace('.git', ''),
        "url": repo.git_url,
        "branch": repo.branch,
        "created_at": repo.created_at,
        "last_scan_at": repo.last_sync_timestamp
    }


@router.post("/{repo_id}/scan", status_code=202)
async def trigger_scan(repo_id: str, db: Session = Depends(get_db)):
    """
    Trigger a drift detection scan for a repository.
    """
    try:
        repo_uuid = UUID(repo_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid repository ID format")

    repo = db.query(Repository).filter(Repository.id == repo_uuid).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")

    # Enqueue drift detection job
    job_id = enqueue_drift_detection(repo.id)

    return {
        "message": "Drift detection scan enqueued",
        "job_id": job_id,
        "repository_id": str(repo.id)
    }
