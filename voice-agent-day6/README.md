# 30 Days of AI Voice Agents | Day 6: Implement Server-Side Transcription

## Overview
On Day 6, we extend the Echo Bot by implementing **server-side transcription**. Instead of just uploading audio, the server now transcribes the recorded audio and returns the text transcription to the UI. The transcription is done using **AssemblyAI's Python SDK**.

---

## Features
- **Record Voice**: Continue using the Echo Bot to record audio in the browser.
- **Server-Side Transcription**: Recorded audio is sent directly to the `/transcribe/file` endpoint.
- **Display Transcription**: The returned text is displayed in the UI.
- **No Temporary Storage**: Audio files are sent and transcribed directly, without saving on the server.

---

## How It Works
1. User records audio using the **Echo Bot**.
2. On stopping the recording, the audio file is sent to the FastAPI server at `/transcribe/file`.
3. The server uses **AssemblyAI** to transcribe the audio file.
4. AssemblyAI returns the transcription as a string.
5. The frontend displays the transcription on the page.

---

## Usage
1. Sign up for AssemblyAI and get your API key: [AssemblyAI Signup](https://www.assemblyai.com/dashboard/signup)
2. Install AssemblyAI Python SDK:
```bash
pip install assemblyai
````

3. Set your API key in your server environment:

```bash
export ASSEMBLYAI_API_KEY="your_api_key_here"  # Linux/Mac
set ASSEMBLYAI_API_KEY="your_api_key_here"     # Windows
```

4. Run your FastAPI server:

```bash
uvicorn main:app --reload
```

5. Open your HTML page, record your voice, and stop recording.
6. The server will transcribe the audio and display the text in the UI.

---

## Backend Endpoint Example

* **Endpoint**: `POST /transcribe/file`
* **Request**: `multipart/form-data` with audio file
* **Response**:

```json
{
  "transcription": "Hello, this is a test of the server-side transcription."
}
```

---

## Resources

* [AssemblyAI Getting Started](https://www.assemblyai.com/docs/getting-started/transcribe-an-audio-file)
* [AssemblyAI Python SDK](https://pypi.org/project/assemblyai/)
* [AssemblyAI Python SDK Core Examples](https://github.com/AssemblyAI/assemblyai-python-sdk?tab=readme-ov-file#core-examples)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student


