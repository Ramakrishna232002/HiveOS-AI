from fastapi import FastAPI
from app.api.router import router as api_router
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title="HiveOS AI",
    description="Enterprise AI Operating Platform",
    version="1.0.0",
)

register_exception_handlers(app)
app.include_router(api_router, prefix="/api/v1")



@app.get("/")
def home():
    return {
        "message": "Welcome to HiveOS AI",
        "status": "Running"
    }