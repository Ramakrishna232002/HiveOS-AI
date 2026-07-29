from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str
    environment: str

    host: str
    port: int

    debug: bool

    api_v1_prefix: str

    ollama_base_url: str
    llm_model: str
    embedding_model: str

    vector_db: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )