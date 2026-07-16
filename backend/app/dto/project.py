from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class ProjectDTO:
    """DTO for project data transfer."""

    id: int
    uuid: UUID
    title: str
    description: str | None
    status: str
    user_id: int
    created_at: datetime
    updated_at: datetime
