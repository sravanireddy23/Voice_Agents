const micBtn = document.getElementById("mic-btn");
const statusDiv = document.getElementById("status");
const fileLinkDiv = document.getElementById("file-link");

let ws = null;
let mediaRecorder = null;
let isRecording = false;
let currentUrl = null;

// Create or reuse a session id (to group files per user/session)
function getSessionId() {
  const params = new URLSearchParams(window.location.search);
  let sid = params.get("session_id");
  if (!sid) {
    sid = Math.random().toString(36).slice(2, 10);
    params.set("session_id", sid);
    // Keep the URL clean (optional)
    window.history.replaceState({}, "", "?" + params.toString());
  }
  return sid;
}

const sessionId = getSessionId();

micBtn.addEventListener("click", async () => {
  if (!isRecording) {
    await startStreaming();
  } else {
    await stopStreaming();
  }
});

async function startStreaming() {
  try {
    // 1) Open WS
    ws = new WebSocket(`ws://${location.host}/ws/audio?session_id=${sessionId}`);

    ws.onopen = () => {
      statusDiv.textContent = "Connected. Initializing mic…";
    };

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        if (msg.type === "ready") {
          // server created/selected a file
          currentUrl = msg.url;
          fileLinkDiv.innerHTML = `<a href="${msg.url}" target="_blank">📁 ${msg.filename}</a>`;
        } else if (msg.type === "saved") {
          // final confirmation
          statusDiv.textContent = `Saved: ${msg.filename}`;
          fileLinkDiv.innerHTML = `<a href="${msg.url}" target="_blank">▶️ Play: ${msg.filename}</a>`;
        }
      } catch { /* ignore non-JSON */ }
    };

    ws.onclose = () => {
      statusDiv.textContent = "Disconnected";
      ws = null;
    };

    ws.onerror = (e) => {
      console.error("WS error:", e);
      statusDiv.textContent = "WS error (check server)";
    };

    // 2) Get mic
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    // Choose a stable mimeType if available
    const preferred = "audio/webm;codecs=opus";
    const mimeType = MediaRecorder.isTypeSupported(preferred) ? preferred : (MediaRecorder.isTypeSupported("audio/webm") ? "audio/webm" : "");

    mediaRecorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);

    // 3) Start recording; send control "start"
    ws.addEventListener("open", () => {
      ws.send(JSON.stringify({ type: "start", mimeType: mediaRecorder.mimeType || "audio/webm" }));
    });

    mediaRecorder.addEventListener("dataavailable", async (e) => {
      // Called every timeslice; stream chunk to server
      if (e.data && e.data.size > 0 && ws && ws.readyState === WebSocket.OPEN) {
        const buf = await e.data.arrayBuffer();
        ws.send(buf); // send binary frame
      }
    });

    mediaRecorder.addEventListener("start", () => {
      statusDiv.textContent = "Recording… (streaming)";
      micBtn.classList.add("recording");
    });

    mediaRecorder.addEventListener("stop", () => {
      micBtn.classList.remove("recording");
    });

    // 4) Record with a timeslice (ms) so we get periodic chunks
    mediaRecorder.start(400); // ~every 400ms
    isRecording = true;
  } catch (err) {
    console.error(err);
    statusDiv.textContent = "Mic error: " + err.message;
  }
}

async function stopStreaming() {
  try {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
      mediaRecorder.stop();
    }
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: "stop" }));
      // Give the server a moment to flush file before closing
      setTimeout(() => {
        try { ws.close(); } catch {}
      }, 150);
    }
  } finally {
    isRecording = false;
    statusDiv.textContent = "Stopping…";
  }
}
