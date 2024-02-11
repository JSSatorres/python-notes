import cv2
from flask import Flask
video = cv2.VideoCapture(1) # 0 for default camera, 1 for external camera

def get_frame():
  success, frame = video.read()
