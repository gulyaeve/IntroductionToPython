from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str
    POSTGRES_DB: str
    MODE: tuple
    STATUS: Literal['dev', 'release']

    @property
    def database_url(self):
        user = f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
        database = f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return f"postgres+asyncpg://{user}@{database}"

    def database_url_custom(self, engine: str):
        user = f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
        database = f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return f"{engine}://{user}@{database}"

    class Config:
        env_file = ".env"


if __name__ == '__main__':
    settings = Settings()
    print(f"{settings.POSTGRES_USER=}")
    print(f"{settings.POSTGRES_PASSWORD=}")
    print(f"{settings.POSTGRES_PORT=}")
    print(f"{settings.MODE=}")
    print(f"{settings.STATUS=}")
    print(f"{settings.database_url_custom('sqlite3')}")
    print(f"{settings.database_url}")
