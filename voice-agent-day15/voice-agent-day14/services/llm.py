# services/llm.py
import logging
from typing import List
from google import genai
from models import ChatMessage

logger = logging.getLogger(__name__)

class GeminiLLM:
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, history: List[ChatMessage]) -> str:
        """
        Build a simple prompt from the chat history and get the next assistant response.
        """
        logger.info("Generating LLM response with Gemini...")
        prompt_lines = []
        for msg in history:
            role = "User" if msg.role == "user" else "AI"
            prompt_lines.append(f"{role}: {msg.content}")
        prompt_lines.append("AI:")
        prompt = "\n".join(prompt_lines)

        resp = self.client.models.generate_content(model=self.model, contents=prompt)
        text = (resp.text or "").strip()
        logger.info("LLM response generated.")
        return text
