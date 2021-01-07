# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from next import Ui_OtherWindow

class Ui_MainWindow(object):
    def openWindow(self):
        #self.window = QtWidgets.QMainWindow()
        #self.ui = Ui_OtherWindow()
        #self.ui.setupUi(self.window)
        #MainWindow.hide()
        #self.window.show()
        self.OtherWindow = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.OtherWindow)
        self.OtherWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 70, 201, 71))
        self.pushButton_3.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(170, 170, 255);\n"
"font: 57 12pt \"Quicksand Medium\";")
        self.pushButton_3.setObjectName("pushButton_3")        
        self.pushButton_3.clicked.connect(self.openWindow)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 230, 201, 71))
        self.pushButton_5.setStyleSheet("color: rgb(74, 74, 222);\n"
"font: 57 12pt \"Quicksand Medium\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.btn5_clicked)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", " start create (non-image)"))
        self.pushButton_5.setText(_translate("MainWindow", "start recognize (image)"))

    def btn5_clicked(self):
        f=open('example.py', 'r')
        exec(f.read())
        f.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

