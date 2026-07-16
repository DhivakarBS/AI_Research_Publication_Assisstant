from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelT = TypeVar("ModelT", bound=DeclarativeBase)


class BaseRepository(Generic[ModelT]):
    """Generic repository for common database operations."""

    def __init__(self, session: AsyncSession, model_class: type[ModelT]) -> None:
        self._session = session
        self._model_class = model_class

    async def create(self, instance: ModelT) -> ModelT:
        """Persist a new instance and return it."""
        self._session.add(instance)
        await self._session.flush()
        return instance

    async def get_by_id(self, record_id: int) -> ModelT | None:
        """Fetch a row by integer primary key."""
        result = await self._session.execute(select(self._model_class).where(self._model_class.id == record_id))
        return result.scalar_one_or_none()

    async def get_by_uuid(self, uuid_value: str) -> ModelT | None:
        """Fetch a row by UUID."""
        result = await self._session.execute(select(self._model_class).where(self._model_class.uuid == uuid_value))
        return result.scalar_one_or_none()

    async def get_all(self) -> list[ModelT]:
        """Return all rows for the model."""
        result = await self._session.execute(select(self._model_class))
        return list(result.scalars().all())

    async def update(self, instance: ModelT) -> ModelT:
        """Persist changes to an existing instance."""
        self._session.add(instance)
        await self._session.flush()
        return instance

    async def delete(self, instance: ModelT) -> None:
        """Delete an instance."""
        await self._session.delete(instance)
        await self._session.flush()

    async def exists(self, *, record_id: int | None = None, uuid_value: str | None = None) -> bool:
        """Check whether a matching record exists."""
        if record_id is not None:
            result = await self._session.execute(select(self._model_class.id).where(self._model_class.id == record_id))
            return result.scalar_one_or_none() is not None
        if uuid_value is not None:
            result = await self._session.execute(select(self._model_class.id).where(self._model_class.uuid == uuid_value))
            return result.scalar_one_or_none() is not None
        return False

    async def count(self) -> int:
        """Count all rows for the model."""
        result = await self._session.execute(select(self._model_class))
        return len(result.scalars().all())
