FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install 'ffmpeg' 'libsm6' 'libxext6' 'wget' -y

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN rm -rf models
RUN mkdir models
RUN wget https://binhps1-yolov7-models.s3.amazonaws.com/yolov7_256x480.onnx
RUN mv yolov7_256x480.onnx models/yolov7_256x480.onnx
RUN wget https://binhps1-yolov7-models.s3.amazonaws.com/yolov7_480x640.onnx 
RUN mv yolov7_480x640.onnx models/yolov7_480x640.onnx
RUN wget https://binhps1-yolov7-models.s3.amazonaws.com/yolov7-tiny_256x640.onnx 
RUN mv yolov7-tiny_256x640.onnx models/yolov7-tiny_256x640.onnx
RUN wget https://binhps1-yolov7-models.s3.amazonaws.com/yolov7-tiny_480x640.onnx 
RUN mv yolov7-tiny_480x640.onnx models/yolov7-tiny_480x640.onnx

EXPOSE 8080

CMD ["python", "main.py"]
