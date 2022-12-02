from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "some mail"
    DB_USER:str

    class Config:
        env_file = ".env"


settings = Settings()