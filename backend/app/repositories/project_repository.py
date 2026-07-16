from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.enums import ProjectStatus
from app.models.project import Project
from app.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    """Repository for project persistence operations."""

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Project)

    async def get_projects_by_user(self, user_id: int) -> list[Project]:
        """Return all projects owned by the given user."""
        result = await self._session.execute(select(Project).where(Project.user_id == user_id).order_by(Project.created_at.asc()))
        return list(result.scalars().all())

    async def update_status(self, project: Project, status: ProjectStatus) -> Project:
        """Update the status of a project."""
        project.status = status
        return await self.update(project)
