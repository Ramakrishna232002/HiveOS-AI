from pathlib import Path
import logging
from docling.document_converter import DocumentConverter


logger = logging.getLogger(__name__)


class DoclingLoader:
    """Loads PDF documents using Docling."""

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
        self.converter = DocumentConverter()

    def load(self):

        if not self.pdf_path.exists():
            logger.error(
                "PDF file not found: %s",
                self.pdf_path
            )
            raise FileNotFoundError(
                f"PDF file not found: {self.pdf_path}"
            )

        try:
            logger.info(
                "Starting document loading: %s",
                self.pdf_path.name
            )

            result = self.converter.convert(
                str(self.pdf_path)
            )

            logger.info(
                "Document loaded successfully: %s",
                self.pdf_path.name
            )

            return result.document

        except Exception as exc:
            logger.exception(
                "Failed to load document: %s",
                self.pdf_path.name
            )

            raise RuntimeError(
                f"Failed to load document: {self.pdf_path}"
            ) from exc