const startBtn = document.getElementById("start-record");
const stopBtn = document.getElementById("stop-record");
const statusDiv = document.getElementById("status");
const resultDiv = document.getElementById("result");
const transcriptionP = document.getElementById("transcription");
const llmResponseP = document.getElementById("llm-response");
const audioPlayer = document.getElementById("audio-player");

let mediaRecorder;
let audioChunks = [];

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
        const response = await fetch("/llm/query", {
          method: "POST",
          body: formData
        });

        if (!response.ok) {
          const errData = await response.json();
          throw new Error(errData.detail || "Unknown error");
        }

        const data = await response.json();

        transcriptionP.textContent = data.transcription || "No transcription.";
        llmResponseP.textContent = data.llm_response || "No AI response.";

        if (data.murf_audio_url) {
          audioPlayer.src = data.murf_audio_url;
          audioPlayer.play();
        } else {
          audioPlayer.src = "";
        }

        statusDiv.textContent = "Done! 🎉";
        resultDiv.classList.remove("hidden");
      } catch (error) {
        statusDiv.textContent = "Error: " + error.message;
        resultDiv.classList.add("hidden");
      }

      startBtn.disabled = false;
      stopBtn.disabled = true;
    };
  } catch (err) {
    alert("Could not start recording: " + err.message);
  }
});

stopBtn.addEventListener("click", () => {
  if (mediaRecorder && mediaRecorder.state === "recording") {
    mediaRecorder.stop();
    statusDiv.textContent = "Stopping recording...";
    stopBtn.disabled = true;
  }
});
