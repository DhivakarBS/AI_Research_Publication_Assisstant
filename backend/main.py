from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.documents import router as documents_router
from app.config.logging import configure_logging
from app.config.settings import get_settings

settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(
    title="ResearchAI",
    description="ResearchAI IEEE Compliance Engine",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(documents_router)


@app.on_event("startup")
async def startup_event() -> None:
    """Log application startup."""
    import logging

    logging.getLogger("researchai").info("Application startup")


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Log application shutdown."""
    import logging

    logging.getLogger("researchai").info("Application shutdown")
