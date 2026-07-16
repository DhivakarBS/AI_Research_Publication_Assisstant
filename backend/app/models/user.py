from __future__ import annotations

from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, IntIdMixin, TimestampMixin
from app.models.enums import UserRole


class User(Base, IntIdMixin, TimestampMixin):
    """Application user account."""

    __tablename__ = "users"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_users_uuid"),
        UniqueConstraint("email", name="uq_users_email"),
    )

    uuid: Mapped[UUID] = mapped_column(default=uuid4, nullable=False, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(String(50), nullable=False, default=UserRole.STUDENT, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, index=True)

    projects: Mapped[list["Project"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
