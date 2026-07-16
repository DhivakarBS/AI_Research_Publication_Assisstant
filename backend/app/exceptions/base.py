from __future__ import annotations

from typing import Any


class ApplicationException(Exception):
    """Base exception for application-level failures."""

    def __init__(self, error_code: str, message: str, http_status: int = 500) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.message = message
        self.http_status = http_status

    def to_dict(self) -> dict[str, Any]:
        """Return the exception payload for serialization."""
        return {"error_code": self.error_code, "message": self.message, "http_status": self.http_status}
