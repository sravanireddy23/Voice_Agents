
# 🎤 30 Days of AI Voice Agents – Day 2

Welcome to **Day 2** of the *30 Days of AI Voice Agents* challenge!  

On Day 2, the focus is on creating a **Text-to-Speech (TTS) REST endpoint** using Murf’s API.

---

## 📝 Day 2 Task – Your First REST TTS Call

- **Objective:** Create a server endpoint that accepts text input and returns a URL pointing to the generated audio file using Murf’s REST TTS API.  
- **Details:**  
  - Implemented a FastAPI endpoint `/generate-audio` that accepts POST requests with text.  
  - Calls Murf’s `/generate` TTS API to generate speech.  
  - Returns the audio URL in the JSON response.  
  - No changes were made to the frontend HTML for this task.  
  - Endpoint can be tested via FastAPI Swagger UI (`http://localhost:8000/docs`) or Postman.  
  - **API keys are secured in `.env`** and not exposed publicly.  

---

## 🔧 Installation & Setup

1. Make sure you have your Day 1 setup ready (FastAPI backend, virtual environment, dependencies).  
2. Add your Murf API key to `.env`:

```env
MURF_API_KEY=your_murf_api_key_here
````

3. Install any additional dependencies if needed:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Start your FastAPI server:

```bash
uvicorn app.main:app --reload
```

2. Test your endpoint:

* Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Find the `/generate-audio` POST endpoint
* Input your text and execute
* You will receive a JSON response containing the audio URL

```json
{
  "audio_url": "https://link-to-generated-audio-file"
}
```

3. Optionally, test with **Postman** or any API testing tool.

---

## 💡 What I Learned

* How to integrate a third-party TTS API (Murf) with FastAPI
* How to create a REST endpoint that accepts input and returns dynamic responses
* Best practices for **securing API keys** with `.env` files

---

## 🛠️ Technologies Used

* Python
* FastAPI
* Murf REST TTS API
* dotenv for environment variables

---

## 📌 Next Steps

* Day 3 will focus on **adding a working frontend** to input text and play the generated speech.

```

---

If you want, I can **also prepare a GitHub-ready folder structure suggestion and a screenshot/demo section** for Day 2 so your README looks very professional and visually engaging.  

Do you want me to do that next?
```
