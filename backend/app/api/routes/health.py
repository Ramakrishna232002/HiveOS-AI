from fastapi import APIRouter
from app.services.health_service import get_health_status
from app.schemas.health import HealthResponse


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return get_health_status()