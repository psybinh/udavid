# backend/main.py

import uuid

import os
import numpy as np
from PIL import Image
import cv2
import uvicorn
from fastapi import File, FastAPI, UploadFile
import json

import config
import inference


app = FastAPI()


@app.get('/')
def read_root():
    return {'message:': 'Welcome from the API'}

@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    model = config.STYLES[style]
    detector = inference.init(model)

    image = np.array(Image.open(file.file))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    boxes, scores, class_ids = inference.inference_image(detector, image)

    return {"size": "{0} x {1}".format(*image.shape[:2]), "boxes": json.dumps(boxes.tolist()), "scores": json.dumps(scores.tolist()), "class_ids": json.dumps(class_ids.tolist())}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)