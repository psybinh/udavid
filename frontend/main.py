# frontend/main.py

import requests
import streamlit as st
from PIL import Image
from utils import draw_detections
import numpy as np
import json

STYLES = {
    "yolov7_256x480": "yolov7_256x480",
    "yolov7_480x640": "yolov7_480x640",
    "yolov7-tiny_256x640": "yolov7-tiny_256x640",
    "yolov7-tiny_480x640": "yolov7-tiny_480x640",
}

st.set_option('deprecation.showfileUploaderEncoding', False)
# st.title('Udavid - Object detection')
st.title('Udavid - Semantic segmentation')
image = st.file_uploader('Choose an image (Support: png, jpg, jpeg)', type=['png', 'jpg', 'jpeg'])
style = st.selectbox('Choose the model', [i for i in STYLES.keys()])

if st.button('Detect'):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://backend:8080/{style}", files=files)
        rs = res.json()
        
        if "message" in rs:
            st.error(rs.get('message'), icon="🚨")

        size = rs.get('size')
        boxes = np.asarray(json.loads(rs.get('boxes')))
        scores = np.asarray(json.loads(rs.get('scores')))
        class_ids = np.asarray(json.loads(rs.get('class_ids')))

        st_image = st.image(image, caption="Original")
        pilimage = Image.open(image).convert("RGB")
        np_image = np.asarray(pilimage)

        image_output = draw_detections(np_image, boxes, scores, class_ids)
        
        st.image(image_output, caption="Anotated")
        st.write("Size: {}".format(rs.get('size')))