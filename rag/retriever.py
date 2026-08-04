from rag.embedding import EmbeddingGenerator
from rag.vector_store import VectorStore


class Retriever:
    """
    Retrieves relevant document chunks
    from the Vector Store.
    """

    def __init__(
        self,
        top_k: int = 8
    ):

        self.top_k = top_k

        self.embedding_generator = EmbeddingGenerator()

        self.vector_store = VectorStore()



    def search(
        self,
        query: str
    ) -> list[dict]:
        """
        Search documents relevant to user query.

        Args:
            query:
                User question

        Returns:
            Retrieved chunks with metadata
        """


        # Convert query into embedding
        query_embedding = (
            self.embedding_generator.embed_text(
                query
            )
        )


        # Search vector database
        results = (
            self.vector_store.similarity_search(
                query_embedding=query_embedding,
                k=self.top_k
            )
        )


        return self._format_results(
            results
        )



    def _format_results(
        self,
        results
    ) -> list[dict]:
        """
        Convert Chroma response into
        clean retriever output.
        """

        documents = results.get(
            "documents",
            [[]]
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]]
        )[0]

        distances = results.get(
            "distances",
            [[]]
        )[0]


        formatted = []


        for i, document in enumerate(documents):

            formatted.append(
                {
                    "content": document,

                    "metadata": metadatas[i],

                    "score": distances[i]
                    if i < len(distances)
                    else None
                }
            )


        return formatted