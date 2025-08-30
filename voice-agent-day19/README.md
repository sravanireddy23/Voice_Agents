
# 30 Days of AI Voice Agents | Day 19: Streaming LLM Responses

## Overview
Day 19 focuses on **streaming responses from the LLM**. After receiving the final transcript from AssemblyAI, the text is sent to the LLM API. The LLM streams its response incrementally, allowing real-time monitoring and accumulation of the generated text.

---

## Features
- **Streaming LLM Response**: Receive LLM-generated text in real-time instead of waiting for the full response.
- **Console Output**: Partial and complete responses are printed to the server console.
- **Integration with Turn Detection**: LLM responds after the user’s turn has ended.
- **No UI Changes Required**: Streaming occurs on the server side for now.

---

## How It Works
1. AssemblyAI detects the end of the user’s turn and provides the final transcript.
2. The server sends the transcript to the LLM API.
3. The LLM streams its response in chunks.
4. Each chunk is accumulated and printed to the console.
5. The final output represents the complete LLM response to the user input.

---

## Usage
1. Ensure you are on the **streaming** branch:
```bash
git checkout streaming
````

2. Set your **Gemini API key**:

```bash
export GEMINI_API_KEY="your_gemini_key"
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

4. Stream audio from the client and wait for the server to print the LLM response.

---

## Example Server Code

```python
from fastapi import FastAPI
from gemini import GeminiClient  # Example client

app = FastAPI()
client = GeminiClient(api_key="your_gemini_key")

async def stream_llm_response(transcript: str):
    response_text = ""
    async for chunk in client.stream_generate_content(prompt=transcript):
        response_text += chunk
        print("Partial Response:", chunk)
    print("Final LLM Response:", response_text)
```

---

## Notes

* Streaming allows **real-time monitoring** of the LLM output.
* Currently, output is printed to the server console. Future tasks will integrate this with TTS for real-time audio responses.
* Works seamlessly with **turn detection** and streaming audio inputs.

---

## Resources

* [Google Gemini API - Stream Generate Content](https://ai.google.dev/api/generate-content#method:-models.streamgeneratecontent)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

