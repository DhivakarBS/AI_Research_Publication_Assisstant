from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """Standard error payload for future API layers."""

    success: bool = False
    error_code: str = Field(default="unknown_error")
    message: str = Field(default="An unexpected error occurred")
    http_status: int = 500
