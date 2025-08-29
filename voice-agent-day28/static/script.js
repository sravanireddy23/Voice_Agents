// ---------------- DOM Elements ----------------
const startBtn = document.getElementById("start-record");
const stopBtn = document.getElementById("stop-record");
const statusDiv = document.getElementById("status");
const resultDiv = document.getElementById("result");
const transcriptionP = document.getElementById("transcription");
const llmResponseP = document.getElementById("llm-response");
const audioPlayer = document.getElementById("audio-player");
const chatHistoryDiv = document.getElementById("history-messages");

let mediaRecorder;
let audioChunks = [];

// ---------------- 1. Load API Keys from localStorage ----------------
const assemblyAIKey = localStorage.getItem("assemblyai_key");
const murfKey = localStorage.getItem("murf_key");
const googleKey = localStorage.getItem("google_key");

if (!assemblyAIKey || !murfKey || !googleKey) {
  // Redirect to config if any key is missing
  window.location.href = "/static/config.html";
}

// ---------------- 2. Session Management ----------------
function getSessionId() {
  const params = new URLSearchParams(window.location.search);
  let sid = params.get("session_id");
  if (!sid) {
    sid = Math.random().toString(36).substring(2, 10);
    params.set("session_id", sid);
    window.history.replaceState({}, "", "?" + params.toString());
  }
  return sid;
}

const sessionId = getSessionId();

// ---------------- 3. Chat Message Helper ----------------
function appendChatMessage(role, text) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("chat-message", role);
  msgDiv.textContent = text;
  chatHistoryDiv.appendChild(msgDiv);
  chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight;
}

// ---------------- 4. Start Recording ----------------
startBtn.addEventListener("click", async () => {
  audioChunks = [];

  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert("Your browser does not support audio recording.");
    return;
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();
    statusDiv.textContent = "Recording... 🎙️";
    startBtn.disabled = true;
    stopBtn.disabled = false;

    mediaRecorder.ondataavailable = e => {
      audioChunks.push(e.data);
    };

    mediaRecorder.onstop = async () => {
      statusDiv.textContent = "Processing audio... ⏳";

      const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
      const file = new File([audioBlob], "voice.webm", { type: "audio/webm" });

      const formData = new FormData();
      formData.append("audio", file);

      try {
        // ---------------- 5. Send audio + headers to backend ----------------
        const response = await fetch(`/agent/chat/${sessionId}`, {
          method: "POST",
          headers: {
            "x-assemblyai-key": assemblyAIKey,
            "x-murf-key": murfKey,
            "x-google-key": googleKey
          },
          body: formData
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.detail || "Unknown error");
        }

        // ---------------- 6. Update UI ----------------
        transcriptionP.textContent = data.transcription || "No transcription.";
        llmResponseP.textContent = data.llm_response || "No AI response.";
        resultDiv.classList.remove("hidden");

        // Render chat history
        chatHistoryDiv.innerHTML = "";
        if (data.chat_history) {
          data.chat_history.forEach(msg => {
            appendChatMessage(msg.role, msg.content);
          });
        }

        // Play audio
        if (data.murf_audio_url) {
          audioPlayer.src = data.murf_audio_url;
          audioPlayer.play();
          audioPlayer.onended = () => {
            statusDiv.textContent = "Done! 🎉";
            startBtn.disabled = false;
            stopBtn.disabled = true;
          };
          statusDiv.textContent = "Playing audio response...";
        } else {
          audioPlayer.src = "";
          statusDiv.textContent = "Done! 🎉";
          startBtn.disabled = false;
          stopBtn.disabled = true;
        }

      } catch (error) {
        console.error(error);
        statusDiv.textContent = "Error: " + (error.message || JSON.stringify(error));
        resultDiv.classList.add("hidden");
        startBtn.disabled = false;
        stopBtn.disabled = true;
      }
    };

  } catch (err) {
    alert("Could not start recording: " + err.message);
  }
});

// ---------------- 7. Stop Recording ----------------
stopBtn.addEventListener("click", () => {
  if (mediaRecorder && mediaRecorder.state === "recording") {
    mediaRecorder.stop();
    statusDiv.textContent = "Stopping recording...";
    stopBtn.disabled = true;
  }
});
