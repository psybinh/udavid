import config
from YOLOv7 import YOLOv7

def init(model):
    model_name = f"{config.MODEL_PATH}{model}.onnx"
    yolov7_detector = YOLOv7(model_name, conf_thres=0.3, iou_thres=0.5)
    return yolov7_detector

def inference_image(detector, image):
    boxes, scores, class_ids = detector(image)
    return boxes, scores, class_ids