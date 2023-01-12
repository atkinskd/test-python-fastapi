# pylint: disable=too-few-public-methods

from pydantic import BaseModel


class HealthCheck(BaseModel):
    """HealthCheck model"""

    health: str = "up"
    version: str
