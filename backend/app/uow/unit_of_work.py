from __future__ import annotations

from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.document_repository import DocumentRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.report_repository import ReportRepository
from app.repositories.user_repository import UserRepository

T = TypeVar("T")


class UnitOfWork(Generic[T]):
    """Reusable unit of work that manages the SQLAlchemy session lifecycle."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self.users = UserRepository(session)
        self.projects = ProjectRepository(session)
        self.documents = DocumentRepository(session)
        self.analyses = AnalysisRepository(session)
        self.reports = ReportRepository(session)

    async def commit(self) -> None:
        """Commit the current transaction."""
        await self._session.commit()

    async def rollback(self) -> None:
        """Rollback the current transaction."""
        await self._session.rollback()

    async def close(self) -> None:
        """Close the session."""
        await self._session.close()
