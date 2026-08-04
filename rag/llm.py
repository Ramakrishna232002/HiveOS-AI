from ollama import Client


class OllamaLLM:
    """
    Generates answers using Ollama LLM.
    Uses grounded prompting for RAG.
    """

    def __init__(
        self,
        model: str = "llama3.2:1b",
        host: str = "http://localhost:11434"
    ):

        self.model = model

        self.client = Client(
            host=host
        )


    def generate(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Generate answer using retrieved context only.
        """


        prompt = f"""
You are HiveOS AI Assistant.

Your task is to answer user questions using ONLY the provided context.

Strict rules:
1. Use only information available in the context.
2. Do not use your pretrained knowledge.
3. Do not guess or assume anything.
4. If the answer is not present in the context, reply:
   "I don't have enough information in the knowledge base."
5. Keep the answer professional and concise.

---------------------
Context:
{context}
---------------------

Question:
{question}

Answer:
"""


        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict enterprise knowledge assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.1
            }
        )


        return response["message"]["content"]