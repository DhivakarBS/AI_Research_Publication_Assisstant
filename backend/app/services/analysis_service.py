from app.models.analysis import Analysis
from app.models.enums import AnalysisStatus
from app.repositories.analysis_repository import AnalysisRepository


class AnalysisService:
    """Service layer for analysis persistence operations."""

    def __init__(self, repository: AnalysisRepository) -> None:
        self._repository = repository

    async def create_analysis(self, analysis: Analysis) -> Analysis:
        """Persist a new analysis."""
        return await self._repository.create(analysis)

    async def get_pending_analyses(self) -> list[Analysis]:
        """Return pending analyses."""
        return await self._repository.get_pending()

    async def update_analysis_status(self, analysis: Analysis, status: AnalysisStatus) -> Analysis:
        """Update the execution status of an analysis."""
        return await self._repository.update_status(analysis, status)

    async def list_document_analyses(self, document_id: int) -> list[Analysis]:
        """Return all analyses for a document."""
        return await self._repository.list_document_analysis(document_id)
