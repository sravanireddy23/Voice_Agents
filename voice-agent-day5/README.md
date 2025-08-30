# 30 Days of AI Voice Agents | Day 5: Send Audio to the Server

## Overview
In Day 5, we extend the **Echo Bot** from Day 4 to upload the recorded audio to a Python backend server using **FastAPI**. The server receives the audio file, saves it temporarily, and returns information about the file including name, content type, and size. A status message on the UI shows the upload progress.

---

## Features
- **Record Voice**: Continue using the Echo Bot to record your voice in the browser.
- **Upload Audio**: After stopping the recording, the audio file is sent to the server automatically.
- **Server Response**: The backend returns:
  - File name
  - Content type
  - File size
- **UI Status**: Shows a message indicating the upload progress and completion.

---

## How It Works
1. User records audio using the **Echo Bot**.
2. When recording stops, JavaScript sends the audio file to the FastAPI backend via a `POST` request.
3. FastAPI receives the file at a `/upload` endpoint, saves it temporarily in an `/uploads` folder, and responds with file metadata.
4. The frontend displays the upload status and server response.

---

## Usage
1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
````

2. Open the HTML page with the Echo Bot in a browser.
3. Record your voice using the **Start Recording** button.
4. Click **Stop Recording** to stop and automatically upload the file.
5. View the upload status and server response on the UI.

---

## Backend Endpoint Example

* **Endpoint**: `POST /upload`
* **Request**: `multipart/form-data` with audio file
* **Response**:

```json
{
  "filename": "audio.wav",
  "content_type": "audio/wav",
  "size": 34567
}
```

---

## Resources

* [FastAPI File Upload Tutorial](https://fastapi.tiangolo.com/tutorial/request-files/)
* [FastAPI UploadFile Reference](https://fastapi.tiangolo.com/reference/uploadfile/)
* [Saving UploadFile in FastAPI (GeeksforGeeks)](https://www.geeksforgeeks.org/python/save-uploadfile-in-fastapi/)

---

## Author

**Sravani Reddy Gavinolla**
Computer Science & Engineering Student

