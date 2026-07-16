from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    """DTO for user data transfer."""

    id: int
    uuid: UUID
    full_name: str
    email: str
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
