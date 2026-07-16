from app.exceptions.base import ApplicationException


class DocumentException(ApplicationException):
    """Raised for document-related infrastructure errors."""

    def __init__(self, message: str, error_code: str = "document_error", http_status: int = 400) -> None:
        super().__init__(error_code=error_code, message=message, http_status=http_status)
