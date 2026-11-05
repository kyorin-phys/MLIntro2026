# app.py
import streamlit as st
import cv2
import numpy as np
import requests
from pyzbar import pyzbar
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class BarcodeScanner(VideoTransformerBase):
    def __init__(self):
        self.last_isbn = None

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        barcodes = pyzbar.decode(img)
        for b in barcodes:
            code = b.data.decode()
            if code.startswith(('978', '979')) and len(code) == 13:
                self.last_isbn = code
            # バーコードを囲む
            x, y, w, h = b.rect
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, code, (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return img

st.title('📚 蔵書バーコードリーダー')

ctx = webrtc_streamer(key="scanner", video_transformer_factory=BarcodeScanner)

if ctx.video_transformer and ctx.video_transformer.last_isbn:
    isbn = ctx.video_transformer.last_isbn
    st.write(f"ISBN: {isbn}")
    r = requests.get('https://api.openbd.jp/v1/get', params={'isbn': isbn})
    book = r.json()[0]
    if book:
        s = book['summary']
        st.write(f"**{s['title']}** / {s['author']} / {s['publisher']}")