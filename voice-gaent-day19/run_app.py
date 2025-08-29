import webbrowser
import subprocess
import time

# Open the browser after a short delay
url = "http://127.0.0.1:8000/"

# Start Uvicorn in a subprocess
proc = subprocess.Popen(
    ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
)

# Wait a few seconds for server to start
time.sleep(2)

# Open the browser
webbrowser.open(url)

# Keep the script running so the server stays up
proc.wait()
