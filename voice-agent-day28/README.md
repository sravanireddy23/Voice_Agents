
# 30 Days of AI Voice Agents | Day 28: Deploy Your Agent

## Overview
Day 28 focuses on **deploying your fully functional voice agent** so that it can be accessed publicly. Hosting your agent allows others to interact with it and showcases your work online.

---

## Features
- **Public Access**: Your agent can be accessed from anywhere via a hosted URL.
- **Full Functionality Online**: All features like STT, LLM responses, Murf TTS, chat history, and special skills are available online.
- **User-Friendly Deployment**: Easy setup using cloud providers with free tiers.

---

## How It Works
1. **Choose a Hosting Provider**:
   - Recommended: [Render.com](https://render.com)
   - Other options: Heroku, Railway, AWS Free Tier, etc.
2. **Prepare Your Project**:
   - Ensure all dependencies are listed in `requirements.txt`.
   - Confirm API keys are configured via environment variables or the UI.
   - Check that `uvicorn` is set as the startup command:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
3. **Deploy**:
   - Push your project to a GitHub repository.
   - Connect the repository to the hosting provider.
   - Follow provider instructions to deploy and expose your agent publicly.
4. **Test Your Agent**:
   - Access the public URL.
   - Interact with your agent and verify all features work online.

---

## Usage
1. Open the hosted URL in a browser.
2. Enter any required API keys in the UI (if configured).
3. Interact with your voice agent:
   - Record your voice
   - Receive transcriptions
   - Get LLM responses
   - Listen to Murf-generated audio
4. Share the link with others for public interaction.

---

## Notes
- Monitor usage to ensure you stay within free tier limits.
- Make sure sensitive API keys are not exposed publicly.
- Hosting enables you to **showcase your project** and share your work on LinkedIn.

---

## Resources
- [Render.com](https://render.com)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/fastapi-cli/#fastapi-run)
- Cloud deployment tutorials for Heroku, Railway, AWS Free Tier

---

## Author
**Sravani Reddy Gavinolla**  
Computer Science & Engineering Student
