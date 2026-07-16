from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class ReportDTO:
    """DTO for report data transfer."""

    id: int
    uuid: UUID
    analysis_id: int
    overall_score: float | None
    recommendation: str | None
    report_path: str | None
    generated_at: datetime
