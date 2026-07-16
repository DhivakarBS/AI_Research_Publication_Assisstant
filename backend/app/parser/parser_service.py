from __future__ import annotations

from pathlib import Path
from typing import Any

from app.models.parsed.parsed_document import ParsedDocument
from app.parser.image_parser import ImageParser
from app.parser.metadata_parser import MetadataParser
from app.parser.page_parser import PageParser
from app.parser.pdf_reader import PDFReader
from app.parser.text_parser import TextParser


class ParserService:
    """Orchestrate deterministic PDF parsing into ResearchAI models."""

    def __init__(self) -> None:
        self._reader = PDFReader
        self._metadata_parser = MetadataParser()
        self._page_parser = PageParser()
        self._text_parser = TextParser()
        self._image_parser = ImageParser()

    def parse_file(self, file_path: str | Path) -> ParsedDocument:
        """Parse a PDF file and return custom parsed document models."""
        document = self._reader(file_path).open()
        try:
            metadata = self._metadata_parser.parse(document)
            pages: list[Any] = []
            for page_number in range(document.page_count):
                page = document.load_page(page_number)
                parsed_page = self._page_parser.parse(page, page_number + 1)
                parsed_page.text_blocks = self._text_parser.parse(page, page_number + 1)
                parsed_page.images = self._image_parser.parse(page, page_number + 1)
                pages.append(parsed_page)

            return ParsedDocument(metadata=metadata, pages=pages)
        finally:
            self._reader(file_path).close(document)
