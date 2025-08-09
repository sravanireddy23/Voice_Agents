# main.py
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file (optional)
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found. Set it in your environment or .env file.")

# Create the Google Generative AI client
client = genai.Client(api_key=api_key)

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice Agent API is running!"}

@app.get("/ask")
def ask(question: str):
    """Send a text prompt to Google Generative AI and return the response."""
    response = client.models.generate_content(
        model="gemini-1.5-flash",  # or "gemini-1.5-pro"
        contents=question
    )
    return {"question": question, "answer": response.text}
