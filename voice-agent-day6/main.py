from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil, os
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv()
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    audio_path = os.path.join(UPLOAD_FOLDER, "voice.wav")
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"file_path": f"/uploads/voice.wav"}

@app.post("/transcribe/")
async def transcribe_audio():
    audio_path = os.path.join(UPLOAD_FOLDER, "voice.wav")
    if not os.path.exists(audio_path):
        return JSONResponse(status_code=404, content={"error": "Audio file not found."})
    
    transcriber = aai.Transcriber()
    try:
        transcript = transcriber.transcribe(audio_path)
        return {"transcript": transcript.text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Transcription failed: {str(e)}"})
