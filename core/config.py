from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgres@0.0.0.0:5433/app_db'


    class Config:
        case_sensitive = True


settings = Settings()
