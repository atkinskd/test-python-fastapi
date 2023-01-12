import os
import sys
from functools import lru_cache

from pydantic import BaseSettings

sys.path.append(os.path.realpath("."))
# pylint: disable=wrong-import-position
from __version__ import __version__


class Settings(BaseSettings):

    version: str = __version__


@lru_cache()
def get_settings() -> Settings:
    return Settings()
