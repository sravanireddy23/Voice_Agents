import os
import requests
from dotenv import load_dotenv

load_dotenv()
MURF_API_KEY = os.getenv("MURF_API_KEY")
VOICE_ID = os.getenv("MURF_VOICE_ID")

url = "https://api.murf.ai/v1/speech/generate"

headers = {
    "accept": "application/json",
    "api-key": MURF_API_KEY,
    "Content-Type": "application/json",
}

payload = {
    "voiceId": VOICE_ID,
    "text": "Hello Sravani, your Murf API is now working!",
    "format": "MP3",
    "sampleRate": "44100"
}

resp = requests.post(url, headers=headers, json=payload)
print("Status:", resp.status_code)
print(resp.json())
