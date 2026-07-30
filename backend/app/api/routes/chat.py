from fastapi import APIRouter

from app.schemas.chat import ChatRequest

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": request.message
    }