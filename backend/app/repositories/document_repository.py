from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.repositories.base_repository import BaseRepository


class DocumentRepository(BaseRepository[Document]):
    """Repository for document persistence operations."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Document)

    async def get_by_checksum(self, checksum: str) -> Document | None:
        """Fetch a document by checksum."""
        result = await self._session.execute(select(Document).where(Document.checksum == checksum))
        return result.scalar_one_or_none()

    async def get_latest_version(self, project_id: int) -> Document | None:
        """Fetch the latest document version for a project."""
        result = await self._session.execute(
            select(Document).where(Document.project_id == project_id).order_by(Document.uploaded_at.desc(), Document.id.desc())
        )
        return result.scalar_one_or_none()

    async def list_project_documents(self, project_id: int) -> list[Document]:
        """Return all documents associated with a project."""
        result = await self._session.execute(select(Document).where(Document.project_id == project_id).order_by(Document.uploaded_at.asc()))
        return list(result.scalars().all())
