from pydantic import BaseModel
from typing import Any

class SuccessResponse(BaseModel):
    success: bool
    data: dict[str, Any]