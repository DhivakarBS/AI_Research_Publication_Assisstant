from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.responses import JSONResponse

from app.dependencies.database import get_unit_of_work
from app.dependencies.services import get_document_service
from app.dto.document import DocumentUploadPayload
from app.exceptions.document import DocumentException
from app.exceptions.validation import ValidationException
from app.responses.error import ErrorResponse
from app.responses.success import SuccessResponse
from app.services.document_service import DocumentService
from app.uow.unit_of_work import UnitOfWork

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.post("/upload", response_model=SuccessResponse)
async def upload_document(
    project_id: int = Form(...),
    file: UploadFile | None = File(None),
    service: DocumentService = Depends(get_document_service),
    unit_of_work: UnitOfWork = Depends(get_unit_of_work),
) -> JSONResponse:
    """Upload a PDF document and register it in the database."""
    try:
        if file is None or file.filename is None:
            raise ValidationException("File is required", error_code="missing_file")
        contents = await file.read()
        payload = DocumentUploadPayload(
            project_id=project_id,
            original_filename=file.filename,
            mime_type=file.content_type,
            content=contents,
        )
        document = await service.upload_document(payload)
        return JSONResponse(
            status_code=201,
            content=SuccessResponse(data={"uuid": str(document.uuid), "filename": document.original_filename}).model_dump(),
        )
    except (ValidationException, DocumentException) as exc:
        return JSONResponse(
            status_code=exc.http_status,
            content=ErrorResponse(error_code=exc.error_code, message=exc.message, http_status=exc.http_status).model_dump(),
        )
