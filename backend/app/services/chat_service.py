from app.clients.ollama_client import generate_response
from app.core.logger import logger


def process_chat(message: str):

    logger.info("Processing chat request")

    response = generate_response(message)

    logger.info("AI response generated successfully")

    return response