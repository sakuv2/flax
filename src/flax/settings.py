from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    # JWT settings
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # administrator account settings
    admin_password: str

    # db settings
    # redis_dsn: RedisDsn
    postgres_dsn: PostgresDsn

    # server settings
    port: int = 80
    debug: bool = False

    class Config:
        env_file = ".env"
