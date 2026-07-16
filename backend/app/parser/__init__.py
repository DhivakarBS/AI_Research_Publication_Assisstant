"""Document parser package."""

from app.parser.document_parser import DocumentParser
from app.parser.image_parser import ImageParser
from app.parser.metadata_parser import MetadataParser
from app.parser.page_parser import PageParser
from app.parser.parser_service import ParserService
from app.parser.pdf_reader import PDFReader
from app.parser.text_parser import TextParser

__all__ = [
    "DocumentParser",
    "ImageParser",
    "MetadataParser",
    "PageParser",
    "ParserService",
    "PDFReader",
    "TextParser",
]
