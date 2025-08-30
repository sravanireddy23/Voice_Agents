
# 30 Days of AI Voice Agents | Day 29: Final Documentation

## Overview
Day 29 focuses on **finalizing documentation** for your AI voice agent. Update your README.md to reflect all features, improvements, and special skills added throughout the challenge. Optionally, create a blog post to showcase your project and journey.

---

## Features
- **Voice Recording & Playback**: Record your voice and hear it played back.
- **Server-Side Transcription**: Audio is transcribed using AssemblyAI.
- **Echo Bot v2**: Transcribe user audio, generate Murf voice response, and play it back.
- **LLM Integration**: Google Gemini API powers conversational responses.
- **Chat History**: Maintains session-wise conversation history for context-aware responses.
- **Error Handling**: Robust handling of API failures with fallback messages.
- **Special Skills**:
  - Skill 1: Web search / Weather / News queries
  - Skill 2: Additional skill or enhancement from Day 26
- **UI Revamp & Customization**:
  - Modern and interactive interface
  - API key input section for user-provided credentials
  - Record button animation and improved audio playback experience
- **Streaming & Websockets**:
  - Real-time audio streaming to the server and client
  - Streaming LLM responses
  - Murf Websocket integration for live TTS audio
- **Deployment**: Fully hosted agent accessible publicly via cloud provider

---

## How It Works
1. **Client Interaction**:
   - User records audio using the browser UI.
   - Audio is sent to server endpoints or streamed via websockets.
2. **Server Processing**:
   - Audio is transcribed using AssemblyAI.
   - LLM processes the transcript and generates a response.
   - Chat history is maintained for context.
   - Response is sent to Murf TTS for voice output.
3. **Client Playback**:
   - Streaming audio or completed response audio is played back to the user.
   - Special skills can be invoked automatically based on the user query.
4. **Configuration**:
   - Users can provide API keys via the UI or environment variables.

---

## Usage
1. Clone the repository:
```bash
git clone <repo_url>
cd voice-agent
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set API keys as environment variables or enter them in the UI.
4. Run the server:

```bash
uvicorn main:app --reload
```

5. Open the client in a browser and start interacting with your agent.
6. Enjoy a fully functional, persona-driven conversational AI agent.

---

## Notes

* Ensure API keys are valid to prevent connection issues.
* Free tiers of cloud services should be monitored for usage limits.
* The project demonstrates integration of **STT, LLM, TTS, Websockets, and special skills** in a single AI voice agent.

---

## Resources

* [AssemblyAI Streaming API](https://www.assemblyai.com/docs/api-reference/streaming-api/streaming-api)
* [Google Gemini API](https://ai.google.dev/api/generate-content)
* [Murf Websockets API](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)
* [Render.com Deployment](https://render.com/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

