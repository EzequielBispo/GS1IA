from roboflow import Roboflow
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Any

rf = Roboflow(api_key="KWRMPoXDg6S94OZZwlhY")
project = rf.workspace("bxspoworkspace").project("corais")
modelo = project.version(2).model 

app = FastAPI()

class Detection(BaseModel):
    class_name: str
    confidence: float
    x: int
    y: int
    width: int
    height: int

class DetectionResponse(BaseModel):
    filename: str
    width: int
    height: int
    size_bytes: int
    detections: List[Detection]

@app.post("/detect-coral/", response_model=DetectionResponse)
async def detect_coral(file: UploadFile = File(...)):
    image = np.frombuffer(await file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    height, width, _ = image.shape
    file_size = image.nbytes

    predictions = model.predict(image, confidence=40, overlap=30).json()

    detections = []
    for prediction in predictions.get('predictions', []):
        detections.append(Detection(
            class_name=prediction['class'],
            confidence=float(prediction['confidence']),
            x=int(prediction['x']),
            y=int(prediction['y']),
            width=int(prediction['width']),
            height=int(prediction['height'])
        ))

    response = DetectionResponse(
        filename=file.filename,
        width=width,
        height=height,
        size_bytes=file_size,
        detections=detections
    )
    
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)