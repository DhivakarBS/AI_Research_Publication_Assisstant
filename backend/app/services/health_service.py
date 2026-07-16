class HealthService:
    """Service abstraction for health checks."""

    def get_health_payload(self) -> dict[str, str]:
        """Return the health payload."""
        return {
            "status": "healthy",
            "service": "ResearchAI IEEE Compliance Engine",
            "version": "1.0.0",
        }
