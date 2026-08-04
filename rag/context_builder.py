class ContextBuilder:


    def build(
        self,
        results
    ):

        contexts = []


        documents = results["documents"][0]


        for doc in documents:

            contexts.append(
                doc
            )


        return "\n\n".join(
            contexts
        )