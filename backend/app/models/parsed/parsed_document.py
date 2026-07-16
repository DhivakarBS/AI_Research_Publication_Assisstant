from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class ParsedMetadata:
    title: str = ""
    author: str = ""
    creator: str = ""
    producer: str = ""
    subject: str = ""
    keywords: str = ""
    creation_date: datetime | None = None
    modification_date: datetime | None = None
    page_count: int = 0
    pdf_version: str = ""


@dataclass(slots=True)
class ParsedText:
    text: str = ""
    bounding_box: list[float] = field(default_factory=list)
    font_name: str = ""
    font_size: float = 0.0
    font_flags: int = 0
    color: str = ""
    rotation: int = 0


@dataclass(slots=True)
class ParsedImage:
    image_index: int = 0
    width: int | None = None
    height: int | None = None
    xref: int = 0
    transform: Any | None = None
    page_number: int = 0


@dataclass(slots=True)
class ParsedPage:
    page_number: int = 0
    width: float = 0.0
    height: float = 0.0
    rotation: int = 0
    text_blocks: list[ParsedText] = field(default_factory=list)
    images: list[ParsedImage] = field(default_factory=list)


@dataclass(slots=True)
class ParsedDocument:
    metadata: ParsedMetadata = field(default_factory=ParsedMetadata)
    pages: list[ParsedPage] = field(default_factory=list)
