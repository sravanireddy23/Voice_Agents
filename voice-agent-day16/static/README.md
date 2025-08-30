
# 30 Days of AI Voice Agents | Day 16: Streaming Audio

## Overview
Day 16 focuses on **streaming audio** from the client to the server using **websockets**. Instead of sending the entire recording at once, audio data is streamed in real-time and saved to a file on the server. This is a foundational step for real-time transcription and TTS in future tasks.

---

## Features
- **Websocket Audio Streaming**: Audio chunks are sent continuously from the client to the server.
- **Server-Side Saving**: Received audio chunks are written to a file in binary format.
- **Binary Data Handling**: Websockets handle `bytes` for audio streaming.
- **Prototype-Friendly**: No transcription, LLM processing, or TTS is required in this task.
- **UI Independence**: Existing UI may break; focus is on reliable audio streaming.

---

## How It Works
1. The client records audio in small chunks.
2. Each audio chunk is sent to the server over a websocket connection at a regular interval.
3. The server receives the audio data and writes it sequentially to a file.
4. The saved file can later be used for transcription, LLM processing, or TTS.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

3. Connect to `/ws` websocket endpoint using your updated recording client.
4. Stream audio from the browser; the server saves the audio chunks to a file (e.g., `recorded_audio.wav`).

---

## Example Server Code

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_audio_stream(websocket: WebSocket):
    await websocket.accept()
    with open("recorded_audio.wav", "wb") as f:
        while True:
            data = await websocket.receive_bytes()
            f.write(data)
```

---

## Notes

* This task focuses purely on **audio streaming and file saving**.
* UI may not function as before; the goal is to ensure audio is received and saved reliably.
* Later tasks will add real-time transcription and TTS on top of this streaming pipeline.

---

## Resources

* [FastAPI Websockets Tutorial](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


