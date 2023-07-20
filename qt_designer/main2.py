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
from PyQt5.QtCore import QTimer
import cvlib as cv
from cvlib.object_detection import draw_bbox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QIcon


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
        video_path = 'C:\\Users\\cofla\\Desktop\\laon\\Summer-Field-Practice\\qt_designer\\spongebob.mp4'
        self.cap = cv2.VideoCapture(video_path)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if self.total_frames == 0:
            self.total_frames = 1

        self.fps = 0  # 초당 프레임 수(Frames Per Second)를 저장할 속성

        # fps 초기화
        self.update_fps()  # 초당 프레임 수를 업데이트하는 함수 호출

        # timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_slider_position)
        self.timer.start(100)

        # signal
        self.play_video.clicked.connect(self.toggle_video)
        self.stop_button.clicked.connect(self.stop_video)
        #self.stop_video.clicked.connect(self.stop)
        self.vol.valueChanged.connect(self.volumeChanged)
        self.bar.sliderMoved.connect(self.barChanged) 

 
        self.gaussian_flitter = self.findChild(QPushButton, "gaussian_flitter")
        self.gaussian_flitter.clicked.connect(self.toggle_gaussian)

        # Find the QPushButtons for the filters
        self.canny_flitter = self.findChild(QPushButton, "canny_flitter")
        self.canny_flitter.clicked.connect(self.toggle_canny)

        self.median_flitter = self.findChild(QPushButton, "median_flitter")
        self.median_flitter.clicked.connect(self.toggle_median)

        # Add QLabel to show video frames
        self.label_video = QLabel(self)
        self.label_video.setGeometry(10, 10, 800, 550)


        # webcam
        self.web_cam.stateChanged.connect(self.toggle_webcam)
        
        self.yolov3_radio.clicked.connect(self.set_yolov3_model)

        self.cap = None
        self.running = False
        self.is_gaussian_on = False
        self.is_median_on = False
        self.is_canny_on = False
        self.webcam_on = False
        self.video_on = False 
        
        self.update_fps()  # 초당 프레임 수를 업데이트하는 함수 호출


        self.selected_model = 'yolov3'
  
    def run(self):
        cap = cv2.VideoCapture('C:\\Users\\cofla\\Desktop\\laon\\Summer-Field-Practice\\qt_designer\\spongebob.mp4')
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
                self.label_video.setPixmap(pixmap)
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
        self.timer.start(100)

    def onExit(self):
        print("exit")
        self.stop()
    
    def update_slider_position(self):
        if self.cap is not None:
            total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            current_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            if total_frames == 0:
                total_frames = 1
            self.bar.setValue(int((current_frame / total_frames) * 100))

    def volumeChanged(self):
        volume_value = self.vol.value()
        # self.vol_label.setText(f"Volume: {volume_value}")

        # Set the volume of the video (if video is playing)
        if self.cap is not None and self.video_on:
            volume = volume_value / 100
            self.cap.set(cv2.CAP_PROP_VOLUME, volume)

    def update_fps(self):
        if self.cap is not None:
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        else:
            self.fps = 0


 #   def barChanged(self):
        # if self.running and self.cap is not None:
        #     total_duration = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #     current_position = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        #     self.bar.setRange(0, total_duration)
        #     self.bar.setValue(current_position)

        #     current_time = datetime.timedelta(seconds=int(current_position / self.fps))
        #     total_time = datetime.timedelta(seconds=int(total_duration / self.fps))
        #     self.playtime.setText(f"Time: {current_time} / {total_time}")
    def barChanged(self):
        if self.running and self.cap is not None:
            total_duration = self.total_frames
            current_position = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
            self.bar.setRange(0, total_duration)
            self.bar.setValue(current_position)

            if total_duration != 0 and self.fps != 0:  # total_duration 또는 self.fps가 0이 아닌 경우에만 시간 계산
                current_time = datetime.timedelta(seconds=int(current_position / self.fps))
                total_time = datetime.timedelta(seconds=int(total_duration / self.fps))
                self.playtime.setText(f"Time: {current_time} / {total_time}")
            else:
                self.playtime.setText(f"Time: - / -")  # fps가 0이거나 total_duration이 0인 경우 표시할 값 설정

    def toggle_gaussian(self):
        if self.sender() == self.findChild(QPushButton, "gaussian_flitter"):
            self.is_gaussian_on = not self.is_gaussian_on

    def toggle_canny(self):
        if self.sender() == self.findChild(QPushButton, "canny_flitter"):
            self.is_canny_on = not self.is_canny_on

    def toggle_median(self):
        if self.sender() == self.findChild(QPushButton, "median_flitter"):
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
        self.cap = cv2.VideoCapture('C:\\Users\\cofla\\Desktop\\laon\\Summer-Field-Practice\\qt_designer\\spongebob.mp4')
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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )

