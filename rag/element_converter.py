from rag.element import Element


class ElementConverter:

    def convert(self, document) -> list[Element]:

        elements = []

        current_section = None


        # Text elements
        for item in document.texts:

            label = item.label.value


            # Ignore noise
            if label in [
                "page_header",
                "page_footer"
            ]:
                continue


            # Track section
            if label == "section_header":

                current_section = item.text


            elements.append(
                Element(
                    element_type=label,
                    content=item.text,
                    metadata={
                        "page": item.prov[0].page_no
                        if item.prov
                        else None,

                        "section": current_section
                    }
                )
            )


        # Tables
        for table in document.tables:

            elements.append(
                Element(
                    element_type="table",
                    content=self._table_to_text(table),
                    metadata={
                        "page": table.prov[0].page_no
                        if table.prov
                        else None,

                        "section": current_section
                    }
                )
            )


        return elements



    def _table_to_text(self, table):

        rows = []

        for row in table.data.grid:

            values = []

            for cell in row:
                values.append(cell.text)

            rows.append(
                " | ".join(values)
            )


        return "\n".join(rows)