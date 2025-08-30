
# 30 Days of AI Voice Agents | Day 8: Integrating a Large Language Model (LLM)

## Overview
Day 8 introduces a **Large Language Model (LLM)** integration to the AI Voice Agent. A new backend endpoint allows sending text input to an LLM API (we recommend **Google's Gemini API**) and receiving a generated response. This forms the foundation for conversational AI capabilities in future tasks.

---

## Features
- **POST /llm/query** endpoint to send text input.
- Calls an LLM API (e.g., Google Gemini) to generate a response.
- Returns the LLM-generated response in JSON format.
- No UI changes needed for this task.

---

## How It Works
1. Client sends a POST request to `/llm/query` with text input.
2. The backend receives the request and forwards the text to the LLM API.
3. The LLM processes the input and generates a response.
4. The backend returns the LLM response as JSON to the client.

---

## Usage
1. Create an API key for **Google Gemini**: [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
2. Add the API key to your server environment:
```bash
export GEMINI_API_KEY="your_api_key_here"  # Linux/Mac
set GEMINI_API_KEY="your_api_key_here"     # Windows
````

3. Run your FastAPI server:

```bash
uvicorn main:app --reload
```

4. Test the endpoint:

```bash
POST /llm/query
Content-Type: application/json

{
  "text": "Hello, how are you?"
}
```

* Example Response:

```json
{
  "response": "I'm doing great! How can I assist you today?"
}
```

---

## Resources

* [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
* [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

