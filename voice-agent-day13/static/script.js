const micBtn = document.getElementById("mic-btn");
const statusDiv = document.getElementById("status");
const transcriptionP = document.getElementById("transcription");
const llmResponseP = document.getElementById("llm-response");
const audioPlayer = document.getElementById("audio-player");
const chatHistoryDiv = document.getElementById("history-messages");

let mediaRecorder;
let audioChunks = [];
let isRecording = false;
const sessionId = "user_" + Math.random().toString(36).substring(2, 10);

function appendChatMessage(role, text) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("chat-message", role);
  msgDiv.textContent = text;
  chatHistoryDiv.appendChild(msgDiv);
  chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight;
}

micBtn.addEventListener("click", () => {
  if (!isRecording) {
    startRecording();
  } else {
    stopRecording();
  }
});

async function startRecording() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

    mediaRecorder.onstop = async () => {
      statusDiv.textContent = "Processing audio...";
      const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
      const file = new File([audioBlob], "voice.webm", { type: "audio/webm" });

      const formData = new FormData();
      formData.append("audio", file);

      try {
        const res = await fetch(`/agent/chat/${sessionId}`, {
          method: "POST",
          body: formData
        });

        if (!res.ok) throw new Error("Server error");
        const data = await res.json();

        transcriptionP.textContent = data.transcription || "";
        llmResponseP.textContent = data.llm_response || "";

        chatHistoryDiv.innerHTML = "";
        data.chat_history.forEach(msg => appendChatMessage(msg.role, msg.content));

        if (data.murf_audio_url) {
          audioPlayer.src = data.murf_audio_url;
          audioPlayer.play();
        }

        statusDiv.textContent = "Done!";
      } catch (err) {
        statusDiv.textContent = "Error: " + err.message;
      }
    };

    mediaRecorder.start();
    isRecording = true;
    micBtn.classList.add("recording");
    statusDiv.textContent = "Recording...";
  } catch (err) {
    alert("Microphone error: " + err.message);
  }
}

function stopRecording() {
  mediaRecorder.stop();
  isRecording = false;
  micBtn.classList.remove("recording");
  statusDiv.textContent = "Stopping...";
}
