from dataclasses import dataclass

from app.config.settings import get_settings


@dataclass(frozen=True)
class AppConfig:
    """Centralized application constants derived from settings."""

    upload_directory: str
    report_directory: str
    max_upload_size: int
    log_level: str


def get_app_config() -> AppConfig:
    """Build the application configuration object."""
    settings = get_settings()
    return AppConfig(
        upload_directory=settings.upload_directory,
        report_directory=settings.report_directory,
        max_upload_size=settings.max_upload_size,
        log_level=settings.log_level,
    )
