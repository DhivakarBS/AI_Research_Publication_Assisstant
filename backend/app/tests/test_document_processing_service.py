import unittest
from types import SimpleNamespace
from uuid import uuid4

from app.models.document import Document
from app.models.enums import DocumentStatus
from app.models.parsed.parsed_document import ParsedDocument, ParsedMetadata
from app.services.document_processing_service import DocumentProcessingService


class FakeDocumentRepository:
    def __init__(self, document: Document) -> None:
        self._document = document

    async def get_by_uuid(self, uuid_value: str) -> Document | None:
        if str(self._document.uuid) == uuid_value:
            return self._document
        return None

    async def update(self, instance: Document) -> Document:
        self._document = instance
        return self._document


class FakeUnitOfWork:
    def __init__(self, document: Document) -> None:
        self.documents = FakeDocumentRepository(document)
        self.committed = False

    async def commit(self) -> None:
        self.committed = True

    async def rollback(self) -> None:
        self.committed = False


class FakeParserService:
    def __init__(self, should_fail: bool = False) -> None:
        self.should_fail = should_fail

    def parse_file(self, file_path: str) -> ParsedDocument:
        if self.should_fail:
            raise RuntimeError("parser failed")
        return ParsedDocument(metadata=ParsedMetadata(title="Sample"), pages=[])


class DocumentProcessingServiceTests(unittest.IsolatedAsyncioTestCase):
    async def test_processes_uploaded_document_and_updates_status(self) -> None:
        document = Document(
            project_id=1,
            original_filename="sample.pdf",
            stored_filename="sample.pdf",
            storage_path="sample.pdf",
            mime_type="application/pdf",
            file_size_bytes=10,
            checksum="abc123",
            version="1.0",
            status=DocumentStatus.UPLOADED,
        )
        document.uuid = uuid4()

        unit_of_work = FakeUnitOfWork(document)
        service = DocumentProcessingService(unit_of_work=unit_of_work, parser_service=FakeParserService())

        result = await service.process_document(str(document.uuid))

        self.assertEqual(result.status, DocumentStatus.PARSED)
        self.assertEqual(document.status, DocumentStatus.PARSED)
        self.assertIsNotNone(result.parsed_document)
        self.assertTrue(unit_of_work.committed)

    async def test_marks_document_failed_when_parser_raises(self) -> None:
        document = Document(
            project_id=1,
            original_filename="sample.pdf",
            stored_filename="sample.pdf",
            storage_path="sample.pdf",
            mime_type="application/pdf",
            file_size_bytes=10,
            checksum="def456",
            version="1.0",
            status=DocumentStatus.UPLOADED,
        )
        document.uuid = uuid4()

        unit_of_work = FakeUnitOfWork(document)
        service = DocumentProcessingService(unit_of_work=unit_of_work, parser_service=FakeParserService(should_fail=True))

        result = await service.process_document(str(document.uuid))

        self.assertEqual(result.status, DocumentStatus.FAILED)
        self.assertEqual(document.status, DocumentStatus.FAILED)
        self.assertIsNone(result.parsed_document)
        self.assertTrue(unit_of_work.committed)


if __name__ == "__main__":
    unittest.main()
