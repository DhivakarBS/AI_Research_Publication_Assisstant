import re

from app.exceptions.validation import ValidationException


class EmailValidator:
    """Validate the shape of an email address."""

    @staticmethod
    def validate(value: str) -> str:
        if not isinstance(value, str) or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
            raise ValidationException("Invalid email address", error_code="invalid_email")
        return value
