from app.exceptions.base import ApplicationException


class ValidationException(ApplicationException):
    """Raised for deterministic validation failures."""

    def __init__(self, message: str, error_code: str = "validation_error", http_status: int = 400) -> None:
        super().__init__(error_code=error_code, message=message, http_status=http_status)
