# 30 Days of AI Voice Agents | Day 10: Chat History

## Overview
Day 10 introduces a **chat history** feature to the AI Voice Agent, allowing the LLM to remember previous messages in a conversation. Each conversation session is tracked using a **session ID**, and the chat history is stored in a datastore (e.g., an in-memory dictionary for prototype purposes). This enables the bot to maintain context and provide coherent multi-turn conversations.

---

## Features
- **Session-Based Chat History**: Conversations are tracked per session using a unique session ID.
- **Audio Input**: Users record their voice; the audio is transcribed into text.
- **LLM Response with Context**: Previous messages in the session are included in the LLM prompt for context-aware responses.
- **Murf TTS Playback**: LLM responses are converted to speech using Murf API and played in the UI.
- **Continuous Conversation**: The bot automatically starts recording the user's next message after a response is played.

---

## How It Works
1. User records audio in the browser.
2. Recorded audio is sent to `/agent/chat/{session_id}` endpoint.
3. Server transcribes the audio using AssemblyAI.
4. Previous chat history for the session is fetched from the datastore.
5. Transcribed text is appended to chat history.
6. The full conversation history is sent to the LLM API to generate a response.
7. LLM response is added to chat history and converted to audio using Murf TTS.
8. Murf-generated audio is returned to the frontend and played in the `<audio>` element.
9. After playback, the bot automatically starts recording the next user message.

---

## Usage
1. Run the FastAPI server:
```bash
uvicorn main:app --reload
````

2. Open the UI in a browser with a session ID in the query parameters:

```
http://localhost:8000/?session_id=abc123
```

3. Start recording your voice and interact with the bot.
4. The bot maintains context across multiple turns and replies in Murf-generated speech.

---

## Backend Endpoint Example

* **Endpoint**: `POST /agent/chat/{session_id}`
* **Request**: `multipart/form-data` with audio file
* **Response**:

```json
{
  "audio_url": "https://api.murf.ai/v1/audio/session_response.mp3"
}
```

---

## Notes

* Use a single FastAPI worker to ensure in-memory datastore consistency.
* The chat history can be stored in a simple dictionary for prototyping:

```python
chat_history = {}  # Key: session_id, Value: list of messages
```

* Each new user input and LLM response is appended to the session’s chat history.

---

## Resources

* [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
* [Murf API Documentation](https://murf.ai/api/docs/api-reference/text-to-speech/generate)
* [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

