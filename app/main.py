from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import cv2
import numpy as np
from app.face_utils import compare_faces

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("app/static/index.html", "r") as f:
        return f.read()

class ImageData(BaseModel):
    image: str

@app.post("/unlock")
async def unlock(data: ImageData):
    try:
        _, encoded = data.image.split(",") if "," in data.image else ("", data.image)
        img_bytes = base64.b64decode(encoded)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        result = compare_faces(img)
        return {"success": result}
    except Exception as e:
        return {"success": False, "error": str(e)}