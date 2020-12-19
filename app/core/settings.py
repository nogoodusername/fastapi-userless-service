from typing import Optional

from pydantic import BaseSettings, Field


class GlobalConfig(BaseSettings):
    """Global configurations."""

    FLAVOUR: Optional[str] = Field(..., env="FLAVOUR")

    API_PREFIX: str = ""
    DOCS_URL: Optional[str] = None
    REDOC_URL: Optional[str] = None
    ALLOWED_HOSTS: Optional[list] = None

    class Config:
        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configurations."""

    DEBUG = True

    DOCS_URL = "/docs"
    REDOC_URL = "/redocs"


class ProdConfig(GlobalConfig):
    """Production configurations."""

    DEBUG = False


class StageConfig(GlobalConfig):
    """Staging configurations."""

    DEBUG = False

    DOCS_URL = "/docs"
    REDOC_URL = "/redocs"


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, flavour: Optional[str]):
        self.flavour = flavour

    def __call__(self):
        if self.flavour == "dev":
            return DevConfig()

        elif self.flavour == "prod":
            return ProdConfig()

        elif self.flavour == "stag":
            return StageConfig()


config = FactoryConfig(GlobalConfig().FLAVOUR)()
# print(config.__repr__())
