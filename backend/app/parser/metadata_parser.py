from __future__ import annotations

from datetime import datetime
from typing import Any

from app.models.parsed.parsed_document import ParsedMetadata


class MetadataParser:
    """Extract metadata-only information from a PDF document."""

    def parse(self, document: Any) -> ParsedMetadata:
        """Return a custom metadata container without exposing PyMuPDF objects."""
        metadata = document.metadata or {}
        return ParsedMetadata(
            title=str(metadata.get("title") or ""),
            author=str(metadata.get("author") or ""),
            creator=str(metadata.get("creator") or ""),
            producer=str(metadata.get("producer") or ""),
            subject=str(metadata.get("subject") or ""),
            keywords=str(metadata.get("keywords") or ""),
            creation_date=self._to_datetime(metadata.get("creationDate")),
            modification_date=self._to_datetime(metadata.get("modDate")),
            page_count=document.page_count,
            pdf_version=str(document.pdf_version or ""),
        )

    def _to_datetime(self, value: Any) -> datetime | None:
        if not value:
            return None
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(str(value))
        except ValueError:
            return None
