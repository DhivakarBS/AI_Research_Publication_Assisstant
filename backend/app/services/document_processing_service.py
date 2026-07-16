from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID

from app.core.logger import get_logger
from app.exceptions.document import DocumentException
from app.models.document import Document
from app.models.enums import DocumentStatus
from app.models.parsed.parsed_document import ParsedDocument
from app.parser.document_parser import DocumentParser
from app.uow.unit_of_work import UnitOfWork


@dataclass(slots=True)
class ParserResult:
    """Envelope returned by the document processing orchestrator."""

    document_uuid: UUID
    status: DocumentStatus
    parsed_document: ParsedDocument | None = None
    error_message: str | None = None


class DocumentProcessingService:
    """Coordinate document processing without knowing parser internals."""

    def __init__(self, unit_of_work: UnitOfWork, parser_service: DocumentParser | None = None) -> None:
        self._unit_of_work = unit_of_work
        self._parser_service = parser_service or DocumentParser()
        self._logger = get_logger(__name__)

    async def process_document(self, document_uuid: str | UUID) -> ParserResult:
        """Load a document, parse it, and update its lifecycle state."""
        document_id = str(document_uuid)
        document = await self._unit_of_work.documents.get_by_uuid(document_id)
        if document is None:
            raise DocumentException("Document not found", error_code="document_not_found")

        if document.status != DocumentStatus.UPLOADED:
            self._logger.info("Document skipped because state is not uploaded", extra={"document_uuid": document_id, "status": document.status.value})
            return ParserResult(document_uuid=document.uuid, status=document.status)

        document.status = DocumentStatus.PROCESSING
        await self._unit_of_work.documents.update(document)
        await self._unit_of_work.commit()

        try:
            parsed_document = self._parser_service.parse_file(document.storage_path)
            document.status = DocumentStatus.PARSED
            await self._unit_of_work.documents.update(document)
            await self._unit_of_work.commit()
            self._logger.info("Document parsed successfully", extra={"document_uuid": document_id})
            return ParserResult(document_uuid=document.uuid, status=document.status, parsed_document=parsed_document)
        except Exception as exc:  # pragma: no cover - graceful orchestration boundary
            document.status = DocumentStatus.FAILED
            await self._unit_of_work.documents.update(document)
            await self._unit_of_work.commit()
            message = str(exc) or "Document parsing failed"
            self._logger.exception("Document parsing failed", extra={"document_uuid": document_id})
            return ParserResult(document_uuid=document.uuid, status=document.status, error_message=message)
