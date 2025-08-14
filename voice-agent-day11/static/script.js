console.log("Script loaded!");

let sessionId = new URLSearchParams(window.location.search).get("session_id");
if (!sessionId) {
    sessionId = Math.random().toString(36).substring(2, 10);
    window.history.replaceState({}, "", `?session_id=${sessionId}`);
}

let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const outputDiv = document.getElementById("output");

startBtn.addEventListener("click", async () => {
    console.log("Start clicked");
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        console.log("Microphone granted");
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = e => {
            if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = async () => {
            console.log("Stopped, sending to backend...");
            const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
            const formData = new FormData();
            formData.append("audio", audioBlob, "recording.webm");

            const res = await fetch(`/agent/chat/${sessionId}`, {
                method: "POST",
                body: formData
            });

            const data = await res.json();
            if (!res.ok) {
                outputDiv.innerHTML += `<p>Error: ${data.detail}</p>`;
                return;
            }

            outputDiv.innerHTML += `
                <p><strong>You:</strong> ${data.transcription}</p>
                <p><strong>AI:</strong> ${data.llm_response}</p>
                <audio controls src="${data.murf_audio_url}"></audio>
            `;
        };

        mediaRecorder.start();
        startBtn.disabled = true;
        stopBtn.disabled = false;
    } catch (err) {
        console.error("Mic error:", err);
        alert("Microphone access denied!");
    }
});

stopBtn.addEventListener("click", () => {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
    }
    startBtn.disabled = false;
    stopBtn.disabled = true;
});
