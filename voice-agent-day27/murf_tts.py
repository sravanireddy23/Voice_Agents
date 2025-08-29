import os
import requests
from dotenv import load_dotenv

load_dotenv()

MURF_API_KEY = os.getenv("MURF_API_KEY")
MURF_VOICE_ID = os.getenv("MURF_VOICE_ID")  # use from .env
MURF_TTS_URL = "https://api.murf.ai/v1/speech/generate"

def generate_tts_murf(text: str, voice: str = None) -> str:
    """
    Generate speech using Murf API and return audio URL.
    """
    headers = {
        "accept": "application/json",
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "voiceId": voice or MURF_VOICE_ID,  # fallback to .env voice
        "text": text,
        "format": "MP3",
        "sampleRate": "44100"
    }

    response = requests.post(MURF_TTS_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Murf API Error {response.status_code}: {response.text}")

    data = response.json()
    return data.get("audioFile")  # ✅ correct key
