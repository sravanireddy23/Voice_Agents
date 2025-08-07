let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const transcribeBtn = document.getElementById("transcribeBtn");
const statusText = document.getElementById("status");
const audioPlayer = document.getElementById("audioPlayer");
const transcriptText = document.getElementById("transcriptText");

startBtn.onclick = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();
  audioChunks = [];

  mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
  mediaRecorder.onstop = async () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append("file", audioBlob, "voice.wav");

    statusText.textContent = "Uploading...";
    await fetch("/upload-audio/", {
      method: "POST",
      body: formData,
    });

    const audioUrl = URL.createObjectURL(audioBlob);
    audioPlayer.src = audioUrl;
    statusText.textContent = "Recording uploaded successfully!";
  };

  statusText.textContent = "Recording...";
  startBtn.disabled = true;
  stopBtn.disabled = false;
};

stopBtn.onclick = () => {
  mediaRecorder.stop();
  startBtn.disabled = false;
  stopBtn.disabled = true;
};

transcribeBtn.onclick = async () => {
  transcriptText.textContent = "Transcribing...";
  const response = await fetch("/transcribe/", { method: "POST" });
  const result = await response.json();

  if (result.transcript) {
    transcriptText.textContent = "📝 " + result.transcript;
  } else {
    transcriptText.textContent = "⚠️ Transcription failed.";
  }
};
