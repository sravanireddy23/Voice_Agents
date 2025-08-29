"""Configuration settings and environment variables"""
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API Keys and URLs
    gemini_api_key: str
    murf_api_key: str
    murf_api_key_url: str
    murf_api_url: str
    assemblyai_api_key: str
    google_api_key: str

    # Server Settings
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True

    # File Settings
    upload_dir: str = "uploads"
    max_file_size: int = 25 * 1024 * 1024  # 25MB
    allowed_audio_types: list = [
        "audio/wav", "audio/mpeg", "audio/mp3",
        "audio/webm", "audio/ogg", "audio/mp4"
    ]

    # AI Model Settings
    default_llm_model: str = "gemini-1.5-flash"
    default_voice_id: str = "en-IN-arohi"
    default_language: str = "en-IN"
    max_prompt_length: int = 10000
    max_response_tokens: int = 1000

    class Config:
        env_file = ".env"  # ensure .env is in your project root
        extra = "forbid"   # strictly forbid unknown environment variables


# Create a global settings instance
settings = Settings()
