from fastapi import APIRouter
from app.services.health_service import get_health_status
from app.schemas.health import HealthSuccessResponse


router = APIRouter()


@router.get("/health", response_model=HealthSuccessResponse)
def health_check():
    return {
    "success": True,
    "data": get_health_status()
}