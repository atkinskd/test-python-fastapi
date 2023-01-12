import pytest
from app.routers.health import health


@pytest.mark.asyncio
async def test_health(mock_settings):
    result = await health(mock_settings)
    assert result
    assert result.health == "up"
    assert result.version == mock_settings.version
