from fastapi import APIRouter, Depends

from ..core.configs import Settings, get_settings
from ..core.models import HealthCheck

router = APIRouter(
    responses={404: {"description": "Not found"}},
    tags=["health"],
)


@router.get("/health", response_model=HealthCheck)
async def health(settings: Settings = Depends(get_settings)):
    return HealthCheck(health="up", version=settings.version)
