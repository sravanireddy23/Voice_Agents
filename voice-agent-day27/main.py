import os
import time
import requests
import aiofiles
import webbrowser
from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from google import genai


app = FastAPI()
import os
from dotenv import load_dotenv

load_dotenv()
print("API Key Loaded:", os.getenv("MURF_API_KEY"))


# CORS and static files
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve config.html at root
@app.get("/", response_class=HTMLResponse)
async def config_page():
    return FileResponse("static/config.html")

# In-memory chat history store: { session_id: [ {"role": "user"/"assistant", "content": "..."} ] }
chat_history_store = {}

# ---------------- Helpers ----------------

async def upload_audio_to_assemblyai(file_path: str, assemblyai_key: str) -> str:
    headers = {"authorization": assemblyai_key}
    async with aiofiles.open(file_path, "rb") as f:
        data = await f.read()
    response = requests.post("https://api.assemblyai.com/v2/upload", headers=headers, data=data)
    response.raise_for_status()
    return response.json()["upload_url"]

def request_transcription(upload_url: str, assemblyai_key: str) -> str:
    headers = {"authorization": assemblyai_key, "content-type": "application/json"}
    json_data = {"audio_url": upload_url}
    response = requests.post("https://api.assemblyai.com/v2/transcript", json=json_data, headers=headers)
    response.raise_for_status()
    transcript_id = response.json()["id"]

    # Poll transcription until done
    while True:
        poll_resp = requests.get(f"https://api.assemblyai.com/v2/transcript/{transcript_id}", headers=headers)
        poll_resp.raise_for_status()
        status = poll_resp.json()["status"]
        if status == "completed":
            return poll_resp.json()["text"]
        elif status == "error":
            raise Exception("AssemblyAI transcription failed: " + poll_resp.json().get("error", "Unknown error"))
        time.sleep(3)

def get_gemini_response(chat_messages: list, gemini_key: str) -> str:
    genai_client = genai.Client(api_key=gemini_key)
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

def generate_murf_tts(text: str, murf_key: str, murf_voice_id: str = "en-US-ken") -> str:
    """
    Generate speech using Murf API and return audio URL.
    """
    if len(text) > 3000:
        text = text[:3000]

    headers = {
        "accept": "application/json",
        "api-key": murf_key,          # ✅ correct header
        "content-type": "application/json",
    }

    payload = {
        "voiceId": murf_voice_id,     # ✅ correct field
        "text": text,
        "format": "MP3",
        "sampleRate": "44100"
    }

    response = requests.post("https://api.murf.ai/v1/speech/generate", json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Murf API Error {response.status_code}: {response.text}")

    data = response.json()
    audio_url = data.get("audioFile")  # ✅ correct field from working test

    if not audio_url:
        raise Exception(f"Murf API did not return audioFile. Full response: {data}")

    return audio_url


# ---------------- Agent Endpoint ----------------
@app.post("/agent/chat/{session_id}")
async def agent_chat(
    session_id: str,
    audio: UploadFile = File(...),
    x_assemblyai_key: str = Header(...),
    x_murf_key: str = Header(...),
    x_google_key: str = Header(...),
    x_murf_voice_id: str = Header(None)  # optional, can use default
):
    try:
        # Save temp audio file
        temp_file_path = f"temp_{audio.filename}"
        async with aiofiles.open(temp_file_path, "wb") as out_file:
            content = await audio.read()
            await out_file.write(content)

        # Upload and transcribe
        upload_url = await upload_audio_to_assemblyai(temp_file_path, x_assemblyai_key)
        transcript_text = request_transcription(upload_url, x_assemblyai_key)

        # ---------------- Day26 skill example ----------------
        # ---------------- Day26 skill example ----------------
        if "open youtube" in transcript_text.lower():
            webbrowser.open("https://www.youtube.com")
            ai_response = "Opening YouTube for you!"
            murf_audio_url = generate_murf_tts(ai_response, x_murf_key, x_murf_voice_id or "en-US-ken")
    
            os.remove(temp_file_path)
            return {
                "transcription": transcript_text,
                "llm_response": ai_response,
                "murf_audio_url": murf_audio_url,
                "chat_history": chat_history_store.get(session_id, [])
            }

        # Normal flow
        history = chat_history_store.get(session_id, [])
        history.append({"role": "user", "content": transcript_text})
        ai_response = get_gemini_response(history, x_google_key)
        history.append({"role": "assistant", "content": ai_response})
        chat_history_store[session_id] = history
        murf_audio_url = generate_murf_tts(ai_response, x_murf_key, x_murf_voice_id or "en-US-ken")


        os.remove(temp_file_path)

        return {
            "transcription": transcript_text,
            "llm_response": ai_response,
            "murf_audio_url": murf_audio_url,
            "chat_history": history
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
