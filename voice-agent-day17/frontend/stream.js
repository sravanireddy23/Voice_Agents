let ws;
let mediaRecorder;

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const statusEl = document.getElementById("status");
const transcriptBox = document.getElementById("transcriptBox");

startBtn.onclick = async () => {
  ws = new WebSocket("ws://127.0.0.1:8000/ws/audio");

  ws.onopen = () => {
    console.log("✅ Connected to server");
    statusEl.textContent = "Streaming...";
  };

  ws.onclose = () => {
    console.log("❌ Disconnected");
    statusEl.textContent = "Disconnected";
  };

  // Start mic recording
  let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream, { mimeType: "audio/webm" });

  mediaRecorder.ondataavailable = async (e) => {
    if (e.data.size > 0 && ws.readyState === WebSocket.OPEN) {
      let arrayBuffer = await e.data.arrayBuffer();
      let audioBuffer = new Int16Array(arrayBuffer);
      ws.send(audioBuffer);
    }
  };

  mediaRecorder.start(250); // send every 250ms

  startBtn.disabled = true;
  stopBtn.disabled = false;
};

stopBtn.onclick = () => {
  mediaRecorder.stop();
  ws.close();
  statusEl.textContent = "Stopped";
  startBtn.disabled = false;
  stopBtn.disabled = true;
};
