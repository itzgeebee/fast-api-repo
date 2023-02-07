from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_PORT: int
    DATABASE_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_HOSTNAME: str

    class Config:
        env_file = './.env'


settings = Settings()
