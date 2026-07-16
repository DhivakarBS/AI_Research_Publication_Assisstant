from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import AsyncSessionLocal
from app.uow.unit_of_work import UnitOfWork


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provide a database session for dependency injection."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


def get_unit_of_work(session: AsyncSession) -> UnitOfWork:
    """Create a unit of work from the injected session."""
    return UnitOfWork(session)
