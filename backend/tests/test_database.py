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
