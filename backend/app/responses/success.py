from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    """Standard success payload for future API layers."""

    success: bool = True
    data: T | None = None
    message: str | None = None


class PaginationResponse(BaseModel, Generic[T]):
    """Standard paginated payload for future API layers."""

    items: list[T] = Field(default_factory=list)
    page: int = 1
    page_size: int = 20
    total: int = 0
