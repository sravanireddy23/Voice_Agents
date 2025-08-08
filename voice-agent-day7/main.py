import os
import uuid
import requests
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
GENERATED_FOLDER = "static/generated"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def get_valid_voice_id():
    voices_url = "https://api.murf.ai/v1/speech/voices"
    headers = {"accept": "application/json", "api-key": MURF_API_KEY}
    res = requests.get(voices_url, headers=headers, timeout=10)
    res.raise_for_status()
    voices = res.json()
    if not voices:
        raise RuntimeError("No voices returned by Murf voices API")
    # Pick first English voice (or any you want)
    for v in voices:
        if "en" in v.get("language", "").lower():
            return v["voiceId"]
    return voices[0]["voiceId"]

@app.post("/tts/echo")
async def tts_echo(file: UploadFile = File(...)):
    # Save original audio file
    original_filename = f"{uuid.uuid4()}_{file.filename}"
    original_path = os.path.join(UPLOAD_FOLDER, original_filename)
    with open(original_path, "wb") as f:
        f.write(await file.read())

    # Transcribe with AssemblyAI
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(original_path)
    text = (transcript.text or "").strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "No speech detected."})

    # Get Murf voiceId dynamically
    try:
        voice_id = get_valid_voice_id()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to get voice ID: {e}"})

    # Generate Murf voice
    tts_url = "https://api.murf.ai/v1/speech/generate"
    payload = {"voiceId": voice_id, "text": text, "format": "MP3"}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "api-key": MURF_API_KEY
    }
    res = requests.post(tts_url, json=payload, headers=headers)
    if res.status_code != 200:
        return JSONResponse(status_code=500, content={"error": f"Murf error: {res.text}"})

    murf_audio_url = res.json().get("audioFile")
    if not murf_audio_url:
        return JSONResponse(status_code=500, content={"error": "No audio returned by Murf."})

    # Save Murf voice audio locally
    murf_filename = f"{uuid.uuid4()}_murf.mp3"
    murf_path = os.path.join(GENERATED_FOLDER, murf_filename)
    audio_data = requests.get(murf_audio_url, timeout=30).content
    with open(murf_path, "wb") as f:
        f.write(audio_data)

    # Return both file URLs
    return {
        "original_audio_url": f"/uploads/{original_filename}",
        "murf_audio_url": f"/static/generated/{murf_filename}",
        "transcription": text
    }
