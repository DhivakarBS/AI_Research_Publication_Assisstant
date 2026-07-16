from __future__ import annotations

from uuid import UUID, uuid4

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IntIdMixin, TimestampMixin
from app.models.enums import ProjectStatus


class Project(Base, IntIdMixin, TimestampMixin):
    """Research project owned by a user."""

    __tablename__ = "projects"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_projects_uuid"),
    )

    uuid: Mapped[UUID] = mapped_column(default=uuid4, nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    status: Mapped[ProjectStatus] = mapped_column(String(50), nullable=False, default=ProjectStatus.DRAFT, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)

    owner: Mapped["User"] = relationship(back_populates="projects")
    documents: Mapped[list["Document"]] = relationship(back_populates="project", cascade="all, delete-orphan")
