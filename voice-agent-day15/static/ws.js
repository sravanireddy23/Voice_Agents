const urlInput = document.getElementById("ws-url");
const connectBtn = document.getElementById("connect-btn");
const disconnectBtn = document.getElementById("disconnect-btn");
const statusDiv = document.getElementById("status");
const msgInput = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");
const logDiv = document.getElementById("log");

let socket = null;

// Default ws:// URL for current host
window.addEventListener("DOMContentLoaded", () => {
  const defaultURL = `ws://${location.host}/ws`;
  urlInput.value = defaultURL;
});

function log(line, type = "info") {
  const el = document.createElement("div");
  el.className = `line ${type}`;
  el.textContent = line;
  logDiv.appendChild(el);
  logDiv.scrollTop = logDiv.scrollHeight;
}

function setConnectedUI(connected) {
  connectBtn.disabled = connected;
  disconnectBtn.disabled = !connected;
  msgInput.disabled = !connected;
  sendBtn.disabled = !connected;
}

connectBtn.addEventListener("click", () => {
  const url = urlInput.value.trim();
  if (!url) return;

  socket = new WebSocket(url);

  socket.addEventListener("open", () => {
    statusDiv.textContent = "Status: Connected";
    log("✅ Connected", "ok");
    setConnectedUI(true);
  });

  socket.addEventListener("message", (event) => {
    log(`⬅️  ${event.data}`, "recv");
  });

  socket.addEventListener("close", () => {
    statusDiv.textContent = "Status: Disconnected";
    log("❌ Disconnected", "warn");
    setConnectedUI(false);
  });

  socket.addEventListener("error", (e) => {
    log("⚠️  WebSocket error (check server/logs)", "err");
  });
});

disconnectBtn.addEventListener("click", () => {
  if (socket && socket.readyState === WebSocket.OPEN) {
    socket.close();
  }
});

sendBtn.addEventListener("click", () => {
  const text = msgInput.value.trim();
  if (!text || !socket || socket.readyState !== WebSocket.OPEN) return;
  socket.send(text);
  log(`➡️  ${text}`, "send");
  msgInput.value = "";
});

msgInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendBtn.click();
});
