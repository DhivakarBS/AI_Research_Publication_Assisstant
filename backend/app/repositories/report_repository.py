from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.report import Report
from app.repositories.base_repository import BaseRepository


class ReportRepository(BaseRepository[Report]):
    """Repository for report persistence operations."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Report)

    async def get_by_analysis(self, analysis_id: int) -> Report | None:
        """Fetch a report by analysis identifier."""
        result = await self._session.execute(select(Report).where(Report.analysis_id == analysis_id))
        return result.scalar_one_or_none()

    async def list_reports(self) -> list[Report]:
        """Return all reports."""
        result = await self._session.execute(select(Report).order_by(Report.generated_at.asc()))
        return list(result.scalars().all())
