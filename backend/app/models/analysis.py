from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IntIdMixin, TimestampMixin
from app.models.enums import AnalysisStatus


class Analysis(Base, IntIdMixin, TimestampMixin):
    """Analysis execution record for a document."""

    __tablename__ = "analyses"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_analyses_uuid"),
    )

    uuid: Mapped[UUID] = mapped_column(default=uuid4, nullable=False, unique=True, index=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id", ondelete="CASCADE"), nullable=False, index=True)
    analysis_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    status: Mapped[AnalysisStatus] = mapped_column(String(50), nullable=False, default=AnalysisStatus.PENDING, index=True)
    engine_version: Mapped[str] = mapped_column(String(50), nullable=False, default="1.0.0")
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, index=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True, index=True)

    document: Mapped["Document"] = relationship(back_populates="analysis_records")
    report: Mapped["Report | None"] = relationship(back_populates="analysis", cascade="all, delete-orphan")
