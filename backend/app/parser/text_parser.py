from __future__ import annotations

from typing import Any

from app.models.parsed.parsed_document import ParsedText


class TextParser:
    """Extract text spans exactly as represented in the PDF."""

    def parse(self, page: Any, page_number: int) -> list[ParsedText]:
        """Convert text blocks into ResearchAI models without inference or merging."""
        texts: list[ParsedText] = []
        for block in page.get_text("blocks"):
            text = block[4] if len(block) > 4 else ""
            bbox = list(block[:4])
            texts.append(
                ParsedText(
                    text=text,
                    bounding_box=bbox,
                    font_name="",
                    font_size=0.0,
                    font_flags=0,
                    color="",
                    rotation=0,
                )
            )
        return texts
