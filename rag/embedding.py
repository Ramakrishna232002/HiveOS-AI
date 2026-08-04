from ollama import Client

from models.chunk import Chunk
from models.embedded_chunk import EmbeddedChunk


class EmbeddingGenerator:
    """
    Generates embeddings for text chunks using Ollama.
    """

    def __init__(
        self,
        model: str = "nomic-embed-text",
        host: str = "http://localhost:11434"
    ):
        self.model = model
        self.client = Client(host=host)


    def embed_text(
        self,
        text: str
    ) -> list[float]:
        """
        Generate an embedding for a single piece of text.
        """

        response = self.client.embed(
            model=self.model,
            input=text
        )

        return response.embeddings[0]


    def embed_chunk(
        self,
        chunk: Chunk
    ) -> EmbeddedChunk:
        """
        Generate an embedding for a single chunk.
        """

        embedding = self.embed_text(
            chunk.content
        )

        return EmbeddedChunk(
            chunk=chunk,
            embedding=embedding
        )


    def embed_chunks(
        self,
        chunks: list[Chunk]
    ) -> list[EmbeddedChunk]:
        """
        Generate embeddings for multiple chunks.
        """

        embedded_chunks = []

        for chunk in chunks:

            embedded_chunks.append(
                self.embed_chunk(chunk)
            )

        return embedded_chunks