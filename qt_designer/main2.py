import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from time import sleep
from PyQt5.uic import loadUi
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime
from PyQt5.QtCore import Qt, QEvent
from cv2 import GaussianBlur
import cvlib as cv
from cvlib.object_detection import draw_bbox

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))    
    return os.path.join(base_path, relative_path)

form = resource_path('main2.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)

        # volume, slider
        self.vol.setRange(0,100)
        self.vol.setValue(50)

        # signal
        self.play_video.clicked.connect(self.toggle_video)
        self.stop_video.clicked.connect(self.stop)
        self.vol.valueChanged.connect(self.volumeChanged)
        self.bar.sliderMoved.connect(self.barChanged) 

     
        self.gaussian_flitter.clicked.connect(self.toggle_gaussian)
        self.canny_flitter.clicked.connect(self.toggle_canny)
        #self.median_flitter = self.findChild(QPushButton, "median_flitter")
        self.median_flitter.clicked.connect(self.toggle_median)
        
        #self.web_cam = self.findChild(QCheckBox, "web_cam")
        self.web_cam.stateChanged.connect(self.toggle_webcam)
        
        self.yolov3_radio.clicked.connect(self.set_yolov3_model)

        self.cap = None
        self.running = False
        self.is_gaussian_on = False
        self.is_median_on = False
        self.is_canny_on = False
        self.webcam_on = False
        self.video_on = False
        self.selected_model = 'yolov3'
  
    def run(self):
        cap = cv2.VideoCapture('C:\\Users\\cofla\\Desktop\\laon\\spongebob.mp4')
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
   
        while self.running:
            ret, img = self.cap.read()
            if ret:
       
                if self.is_gaussian_on:
                    img = cv2.GaussianBlur(img, (0, 0), 3)
                if self.is_median_on:
                    img = cv2.medianBlur(img, 21)
                if self.is_canny_on:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 100, 200)
                    img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


                if self.webcam_on and self.selected_model:
                    bbox, label, conf = cv.detect_common_objects(img, model=self.selected_model)
                    img = draw_bbox(img, bbox, label, conf)

            # 화면에 출력합니다.
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.video_container.setPixmap(pixmap)
                sleep(0.02)  # 배속 조정 0.02 -> 0.5배속
            else:
                QtWidgets.QMessageBox.about(self, "Error", "Cannot read frame.")
                print("cannot read frame.")
                break
        self.cap.release()
        print("Thread end.")

    def stop(self):
        self.running = False
        print("stoped..")

    def start(self):
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")

    def onExit(self):
        print("exit")
        self.stop()
    

    def volumeChanged(self):
        #self.vol.value()
        self.vol.setNum(self.vol.value())

    def barChanged(self):
        value = self.bar.value()  
        print(self.bar)
        self.bar.setNum(value)    

    def updateState(self):
        self.state.setText(self.msg)


    def updateBar(self):
        self.bar.setRange(0,self.duration)    
        self.bar.setSingleStep(int(self.duration/10))
        self.bar.setPageStep(int(self.duration/10))
        self.bar.setTickInterval(int(self.duration/10))
        td = datetime.timedelta(milliseconds=self.duration)        
        stime = str(td)
        idx = stime.rfind('.')
        self.duration = stime[:idx]

    def updatePos(self, pos):
        self.bar.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.duration}'
        self(stime)

    def updatePos(self, pos):
        self.bar.setValue(pos)
        td = datetime.timedelta(milliseconds=pos)
        stime = str(td)
        idx = stime.rfind('.')
        stime = f'{stime[:idx]} / {self.duration}'
        self.playtime.setText(stime)
 

    def toggle_gaussian(self):
        self.is_gaussian_on = not self.is_gaussian_on

    def toggle_canny(self):
        self.is_canny_on = not self.is_canny_on

    def toggle_median(self):
        self.is_median_on = not self.is_median_on

    def toggle_webcam(self):
        self.webcam_on = self.web_cam.isChecked()
        if self.webcam_on:
            self.start_webcam()
        else:
            self.stop_webcam()

    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("Webcam started..")

    def stop_webcam(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
            print("Webcam stopped..")

    def toggle_video(self):
        self.video_on = not self.video_on
        if self.video_on:
            self.start_video()
        else:
            self.stop_video()
    
    def start_video(self):
        self.cap = cv2.VideoCapture('C:\\Users\\cofla\\Desktop\\laon\\spongebob.mp4')
        self.running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("Video playback started..")

    def stop_video(self):
        self.running = False
        if self.cap is not None:
            self.cap.release()
            print("Video playback stopped..")

    def set_yolov3_model(self):
        self.selected_model = 'yolov3'


    def update_button_text(self):
        # Update the button's text based on the current state
        self.gaussian_flitter.setText("On" if self.is_on else "Off")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )

