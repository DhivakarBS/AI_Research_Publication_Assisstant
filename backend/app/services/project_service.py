from app.models.enums import ProjectStatus
from app.models.project import Project
from app.repositories.project_repository import ProjectRepository


class ProjectService:
    """Service layer for project persistence operations."""

    def __init__(self, repository: ProjectRepository) -> None:
        self._repository = repository

    async def create_project(self, project: Project) -> Project:
        """Persist a new project."""
        return await self._repository.create(project)

    async def get_projects_by_user(self, user_id: int) -> list[Project]:
        """Return all projects for a user."""
        return await self._repository.get_projects_by_user(user_id)

    async def update_project_status(self, project: Project, status: ProjectStatus) -> Project:
        """Update a project status."""
        return await self._repository.update_status(project, status)
