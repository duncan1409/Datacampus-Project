import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('mainwindow.ui')
form_class = uic.loadUiType(form)[0]

form_second = resource_path('secondwindow.ui')
form_secondwindow = uic.loadUiType(form_second)[0]

"""form_cv = resource_path('cv.ui')
form_cvwindow = uic.loadUiTye(form_cv)[0]"""

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def btn_main_to_second(self):
        self.hide()                     
        self.second = secondwindow()    
        self.second.exec()              
        self.show()    

class secondwindow(QDialog,QWidget,form_secondwindow):
    def __init__(self):
        super(secondwindow,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupUi(self)
    
    def btn_second_to_main(self):
        self.close()

"""class cvwindow(QDialog,QWidget,form_cvwindow):
    def __init__(self):
        super(cvwindow,self).__init__()
        self.initUi()
        self.show()
    def initUi(self):
        self.setupUi(self)
    
    def btn_second_to_main(self):
        self.close()

class Worker1(QThread): #MW method 안의 method Worker1
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()