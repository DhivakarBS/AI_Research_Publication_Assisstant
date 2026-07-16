from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import RecommendationStatus


class ReportBase(BaseModel):
    overall_score: float | None = None
    recommendation: RecommendationStatus | None = None
    report_path: str | None = Field(default=None, max_length=1000)


class ReportCreate(ReportBase):
    analysis_id: int


class ReportUpdate(BaseModel):
    overall_score: float | None = None
    recommendation: RecommendationStatus | None = None
    report_path: str | None = Field(default=None, max_length=1000)


class ReportRead(ReportBase):
    id: int
    uuid: UUID
    analysis_id: int
    generated_at: datetime

    model_config = {"from_attributes": True}
