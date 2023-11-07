# backend/inference.py

import uuid

import os
import config
import cv2
from YOLOv7 import YOLOv7


def init(model):
    model_name = f"{config.MODEL_PATH}{model}.onnx"

    # Initialize YOLOv7 object detector
    yolov7_detector = YOLOv7(model_name, conf_thres=0.3, iou_thres=0.5)

    return yolov7_detector

def inference_image(detector, image):
    boxes, scores, class_ids = detector(image)
    output = detector.draw_detections(image)

    return output