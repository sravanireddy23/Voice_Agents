# 🎤 30 Days of AI Voice Agents – Day 3

Welcome to **Day 3** of the *30 Days of AI Voice Agents* challenge!  

On Day 3, the focus is on **playing back TTS audio on the frontend** using the endpoint created on Day 2.

---

## 📝 Day 3 Task – Playing Back TTS Audio

- **Objective:** Add a text input and submit button on your HTML page to send text to the `/generate-audio` endpoint (Day 2) and play the returned audio.  
- **Details:**  
  - Updated `index.html` to include:  
    - A `<input>` field for text  
    - A `<button>` to submit the text  
    - An `<audio>` element to play the generated audio  
  - Frontend uses JavaScript (`script.js`) to send a POST request to `/generate-audio`  
  - On receiving the `audio_url` from the server, the `<audio>` element is updated and played automatically  
  - Tested in browser to ensure smooth playback  

---

## 📂 Updated Folder Structure

```

app/
templates/
index.html
static/
script.js

````

- Backend and static folder structure remains the same  
- Frontend now includes TTS playback functionality  

---

## 🔧 Installation & Setup

1. Ensure Day 1 and Day 2 setups are complete (backend server and `/generate-audio` endpoint).  
2. Start FastAPI server:

```bash
uvicorn app.main:app --reload
````

3. Open the HTML page in your browser (`index.html` in `templates/`).

---

## ▶️ Usage

1. Enter text in the input field.
2. Click the submit button.
3. The frontend sends the text to the `/generate-audio` endpoint.
4. The returned audio URL is automatically loaded into the `<audio>` element and played.

---

## 💡 What I Learned

* How to connect frontend HTML/JS with a FastAPI backend
* Handling JSON responses from REST APIs in JavaScript
* Dynamically updating and playing audio in a web page using the `<audio>` element
* Understanding the end-to-end flow from user input → API call → audio playback

---

## 🛠️ Technologies Used

* Python
* FastAPI
* HTML, CSS, JavaScript
* Murf REST TTS API

---

## 📌 Next Steps

* Day 4 will focus on **enhancing the frontend UI** and adding additional TTS features like voice selection and moods.

```

---

If you want, I can **also draft a visually enhanced version with emojis, badges, and a placeholder for a screenshot or demo** so your Day 3 README looks professional on GitHub.  

Do you want me to do that?
```
