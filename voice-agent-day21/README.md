
# 30 Days of AI Voice Agents | Day 21: Streaming Audio Data to Client

## Overview
Day 21 focuses on **streaming audio data from the server to the client**. Murf-generated audio (base64) is sent over websockets to the client in real-time. The client accumulates the chunks, laying the groundwork for eventual audio playback in the browser.

---

## Features
- **Websocket Streaming**: Send Murf audio chunks (base64) to the client over a websocket connection.
- **Chunk Accumulation**: Client accumulates base64 audio chunks in an array.
- **Server Acknowledgement**: Print acknowledgements in the server console when chunks are received by the client.
- **UI-Independent**: Audio playback in `<audio>` is not required at this stage.

---

## How It Works
1. The server receives streaming LLM responses and converts them to audio via Murf.
2. Base64 audio chunks are sent to the client over a websocket.
3. The client stores each chunk in an array for future use.
4. Server prints acknowledgements for each chunk received by the client.

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

3. Connect to the websocket endpoint from your client.
4. Stream audio from Murf to the client.
5. Observe acknowledgements printed on the server console.

---

## Example Server Code

```python
from fastapi import FastAPI, WebSocket
import json

app = FastAPI()

@app.websocket("/ws/audio")
async def stream_audio_to_client(websocket: WebSocket):
    await websocket.accept()
    for base64_chunk in get_murf_audio_chunks():
        await websocket.send_text(base64_chunk)
        print("Sent audio chunk to client")
```

---

## Notes

* Audio is streamed in **real-time** as base64 chunks.
* The client accumulates chunks for **future playback**.
* This step enables fully streaming voice interaction between server and client.

---

## Resources

* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)
* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student
