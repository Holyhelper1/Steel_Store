from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent

class AuthJWT(BaseModel):
    PRIVATE_KEY_PATH: Path = BASE_DIR / 'app' / 'certs' / 'jwt-private.pem'
    PUBLIC_KEY_PATH:Path = BASE_DIR / 'app' / 'certs' / 'jwt-public.pem'
    ALGORITHM: str = 'RS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30


class Settings(BaseSettings):
    DEBUG: bool

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    REDIS_HOST: str
    REDIS_PORT: int

    LIMIT_DEFAULT: int
    OFFSET_DEFAULT: int

    AUTH_JWT: AuthJWT = AuthJWT()

    model_config = SettingsConfigDict(env_file=BASE_DIR / '.env', env_file_encoding='utf-8')

settings = Settings()