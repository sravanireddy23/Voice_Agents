
# 30 Days of AI Voice Agents | Day 23: Complete Voice Agent

## Overview
Day 23 is about **connecting all components** to create a fully functional **voice agent**. The agent can now handle end-to-end conversational interactions: recording, transcription, LLM response, TTS conversion, and streaming audio playback.

---

## Features
- **End-to-End Conversation**: From user voice input to AI response.
- **AssemblyAI STT**: Transcribes user audio in real-time.
- **LLM Integration**: Generates contextual responses.
- **Chat History**: Maintains conversation context across sessions.
- **Murf TTS**: Converts LLM responses to audio.
- **Streaming Playback**: Sends audio chunks to the client and plays them in real-time.
- **Websocket Communication**: Handles audio streaming between server and client.

---

## How It Works
1. The client records the user’s voice and streams it to the server.
2. Server transcribes the audio using **AssemblyAI**.
3. The transcript is sent to the **LLM API** to generate a response.
4. The server stores the conversation in **chat history**.
5. The response is sent to **Murf** to generate audio.
6. Audio chunks are streamed back to the client via **websockets**.
7. Client plays the audio in real-time, completing the conversational loop.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Set your API keys:

```bash
export ASSEMBLYAI_API_KEY="your_assemblyai_key"
export GEMINI_API_KEY="your_gemini_key"
export MURF_API_KEY="your_murf_key"
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Open the client UI and start interacting with the voice agent.
5. Observe real-time transcription and streaming audio responses.

---

## Notes

* This is a **complete conversational voice agent**.
* Combines transcription, LLM generation, TTS, chat history, and streaming audio.
* Provides a solid foundation for further enhancements like emotion detection, multi-user sessions, or advanced voice effects.

---

## Resources

* [AssemblyAI Streaming API](https://www.assemblyai.com/docs/api-reference/streaming-api/streaming-api)
* [Google Gemini API](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent)
* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


