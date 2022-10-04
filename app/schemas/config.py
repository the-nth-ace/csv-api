from pydantic import BaseSettings


class ConfigSettings(BaseSettings):
    MONGO_URL: str

    class Config:
        env_file = ".env"
