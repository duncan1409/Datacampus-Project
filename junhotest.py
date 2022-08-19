import sys
import cv2
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import uic


class introWindow(QDialog):
    def __init__(self):
        super().__init__()
        screenName = QLabel('IntroWindow', self)
        
        label = QLabel(self)
        icon = QPixmap('icon.png')
        label.setPixmap(icon)
        label.move(250, 250)

        button1 = QPushButton('깜빡 창 닫기', self)
        button1.move(10, 250)
        button1.clicked.connect(lambda: self.closeWindow())

        button2 = QPushButton('깜빡 다음으로', self)
        button2.move(10, 500)
        button2.clicked.connect(lambda: self.nextScreen())


    def closeWindow(self):
        widget.close()

    def nextScreen(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        screenName = QLabel('MainWindow', self)

        label = QLabel(self)
        icon = QPixmap('icon.png')
        label.setPixmap(icon)
        label.move(250, 250)

        button1 = QPushButton('깜빡 창 닫기', self)
        button1.move(10, 250)
        button1.clicked.connect(lambda: self.closeWindow())


        button2 = QPushButton('깜빡 다음으로', self)
        button2.move(10, 700)
        button2.clicked.connect(lambda: self.nextScreen())

        button2 = QPushButton('깜빡 이전으로', self)
        button2.move(10, 500)
        button2.clicked.connect(lambda: self.prevScreen())

        button3 = QPushButton('1. 눈 피로도 측정', self)
        button3.move(250, 800)
        button4 = QPushButton('2. 눈 스트레칭', self)
        button4.move(250, 900)
        button5 = QPushButton('3. 눈 건강에 딱좋아', self)
        button5.move(250, 1000)
        button6 = QPushButton('4. 개발진', self)
        button6.move(250, 1100)

    def closeWindow(self):
        widget.close()

    def prevScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def nextScreen(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
                Pic = ConvertToQtFormat.scaled(1280, 960, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

class detectWindow(QDialog):
    def __init__(self):
        super().__init__()
        screenName = QLabel('DetectWindow', self)
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.Worker1 = Worker1()  # 동영상 출력

        test = QPushButton("test", self)
        test.clicked.connect(lambda: self.prevScreen())
        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

    def prevScreen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QStackedWidget()
    widget.addWidget(introWindow())
    widget.addWidget(mainWindow())
    widget.addWidget(detectWindow())

    widget.setWindowFlag(Qt.FramelessWindowHint)
    widget.setFixedHeight(1500)
    widget.setFixedWidth(2000)
    widget.setWindowTitle("깜빡")

    widget.show()
    app.exec_()