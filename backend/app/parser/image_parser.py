from __future__ import annotations

from typing import Any

from app.models.parsed.parsed_document import ParsedImage


class ImageParser:
    """Extract image references from a PDF page."""

    def parse(self, page: Any, page_number: int) -> list[ParsedImage]:
        """Return image metadata without decoding image content."""
        images: list[ParsedImage] = []
        for image in page.get_images(full=True):
            images.append(
                ParsedImage(
                    image_index=image[0],
                    width=image[2],
                    height=image[3],
                    xref=image[0],
                    transform=image[4] if len(image) > 4 else None,
                    page_number=page_number,
                )
            )
        return images
