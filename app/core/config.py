from pydantic_settings import BaseSettings
from pydantic import ConfigDict

from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5433/app_db'


settings = Settings()
