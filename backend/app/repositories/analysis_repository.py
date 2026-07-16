from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analysis import Analysis
from app.models.enums import AnalysisStatus
from app.repositories.base_repository import BaseRepository


class AnalysisRepository(BaseRepository[Analysis]):
    """Repository for analysis persistence operations."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Analysis)

    async def get_pending(self) -> list[Analysis]:
        """Return analyses that are waiting to be processed."""
        result = await self._session.execute(select(Analysis).where(Analysis.status == AnalysisStatus.PENDING).order_by(Analysis.created_at.asc()))
        return list(result.scalars().all())

    async def update_status(self, analysis: Analysis, status: AnalysisStatus) -> Analysis:
        """Update the status of an analysis."""
        analysis.status = status
        return await self.update(analysis)

    async def list_document_analysis(self, document_id: int) -> list[Analysis]:
        """Return all analyses for a document."""
        result = await self._session.execute(select(Analysis).where(Analysis.document_id == document_id).order_by(Analysis.created_at.asc()))
        return list(result.scalars().all())
