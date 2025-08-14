import os
import asyncio
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import aiohttp

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
MURF_API_KEY = os.getenv("MURF_API_KEY")
MURF_VOICE_ID = os.getenv("MURF_VOICE_ID", "en-US-ken")

if not ASSEMBLYAI_API_KEY or not MURF_API_KEY:
    raise Exception("Missing API keys")

@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/llm/query")
async def llm_query(audio: UploadFile = File(...)):
    try:
        audio_bytes = await audio.read()
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(audio_bytes)

        transcript = await transcribe_assemblyai(audio_path)
        # MOCK Gemini LLM response — replace with real API later
        llm_response = f"Mock reply to: {transcript}"

        audio_url = await call_murf_tts(llm_response)
        return JSONResponse({
            "status": "success",
            "transcript": transcript,
            "llm_response": llm_response,
            "audio_url": audio_url
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

async def transcribe_assemblyai(filepath):
    headers = {'authorization': ASSEMBLYAI_API_KEY}
    async with aiohttp.ClientSession() as session:
        with open(filepath, 'rb') as f:
            upload_resp = await session.post('https://api.assemblyai.com/v2/upload', headers=headers, data=f)
            if upload_resp.status != 200:
                text = await upload_resp.text()
                raise Exception(f"AssemblyAI upload error: {text}")
            upload_json = await upload_resp.json()
            audio_url = upload_json['upload_url']

        transcript_request = {"audio_url": audio_url, "language_code": "en_us"}
        transcript_resp = await session.post('https://api.assemblyai.com/v2/transcript', headers=headers, json=transcript_request)
        transcript_json = await transcript_resp.json()
        transcript_id = transcript_json['id']

        while True:
            status_resp = await session.get(f'https://api.assemblyai.com/v2/transcript/{transcript_id}', headers=headers)
            status_json = await status_resp.json()
            if status_json['status'] == 'completed':
                return status_json['text']
            elif status_json['status'] == 'error':
                raise Exception("Transcription failed: " + status_json.get('error', 'Unknown error'))
            await asyncio.sleep(3)

async def call_murf_tts(text):
    if not text.strip():
        raise Exception("Empty text for TTS")

    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "voice": MURF_VOICE_ID,
        "text": text,
        "format": "mp3"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.murf.ai/v1/speech/generate", headers=headers, json=payload) as resp:
            if resp.status != 200:
                text = await resp.text()
                raise Exception(f"Murf API error: {text}")
            data = await resp.json()
            return data.get("audioFile", "")

