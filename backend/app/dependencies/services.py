from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.document_repository import DocumentRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.report_repository import ReportRepository
from app.repositories.user_repository import UserRepository
from app.services.analysis_service import AnalysisService
from app.services.document_processing_service import DocumentProcessingService
from app.services.document_service import DocumentService
from app.services.project_service import ProjectService
from app.services.report_service import ReportService
from app.services.submission_facade import SubmissionFacade
from app.services.user_service import UserService
from app.uow.unit_of_work import UnitOfWork


def get_user_service(repository: UserRepository) -> UserService:
    """Create a user service from the injected repository."""
    return UserService(repository)


def get_project_service(repository: ProjectRepository) -> ProjectService:
    """Create a project service from the injected repository."""
    return ProjectService(repository)


def get_document_service(unit_of_work: UnitOfWork) -> DocumentService:
    """Create a document service from the injected unit of work."""
    return DocumentService(unit_of_work)


def get_document_processing_service(unit_of_work: UnitOfWork) -> DocumentProcessingService:
    """Create the document processing orchestrator from the injected unit of work."""
    return DocumentProcessingService(unit_of_work)


def get_submission_facade(unit_of_work: UnitOfWork) -> SubmissionFacade:
    """Create the submission facade as the single public entry point for processing workflows."""
    return SubmissionFacade(unit_of_work)


def get_analysis_service(repository: AnalysisRepository) -> AnalysisService:
    """Create an analysis service from the injected repository."""
    return AnalysisService(repository)


def get_report_service(repository: ReportRepository) -> ReportService:
    """Create a report service from the injected repository."""
    return ReportService(repository)
