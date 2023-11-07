# frontend/main.py

import requests
import streamlit as st
from PIL import Image

STYLES = {
    "yolov7_256x640": "yolov7_256x640",
    "yolov7_480x640": "yolov7_480x640",
    "yolov7-tiny_256x640": "yolov7-tiny_256x640",
    "yolov7-tiny_480x640": "yolov7-tiny_480x640",
}

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('Udavid - Object detection')
image = st.file_uploader('Choose an image (Support: png, jpg, jpeg)', type=['png', 'jpg', 'jpeg'])
style = st.selectbox('Choose the model', [i for i in STYLES.keys()])

if st.button('Detect'):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://backend:8080/{style}", files=files)
        json = res.json()
        
        if "message" in json:
            st.error(json.get('message'), icon="🚨")

        image = Image.open(json.get('name'))
        st.image(image)
        st.write("Size: {}".format(json.get('size')))