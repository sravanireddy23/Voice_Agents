let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const status = document.getElementById('status');
const originalAudio = document.getElementById('originalAudio');
const murfAudio = document.getElementById('murfAudio');
const transcriptionText = document.getElementById('transcriptionText');

startBtn.addEventListener('click', async () => {
    audioChunks = [];
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        sendAudio(audioBlob);
    };

    mediaRecorder.start();
    status.textContent = "Recording...";
    status.className = "recording";
    startBtn.disabled = true;
    stopBtn.disabled = false;
});

stopBtn.addEventListener('click', () => {
    mediaRecorder.stop();
    status.textContent = "Processing...";
    status.className = "";
    startBtn.disabled = false;
    stopBtn.disabled = true;
});

async function sendAudio(audioBlob) {
    const formData = new FormData();
    formData.append("file", audioBlob, "recording.webm");

    try {
        const res = await fetch("/tts/echo", {
            method: "POST",
            body: formData
        });
        const data = await res.json();

        if (data.error) {
            status.textContent = "Error: " + data.error;
            return;
        }

        status.textContent = "Done!";
        originalAudio.src = data.original_audio_url;
        murfAudio.src = data.murf_audio_url;
        transcriptionText.textContent = data.transcription;
    } catch (err) {
        status.textContent = "Error sending audio: " + err;
    }
}
