# main.py

import os
import requests
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from murf import Murf

# Load API Key
load_dotenv()
API_KEY = os.getenv("MURF_API_KEY")
client = Murf(api_key=API_KEY)

app = FastAPI()

# Mount folders
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# VOICE & MOOD Options
VOICE_MOODS = {
    "Miles": {
        "voice_id": "en-US-miles",
        "moods": ['Conversational', 'Promo', 'Narration', 'Newscast', 'Sad']
    },
    "Shane": {
        "voice_id": "en-AU-shane",
        "moods": ['Conversational', 'Narration']
    },
    "Natalie": {
        "voice_id": "en-US-natalie",
        "moods": ['Promo', 'Narration', 'Newscast Formal', 'Meditative', 'Sad', 'Angry']
    }
}


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "voices": VOICE_MOODS,
        "message": None,
        "audio_url": None
    })


@app.post("/generate", response_class=HTMLResponse)
async def generate_audio(
    request: Request,
    text: str = Form(...),
    voice: str = Form(...),
    mood: str = Form(...),
    pitch: int = Form(...)
):
    voice_id = VOICE_MOODS.get(voice, {}).get("voice_id")

    try:
        response = client.text_to_speech.generate(
            format="MP3",
            sample_rate=48000.0,
            channel_type="STEREO",
            text=text,
            voice_id=voice_id,
            style=mood,
            pitch=pitch
        )
        audio_url = getattr(response, "audio_file", None)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "voices": VOICE_MOODS,
            "message": "Audio generated successfully!",
            "audio_url": audio_url
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "voices": VOICE_MOODS,
            "message": f"API Error: {str(e)}",
            "audio_url": None
        })
