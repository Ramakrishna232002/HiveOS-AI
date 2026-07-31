from app.core.logger import logger

def get_health_status():

    logger.info("Health service called")

    return {
        "status": "Healthy",
        "service": "HiveOS AI"
    }