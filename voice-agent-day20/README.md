
# 30 Days of AI Voice Agents | Day 20: Murf Websockets

## Overview
Day 20 introduces **Murf Websockets** to generate audio from the LLM’s streaming response. The LLM text is sent to Murf over a websocket, which returns audio in **base64 format**. This allows real-time TTS conversion for the agent’s response.

---

## Features
- **Real-Time TTS**: Send streaming LLM responses to Murf and receive audio instantly.
- **Base64 Audio**: Murf returns audio data encoded in base64 format.
- **Context Management**: Use a static `context_id` to avoid context limit errors.
- **Server-Side Processing**: No changes to the UI; audio is printed on the server console.

---

## How It Works
1. The LLM streams its response to the server.
2. The server forwards the text chunks to Murf over a websocket connection.
3. Murf streams back audio in **base64 format**.
4. The server prints or logs the base64 audio to the console.
5. In future tasks, this audio will be played back in the UI.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Set your Murf API key:

```bash
export MURF_API_KEY="your_murf_key"
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Send the LLM streaming response to Murf via websocket.
5. Observe the base64 encoded audio in the server console.

---

## Example Server Code

```python
import asyncio
import websockets
import json

MURF_WS_URL = "wss://api.murf.ai/v1/tts"

async def send_to_murf(text, context_id="static_context"):
    async with websockets.connect(MURF_WS_URL, extra_headers={"Authorization": "Bearer your_murf_key"}) as ws:
        await ws.send(json.dumps({
            "context_id": context_id,
            "text": text
        }))
        async for message in ws:
            data = json.loads(message)
            if "audio" in data:
                print("Base64 Audio:", data["audio"])
```

---

## Notes

* Murf returns audio in **base64** to allow streaming playback.
* Using a **static context\_id** prevents context limit errors.
* This step prepares the agent for **real-time audio playback** in the UI.

---

## Resources

* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

