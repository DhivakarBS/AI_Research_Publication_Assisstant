from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import AnalysisStatus


class AnalysisBase(BaseModel):
    analysis_type: str = Field(..., min_length=1, max_length=100)
    status: AnalysisStatus = AnalysisStatus.PENDING
    engine_version: str = Field(default="1.0.0", max_length=50)


class AnalysisCreate(AnalysisBase):
    document_id: int


class AnalysisUpdate(BaseModel):
    analysis_type: str | None = Field(default=None, min_length=1, max_length=100)
    status: AnalysisStatus | None = None
    engine_version: str | None = Field(default=None, max_length=50)
    started_at: datetime | None = None
    completed_at: datetime | None = None


class AnalysisRead(AnalysisBase):
    id: int
    uuid: UUID
    document_id: int
    started_at: datetime | None = None
    completed_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
