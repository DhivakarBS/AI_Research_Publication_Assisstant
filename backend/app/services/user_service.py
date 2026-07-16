from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    """Service layer for user persistence operations."""

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    async def create_user(self, user: User) -> User:
        """Persist a new user."""
        return await self._repository.create(user)

    async def get_user_by_email(self, email: str) -> User | None:
        """Retrieve a user by email."""
        return await self._repository.get_by_email(email)

    async def list_users(self) -> list[User]:
        """Return all users."""
        return await self._repository.list_users()
