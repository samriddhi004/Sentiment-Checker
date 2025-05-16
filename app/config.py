from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SentimentChecker"
    class Config:
        env_file = ".env"

settings = Settings()
