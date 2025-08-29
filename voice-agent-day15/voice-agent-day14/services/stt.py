# services/stt.py
import time
import logging
import requests
from typing import Optional

logger = logging.getLogger(__name__)

ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"

class AssemblyAITranscriber:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._headers_auth = {"authorization": self.api_key}

    def _upload_bytes(self, data: bytes) -> str:
        logger.info("Uploading audio to AssemblyAI...")
        resp = requests.post(ASSEMBLYAI_UPLOAD_URL, headers=self._headers_auth, data=data)
        resp.raise_for_status()
        upload_url = resp.json()["upload_url"]
        logger.info("Upload successful. URL received.")
        return upload_url

    def _request_transcription(self, upload_url: str) -> str:
        logger.info("Requesting transcription...")
        headers = {**self._headers_auth, "content-type": "application/json"}
        json_data = {"audio_url": upload_url}
        resp = requests.post(ASSEMBLYAI_TRANSCRIPT_URL, json=json_data, headers=headers)
        resp.raise_for_status()
        transcript_id = resp.json()["id"]

        # Poll until complete
        while True:
            poll = requests.get(f"{ASSEMBLYAI_TRANSCRIPT_URL}/{transcript_id}", headers=headers)
            poll.raise_for_status()
            status = poll.json()["status"]
            if status == "completed":
                text = poll.json().get("text", "")
                logger.info("Transcription completed.")
                return text
            if status == "error":
                err = poll.json().get("error", "Unknown transcription error.")
                logger.error(f"AssemblyAI error: {err}")
                raise RuntimeError(f"AssemblyAI transcription failed: {err}")
            time.sleep(2)

    def transcribe_from_audio_bytes(self, audio_bytes: bytes) -> str:
        upload_url = self._upload_bytes(audio_bytes)
        return self._request_transcription(upload_url)
