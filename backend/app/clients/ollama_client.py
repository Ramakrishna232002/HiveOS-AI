import requests
from app.core.config import settings
from app.core.logger import logger
from app.prompts.prompt_builder import build_prompt

OLLAMA_URL = f'{settings.ollama_base_url}/api/generate'

def generate_response(user_query: str):
    final_prompt = build_prompt(user_query)
    payload = {
        "model": settings.llm_model,
        "prompt": final_prompt,
        "stream": False
    }
    
    try:
        logger.info("Sending request to Ollama")
        response = requests.post(
            OLLAMA_URL,
            json=payload
        )   
        response.raise_for_status()
        logger.info("Received successful response from Ollama")
        result = response.json()
        logger.info("Generated AI response successfully")
        return result["response"]
    
    except Exception as e:
        logger.error(f"Ollama Error: {e}")
        raise Exception("Ollama server is unavailable. Please try again later.")
