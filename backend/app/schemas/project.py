from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import ProjectStatus


class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    status: ProjectStatus = ProjectStatus.DRAFT


class ProjectCreate(ProjectBase):
    user_id: int


class ProjectUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    status: ProjectStatus | None = None


class ProjectRead(ProjectBase):
    id: int
    uuid: UUID
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
