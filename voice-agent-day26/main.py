import os
import time
import requests
import aiofiles
import webbrowser  # <-- Added for Day 26 skill
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = FastAPI()

# CORS and static files
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html for root
@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Load keys
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")
MURF_VOICE_ID = os.getenv("MURF_VOICE_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not all([ASSEMBLYAI_API_KEY, MURF_API_KEY, MURF_VOICE_ID, GEMINI_API_KEY]):
    raise Exception("Missing API keys in .env!")

genai_client = genai.Client(api_key=GEMINI_API_KEY)

ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"
MURF_TTS_URL = "https://api.murf.ai/v1/speech/generate"

# In-memory chat history store: { session_id: [ {"role": "user"/"assistant", "content": "..."} ] }
chat_history_store = {}

async def upload_audio_to_assemblyai(file_path: str) -> str:
    headers = {"authorization": ASSEMBLYAI_API_KEY}
    async with aiofiles.open(file_path, "rb") as f:
        data = await f.read()
    response = requests.post(ASSEMBLYAI_UPLOAD_URL, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["upload_url"]

def request_transcription(upload_url: str) -> str:
    headers = {"authorization": ASSEMBLYAI_API_KEY, "content-type": "application/json"}
    json_data = {"audio_url": upload_url}
    response = requests.post(ASSEMBLYAI_TRANSCRIPT_URL, json=json_data, headers=headers)
    response.raise_for_status()
    transcript_id = response.json()["id"]

    # Poll transcription until done
    while True:
        poll_resp = requests.get(f"{ASSEMBLYAI_TRANSCRIPT_URL}/{transcript_id}", headers=headers)
        poll_resp.raise_for_status()
        status = poll_resp.json()["status"]
        if status == "completed":
            return poll_resp.json()["text"]
        elif status == "error":
            raise Exception("AssemblyAI transcription failed: " + poll_resp.json().get("error", "Unknown error"))
        time.sleep(3)

def get_gemini_response(chat_messages: list) -> str:
    prompt = ""
    for msg in chat_messages:
        role = "User" if msg["role"] == "user" else "AI"
        prompt += f"{role}: {msg['content']}\n"
    prompt += "AI:"
    response = genai_client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text.strip()

def generate_murf_tts(text: str) -> str:
    if len(text) > 3000:
        text = text[:3000]

    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json",
    }
    json_data = {
        "text": text,
        "voice_id": MURF_VOICE_ID,
        "speed": 1.0,
        "pitch": 1.0,
    }

    response = requests.post(MURF_TTS_URL, json=json_data, headers=headers)
    response.raise_for_status()

    resp_json = response.json()
    audio_url = resp_json.get("audioFile")
    if not audio_url:
        raise Exception(f"Murf API error: {resp_json.get('errorMessage', 'No audioFile in response')}")

    return audio_url

@app.post("/agent/chat/{session_id}")
async def agent_chat(session_id: str, audio: UploadFile = File(...)):
    try:
        # Save temp audio file
        temp_file_path = f"temp_{audio.filename}"
        async with aiofiles.open(temp_file_path, "wb") as out_file:
            content = await audio.read()
            await out_file.write(content)

        # Upload and transcribe
        upload_url = await upload_audio_to_assemblyai(temp_file_path)
        transcript_text = request_transcription(upload_url)

        # ---------------- DAY 26: Special Skill 2 ----------------
        if "open youtube" in transcript_text.lower():
            webbrowser.open("https://www.youtube.com")
            ai_response = "Opening YouTube for you!"
            murf_audio_url = generate_murf_tts(ai_response)

            os.remove(temp_file_path)
            return {
                "transcription": transcript_text,
                "llm_response": ai_response,
                "murf_audio_url": murf_audio_url,
                "chat_history": chat_history_store.get(session_id, [])
            }
        # ---------------------------------------------------------

        # Normal flow for other queries
        history = chat_history_store.get(session_id, [])
        history.append({"role": "user", "content": transcript_text})
        ai_response = get_gemini_response(history)
        history.append({"role": "assistant", "content": ai_response})
        chat_history_store[session_id] = history
        murf_audio_url = generate_murf_tts(ai_response)

        os.remove(temp_file_path)

        return {
            "transcription": transcript_text,
            "llm_response": ai_response,
            "murf_audio_url": murf_audio_url,
            "chat_history": history
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
