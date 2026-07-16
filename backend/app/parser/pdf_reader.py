from __future__ import annotations

from pathlib import Path
from typing import Any

import fitz

from app.exceptions.document import DocumentException


class PDFReader:
    """Safely open and validate a PDF file."""

    def __init__(self, file_path: str | Path) -> None:
        self._file_path = Path(file_path)

    def open(self) -> Any:
        """Open the PDF document and ensure it is a valid PDF."""
        if not self._file_path.exists():
            raise DocumentException("PDF file not found", error_code="pdf_not_found")
        if self._file_path.suffix.lower() != ".pdf":
            raise DocumentException("Only PDF files are supported", error_code="invalid_pdf_extension")
        try:
            document = fitz.open(self._file_path)
        except Exception as exc:  # pragma: no cover - defensive wrapper
            raise DocumentException("Unable to open PDF document", error_code="pdf_open_error") from exc
        if document.is_pdf is False:
            document.close()
            raise DocumentException("The supplied file is not a valid PDF", error_code="invalid_pdf")
        return document

    def close(self, document: Any) -> None:
        """Close the PDF document resource."""
        if hasattr(document, "close"):
            document.close()
