# services/tts.py
import logging
import requests

logger = logging.getLogger(__name__)

MURF_TTS_URL = "https://api.murf.ai/v1/speech/generate"

class MurfTTS:
    def __init__(self, api_key: str, voice_id: str):
        self.api_key = api_key
        self.voice_id = voice_id

    def synthesize(self, text: str) -> str | None:
        """
        Returns a URL to the generated audio file (or None if something went wrong).
        """
        if not text:
            logger.warning("Empty text passed to TTS; skipping.")
            return None

        # Murf API often has a payload limit; trim to be safe
        if len(text) > 3000:
            text = text[:3000]

        headers = {"api-key": self.api_key, "Content-Type": "application/json"}
        payload = {"text": text, "voice_id": self.voice_id, "speed": 1.0, "pitch": 1.0}

        logger.info("Calling Murf TTS API...")
        resp = requests.post(MURF_TTS_URL, json=payload, headers=headers)
        try:
            resp.raise_for_status()
        except Exception:
            logger.error("Murf TTS error %s: %s", resp.status_code, resp.text)
            raise

        data = resp.json()
        audio_url = data.get("audioFile")
        if not audio_url:
            logger.error("Murf TTS: No 'audioFile' in response: %s", data)
            return None

        logger.info("Murf TTS success; audio URL received.")
        return audio_url
