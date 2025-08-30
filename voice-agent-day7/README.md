# 30 Days of AI Voice Agents | Day 7: Echo Bot v2

## Overview
Day 7 upgrades the Echo Bot to **Echo Bot v2**, which doesn’t just replay the recorded audio. Instead, it:

1. Transcribes the recorded audio using **AssemblyAI**.
2. Sends the transcription to **Murf API** to generate a new audio file in a Murf voice.
3. Plays back the Murf-generated audio in the browser.

This creates a voice-based echo effect with TTS enhancement.

---

## Features
- **Record Voice**: Record your voice using the Echo Bot.
- **Server-Side Transcription**: Audio is sent to the `/tts/echo` endpoint and transcribed.
- **Murf Voice Playback**: Transcription is converted to audio using Murf TTS API.
- **UI Audio Playback**: Murf-generated audio is returned as a URL and played in the `<audio>` element.

---

## How It Works
1. User records audio in the browser.
2. Recorded audio is sent to `/tts/echo` endpoint in `multipart/form-data`.
3. Server uses **AssemblyAI** to transcribe the audio.
4. Transcription is sent to **Murf API** for text-to-speech generation.
5. Murf returns an audio URL for the new TTS audio.
6. Frontend plays the Murf audio in the `<audio>` element.

---

## Usage
1. Make sure you have API keys for:
   - **AssemblyAI**
   - **Murf**
2. Install required packages:
```bash
pip install assemblyai requests fastapi uvicorn
````

3. Run your FastAPI server:

```bash
uvicorn main:app --reload
```

4. Open the Echo Bot UI in a browser.
5. Record your voice, stop recording, and wait for the Murf audio playback.

---

## Backend Endpoint Example

* **Endpoint**: `POST /tts/echo`
* **Request**: `multipart/form-data` with audio file
* **Response**:

```json
{
  "audio_url": "https://api.murf.ai/v1/audio/generated_audio.mp3"
}
```

---

## Resources

* [FastAPI File Upload](https://fastapi.tiangolo.com/tutorial/request-files/)
* [AssemblyAI Python SDK Core Examples](https://github.com/AssemblyAI/assemblyai-python-sdk?tab=readme-ov-file#core-examples)
* [Murf API Docs - TTS Overview](https://murf.ai/api/docs/text-to-speech/overview)
* [Murf API Docs - TTS Generate](https://murf.ai/api/docs/api-reference/text-to-speech/generate)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

