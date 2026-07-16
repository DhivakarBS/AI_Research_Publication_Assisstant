import hashlib

from app.exceptions.validation import ValidationException


class ChecksumValidator:
    """Validate a SHA256 checksum string."""

    @staticmethod
    def validate(value: str) -> str:
        if not isinstance(value, str) or len(value) != 64:
            raise ValidationException("Checksum must be a 64-character SHA256 value", error_code="invalid_checksum")
        try:
            int(value, 16)
        except ValueError as exc:
            raise ValidationException("Checksum must be hexadecimal", error_code="invalid_checksum") from exc
        return value
