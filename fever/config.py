from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    MASTER_DATABASE_URL: PostgresDsn
    SLAVE_DATABASE_URL: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
