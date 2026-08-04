from rag.embedding import EmbeddingGenerator
from rag.vector_store import VectorStore
from rag.llm import OllamaLLM


class RAGService:


    def __init__(self):

        self.embedding = EmbeddingGenerator()

        self.vector_store = VectorStore()

        self.llm = OllamaLLM()



    def ask(
        self,
        question: str
    ):


        # 1. Create query embedding
        query_embedding = self.embedding.embed_text(
            question
        )


        # 2. Retrieve similar chunks
        result = self.vector_store.similarity_search(
            query_embedding,
            k=5
        )


        documents = result["documents"][0]


        # 3. Build context

        context = "\n\n".join(
            documents
        )


        # 4. Generate answer

        answer = self.llm.generate(
            question,
            context
        )


        return answer