import sys
import threading
import time
import wave

import cv2
import pyaudio
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

class VideoInterview(QMainWindow):
    def __init__(self):
        super(VideoInterview,self).__init__()
        GLOBAL_STATE = 0
        GLOBAL_TITLE_BAR = True
        loadUi('VideoRecordingUI.ui',self)
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
                                              "background-image: url(C:/Users/moham/PycharmProjects/Artiviewer/ClientSide/icons/16x16/cil-terminal.png);\n"
                                              "background-position: center;\n"
                                              "background-repeat: no-repeat;\n"
                                              "")
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
                                        "	border: none;\n"
                                        "	background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(85, 170, 255);\n"
                                        "}")
        icon = QIcon()
        icon.addFile(u"C:/Users/moham/PycharmProjects/Artiviewer/ClientSide/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
                                                "	border: none;\n"
                                                "	background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "	background-color: rgb(52, 59, 72);\n"
                                                "}\n"
                                                "QPushButton:pressed {	\n"
                                                "	background-color: rgb(85, 170, 255);\n"
                                                "}")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/moham/PycharmProjects/Artiviewer/ClientSide/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
                                     "	border: none;\n"
                                     "	background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/moham/PycharmProjects/Artiviewer/ClientSide/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        else:
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.frame_label_top_btns.setMinimumHeight(42)
            self.frame_icon_top_bar.hide()
            self.frame_btns_right.hide()
            self.frame_size_grip.hide()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.frame_main.setGraphicsEffect(self.shadow)

        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        self.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.btn_close.clicked.connect(lambda: self.close())
        self.cancelInterviewButton.clicked.connect(self.cancelInterview)
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.startRecordingButton.clicked.connect(self.controlTimer)
    def cancelInterview(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText("Are you sure you want to cancel the interview?")
        msg.setInformativeText("Cancelling the interview will discard all your progress")
        msg.setWindowTitle("Confirmation")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.msgbtn)
        retval = msg.exec_()

    def msgbtn(self,i):
        if i.text()[1] == 'Y':
            self.close()
    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image info
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.videoFeed.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            start_AudioRecording()
            # start timer
            self.timer.start(20)
            self.startRecordingButton.setText("Stop Recording")
            #fourcc = cv2.VideoWriter_fourcc(*'XVID')
            #out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            stop_AudioRecording()
            self.startRecordingButton.setEnabled(False)
            self.startRecordingButton.setText("Please move on to the next question")
            self.startRecordingButton.setStyleSheet(u"QPushButton{background-color:rgb(44,49,60);\n"
                                                    "                                                color:white;\n"
                                                    "                                                border-style:outset;\n"
                                                    "                                                border-width:2px;\n"
                                                    "                                                border-radius:10px;\n"
                                                    "                                                border-color:grey;\n"
                                                    "                                                font:16px bold;}")


class AudioRecorder():

    # Audio class based on pyAudio and Wave
    def __init__(self):

        self.open = True
        self.rate = 44100
        self.frames_per_buffer = 1024
        self.channels = 2
        self.format = pyaudio.paInt16
        self.audio_filename = "temp_audio.wav"
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.frames_per_buffer)
        self.audio_frames = []

    # Audio starts being recorded
    def record(self):

        self.stream.start_stream()
        while (self.open == True):
            data = self.stream.read(self.frames_per_buffer)
            self.audio_frames.append(data)
            if self.open == False:
                break

    # Finishes the audio recording therefore the thread too
    def stop(self):

        if self.open == True:
            self.open = False
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

            waveFile = wave.open(self.audio_filename, 'wb')
            waveFile.setnchannels(self.channels)
            waveFile.setsampwidth(self.audio.get_sample_size(self.format))
            waveFile.setframerate(self.rate)
            waveFile.writeframes(b''.join(self.audio_frames))
            waveFile.close()

        pass

    # Launches the audio recording function using a thread
    def start(self):
        audio_thread = threading.Thread(target=self.record)
        audio_thread.start()


def start_AudioRecording():
    global audio_thread

    audio_thread = AudioRecorder()

    audio_thread.start()
def stop_AudioRecording():
    audio_thread.stop()



app = QApplication(sys.argv)
w = VideoInterview()
w.show()
app.exec_()
