import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# -----------------------------------------------------------------------------
# FastAPI app
# -----------------------------------------------------------------------------
app = FastAPI(title="Day 15 WebSocket Echo")

# CORS (handy if you test from other origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (ws.html, ws.js, ws.css)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root -> serve the test page
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/ws.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

# -----------------------------------------------------------------------------
# /ws WebSocket echo endpoint
# -----------------------------------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    client = f"{websocket.client.host}:{websocket.client.port}"
    logging.info(f"[WS] Connected: {client}")
    try:
        while True:
            # Receive text message from client
            data = await websocket.receive_text()
            logging.info(f"[WS] From {client}: {data}")

            # Echo it back
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        logging.info(f"[WS] Disconnected: {client}")
