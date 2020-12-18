from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        #Remove Title Bar
        LoginWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        LoginWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(438, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(438, 600))
        LoginWindow.setMaximumSize(QtCore.QSize(438, 600))
        font = QtGui.QFont()
        font.setKerning(True)
        LoginWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Artiviewer Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setToolTip("")
        LoginWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 781))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 131, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/Artiviewer Icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.usernameField = QtWidgets.QTextEdit(self.centralwidget)
        self.usernameField.setGeometry(QtCore.QRect(40, 300, 361, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameField.sizePolicy().hasHeightForWidth())
        self.usernameField.setSizePolicy(sizePolicy)
        self.usernameField.setObjectName("usernameField")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 190, 271, 41))
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
        self.label_4.setGeometry(QtCore.QRect(40, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_4.setObjectName("label_4")
        self.passwordField = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordField.setGeometry(QtCore.QRect(40, 380, 361, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordField.sizePolicy().hasHeightForWidth())
        self.passwordField.setSizePolicy(sizePolicy)
        self.passwordField.setObjectName("passwordField")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(233, 151, 0);")
        self.label_5.setObjectName("label_5")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(150, 430, 131, 41))
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
        self.registerButton.setGeometry(QtCore.QRect(230, 500, 111, 20))
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
        self.label_7.setGeometry(QtCore.QRect(80, 500, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.forgotPasswordButtonr = QtWidgets.QPushButton(self.centralwidget)
        self.forgotPasswordButtonr.setGeometry(QtCore.QRect(22, 407, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setKerning(True)
        self.forgotPasswordButtonr.setFont(font)
        self.forgotPasswordButtonr.setStyleSheet("QPushButton{\n"
"border-color: rgb(233, 151, 0);\n"
"border:none;\n"
"bordder-radius:12px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(233,151,0)\n"
"}")
        self.exit.clicked.connect(self.close)
        self.forgotPasswordButtonr.setObjectName("forgotPasswordButtonr")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
    def close(self):
        app.quit()
    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login - Artiviewer "))
        self.label_3.setText(_translate("LoginWindow", "Login to Artiviewer"))
        self.label_4.setText(_translate("LoginWindow", "Username"))
        self.label_5.setText(_translate("LoginWindow", "Password"))
        self.loginButton.setText(_translate("LoginWindow", "Login"))
        self.label_6.setText(_translate("LoginWindow", "Artiviewer - 2020"))
        self.exit.setText(_translate("LoginWindow", "X"))
        self.registerButton.setText(_translate("LoginWindow", "Register now"))
        self.label_7.setText(_translate("LoginWindow", "New to Artiviewer?"))
        self.forgotPasswordButtonr.setText(_translate("LoginWindow", "Forgot password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
