
# 30 Days of AI Voice Agents | Day 22: Playing Streaming Audio

## Overview
Day 22 focuses on **playing streaming audio in the UI**. Audio chunks received from Murf over websockets are played in real-time in the browser, providing seamless voice feedback for the user.

---

## Features
- **Real-Time Audio Playback**: Play Murf-generated audio as it is received.
- **Chunk-Based Playback**: Audio is streamed in small chunks and appended to the audio buffer.
- **Seamless Experience**: Playback is designed to avoid gaps or delays.
- **Client-Side Implementation**: No server changes are required for this task.

---

## How It Works
1. The server streams Murf-generated audio chunks to the client via websocket.
2. The client receives base64 audio chunks and converts them into **AudioBuffer** objects.
3. The audio is played immediately or appended to a playing buffer for continuous playback.
4. Playback continues until all audio chunks are received and played.

---

## Usage
1. Connect to the websocket endpoint that streams Murf audio.
2. On each `message` event, decode the base64 chunk to audio data.
3. Append the chunk to the current audio buffer or play immediately.

---

## Example Client Code (JavaScript)
```javascript
const audioContext = new AudioContext();
let sourceBuffer = [];

const ws = new WebSocket("ws://localhost:8000/ws/audio");

ws.onmessage = async (event) => {
    const base64Chunk = event.data;
    const audioData = Uint8Array.from(atob(base64Chunk), c => c.charCodeAt(0));
    const audioBuffer = await audioContext.decodeAudioData(audioData.buffer);
    
    const source = audioContext.createBufferSource();
    source.buffer = audioBuffer;
    source.connect(audioContext.destination);
    source.start();
    
    sourceBuffer.push(source);
};
````

---

## Notes

* Ensure audio chunks are received in **sequence** to avoid glitches.
* The goal is to **play streaming audio as smoothly as possible**.
* This completes the pipeline from **LLM → Murf → Client playback**.

---

## Resources

* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [Murf JS Cookbook Example](https://github.com/murf-ai/murf-cookbook/blob/main/examples/text-to-speech/js/websocket/basic/index.js)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

