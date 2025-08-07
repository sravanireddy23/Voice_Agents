let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const statusDiv = document.getElementById("status");
const audioContainer = document.getElementById("audioPlayerContainer");

startBtn.onclick = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  audioChunks = [];

  mediaRecorder.ondataavailable = event => {
    audioChunks.push(event.data);
  };

  mediaRecorder.onstop = async () => {
    const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
    const formData = new FormData();
    formData.append("file", audioBlob, "voice.wav");

    statusDiv.textContent = "Uploading audio...";

    try {
      const response = await fetch("/upload-audio/", {
        method: "POST",
        body: formData
      });

      const data = await response.json();
      statusDiv.textContent = `Uploaded: ${data.filename} | Type: ${data.content_type} | Size: ${data.file_size} bytes`;

      // Clear previous player
      audioContainer.innerHTML = "";

      // Create audio player
      const audioPlayer = document.createElement("audio");
      audioPlayer.controls = true;
      audioPlayer.src = `/uploads/${data.filename}`;
      audioContainer.appendChild(audioPlayer);

      // Create clickable link to open in browser
      const downloadLink = document.createElement("a");
      downloadLink.href = `/uploads/${data.filename}`;
      downloadLink.textContent = `🔗 Open uploaded file`;
      downloadLink.target = "_blank";
      downloadLink.style.display = "block";
      downloadLink.style.marginTop = "10px";
      downloadLink.style.color = "#0d47a1";
      audioContainer.appendChild(downloadLink);

    } catch (err) {
      statusDiv.textContent = "Upload failed!";
      console.error(err);
    }
  };

  mediaRecorder.start();
  startBtn.disabled = true;
  stopBtn.disabled = false;
  statusDiv.textContent = "Recording...";
};

stopBtn.onclick = () => {
  mediaRecorder.stop();
  startBtn.disabled = false;
  stopBtn.disabled = true;
};
