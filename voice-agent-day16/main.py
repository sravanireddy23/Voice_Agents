import os
import json
import time
import logging
from datetime import datetime
from typing import Optional

import aiofiles
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# -------------------------------
# Basic app + logging
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("day16")

app = FastAPI(title="Day 16 - Streaming Audio over WebSockets")

# CORS (handy if you open the page with a different port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

# Static UI
STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Recordings (saved audio)
RECORDINGS_DIR = "recordings"
os.makedirs(RECORDINGS_DIR, exist_ok=True)
app.mount("/recordings", StaticFiles(directory=RECORDINGS_DIR), name="recordings")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the streaming UI."""
    with open(os.path.join(STATIC_DIR, "index.html"), "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


# -------------------------------
# WebSocket: /ws/audio
# -------------------------------
@app.websocket("/ws/audio")
async def ws_audio(
    websocket: WebSocket,
    session_id: Optional[str] = Query(default="default")
):
    """
    Protocol:
      - Client connects
      - Sends a JSON text message: {"type": "start", "mimeType": "..."} (optional but recommended)
      - Then sends binary messages (ArrayBuffer/Uint8Array) repeatedly
      - When done, sends {"type": "stop"}
      - Server writes bytes to recordings/<session_id>_<timestamp>.webm

    Server sends:
      - {"type": "ready", "filename": "...", "url": "/recordings/<file>"}
      - {"type": "saved", "filename": "...", "url": "/recordings/<file>"}
    """
    await websocket.accept()
    logger.info(f"[WS] Connected (session_id={session_id})")

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"{session_id}_{timestamp}.webm"
    file_path = os.path.join(RECORDINGS_DIR, filename)

    file = None
    try:
        while True:
            message = await websocket.receive()

            # Text control frames (JSON)
            if "text" in message and message["text"] is not None:
                try:
                    data = json.loads(message["text"])
                except json.JSONDecodeError:
                    logger.warning(f"[WS] Non-JSON text received: {message['text']}")
                    continue

                msg_type = data.get("type")
                if msg_type == "start":
                    # open file for writing (create if not exists)
                    if file is None:
                        file = await aiofiles.open(file_path, "wb")
                        logger.info(f"[WS] START -> writing to {file_path}")
                        # Let client know where the file will be served
                        await websocket.send_text(json.dumps({
                            "type": "ready",
                            "filename": filename,
                            "url": f"/recordings/{filename}"
                        }))
                elif msg_type in ("stop", "end"):
                    logger.info("[WS] STOP received")
                    break
                else:
                    logger.info(f"[WS] Text message: {data}")

            # Binary audio frames
            elif "bytes" in message and message["bytes"] is not None:
                if file is None:
                    # if client forgot to send "start", lazily open
                    file = await aiofiles.open(file_path, "wb")
                    logger.info(f"[WS] (lazy) START -> writing to {file_path}")

                chunk: bytes = message["bytes"]
                await file.write(chunk)

            # Any other frame types are ignored
            else:
                logger.debug(f"[WS] Unhandled message: {message}")

    except WebSocketDisconnect:
        logger.info("[WS] Disconnected")
    except Exception as e:
        logger.exception(f"[WS] Error: {e}")
    finally:
        if file is not None:
            await file.flush()
            await file.close()
            logger.info(f"[WS] File saved: {file_path}")
            # Tell the client the file is saved
            try:
                await websocket.send_text(json.dumps({
                    "type": "saved",
                    "filename": filename,
                    "url": f"/recordings/{filename}"
                }))
            except Exception:
                # socket might already be closed
                pass
        try:
            await websocket.close()
        except Exception:
            pass
