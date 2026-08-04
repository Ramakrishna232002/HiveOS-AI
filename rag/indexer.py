from pathlib import Path

from rag.loader import DoclingLoader
from rag.element_converter import ElementConverter
from rag.chunker import CustomChunker
from rag.embedding import EmbeddingGenerator
from rag.vector_store import VectorStore


class Indexer:
    """
    Responsible for indexing documents into the Vector Store.
    """

    def __init__(self):

        self.converter = ElementConverter()

        self.chunker = CustomChunker()

        self.embedding = EmbeddingGenerator()

        self.vector_store = VectorStore()


    def index_document(
        self,
        pdf_path: str
    ) -> None:
        """
        Index a single PDF document.
        """

        print(f"\nIndexing: {pdf_path}")

        # Load PDF
        loader = DoclingLoader(pdf_path)

        document = loader.load()


        # Convert document to elements
        elements = self.converter.convert(
            document
        )


        # Create chunks
        chunks = self.chunker.create_chunks(
            elements
        )


        # Generate embeddings
        embedded_chunks = self.embedding.embed_chunks(
            chunks
        )


        # Store into Vector DB
        self.vector_store.add_documents(
            embedded_chunks
        )

        print(
            f"✓ Indexed {len(chunks)} chunks"
        )


    def index_directory(
        self,
        directory: str
    ) -> None:
        """
        Index every PDF inside a directory recursively.
        """

        directory = Path(directory)

        if not directory.exists():

            raise FileNotFoundError(
                f"{directory} does not exist."
            )


        pdf_files = list(
            directory.rglob("*.pdf")
        )


        if not pdf_files:

            print(
                "No PDF files found."
            )

            return


        for pdf in pdf_files:

            self.index_document(
                str(pdf)
            )


        print("\n=================================")
        print(
            "Indexing Completed Successfully"
        )
        print(
            f"Total Chunks Stored : {self.vector_store.count()}"
        )
        print("=================================")