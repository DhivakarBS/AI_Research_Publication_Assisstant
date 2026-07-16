from enum import Enum


class UserRole(str, Enum):
    """User roles for the application."""

    STUDENT = "Student"
    FACULTY = "Faculty"
    ADMIN = "Admin"


class ProjectStatus(str, Enum):
    """Lifecycle status for projects."""

    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    ARCHIVED = "Archived"


class AnalysisStatus(str, Enum):
    """Execution state for analyses."""

    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"


class RecommendationStatus(str, Enum):
    """Recommendation outcome for reports."""

    PASS = "Pass"
    MINOR_REVISION = "MinorRevision"
    MAJOR_REVISION = "MajorRevision"
    REJECT = "Reject"


class DocumentStatus(str, Enum):
    """Lifecycle status for uploaded documents."""

    UPLOADED = "Uploaded"
    PROCESSING = "Processing"
    PARSED = "Parsed"
    FEATURES_EXTRACTED = "FeaturesExtracted"
    VALIDATED = "Validated"
    REPORT_GENERATED = "ReportGenerated"
    FAILED = "Failed"
