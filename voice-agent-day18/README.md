
# 30 Days of AI Voice Agents | Day 18: Turn Detection

## Overview
Day 18 introduces **turn detection** using AssemblyAI’s streaming API. This feature allows the system to detect when a user stops speaking, enabling the AI to respond only after the user’s turn ends. The transcription is displayed on the UI **at the end of the turn**, improving conversational flow and timing.

---

## Features
- **Turn Detection**: Detects when the user has finished speaking.
- **Websocket Notification**: Sends a message to the client signaling the end of the turn.
- **UI Update**: Displays the complete transcription once the user’s turn ends.
- **Real-Time Feedback**: Ensures the agent responds only after the user stops talking.

---

## How It Works
1. Audio is streamed from the client to the server over websockets.
2. AssemblyAI’s streaming API monitors the audio for **end-of-turn cues**.
3. When a turn is detected:
   - The server sends a websocket message to the client.
   - The client updates the UI with the final transcription.
4. The agent can now process the turn and respond appropriately.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Set your AssemblyAI API key in the environment:

```bash
export ASSEMBLYAI_API_KEY="your_assemblyai_key"
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Connect to the `/ws` websocket endpoint from the client and stream audio.
5. Observe **turn detection notifications** and the transcription update on the UI.

---

## Example Server Code

```python
from fastapi import FastAPI, WebSocket
from assemblyai import Transcriber

app = FastAPI()
transcriber = Transcriber(api_key="your_assemblyai_key")

@app.websocket("/ws")
async def websocket_turn_detection(websocket: WebSocket):
    await websocket.accept()
    async for event in transcriber.stream(websocket):
        if event.type == "turn.end":
            await websocket.send_text("TURN_ENDED")
            print("Turn ended. Final transcription:", event.text)
```

---

## Notes

* Turn detection improves **conversational timing** by letting the agent respond only after the user finishes speaking.
* The transcription is displayed **once per turn**, rather than continuously.
* Essential for real-time streaming conversational AI.

---

## Resources

* [AssemblyAI Streaming API](https://www.assemblyai.com/docs/api-reference/streaming-api/streaming-api)
* [Turn Detection Documentation](https://www.assemblyai.com/docs/speech-to-text/universal-streaming#turn-object)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


