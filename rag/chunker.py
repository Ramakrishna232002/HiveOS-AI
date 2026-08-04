from models.chunk import Chunk
from rag.element import Element
from rag.table_chunker import TableChunker


class CustomChunker:
    """
    Creates meaningful chunks from Docling elements.

    Responsibilities:
    - Maintain document section context
    - Chunk normal text content
    - Route tables to TableChunker
    - Handle headings, text, lists, captions, and tables
    """

    def __init__(
        self,
        max_characters: int = 2000
    ):
        """
        Initialize CustomChunker.

        Args:
            max_characters:
                Maximum characters allowed in a text chunk.
                Token handling will be added later.
        """

        self.max_characters = max_characters

        self.table_chunker = TableChunker(
            max_characters=max_characters
        )


    def create_chunks(
        self,
        elements: list[Element]
    ) -> list[Chunk]:

        chunks = []

        current_content = []
        current_metadata = {}

        chunk_index = 0


        for element in elements:


            # -----------------------------
            # Section Header
            # -----------------------------
            if element.element_type == "section_header":

                # Store previous chunk
                if current_content:

                    chunks.append(
                        self._create_chunk(
                            current_content,
                            current_metadata,
                            chunk_index,
                            "text"
                        )
                    )

                    chunk_index += 1
                    current_content = []


                # Update section metadata
                current_metadata = {
                    "section": element.content,
                    "page": element.metadata.get("page")
                }

                continue



            # -----------------------------
            # Table Handling
            # -----------------------------
            if element.element_type == "table":

                # Store pending text first
                if current_content:

                    chunks.append(
                        self._create_chunk(
                            current_content,
                            current_metadata,
                            chunk_index,
                            "text"
                        )
                    )

                    chunk_index += 1
                    current_content = []


                table_metadata = current_metadata.copy()

                table_metadata.update({
                    "page": element.metadata.get("page"),
                    "type": "table"
                })


                table_chunks = self.table_chunker.create_table_chunks(
                    table_text=element.content,
                    metadata=table_metadata,
                    chunk_start_index=chunk_index
                )


                chunks.extend(
                    table_chunks
                )


                chunk_index += len(table_chunks)

                continue



            # -----------------------------
            # Text Content
            # -----------------------------
            if element.element_type in [
                "text",
                "list_item",
                "caption"
            ]:

                current_content.append(
                    element.content
                )


                current_text = "\n".join(
                    current_content
                )


                # Temporary character based limit
                if len(current_text) >= self.max_characters:

                    chunks.append(
                        self._create_chunk(
                            current_content,
                            current_metadata,
                            chunk_index,
                            "text"
                        )
                    )

                    chunk_index += 1

                    current_content = []



        # -----------------------------
        # Remaining Content
        # -----------------------------
        if current_content:

            chunks.append(
                self._create_chunk(
                    current_content,
                    current_metadata,
                    chunk_index,
                    "text"
                )
            )


        return chunks



    def _create_chunk(
        self,
        content: list[str],
        metadata: dict,
        index: int,
        chunk_type: str
    ) -> Chunk:


        chunk_metadata = metadata.copy()

        chunk_metadata["type"] = chunk_type


        return Chunk(

            chunk_id=f"chunk_{index}",

            content="\n".join(content),

            metadata=chunk_metadata
        )