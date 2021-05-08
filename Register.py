import hashlib
import sys

import gspread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from oauth2client.service_account import ServiceAccountCredentials

import Login

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        # Remove Title Bar
        RegisterWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        RegisterWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(438, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterWindow.sizePolicy().hasHeightForWidth())
        RegisterWindow.setSizePolicy(sizePolicy)
        RegisterWindow.setMinimumSize(QtCore.QSize(438, 600))
        RegisterWindow.setMaximumSize(QtCore.QSize(438, 600))
        font = QtGui.QFont()
        font.setKerning(True)
        RegisterWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Artiviewer Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegisterWindow.setWindowIcon(icon)
        RegisterWindow.setToolTip("")
        RegisterWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 900))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(441, 900))
        self.label.setMaximumSize(QtCore.QSize(441, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 131, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/Artiviewer Icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.usernameField = QtWidgets.QTextEdit(self.centralwidget)
        self.usernameField.setGeometry(QtCore.QRect(40, 220, 361, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameField.sizePolicy().hasHeightForWidth())
        self.usernameField.setSizePolicy(sizePolicy)
        self.usernameField.setObjectName("usernameField")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_4.setObjectName("label_4")
        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(40, 350, 361, 26))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordField.sizePolicy().hasHeightForWidth())
        self.passwordField.setSizePolicy(sizePolicy)
        self.passwordField.setObjectName("passwordField")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_5.setObjectName("label_5")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(150, 465, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
"border-color: rgb(233, 151, 0);\n"
"border:none;\n"
"bordder-radius:12px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(233, 151, 0);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 560, 111, 21))
        self.label_6.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_6.setObjectName("label_6")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(400, -1, 41, 31))
        self.exit.setStyleSheet("QPushButton{\n"
"border-color: rgb(233, 151, 0);\n"
"border:none;\n"
"bordder-radius:12px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(233, 151, 0);\n"
"}")
        self.exit.setObjectName("exit")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(260, 520, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton{\n"
"border-color: rgb(233, 151, 0);\n"
"border:none;\n"
"bordder-radius:12px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(233, 151, 0);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 520, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 390, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_8.setObjectName("label_8")
        self.passwordField_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField_2.setGeometry(QtCore.QRect(40, 420, 361, 26))
        self.passwordField_2.setEchoMode(QtWidgets.QLineEdit.Password)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordField_2.sizePolicy().hasHeightForWidth())
        self.passwordField_2.setSizePolicy(sizePolicy)
        self.passwordField_2.setObjectName("passwordField_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 255, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_9.setObjectName("label_9")
        self.emailField = QtWidgets.QTextEdit(self.centralwidget)
        self.emailField.setGeometry(QtCore.QRect(40, 285, 361, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailField.sizePolicy().hasHeightForWidth())
        self.emailField.setSizePolicy(sizePolicy)
        self.emailField.setObjectName("usernameField_2")
        RegisterWindow.setCentralWidget(self.centralwidget)

        self.exit.clicked.connect(self.close)
        #Here register is the login button
        self.registerButton.clicked.connect(self.Login)
        #Here Login is the register button
        self.loginButton.clicked.connect(self.checkRegDetails)
        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Register - Artiviewer "))
        self.label_3.setText(_translate("LoginWindow", "Register to Artiviewer"))
        self.label_4.setText(_translate("LoginWindow", "Username"))
        self.label_5.setText(_translate("LoginWindow", "Password"))
        self.loginButton.setText(_translate("LoginWindow", "Register"))
        self.label_6.setText(_translate("LoginWindow", "Artiviewer - 2020"))
        self.exit.setText(_translate("LoginWindow", "X"))
        self.registerButton.setText(_translate("LoginWindow", "Login now"))
        self.label_7.setText(_translate("LoginWindow", "Already have an account?"))
        self.label_8.setText(_translate("LoginWindow", "Confirm Password"))
        self.label_9.setText(_translate("LoginWindow", "Email"))

    def close(self):
        app.quit()
    def Login(self, checked):
        self.window = QtWidgets.QMainWindow()
        self.ui = Login.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        RegisterWindow.destroy()
        self.window.show()
    def checkRegDetails(self, _str):
        usernameExist = True
        emailExist = True
        password1Exist = True
        password2Exist = True
        errorBox = QMessageBox()
        if self.usernameField.toPlainText() == '':
            usernameExist = False
        if self.emailField.toPlainText() == '':
            emailExist = False
        if self.passwordField.text() == '':
            password1Exist = False
        if self.passwordField_2.text() == '':
            password2Exist = False
        if not usernameExist:
            errorBox.setWindowTitle("Error")
            errorBox.setText("Username field cannot be empty")
            errorBox.setIcon(QMessageBox.Critical)
            show = errorBox.exec_()
        elif not emailExist:
            errorBox.setWindowTitle("Error")
            errorBox.setText("Email field cannot be empty")
            errorBox.setIcon(QMessageBox.Critical)
            show = errorBox.exec_()
        elif not password1Exist:
            errorBox.setWindowTitle("Error")
            errorBox.setText("Password field cannot be empty")
            errorBox.setIcon(QMessageBox.Critical)
            show = errorBox.exec_()
        elif not password2Exist:
            errorBox.setWindowTitle("Error")
            errorBox.setText("Confirm password field cannot be empty")
            errorBox.setIcon(QMessageBox.Critical)
            show = errorBox.exec_()
        else:
            if self.passwordField.text() != self.passwordField_2.text():
                errorBox.setWindowTitle("Error")
                errorBox.setText("Password and Confirm password must be the same")
                errorBox.setIcon(QMessageBox.Critical)
                show = errorBox.exec_()
            else:
                scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleCreds.json", scope)
                client = gspread.authorize(creds)
                Sheet = client.open("User Accounts").sheet1
                UsernameList = Sheet.col_values(1)
                emailList = Sheet.col_values(3)
                username = self.usernameField.toPlainText()
                email = self.emailField.toPlainText()
                email = email.lower()
                if username in UsernameList:
                    errorBox.setWindowTitle("Error")
                    errorBox.setText(
                        "Username already exists, please choose a different one or Login now if you have an account")
                    errorBox.setIcon(QMessageBox.Critical)
                    show = errorBox.exec_()
                elif email in emailList:
                    errorBox.setWindowTitle("Error")
                    errorBox.setText(
                        "Email already exists, please choose a different one or Login now if you have an account")
                    errorBox.setIcon(QMessageBox.Critical)
                    show = errorBox.exec_()
                else:
                    password = self.passwordField.text()
                    password = password.encode("utf-8")
                    password = hashlib.md5(password)
                    password = password.hexdigest()
                    insertDetails = [username, password, email]
                    Sheet.insert_row(insertDetails, 2)
                    errorBox.setWindowTitle("Success")
                    errorBox.setText(
                        "Your account has been created, you will now be taken back to the login screen to login")
                    errorBox.setIcon(QMessageBox.Information)
                    show = errorBox.exec_()
                    self.Login()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
