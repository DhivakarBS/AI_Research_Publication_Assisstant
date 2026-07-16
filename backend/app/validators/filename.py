from pathlib import Path

from app.exceptions.validation import ValidationException


class FilenameValidator:
    """Validate a filesystem-safe filename."""

    @staticmethod
    def validate(value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValidationException("Filename is required", error_code="invalid_filename")
        path = Path(value)
        if path.name != value or any(part in {"..", ""} for part in path.parts):
            raise ValidationException("Filename must be a simple file name", error_code="invalid_filename")
        return value
