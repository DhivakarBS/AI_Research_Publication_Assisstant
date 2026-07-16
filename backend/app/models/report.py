from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IntIdMixin
from app.models.enums import RecommendationStatus


class Report(Base, IntIdMixin):
    """Report generated for an analysis."""

    __tablename__ = "reports"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_reports_uuid"),
    )

    uuid: Mapped[UUID] = mapped_column(default=uuid4, nullable=False, unique=True, index=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    overall_score: Mapped[float | None] = mapped_column(nullable=True)
    recommendation: Mapped[RecommendationStatus | None] = mapped_column(String(50), nullable=True, index=True)
    report_path: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    generated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    analysis: Mapped["Analysis"] = relationship(back_populates="report")
