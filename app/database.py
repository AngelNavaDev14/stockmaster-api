import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # El valor por defecto sigue siendo el de tu máquina local,
    # pero ahora Render lo reemplazará con la variable de entorno.
    DATABASE_URL: str = "postgresql://angel_dev:brasiljr08@localhost/stockmaster_db"

    class Config:
        env_file = ".env"

settings = Settings()

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()