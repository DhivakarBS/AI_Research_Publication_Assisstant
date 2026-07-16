from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class DocumentUploadPayload:
    """Input payload for document upload processing."""

    project_id: int
    original_filename: str | None
    mime_type: str | None
    content: bytes


@dataclass(frozen=True)
class DocumentDTO:
    """DTO for document data transfer."""

    id: int
    uuid: UUID
    project_id: int
    original_filename: str
    stored_filename: str
    storage_path: str
    mime_type: str
    file_size: int
    checksum: str
    version: str
    uploaded_at: datetime
