# 30 Days of AI Voice Agents | Day 9: The Full Non-Streaming Pipeline

## Overview
Day 9 integrates the full **non-streaming voice pipeline**. The AI Voice Agent now not only records your voice but also transcribes it, generates a response using an LLM (e.g., Google Gemini), and converts the response into speech using **Murf TTS**. The resulting audio is played back in the browser, completing the end-to-end voice interaction.

---

## Features
- **Record Voice**: Capture audio input from the user.
- **Server-Side Transcription**: Audio is transcribed using AssemblyAI.
- **LLM Response**: The transcription is sent to the LLM API for text generation.
- **Murf TTS**: LLM text output is converted to audio using Murf API.
- **Playback**: Murf-generated audio is returned to the frontend and played in the `<audio>` element.
- Handles LLM responses exceeding Murf's 3000-character limit by splitting into multiple requests or limiting prompt size.

---

## How It Works
1. User records audio in the browser.
2. Recorded audio is sent to `/llm/query` endpoint in `multipart/form-data`.
3. Server transcribes the audio using **AssemblyAI**.
4. Transcription is sent to **LLM API** to generate a response.
5. LLM response is converted to speech using **Murf TTS API**.
6. Murf-generated audio file(s) URL(s) are returned to the frontend.
7. Frontend plays the audio response in the `<audio>` element.

---

## Usage
1. Ensure you have API keys for:
   - **AssemblyAI**
   - **Google Gemini (LLM)**
   - **Murf**
2. Install required packages:
```bash
pip install assemblyai requests fastapi uvicorn
````

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Open the UI in a browser, record your voice, and stop recording.
5. The bot will respond with Murf-generated speech corresponding to the LLM response.

---

## Backend Endpoint Example

* **Endpoint**: `POST /llm/query`
* **Request**: `multipart/form-data` with audio file
* **Response**:

```json
{
  "audio_url": "https://api.murf.ai/v1/audio/llm_response.mp3"
}
```

---

## Notes

* Murf TTS `/v1/speech/generate` endpoint has a **3000-character limit** per request.
* If the LLM response exceeds this limit, the response should be split into multiple TTS requests or the prompt adjusted to shorten output.

---

## Resources

* [AssemblyAI Python SDK](https://github.com/AssemblyAI/assemblyai-python-sdk)
* [Murf API Documentation](https://murf.ai/api/docs/api-reference/text-to-speech/generate)
* [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

