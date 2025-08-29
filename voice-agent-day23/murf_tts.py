def generate_murf_tts(text: str) -> str:
    if len(text) > 3000:
        text = text[:3000]

    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json",
    }
    json_data = {
        "text": text,
        "voice_id": MURF_VOICE_ID,
        "speed": 1.0,
        "pitch": 1.0,
    }

    response = requests.post(MURF_TTS_URL, json=json_data, headers=headers)
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"Murf API error {response.status_code}: {response.text}")
        raise e

    resp_json = response.json()
    print("Murf API full response:", resp_json)

    audio_url = resp_json.get("audioFile")  # <-- use "audioFile" here
    if not audio_url:
        raise Exception(f"Murf API error: {resp_json.get('errorMessage', 'No audioFile in response')}")

    return audio_url
