from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.document_repository import DocumentRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.report_repository import ReportRepository
from app.repositories.user_repository import UserRepository


def get_user_repository(session: AsyncSession) -> UserRepository:
    """Create a user repository from the injected session."""
    return UserRepository(session)


def get_project_repository(session: AsyncSession) -> ProjectRepository:
    """Create a project repository from the injected session."""
    return ProjectRepository(session)


def get_document_repository(session: AsyncSession) -> DocumentRepository:
    """Create a document repository from the injected session."""
    return DocumentRepository(session)


def get_analysis_repository(session: AsyncSession) -> AnalysisRepository:
    """Create an analysis repository from the injected session."""
    return AnalysisRepository(session)


def get_report_repository(session: AsyncSession) -> ReportRepository:
    """Create a report repository from the injected session."""
    return ReportRepository(session)
