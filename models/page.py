from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Page:
    """Represents a single page flowing through the RAG pipeline."""

    page_number: int
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)