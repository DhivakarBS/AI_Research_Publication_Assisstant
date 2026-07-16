from app.database.session import Base, engine
from app.models import Analysis, Document, Project, Report, User


def init_database() -> None:
    """Create all tables for the current metadata."""
    Base.metadata.create_all(bind=engine)
