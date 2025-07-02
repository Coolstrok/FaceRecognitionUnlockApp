const video = document.getElementById("video");
const statusDiv = document.getElementById("status");
const captureBtn = document.getElementById("captureBtn");

let stream = null;

// Start webcam
navigator.mediaDevices.getUserMedia({ video: true })
  .then((s) => {
    stream = s;
    video.srcObject = stream;
  })
  .catch((err) => {
    console.error("Error accessing webcam:", err);
    statusDiv.textContent = "❌ Error accessing camera.";
    statusDiv.className = "failure";
  });

// Handle Unlock button click
captureBtn.addEventListener("click", async () => {
  // Pause the video to freeze the frame
  video.pause();

  statusDiv.textContent = "🔍 Processing...";
  statusDiv.className = "";

  // Draw current frame to canvas
  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const context = canvas.getContext("2d");
  context.drawImage(video, 0, 0);

  // Convert canvas to base64 image
  const imageData = canvas.toDataURL("image/jpeg");

  try {
    const response = await fetch("/unlock", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: imageData }),
    });

    const result = await response.json();

    if (result.success) {
      statusDiv.textContent = "✅ Face recognized. Access granted!";
      statusDiv.className = "success";
    } else {
      statusDiv.textContent = "❌ Face not recognized. Try again.";
      statusDiv.className = "failure";
    }
  } catch (error) {
    console.error("Error:", error);
    statusDiv.textContent = "❌ Error occurred during unlock.";
    statusDiv.className = "failure";
  }

  // Resume video after short delay
  setTimeout(() => {
    video.play();
  }, 1000); // 1 second delay — you can reduce or increase it
});