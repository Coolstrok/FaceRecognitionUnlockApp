🔓 Face Unlock Web App (FastAPI + OpenCV)

A web-based face recognition system built using FastAPI, OpenCV (ORB features), HTML, and JavaScript. Capture an image using your webcam and unlock the screen if your face matches a known face.

⸻

📸 Demo

https://github.com/Coolstrok/FaceRecognitionUnlockApp/blob/main/demoFaceUnlockApp.mp4

⸻

⚙️ Tech Stack
	•	Backend: FastAPI (Python)
	•	Frontend: HTML, JavaScript, CSS
	•	Computer Vision: OpenCV (Haar Cascades + ORB features)

⸻

✨ Features
	•	Live webcam capture via browser
	•	ORB-based face matching (no deep learning, no heavy dependencies)
	•	Works without face_recognition or dlib
	•	Shows success/failure message
	•	Simple retry experience

⸻

📁 Project Structure

face-unlock-app/
├── app/
│   ├── main.py              # FastAPI server
│   ├── face_utils.py        # Face comparison logic
│   └── static/
│       ├── index.html       # Frontend page
│       ├── script.js        # JS to capture webcam + send image
│       └── styles.css       # UI styles
├── known_faces/             # Store known face images (e.g., sam2.jpg)
├── requirements.txt         # Python dependencies
└── README.md


⸻

🚀 Getting Started

🔧 Prerequisites
	•	Python 3.9+
	•	opencv-python, fastapi, uvicorn

📦 Install Requirements

pip install -r requirements.txt

📸 Add Known Faces
	•	Put clear frontal face images inside known_faces/ directory (e.g., sam2.jpg)

🧠 Run the App

uvicorn app.main:app --reload

	•	Visit: http://localhost:8000

⸻

💡 Usage
	1.	Open browser → localhost:8000
	2.	Click on video feed to capture your face
	3.	Wait for the result (match or fail)

⸻

🧪 Testing
	•	Try showing a known face → ✅ Access granted
	•	Try unknown face or no face → ❌ Access denied

⸻

🎨 UI Design
	•	Simple and responsive layout
	•	Webcam displayed in rounded frame
	•	Color-coded result alerts

⸻

📹 Submission Checklist
	•	✅ All requirements implemented
	•	📂 Hosted on GitHub
	•	📹 Screen recording with backend logs

⸻

🙏 Credits
	•	Instructor: Kraken
	•	Student: [Sebastián Ramírez]
	•	Framework: FastAPI
	•	Vision Library: OpenCV
