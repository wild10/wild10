# app.py (dentro del contenedor)
## this code only make the inference & comunication to host

# import libs
from fastapi import FastAPI, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO

# Load api + model
app = FastAPI()
model = YOLO("yolo12n.pt")

# start connection & use model inference
# Define el endPoint : expone endpoint http://<host>:<port>/predict
@app.post("/predict")
async def predict(file: UploadFile):
    # read image bytes sent from host.
    img_bytes = await file.read()
    # Decode image & convert bytes to opencv's image.
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)

    # model inference + results.
    results = model(img, verbose=False)[0]

    # Extract details: [x1,y1, x2, y2, confidence, class_id]
    detections = []
    for box in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = box 
        detections.append({
            "box": [round(x, 2) for x in [x1, y1, x2, y2]], # coordenadas.
            "confidence": round(score, 4),
            "class_id": int(class_id),
            "label": model.names[int(class_id)]

        })

    # return de list of dicts.
    return {"detections": detections}
