from __future__ import annotations

from pathlib import Path

from app.models.parsed.parsed_document import ParsedDocument
from app.parser.parser_service import ParserService


class DocumentParser:
    """Parse PDF files into structured ResearchAI models."""

    def __init__(self, parser_service: ParserService | None = None) -> None:
        self._parser_service = parser_service or ParserService()

    def parse(self, file_path: str | Path) -> ParsedDocument:
        """Parse a PDF file and return structured parsed document models."""
        return self._parser_service.parse_file(file_path)

    def parse_file(self, file_path: str | Path) -> ParsedDocument:
        """Alias for parse for clearer service-style usage."""
        return self.parse(file_path)
