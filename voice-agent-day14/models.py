# models.py
from typing import List, Literal
from pydantic import BaseModel

Role = Literal["user", "assistant"]

class ChatMessage(BaseModel):
    role: Role
    content: str

class ChatTurnResponse(BaseModel):
    session_id: str
    transcription: str
    llm_response: str
    murf_audio_url: str | None
    chat_history: List[ChatMessage]
