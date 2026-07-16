from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginationResponse(BaseModel, Generic[T]):
    """Reusable pagination envelope."""

    items: list[T] = Field(default_factory=list)
    page: int = 1
    page_size: int = 20
    total: int = 0
