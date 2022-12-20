from pydantic import BaseSettings, HttpUrl, PostgresDsn


class Settings(BaseSettings):
    MASTER_DATABASE_URL: PostgresDsn
    SLAVE_DATABASE_URL: PostgresDsn

    EVENTS_API_URL: HttpUrl

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
