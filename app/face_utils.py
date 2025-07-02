import cv2
import numpy as np
import os

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# ORB feature detector
orb = cv2.ORB_create()

def crop_face(image):
    """Detect and crop the first face found."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        return None
    x, y, w, h = faces[0]
    return gray[y:y+h, x:x+w]

def extract_descriptors(image):
    """Crop face and extract ORB descriptors."""
    face = crop_face(image)
    if face is None:
        return None, None
    keypoints, descriptors = orb.detectAndCompute(face, None)
    return keypoints, descriptors

def compare_faces(test_img: np.ndarray, threshold: int = 15) -> bool:
    """Compare test image with all faces in known_faces folder."""
    known_faces_dir = "app/known_faces"
    test_kp, test_des = extract_descriptors(test_img)

    if test_des is None:
        print("[WARN] No descriptors in test image")
        return False

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)

    for filename in os.listdir(known_faces_dir):
        path = os.path.join(known_faces_dir, filename)
        known_img = cv2.imread(path)
        if known_img is None:
            print(f"[WARN] Failed to load {filename}")
            continue

        known_kp, known_des = extract_descriptors(known_img)
        if known_des is None:
            print(f"[WARN] No descriptors in {filename}")
            continue

        # Match descriptors
        matches = bf.knnMatch(known_des, test_des, k=2)
        good = [m for m, n in matches if m.distance < 0.75 * n.distance]

        print(f"[INFO] Matches with {filename}: {len(good)}")

        if len(good) > threshold:
            print(f"[INFO] {filename} matched successfully!")
            return True  # Found a match

    return False  # No match found