from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Element:
    """
    Represents a structured document element
    extracted from Docling.
    """

    element_type: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)