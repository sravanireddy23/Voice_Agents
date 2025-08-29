const speakBtn = document.getElementById('speakBtn');
const userText = document.getElementById('userText');
const responseText = document.getElementById('responseText');
const audioPlayer = document.getElementById('audioPlayer');

speakBtn.addEventListener('click', async () => {
  const text = userText.value.trim();
  const voice = document.getElementById('voiceSelect').value;
  const mood = document.getElementById('moodSelect').value;
  const pitch = document.getElementById('pitchSelect').value;

  if (!text) {
    alert("Please enter a message!");
    return;
  }

  responseText.textContent = "Generating voice...";
  audioPlayer.src = "";

  // Mock API call (replace with your FastAPI endpoint)
  setTimeout(() => {
    responseText.textContent = `Agent response for: "${text}"`;
    
    // Mock audio playback
    audioPlayer.src = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3";
    audioPlayer.play();
  }, 1000);
});
