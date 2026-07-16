import unittest
from uuid import uuid4

from app.models.document import Document
from app.models.enums import DocumentStatus
from app.models.parsed.parsed_document import ParsedDocument, ParsedMetadata
from app.responses.error import ErrorResponse
from app.responses.success import SuccessResponse
from app.services.document_processing_service import ParserResult
from app.services.submission_facade import SubmissionFacade


class FakeDocumentRepository:
    def __init__(self, document: Document) -> None:
        self._document = document

    async def get_by_uuid(self, uuid_value: str) -> Document | None:
        if str(self._document.uuid) == uuid_value:
            return self._document
        return None


class FakeUnitOfWork:
    def __init__(self, document: Document) -> None:
        self.documents = FakeDocumentRepository(document)


class FakeProcessingService:
    async def process_document(self, document_uuid: str) -> ParserResult:
        return ParserResult(document_uuid=uuid4(), status=DocumentStatus.PARSED, parsed_document=ParsedDocument(metadata=ParsedMetadata(title="sample"), pages=[]))


class SubmissionFacadeTests(unittest.IsolatedAsyncioTestCase):
    async def test_submit_document_returns_success_payload_for_eligible_document(self) -> None:
        document = Document(
            project_id=1,
            original_filename="sample.pdf",
            stored_filename="sample.pdf",
            storage_path="sample.pdf",
            mime_type="application/pdf",
            file_size_bytes=10,
            checksum="abc",
            version="1.0",
            status=DocumentStatus.UPLOADED,
        )
        document.uuid = uuid4()

        facade = SubmissionFacade(unit_of_work=FakeUnitOfWork(document), document_processing_service=FakeProcessingService())
        result = await facade.submit_document(str(document.uuid))

        self.assertIsInstance(result, SuccessResponse)
        self.assertTrue(result.success)
        self.assertIsNotNone(result.data)
        self.assertEqual(result.data.status, DocumentStatus.PARSED)

    async def test_submit_document_returns_error_payload_for_ineligible_document(self) -> None:
        document = Document(
            project_id=1,
            original_filename="sample.pdf",
            stored_filename="sample.pdf",
            storage_path="sample.pdf",
            mime_type="application/pdf",
            file_size_bytes=10,
            checksum="def",
            version="1.0",
            status=DocumentStatus.PARSED,
        )
        document.uuid = uuid4()

        facade = SubmissionFacade(unit_of_work=FakeUnitOfWork(document), document_processing_service=FakeProcessingService())
        result = await facade.submit_document(str(document.uuid))

        self.assertIsInstance(result, ErrorResponse)
        self.assertFalse(result.success)
        self.assertEqual(result.error_code, "document_not_eligible")


if __name__ == "__main__":
    unittest.main()
