
# 30 Days of AI Voice Agents | Day 14: Refactor & Cleanup

## Overview
Day 14 focuses on **refactoring** and **cleaning up** the AI Voice Agent project to make it more maintainable, readable, and production-ready. The code is now organized with proper structure, logging, and separation of concerns, while preserving all existing functionality.

---

## Refactoring Highlights
- **Pydantic Schemas**: Defined request and response models for all endpoints.
- **Service Layer**: Extracted third-party API interactions (AssemblyAI STT, Murf TTS, LLM) into `/services` folder.
- **Logging**: Added structured logging for better visibility of API calls, errors, and workflow.
- **Code Cleanup**: Removed unused imports, variables, and redundant functions.
- **Readable Handlers**: Endpoints now have clean and concise logic by delegating processing to services.

---

## Features
All existing features remain intact, with improved code quality:
- **Voice Recording & Playback**
- **Server-Side Transcription (STT)**
- **LLM Integration for Responses**
- **Murf TTS Audio Generation**
- **Chat History Management**
- **Error Handling with Fallback Responses**
- **Polished UI with Interactive Record Button**

---

## Project Structure (Refactored)
- `/services` – Handles third-party API calls (STT, TTS, LLM)
- `/schemas` – Pydantic models for request/response validation
- `/static` – Frontend assets (CSS, JS)
- `/templates` – HTML files
- `main.py` – FastAPI server
- `.env` – API keys and environment variables
- `README.md` – Project documentation

---

## Setup & Running
1. **Clone Repository**
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
export ASSEMBLYAI_API_KEY="your_assemblyai_key"
export GEMINI_API_KEY="your_gemini_key"
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

## Notes

* Code is now structured for easier future enhancements.
* Service layer and schemas make adding new features simpler and cleaner.
* Logging ensures easier debugging in development and production environments.

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


