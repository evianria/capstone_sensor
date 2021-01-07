import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import pickle
from time import sleep
import requests
import json


f=open('training.py', 'r')
exec(f.read())
f.close()

with open('labels', 'rb') as f:
    dict = pickle.load(f)
    f.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

faceCascade = cv2.CascadeClassifier("/home/pi/opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
font = cv2.FONT_HERSHEY_SIMPLEX
a=True
b=True

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = frame.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x, y, w, h) in faces:
        roiGray = gray[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roiGray)

        for name, value in dict.items():
            if value == id_:
                if conf <= 70:
                    print(name) 
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, str(int(conf)) + str('%'), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)
                    #res = requests.post('http://192.168.0.2:3000/process/sensorimg', data = {'id':name, 'data':'1'}, headers={})
                    #print(res.text)
                    #if res.text != '':
                    #    a=False
                     #   break
        if a == False:
            b=False
            break
        
    if b == False:
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key == 27:
        break


cv2.destroyAllWindows()