from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IntIdMixin
from app.models.enums import AnalysisStatus, DocumentStatus


class Document(Base, IntIdMixin):
    """Uploaded document belonging to a project."""

    __tablename__ = "documents"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_documents_uuid"),
        UniqueConstraint("checksum", name="uq_documents_checksum"),
    )

    uuid: Mapped[UUID] = mapped_column(default=uuid4, nullable=False, unique=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    stored_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_path: Mapped[str] = mapped_column(String(1000), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False)
    file_size_bytes: Mapped[int] = mapped_column(nullable=False)
    checksum: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True)
    version: Mapped[str] = mapped_column(String(50), nullable=False, default="1.0")
    status: Mapped[DocumentStatus] = mapped_column(String(50), nullable=False, default=DocumentStatus.UPLOADED, index=True)
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    project: Mapped["Project"] = relationship(back_populates="documents")
    analysis_records: Mapped[list["Analysis"]] = relationship(back_populates="document", cascade="all, delete-orphan")
