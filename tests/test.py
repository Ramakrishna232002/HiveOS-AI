from rag.retriever import Retriever


retriever = Retriever(
    top_k=5
)


results = retriever.search(
    "Who founded HiveOS Technologies?"
)


for result in results:

    print("----------------")

    print("CONTENT:")
    print(result["content"])

    print("\nMETADATA:")
    print(result["metadata"])

    print("\nSCORE:")
    print(result["score"])