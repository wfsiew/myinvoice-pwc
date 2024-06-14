from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_base_url: str
    client_id: str
    client_secret: str
    scope: str

    model_config = SettingsConfigDict(env_file=".envx")