# 30 Days of AI Voice Agents | Day 11: Error Handling

## Overview
Day 11 focuses on making the AI Voice Agent **more robust** by adding comprehensive error handling. This ensures the bot can gracefully handle failures from APIs such as **STT (AssemblyAI), LLM (Gemini), or TTS (Murf)** and provide a fallback response to the user instead of crashing.

---

## Features
- **Server-Side Error Handling**: Try-except blocks around API calls to catch and log errors.
- **Client-Side Error Handling**: Displays a status message or plays a fallback audio when an error occurs.
- **Fallback Response**: Provides a default response like:
```

"I'm having trouble connecting right now."

````
- **Simulated Error Testing**: Errors can be tested by commenting out API keys or disabling services.

---

## How It Works
1. API calls (STT, LLM, TTS) are wrapped in `try-except` blocks on the server.
2. If an exception occurs:
   - Log the error details for debugging.
   - Return a fallback audio URL or message to the client.
3. The frontend detects failed responses and:
   - Plays the fallback audio.
   - Updates the status message to inform the user.

---

## Usage
1. Run the FastAPI server with proper API keys:
```bash
uvicorn main:app --reload
````

2. Open the UI in a browser.
3. Test normal usage or simulate errors by commenting out API keys.
4. Verify that fallback messages/audio are returned gracefully.

---

## Example Server-Side Fallback

```python
try:
    transcription = transcriber.transcribe(audio_data)
except Exception as e:
    print(f"STT Error: {e}")
    return {"audio_url": "fallback_audio.mp3"}
```

---

## Example Client-Side Handling

```javascript
fetch('/llm/query', {...})
  .then(res => res.json())
  .then(data => {
    audioElement.src = data.audio_url;
  })
  .catch(err => {
    console.error("API Error:", err);
    audioElement.src = "fallback_audio.mp3";
  });
```

---

## Notes

* Error handling improves the user experience by avoiding crashes.
* Useful for production-ready AI Voice Agents that rely on multiple external APIs.

---

## Resources

* [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)
* [JavaScript Error Handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

