from pathlib import Path

from app.parser.document_parser import DocumentParser


def test_document_parser_parses_pdf_structure() -> None:
    """The parser should return structured metadata and page-level content for a sample PDF."""
    sample_pdf = Path(__file__).resolve().parent / "sample.pdf"
    if not sample_pdf.exists():
        return

    parser = DocumentParser()
    parsed_document = parser.parse(sample_pdf)

    assert parsed_document.metadata.page_count >= 1
    assert parsed_document.pages
    assert parsed_document.pages[0].page_number == 1
