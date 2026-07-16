from __future__ import annotations

from typing import Any

from app.core.logger import get_logger
from app.exceptions.document import DocumentException
from app.models.document import Document
from app.models.enums import DocumentStatus
from app.responses.error import ErrorResponse
from app.responses.success import SuccessResponse
from app.services.document_processing_service import DocumentProcessingService, ParserResult
from app.uow.unit_of_work import UnitOfWork


class SubmissionFacade:
    """Single public entry point for document processing workflows."""

    def __init__(self, unit_of_work: UnitOfWork, document_processing_service: DocumentProcessingService | None = None) -> None:
        self._unit_of_work = unit_of_work
        self._document_processing_service = document_processing_service or DocumentProcessingService(unit_of_work)
        self._logger = get_logger(__name__)

    async def submit_document(self, document_uuid: str) -> SuccessResponse | ErrorResponse:
        """Coordinate document submission and processing through the existing service layer."""
        document = await self._unit_of_work.documents.get_by_uuid(document_uuid)
        if document is None:
            self._logger.warning("Submission rejected because document could not be found", extra={"document_uuid": document_uuid})
            return ErrorResponse(error_code="document_not_found", message="Document not found", http_status=404)

        if document.status != DocumentStatus.UPLOADED:
            self._logger.info("Submission rejected because document is not eligible", extra={"document_uuid": document_uuid, "status": document.status.value})
            return ErrorResponse(error_code="document_not_eligible", message="Document is not eligible for processing", http_status=409)

        result = await self._document_processing_service.process_document(document_uuid)
        self._logger.info("Submission completed", extra={"document_uuid": document_uuid, "status": result.status.value})
        return SuccessResponse(data=result, message="Document processing completed")
