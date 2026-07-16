from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from app.models.enums import UserRole


class UserBase(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    role: UserRole = UserRole.STUDENT
    is_active: bool = True


class UserCreate(UserBase):
    password_hash: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=255)
    email: EmailStr | None = None
    role: UserRole | None = None
    is_active: bool | None = None


class UserRead(UserBase):
    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
