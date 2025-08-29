import assemblyai as aai
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# ✅ Set your AssemblyAI API Key
aai.settings.api_key = "YOUR_ASSEMBLYAI_API_KEY"

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def get():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws/audio")
async def websocket_audio(websocket: WebSocket):
    await websocket.accept()

    # Create realtime transcriber
    transcriber = aai.RealtimeTranscriber(
        sample_rate=16000,
        encoding="pcm_s16le",
        on_open=lambda: print("🔗 Connected to AssemblyAI"),
        on_data=lambda msg: print("📝 Transcript:", msg.text),
        on_error=lambda err: print("❌ Error:", err),
        on_close=lambda code, reason: print(f"🔌 Closed {code}: {reason}"),
    )

    transcriber.connect()

    try:
        while True:
            # Receive audio from frontend
            data = await websocket.receive_bytes()
            transcriber.send_audio(data)

    except Exception as e:
        print("⚠️ WebSocket error:", e)

    finally:
        transcriber.close()
        await websocket.close()
