
# 30 Days of AI Voice Agents | Day 4: Echo Bot

## Overview
This project adds an **Echo Bot** feature to your AI Voice Agent web app. The Echo Bot allows users to record their voice through the browser and play it back immediately. This functionality is built entirely with **HTML, CSS, and JavaScript** using the browser’s MediaRecorder API.

---

## Features
- **Start Recording**: Click the button to start recording your voice.
- **Stop Recording**: Click the button to stop recording.
- **Playback**: Listen to the recorded audio immediately via an `<audio>` element.

---

## How It Works
1. User clicks **Start Recording**.
2. Browser requests microphone access and begins recording audio.
3. Audio data is collected in chunks while recording.
4. User clicks **Stop Recording**.
5. The recorded audio is combined into a Blob.
6. Blob is converted to a URL and set as the `<audio>` element source for playback.

---

## Installation & Usage
1. Open `index.html` in a modern browser (Chrome, Firefox, Edge).
2. Scroll to the **Echo Bot** section.
3. Click **Start Recording** to record your voice.
4. Click **Stop Recording** to stop and playback the recording.

---

## Demo
- Record your voice and hear the playback instantly.
- Works entirely in the browser; no backend changes needed.

---

## Resources
- [MDN: MediaStream Recording API](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API)

---

## Author
**Sravani Reddy Gavinolla**  
Computer Science & Engineering Student
```

I can also make a **LinkedIn-ready version** with emojis and highlights to make it look more engaging. Do you want me to do that?
