from cv2 import *
import time

def callCam():
    cam = VideoCapture(1)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        imwrite("../../Django/RobotCMS/static/img/capture.jpg",img) #save image

while(True):
    callCam()
    time.sleep(0.33)
