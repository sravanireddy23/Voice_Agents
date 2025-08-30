# 30 Days of AI Voice Agents | Day 15: Websockets

## Overview
Day 15 marks the halfway point of the challenge! 🎉  
Today, we implement **websocket communication** between the client and the server. This lays the foundation for real-time streaming interactions in the AI Voice Agent in future tasks.

---

## Features
- **Websocket Endpoint**: `/ws` to establish a connection between client and server.
- **Echo Server**: Messages sent from the client are echoed back by the server.
- **Real-Time Communication**: Enables sending and receiving messages instantly.
- **Non-Intrusive**: This task does not modify existing conversational agent functionality; it’s developed in a separate branch (`streaming`).

---

## How It Works
1. The client opens a websocket connection to `/ws`.
2. Any message sent by the client is received by the server.
3. The server echoes the message back to the client.
4. You can test this using **Postman**, **websocket clients**, or custom frontend code.

---

## Usage
1. Create a new branch to work on websockets:
```bash
git checkout -b streaming
````

2. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

3. Connect to the websocket endpoint `/ws` using Postman or a websocket client.
4. Send a message and observe the server echo it back.

---

## Example Server Code

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
```

---

## Notes

* This task establishes the **streaming foundation** for future real-time audio transcription and TTS.
* Non-streaming functionality continues to work on the `main` branch.
* Testing can be done via Postman, browser console, or any websocket client.

---

## Resources

* [FastAPI Websockets Tutorial](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student
