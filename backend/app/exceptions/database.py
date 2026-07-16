from app.exceptions.base import ApplicationException


class DatabaseException(ApplicationException):
    """Raised for persistence-layer errors."""

    def __init__(self, message: str, error_code: str = "database_error", http_status: int = 500) -> None:
        super().__init__(error_code=error_code, message=message, http_status=http_status)
