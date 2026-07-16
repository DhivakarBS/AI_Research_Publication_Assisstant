from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for user persistence operations."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User)

    async def get_by_email(self, email: str) -> User | None:
        """Fetch a user by email."""
        result = await self._session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def email_exists(self, email: str) -> bool:
        """Check whether a user with the supplied email exists."""
        result = await self._session.execute(select(User.id).where(User.email == email))
        return result.scalar_one_or_none() is not None

    async def list_users(self) -> list[User]:
        """Return all users."""
        result = await self._session.execute(select(User).order_by(User.created_at.asc()))
        return list(result.scalars().all())
