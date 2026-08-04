from models.chunk import Chunk


class TableChunker:
    """
    Splits large tables into smaller chunks.

    Responsibilities:
    - Preserve table header in every chunk
    - Split large tables by character size
    - Maintain table metadata
    """


    def __init__(
        self,
        max_characters: int = 2000
    ):
        """
        Initialize TableChunker.

        Args:
            max_characters:
                Maximum characters per table chunk.
        """

        self.max_characters = max_characters



    def create_table_chunks(
        self,
        table_text: str,
        metadata: dict,
        chunk_start_index: int
    ) -> list[Chunk]:
        """
        Split table into multiple chunks.

        Args:
            table_text:
                Table content converted into text.

            metadata:
                Section/page information.

            chunk_start_index:
                Starting chunk id.

        Returns:
            List of table chunks.
        """

        chunks = []


        rows = table_text.split("\n")


        if not rows:
            return chunks



        # First row is treated as header
        header = rows[0]


        current_rows = []

        chunk_index = chunk_start_index



        for row in rows[1:]:


            current_rows.append(row)


            table_content = (
                header
                + "\n"
                + "\n".join(current_rows)
            )


            # Character based splitting
            if len(table_content) >= self.max_characters:


                # Avoid empty chunk
                if current_rows[:-1]:

                    chunks.append(
                        self._create_table_chunk(
                            header,
                            current_rows[:-1],
                            metadata,
                            chunk_index
                        )
                    )

                    chunk_index += 1


                # Carry overflow row
                current_rows = [row]



        # Remaining rows

        if current_rows:

            chunks.append(
                self._create_table_chunk(
                    header,
                    current_rows,
                    metadata,
                    chunk_index
                )
            )


        return chunks



    def _create_table_chunk(
        self,
        header: str,
        rows: list[str],
        metadata: dict,
        index: int
    ) -> Chunk:


        return Chunk(

            chunk_id=f"chunk_{index}",

            content=(
                header
                + "\n"
                + "\n".join(rows)
            ),

            metadata={
                **metadata,
                "type": "table",
                "table_part": index
            }
        )