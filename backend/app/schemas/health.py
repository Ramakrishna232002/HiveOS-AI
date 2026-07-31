from pydantic import BaseModel

from app.schemas.common import SuccessResponse


class HealthResponse(BaseModel):
    status: str
    service: str


class HealthSuccessResponse(SuccessResponse):
    data: HealthResponse