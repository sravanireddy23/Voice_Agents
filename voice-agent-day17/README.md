
# 30 Days of AI Voice Agents | Day 17: Websockets and AssemblyAI

## Overview
Day 17 introduces **real-time audio transcription** using **AssemblyAI's streaming API**. Audio streamed via websockets from the client is now transcribed on the server as it arrives, providing instant text output. This is a key step towards building a fully **streaming conversational voice agent**.

---

## Features
- **Websocket Streaming**: Continuously receive audio chunks from the client.
- **AssemblyAI Streaming Transcription**: Transcribe incoming audio in real-time.
- **Immediate Output**: Transcriptions are printed to the server console or displayed on the UI.
- **Audio Format Requirement**: Audio must be **16kHz, 16-bit, mono PCM** to be compatible with AssemblyAI.

---

## How It Works
1. The client records audio in small chunks and sends them via websocket.
2. The server receives audio chunks and feeds them to AssemblyAI's streaming transcription SDK.
3. AssemblyAI returns partial or complete transcription text as the audio is processed.
4. The server prints or updates the transcription output in real-time.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Set your **AssemblyAI API key** in the environment:

```bash
export ASSEMBLYAI_API_KEY="your_assemblyai_key"
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Connect to the `/ws` endpoint from your recording client and stream audio.
5. Watch the server console or UI update with the live transcription.

---

## Example Server Code

```python
from fastapi import FastAPI, WebSocket
from assemblyai import Transcriber
import asyncio

app = FastAPI()
transcriber = Transcriber(api_key="your_assemblyai_key")

@app.websocket("/ws")
async def websocket_stream_transcription(websocket: WebSocket):
    await websocket.accept()
    async for audio_chunk in websocket.iter_bytes():
        text = transcriber.transcribe(audio_chunk)
        print("Transcription:", text)
```

---

## Notes

* Audio must be in **16kHz, 16-bit, mono PCM**.
* Focus is on **streaming transcription**, no LLM or TTS is involved yet.
* This sets the foundation for **real-time conversational AI**.

---

## Resources

* [AssemblyAI Streaming API Documentation](https://www.assemblyai.com/docs/api-reference/streaming-api/streaming-api)
* [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk?tab=readme-ov-file#streaming-examples)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

