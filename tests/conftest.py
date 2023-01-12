import pytest
from app.core.configs import Settings


@pytest.fixture(scope="session")
def mock_settings():
    return Settings(version="0.1.0")
