# 30 Days of AI Voice Agents

## Overview
This project is a **30-day journey building a fully functional AI Voice Agent**. The agent can record your voice, transcribe it, process it through a Large Language Model (LLM), generate intelligent responses, and speak back to you using Murf's text-to-speech. It incorporates chat history, error handling, special skills, streaming audio, and a polished UI.

The goal of this challenge was to build an end-to-end conversational AI with **real-time audio streaming**, **LLM integration**, and **TTS output**.

---

## Features

### Core Features
- 🎤 **Voice Recording & Playback** – Record audio in the browser.
- 📝 **Server-Side Transcription** – Using **AssemblyAI** for speech-to-text.
- 💬 **LLM Integration** – Google Gemini API for smart conversational responses.
- 🧠 **Chat History** – Maintains session-wise conversation context.
- 🔊 **Text-to-Speech** – Murf API generates spoken responses.
- ⚡ **Real-Time Streaming** – Audio streaming via websockets between client and server.
- 🛠️ **Error Handling** – Graceful fallback messages for API failures.
- ✨ **Special Skills** – Web search, news updates, weather info, and more.
- 🎨 **UI Revamp & Animation** – Modern, interactive interface with API key input.

### Advanced Features
- 🖥️ **Echo Bot v1 & v2** – Repeat back what you said or generate Murf voice responses.
- 🌎 **Deployment Ready** – Host your agent publicly with services like Render.com.
- 🔧 **Modular & Clean Code** – Refactored code with schemas, services, and logging.
- 🖥️ **Streaming LLM Responses** – Receive and play LLM outputs in real-time.
- 🎭 **Persona Support** – Assign a character or personality to your agent.

---

## Architecture

```

\[Client Browser]
\|-- Record Audio
\|-- Display Chat History
\|-- API Key Input
|
\[FastAPI Server]
\|-- /transcribe/file -> AssemblyAI STT
\|-- /tts/echo -> Murf TTS
\|-- /llm/query -> Google Gemini LLM
\|-- /agent/chat/{session\_id} -> Chat History
\|-- Websockets -> Streaming Audio & Responses
\|-- Special Skills -> Weather / News / Web Search

````

---

## Technologies Used
- **Python 3.13**  
- **FastAPI** – API server and websocket handling
- **AssemblyAI** – Speech-to-text (STT)
- **Google Gemini** – Large Language Model (LLM)
- **Murf** – Text-to-speech (TTS)
- **HTML/CSS/JavaScript** – Interactive UI
- **Websockets** – Real-time streaming
- **Git & GitHub** – Version control
- **Render.com / Cloud Hosting** – Deployment

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone <repo_url>
cd voice-agent
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set API keys** (via environment variables or UI):

```bash
export ASSEMBLYAI_API_KEY=<your_assemblyai_key>
export GEMINI_API_KEY=<your_gemini_key>
export MURF_API_KEY=<your_murf_key>
```

4. **Run the server**

```bash
uvicorn main:app --reload
```

5. **Open the client** in your browser:

* Record your voice, interact with the agent, and hear real-time responses.

---

## Usage

* **Record Audio** → Sends audio to server.
* **Transcription** → AssemblyAI converts speech to text.
* **LLM Response** → Google Gemini processes text.
* **TTS Audio** → Murf generates voice output.
* **Streaming** → Audio can be streamed in real-time via websockets.
* **Special Skills** → Query for weather, news, or web search.
* **Chat History** → Maintains session conversation for context.

---

## Deployment

* The agent can be deployed on any cloud provider with a free tier (e.g., [Render.com](https://render.com)).
* Ensure API keys are configured and `uvicorn` is set as the startup command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Notes

* Ensure correct API keys to prevent connection errors.
* Streaming requires 16kHz, 16-bit, mono PCM audio.
* Murf TTS supports a maximum of 3000 characters per request.
* Run the FastAPI server in a single worker process to maintain chat history consistency.
* Monitor free tier limits of cloud providers to avoid charges.

---

## Resources

* [AssemblyAI Documentation](https://www.assemblyai.com/docs/)
* [Google Gemini API](https://ai.google.dev/api/generate-content)
* [Murf API Websockets](https://murf.ai/api/docs/text-to-speech/web-sockets)
* [FastAPI Websockets](https://fastapi.tiangolo.com/advanced/websockets/)
* [Render Deployment Guide](https://render.com/)

---

## Author

**Sravani Reddy Gavinolla**
Bachelor's in Computer Science & Engineering
GitHub: [https://github.com/sravanireddy23](https://github.com/sravanireddy23)
LinkedIn: [https://www.linkedin.com/in/sravani-reddy-gavinolla-14b421331/](https://www.linkedin.com/in/sravani-reddy-gavinolla-14b421331/)

