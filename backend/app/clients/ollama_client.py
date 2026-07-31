import requests
from app.core.config import settings
from app.core.logger import logger

OLLAMA_URL = f'{settings.ollama_base_url}/api/generate'

def generate_response(prompt: str):
    payload = {
        "model": settings.llm_model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload
        )   
        response.raise_for_status()
        result = response.json()
        return result["response"]
    
    except Exception as e:
        logger.error(f"Ollama Error: {e}")
        raise Exception("Ollama server is unavailable. Please try again later.")
