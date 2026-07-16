from __future__ import annotations

from pathlib import Path
from typing import Protocol

from app.core.config import get_app_config
from app.core.logger import get_logger
from app.exceptions.document import DocumentException


class DocumentStorage(Protocol):
    """Abstract storage contract for document files."""

    def save(self, content: bytes, filename: str) -> str:
        """Persist bytes to storage and return a relative path."""
        ...

    def delete(self, relative_path: str) -> None:
        """Delete a stored file."""
        ...

    def exists(self, relative_path: str) -> bool:
        """Check whether a stored file exists."""
        ...

    def get_relative_path(self, filename: str) -> str:
        """Return the storage path for a filename."""
        ...


class LocalDocumentStorage:
    """Local filesystem implementation of document storage."""

    def __init__(self) -> None:
        self._config = get_app_config()
        self._logger = get_logger(__name__)
        self._root = Path(self._config.upload_directory)
        self._root.mkdir(parents=True, exist_ok=True)

    def save(self, content: bytes, filename: str) -> str:
        """Persist a file on disk."""
        destination = self._root / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        self._logger.info("Stored document file", extra={"filename": filename})
        return self.get_relative_path(filename)

    def delete(self, relative_path: str) -> None:
        """Delete a file from disk if it exists."""
        full_path = self._root / relative_path
        if full_path.exists():
            full_path.unlink()

    def exists(self, relative_path: str) -> bool:
        """Return whether a file exists."""
        return (self._root / relative_path).exists()

    def get_relative_path(self, filename: str) -> str:
        """Return a relative path for the storage location."""
        return Path(filename).as_posix()
