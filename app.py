from flask import Flask, jsonify
app = Flask(__name__)
from threading import Timer
import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime
import pandas as pd

x = 0
y = 0

def update_data(interval):
    Timer(interval, update_data, [interval]).start()
    global x, y
    if x > 400:
        x = 0
        y = 0
    x += 1
    y += 2

    print("UPDATED DATA")

    # READ LAST 5 Lines of CSV (if exists)
    face_df = pd.read_csv("./newWebcam.py")
    print(face_df)
    # 

update_data(2)


@app.route('/')
def hello():
    return jsonify(
        x = x,
        y = y
    )

if __name__ == '__main__':
    app.run()