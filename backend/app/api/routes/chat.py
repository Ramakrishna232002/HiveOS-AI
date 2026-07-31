from fastapi import APIRouter
from app.schemas.common import SuccessResponse
from app.services.chat_service import process_chat
from app.schemas.chat import ChatRequest,ChatResponse

router = APIRouter()

@router.post("/chat", response_model=SuccessResponse)
def chat(request: ChatRequest):
    response = process_chat(request.message)

    return {
        "success": True,
        "data": {
            "message": response
        }
    }