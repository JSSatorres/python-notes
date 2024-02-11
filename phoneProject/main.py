import cv2
from flask import Flask
video = cv2.VideoCapture(1) # 0 for default camera, 1 for external camera

def get_frame():
  success, frame = video.read()
  sc, encoded_image =cv2.imencode('.jpg', frame)
  frame = encoded_image.tobytes()
  yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)