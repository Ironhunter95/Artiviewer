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
from AudioRecorder import AudioRecorder
from keras.models import load_model
from VideoRecorder import VideoRecorder
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import speech_recognition as sr

class VideoInterview(QMainWindow):
    def __init__(self):
        super(VideoInterview,self).__init__()
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleCreds.json", scope)
        client = gspread.authorize(creds)
        Sheet = client.open("Active Interviews").sheet1
        Questions = Sheet.row_values(2)
        self.Questions=Questions[6:]
        self.Question_Index = 0
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
        self.questionTitle.setText(self.Questions[self.Question_Index])
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.dummy)
        # set control_bt callback clicked  function
        self.startRecordingButton.clicked.connect(self.controlTimer)
        self.nextQuestionButton.clicked.connect(self.nextQuestion)
    def transcribeAudio(self):
        r=sr.Recognizer()
        Wav = sr.AudioFile('temp_audio.wav')
        with Wav as source:
            audio = r.record(source)
        val = r.recognize_google(audio)
        Answers = open("answers.txt", "a")  # append mode
        currentAnswer = ("Question "+str(self.Question_Index + 1) +": " + self.Questions[self.Question_Index] + "\n" + "Answer: " + val +"\n")
        Answers.write(currentAnswer)
        Answers.close()
    def nextQuestion(self):
        self.transcribeAudio()
        if self.Question_Index == 4:
            self.close()
        self.startRecordingButton.setEnabled(True)
        self.startRecordingButton.setStyleSheet(u"QPushButton{background-color:rgb(44,49,60);\n"
                                                "                                                color:white;\n"
                                                "                                                border-style:outset;\n"
                                                "                                                border-width:2px;\n"
                                                "                                                border-radius:10px;\n"
                                                "                                                border-color:rgb(233,151,0);\n"
                                                "                                                font:16px bold;}\n"
                                                "QPushButton:Hover{background-color:rgb(64,71,88);\n"
                                                "                                                border-style:outset;\n"
                                                "                                                border-width:2px;\n"
                                                "                                                border-radius:10px;\n"
                                                "                                                border-color:rgb(233,151,0);\n"
                                                "                                                font:16px bold;}\n"
                                                "QPushButton:Pressed{background-color:orange;\\n\n"
                                                "                                                border-style:outset;\n"
                                                "   "
                                                "                                             border-width:2px;\n"
                                                "                                                border-radius:10px;\n"
                                                "                                                border-color:white;\n"
                                                "                                                font:16px bold;}")
        self.startRecordingButton.setText("Start Recording")
        self.Question_Index+=1
        self.questionTitle.setText(self.Questions[self.Question_Index])
        if self.Question_Index==4:
            self.nextQuestionButton.setText("End Interview")
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
    def dummy(self):
        pass
    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            start_VideoRecording()
            start_AudioRecording()
            # start timer
            self.timer.start(20)
            self.startRecordingButton.setText("Stop Recording")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            stop_VideoRecording()
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
def start_AudioRecording():
    global audio_thread

    audio_thread = AudioRecorder()

    audio_thread.start()
def stop_AudioRecording():
    audio_thread.stop()
def start_VideoRecording():
    global video_thread

    video_thread = VideoRecorder()

    video_thread.start()
def stop_VideoRecording():
    video_thread.stop()

app = QApplication(sys.argv)
w = VideoInterview()
w.show()
app.exec_()
