from typing import Optional
from pydantic import BaseSettings

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