# 🎤 **AI Voice Agent – Your Personal Conversational Assistant**

✨ Talk to your AI, hear it reply — powered by **FastAPI**, **AssemblyAI**, **Google Gemini**, and **Murf AI**.  
This project records your voice, **transcribes**, **responds**, and **plays back AI-generated speech** — all wrapped in a **modern, colorful UI**.

---

## 🚀 **Key Features**
✅ **🎙 One-Tap Mic Button** – Tap to start, tap to stop.  
✅ **💬 Chat History** – Full context-aware conversation log.  
✅ **🧠 AI Intelligence** – Contextual responses from **Google Gemini**.  
✅ **📝 Accurate Speech-to-Text** – **AssemblyAI** for clean transcriptions.  
✅ **🔊 Realistic Text-to-Speech** – **Murf AI** voices for lifelike playback.  
✅ **🎨 Modern Design** – Glassmorphic, colorful, and responsive.

---
S
## 🛠 **Tech Stack**
| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | FastAPI (Python) |
| **STT** | 🎤 [AssemblyAI](https://www.assemblyai.com/) |
| **LLM** | 🤖 [Google Gemini](https://deepmind.google/technologies/gemini/) |
| **TTS** | 🔊 [Murf AI](https://murf.ai/) |
| **Other** | python-dotenv, aiofiles, requests, uvicorn |

---

## 🏗 **How It Works**
```

🎙 Speak → 📤 Send to Backend → 📝 Transcribe with AssemblyAI
→ 🤖 Generate Reply with Gemini → 🔊 Convert to Speech with Murf
→ 📜 Update Chat History → ▶ Play AI’s Voice



## ⚙ **Setup Instructions**

### 1️⃣ Clone the Project
```bash
git clone https://github.com/yourusername/voice-agent.git
cd voice-agent


### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt


### 3️⃣ Create `.env` File

```env
ASSEMBLYAI_API_KEY=your_assemblyai_key
MURF_API_KEY=your_murf_api_key
MURF_VOICE_ID=en-US-ken
GEMINI_API_KEY=your_gemini_api_key


### 4️⃣ Run the Server

```bash
uvicorn main:app --reload


### 5️⃣ Open in Browser

🔗 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**



## 📸 **Screenshots**

🖼 **Main Chat Interface**
![Chat UI](screenshots/chat-ui.png)

🖼 **Recording in Progress**
![Recording](screenshots/recording.png)

🖼 **AI Reply Playback**
![AI Reply](screenshots/ai-reply.png)



## 🔮 **Future Improvements**

* 🌍 Multi-language support
* 📱 Mobile-first optimization
* 🎯 Better context handling
* 🔒 User authentication


## 👩‍💻 **Author**

**Sravani Reddy Gavinolla**
📧 **Email:** [sravanigavinolla@gmail.com](mailto:sravanigavinolla@gmail.com)
🔗 **LinkedIn:** [Sravani Reddy Gavinolla](https://www.linkedin.com/in/sravani-reddy-gavinolla-14b421331/)
💻 **GitHub:** [sravanireddy23](https://github.com/sravanireddy23)

