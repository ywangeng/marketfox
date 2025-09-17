from pydantic import BaseModel
import os


class Settings(BaseModel):
    APP_ENV: str = os.getenv("APP_ENV", "local")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SYNC_DATABASE_URL: str = os.getenv("SYNC_DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret")


settings = Settings()
