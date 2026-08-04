from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Chunk:
    """Represents a chunk created from a document page."""

    chunk_id: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)