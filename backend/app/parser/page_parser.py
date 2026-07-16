from __future__ import annotations

from typing import Any

from app.models.parsed.parsed_document import ParsedPage


class PageParser:
    """Extract raw page-level geometry from a PDF page."""

    def parse(self, page: Any, page_number: int) -> ParsedPage:
        """Return page geometry as a ResearchAI model."""
        rect = page.rect
        return ParsedPage(
            page_number=page_number,
            width=float(rect.width),
            height=float(rect.height),
            rotation=int(page.rotation),
            text_blocks=[],
            images=[],
        )
