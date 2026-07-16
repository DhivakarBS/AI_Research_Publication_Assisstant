from app.models.report import Report
from app.repositories.report_repository import ReportRepository


class ReportService:
    """Service layer for report persistence operations."""

    def __init__(self, repository: ReportRepository) -> None:
        self._repository = repository

    async def create_report(self, report: Report) -> Report:
        """Persist a new report."""
        return await self._repository.create(report)

    async def get_report_by_analysis(self, analysis_id: int) -> Report | None:
        """Return the report associated with an analysis."""
        return await self._repository.get_by_analysis(analysis_id)

    async def list_reports(self) -> list[Report]:
        """Return all reports."""
        return await self._repository.list_reports()
