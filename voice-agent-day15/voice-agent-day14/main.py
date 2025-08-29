# main.py
import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Dict, List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

from models import ChatMessage, ChatTurnResponse
from services.stt import AssemblyAITranscriber
from services.llm import GeminiLLM
from services.tts import MurfTTS

# -------------------------
# Logging Setup
# -------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
# Optional rotating file log
if os.getenv("FILE_LOGS", "0") == "1":
    handler = RotatingFileHandler("app.log", maxBytes=2_000_000, backupCount=2)
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))
    logging.getLogger().addHandler(handler)

logger = logging.getLogger("voice-agent")

# -------------------------
# Env & Services
# -------------------------
load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")
MURF_VOICE_ID = os.getenv("MURF_VOICE_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

missing = [k for k, v in {
    "ASSEMBLYAI_API_KEY": ASSEMBLYAI_API_KEY,
    "MURF_API_KEY": MURF_API_KEY,
    "MURF_VOICE_ID": MURF_VOICE_ID,
    "GEMINI_API_KEY": GEMINI_API_KEY,
}.items() if not v]

if missing:
    raise RuntimeError(f"Missing env vars: {', '.join(missing)}. Check your .env.")

stt = AssemblyAITranscriber(api_key=ASSEMBLYAI_API_KEY)
llm = GeminiLLM(api_key=GEMINI_API_KEY, model="gemini-1.5-flash")
tts = MurfTTS(api_key=MURF_API_KEY, voice_id=MURF_VOICE_ID)

# -------------------------
# App & Static
# -------------------------
app = FastAPI(title="Voice Agent - Day14 Refactor", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory chat history
chat_history_store: Dict[str, List[ChatMessage]] = {}

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/agent/chat/{session_id}", response_model=ChatTurnResponse)
async def agent_chat(session_id: str, audio: UploadFile = File(...)):
    try:
        logger.info("New chat turn | session_id=%s | file=%s | size=?", session_id, audio.filename)
        audio_bytes = await audio.read()

        # 1) STT
        user_text = stt.transcribe_from_audio_bytes(audio_bytes)
        logger.info("Transcription: %s", user_text)

        # 2) Load history and append user message
        history = chat_history_store.get(session_id, [])
        history.append(ChatMessage(role="user", content=user_text))

        # 3) LLM
        ai_text = llm.generate(history)
        logger.info("AI response: %s", ai_text)

        # 4) Append assistant message & persist
        history.append(ChatMessage(role="assistant", content=ai_text))
        chat_history_store[session_id] = history

        # 5) TTS
        audio_url = tts.synthesize(ai_text)

        # 6) Response
        return ChatTurnResponse(
            session_id=session_id,
            transcription=user_text,
            llm_response=ai_text,
            murf_audio_url=audio_url,
            chat_history=history,
        )

    except Exception as e:
        logger.exception("Chat turn failed")
        raise HTTPException(status_code=500, detail=str(e))
