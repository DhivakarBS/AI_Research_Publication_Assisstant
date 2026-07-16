from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from app.core.config import get_app_config
from app.core.logger import get_logger
from app.dto.document import DocumentUploadPayload
from app.exceptions.document import DocumentException
from app.exceptions.validation import ValidationException
from app.models.document import Document
from app.models.enums import DocumentStatus
from app.storage.document_storage import LocalDocumentStorage
from app.validators.checksum import ChecksumValidator
from app.validators.email import EmailValidator
from app.validators.filename import FilenameValidator
from app.uow.unit_of_work import UnitOfWork


class DocumentService:
    """Service layer for document upload and registration."""

    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._logger = get_logger(__name__)
        self._storage = LocalDocumentStorage()
        self._config = get_app_config()

    async def upload_document(self, payload: DocumentUploadPayload) -> Document:
        """Validate, save, and register a document."""
        if payload.content is None:
            raise ValidationException("File content is required", error_code="missing_file")
        if not payload.content:
            raise ValidationException("Uploaded file is empty", error_code="empty_file")
        if payload.original_filename is None:
            raise ValidationException("Filename is required", error_code="invalid_filename")

        filename = FilenameValidator.validate(payload.original_filename)
        if not filename.lower().endswith(".pdf"):
            raise ValidationException("Only PDF files are allowed", error_code="invalid_extension")

        if len(payload.content) > self._config.max_upload_size:
            raise ValidationException("File size exceeds configured limit", error_code="file_too_large")

        if payload.mime_type != "application/pdf":
            raise ValidationException("Only PDF MIME type is accepted", error_code="invalid_mime_type")

        checksum = hashlib.sha256(payload.content).hexdigest()
        ChecksumValidator.validate(checksum)

        existing = await self._unit_of_work.documents.get_by_checksum(checksum)
        if existing is not None:
            raise DocumentException("Duplicate document checksum detected", error_code="duplicate_checksum")

        stored_uuid = str(uuid4())
        stored_filename = f"{stored_uuid}.pdf"
        relative_dir = datetime.now(timezone.utc).strftime("%Y/%m")
        storage_path = f"{relative_dir}/{stored_filename}"
        relative_path = self._storage.save(payload.content, storage_path)

        document = Document(
            project_id=payload.project_id,
            original_filename=filename,
            stored_filename=stored_filename,
            storage_path=relative_path,
            mime_type=payload.mime_type,
            file_size_bytes=len(payload.content),
            checksum=checksum,
            version="1.0",
            status=DocumentStatus.UPLOADED,
            uploaded_at=datetime.now(timezone.utc),
        )

        created = await self._unit_of_work.documents.create(document)
        await self._unit_of_work.commit()
        self._logger.info("Uploaded document", extra={"document_uuid": str(created.uuid)})
        return created

    async def create_document(self, document: Document) -> Document:
        """Persist a new document."""
        return await self._unit_of_work.documents.create(document)

    async def get_document_by_checksum(self, checksum: str) -> Document | None:
        """Return a document by checksum."""
        return await self._unit_of_work.documents.get_by_checksum(checksum)

    async def get_latest_document(self, project_id: int) -> Document | None:
        """Return the latest document version for a project."""
        return await self._unit_of_work.documents.get_latest_version(project_id)

    async def list_project_documents(self, project_id: int) -> list[Document]:
        """Return all documents for a project."""
        return await self._unit_of_work.documents.list_project_documents(project_id)
