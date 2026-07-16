from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/researchai"
    secret_key: str = "researchai-dev-secret"
    upload_directory: str = "../storage/uploads"
    report_directory: str = "../storage/reports"
    max_upload_size: int = 10 * 1024 * 1024
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()
