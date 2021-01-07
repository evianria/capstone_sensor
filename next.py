# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import os
import sys
from PyQt5 import QtWidgets as qtw
import requests
import json
#from first import Ui_MainWindow

class Ui_OtherWindow(object):
    #def openWindow(self):
     #   self.window = QtWidgets.QMainWindow()
      #  self.ui = MainWindow()
       # self.ui.setupUi(self.window)
       # Ui_OtherWindow.hide()
       # self.window.show()
       
       
    def closescr(self, OtherWindow):
        OtherWindow.hide()
        
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 214)
        
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 431, 21))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(210, 110, 99, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.btn1_clicked)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 110, 99, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.closescr(OtherWindow))
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 91, 22))
        self.label.setObjectName("label")
        
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        self.pushButton_2.clicked.connect(self.statusbar.close)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.pushButton_1.setText(_translate("OtherWindow", " save"))
        self.pushButton_2.setText(_translate("OtherWindow", "finish"))
        self.label.setText(_translate("OtherWindow", "Std_num : "))

    def btn1_clicked(self):
        global stn_code
        stn_code = self.lineEdit.text()
        print(stn_code)
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 30
        rawCapture = PiRGBArray(camera, size=(640, 480))
        faceCascade = cv2.CascadeClassifier("/home/pi/opencv/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml")
        name = stn_code
        dirName = "./images/" + name
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print("Directory Created")
        else:
            print("Name already exists")
        count = 1
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            if count > 30:
                break
            frame = frame.array
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
            for (x, y, w, h) in faces:
                roiGray = gray[y:y+h, x:x+w]
                fileName = dirName + "/" + name + str(count) + ".jpg"
                cv2.imwrite(fileName, roiGray)
                cv2.imshow("face", roiGray)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                count += 1
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            rawCapture.truncate(0)
            if key == 27:
                break
        cv2.destroyAllWindows()


#if __name__ == "__main__":
 #   import sys
  #  app = QtWidgets.QApplication(sys.argv)
   # OtherWindow = QtWidgets.QMainWindow()
   # ui = Ui_OtherWindow()
   # ui.setupUi(OtherWindow)
   # OtherWindow.show()
   # sys.exit(app.exec_())

