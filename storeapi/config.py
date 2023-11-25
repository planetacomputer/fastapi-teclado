from typing import Optional
from functools import lru_cache
from pydantic.v1 import BaseSettings

class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    class Config:
        """Config for base settings."""
        env_file: str = ".env"
    
class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False

class DevConfig(GlobalConfig):
    class Config:
        env_prefix: str = "DEV_"

class ProdConfig(GlobalConfig):
    class Config:
        env_prefix: str = "PROD_"

class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    class Config:
        env_prefix: str = "TEST_"

@lru_cache()
def get_config(env_state: str):
    """Return config based on env_state."""
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()

config = get_config(BaseConfig().ENV_STATE)