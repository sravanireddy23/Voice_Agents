import os
import requests
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MURF_API_KEY")

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-audio", response_class=HTMLResponse)
async def generate_audio(request: Request, text: str = Form(...)):
    try:
        response = requests.post(
            "https://api.murf.ai/v1/speech/generate",
            headers={
                "accept": "application/json",
                "Content-Type": "application/json",
                "api-key": API_KEY
            },
            json={
                "voice_id": "en-US-natalie",
                "text": text
            }
        )

        if response.status_code == 200:
            audio_url = response.json().get("audio_url")
            return templates.TemplateResponse("index.html", {
                "request": request,
                "message": "Audio generated!",
                "audio_url": audio_url
            })
        else:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "message": f"Error: {response.json().get('errorMessage', 'Failed')}"
            })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "message": f"Internal error: {str(e)}"
        })
