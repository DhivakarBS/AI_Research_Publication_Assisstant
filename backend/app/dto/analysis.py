from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class AnalysisDTO:
    """DTO for analysis data transfer."""

    id: int
    uuid: UUID
    document_id: int
    analysis_type: str
    status: str
    engine_version: str
    started_at: datetime | None
    completed_at: datetime | None
    created_at: datetime
    updated_at: datetime
