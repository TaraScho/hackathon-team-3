"""
FastAPI main application entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import repositories, drift

# Initialize FastAPI app
app = FastAPI(
    title="DriftGuard API",
    description="Infrastructure drift detection REST API",
    version="0.1.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(repositories.router, prefix="/api/repositories", tags=["repositories"])
app.include_router(drift.router, prefix="/api/drift", tags=["drift"])


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
