from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import DocumentStatus


class DocumentBase(BaseModel):
    original_filename: str = Field(..., min_length=1, max_length=255)
    stored_filename: str = Field(..., min_length=1, max_length=255)
    storage_path: str = Field(..., min_length=1, max_length=1000)
    mime_type: str = Field(..., min_length=1, max_length=100)
    file_size_bytes: int = Field(..., ge=0)
    checksum: str = Field(..., min_length=64, max_length=64)
    version: str = Field(default="1.0", max_length=50)
    status: DocumentStatus = DocumentStatus.UPLOADED


class DocumentCreate(DocumentBase):
    project_id: int


class DocumentUpdate(BaseModel):
    original_filename: str | None = Field(default=None, min_length=1, max_length=255)
    stored_filename: str | None = Field(default=None, min_length=1, max_length=255)
    storage_path: str | None = Field(default=None, min_length=1, max_length=1000)
    mime_type: str | None = Field(default=None, min_length=1, max_length=100)
    file_size_bytes: int | None = Field(default=None, ge=0)
    checksum: str | None = Field(default=None, min_length=64, max_length=64)
    version: str | None = Field(default=None, max_length=50)


class DocumentRead(DocumentBase):
    id: int
    uuid: UUID
    project_id: int
    uploaded_at: datetime

    model_config = {"from_attributes": True}
