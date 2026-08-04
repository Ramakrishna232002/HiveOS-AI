from dataclasses import dataclass, field

from models.chunk import Chunk


@dataclass(slots=True)
class EmbeddedChunk:
    """
    Represents a chunk along with its vector embedding.
    """

    chunk: Chunk
    embedding: list[float] = field(default_factory=list)