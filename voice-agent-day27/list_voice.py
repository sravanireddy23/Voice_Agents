import os
import requests
from dotenv import load_dotenv

load_dotenv()
MURF_API_KEY = os.getenv("MURF_API_KEY")

url = "https://api.murf.ai/v1/speech/voices"
headers = {
    "accept": "application/json",
    "api-key": MURF_API_KEY,
}

resp = requests.get(url, headers=headers)
print("Status:", resp.status_code)
print(resp.json())
