
# 30 Days of AI Voice Agents

## Overview
This project is a **multi-day journey** to build a fully functional AI Voice Agent. The agent can record your voice, transcribe it, generate intelligent responses using an LLM, and respond with lifelike speech via **Murf TTS**. Over the 30 days, features such as chat history, error handling, and a polished UI were added to make the agent interactive and production-ready.

---

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI
- **Voice Transcription (STT)**: AssemblyAI
- **Text-to-Speech (TTS)**: Murf API
- **Large Language Model (LLM)**: Google Gemini API
- **Environment Management**: `.env` for API keys
- **Optional**: In-memory datastore for chat history

---

## Architecture
```

\[ User Voice Input ]
↓
Browser MediaRecorder
↓
POST Audio
↓
FastAPI Server
↓
AssemblyAI Transcription
↓
LLM Response
↓
Murf TTS
↓
Return Audio URL → Browser <audio>

````

---

## Features
- **Voice Recording**: Record audio directly from the browser.
- **Server-Side Transcription**: Convert audio to text using AssemblyAI.
- **Conversational AI**: Context-aware responses using Gemini API.
- **Voice Output**: Murf TTS converts text responses to audio.
- **Chat History**: Session-based memory to remember previous messages.
- **Error Handling**: Graceful fallback audio and UI notifications.
- **Polished UI**: Interactive record button, animations, and clean layout.

---

## Setup & Running
1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/voice-agent.git
cd voice-agent
````

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set Environment Variables**

```bash
# AssemblyAI
export ASSEMBLYAI_API_KEY="your_assemblyai_key"
# Gemini (LLM)
export GEMINI_API_KEY="your_gemini_key"
# Murf TTS
export MURF_API_KEY="your_murf_key"
```

4. **Run FastAPI Server**

```bash
uvicorn main:app --reload
```

5. **Open UI**

```
http://127.0.0.1:8000/?session_id=<your_session_id>
```

---

## Usage

* Click the **Record** button to start interacting with the agent.
* The agent will respond in Murf-generated audio, maintaining conversation context.
* The session preserves chat history for multi-turn conversations.

---

## Screenshots

*(Add screenshots of your UI, audio playback, and chat responses here for LinkedIn or documentation.)*

---

## Resources

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
* [Murf API Documentation](https://murf.ai/api/docs/api-reference/text-to-speech/generate)
* [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


