import chromadb

from models.chunk import Chunk
from models.embedded_chunk import EmbeddedChunk


class VectorStore:
    """
    Stores and retrieves document embeddings
    using ChromaDB.
    """

    def __init__(
        self,
        collection_name: str = "hiveos"
    ):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )


    def add_documents(
        self,
        embedded_chunks: list[EmbeddedChunk]
    ) -> None:
        """
        Store embedded chunks in ChromaDB.
        """

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for item in embedded_chunks:

            ids.append(
                item.chunk.chunk_id
            )

            embeddings.append(
                item.embedding
            )

            documents.append(
                item.chunk.content
            )

            metadatas.append(
                item.chunk.metadata
            )

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )


    def similarity_search(
        self,
        query_embedding: list[float],
        k: int = 5
    ):
        """
        Search similar chunks.
        """

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )


    def count(self) -> int:
        """
        Number of stored chunks.
        """

        return self.collection.count()


    def delete_collection(self):
        """
        Delete the current collection.
        """

        self.client.delete_collection(
            self.collection.name
        )
        
    def peek(
        self,
        limit: int = 3
    ):
        """
        Return sample documents from vector store.
        """

        return self.collection.get(
            limit=limit,
            include=[
                "documents",
                "metadatas"
            ]
        )