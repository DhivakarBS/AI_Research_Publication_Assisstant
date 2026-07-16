from fastapi import APIRouter, Depends

from app.services.health_service import HealthService

router = APIRouter(prefix="/api", tags=["health"])


def get_health_service() -> HealthService:
    """Create a health service instance."""
    return HealthService()


@router.get("/health")
def health_check(service: HealthService = Depends(get_health_service)) -> dict[str, str]:
    """Return the service health payload."""
    return service.get_health_payload()
