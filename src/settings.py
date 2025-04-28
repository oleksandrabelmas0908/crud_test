from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./test.db"
    echo: bool = False


settings = Settings(echo=True)