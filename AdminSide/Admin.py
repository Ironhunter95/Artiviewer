
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from Admin_ui_main import AdminUIMain

# IMPORT QSS CUSTOM
from Admin_ui_styles import AdminStyles

# IMPORT FUNCTIONS
from Admin_ui_functions import *

#App Functions
from Admin_app_functions import *

class AdminWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = AdminUIMain()
        self.ui.setupUi(self)

        #Remove standard title bar
        AdminUIFunctions.removeTitleBar(True)

        #Set Window title
        self.setWindowTitle('Artiviewer - Admin')
        AdminUIFunctions.labelTitle(self, 'Artiviewer - Admin')
        AdminUIFunctions.labelDescription(self, 'Admin')

        # Default window size
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)

        # Toggle Menu size
        self.ui.btn_toggle_menu.clicked.connect(lambda: AdminUIFunctions.toggleMenu(self, 220, True))

        #Add Custome menu
        self.ui.stackedWidget.setMinimumWidth(20)
        AdminUIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        AdminUIFunctions.addNewMenu(self, "User Search", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        AdminUIFunctions.addNewMenu(self, "Settings", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        # Start menu selection
        AdminUIFunctions.selectStandardMenu(self, "btn_home")
        #Start page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        # Show User icon
        AdminUIFunctions.userIcon(self, "MA", "", True)
        def moveWindow(event):
            # If maximized change to normal
            if AdminUIFunctions.returnStatus() == 1:
                AdminUIFunctions.maximize_restore(self)

            # Move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        #LOAD DEFINITIONS
        AdminUIFunctions.uiDefinitions(self)

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        ## SHOW MAIN WINDOW
        self.show()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            AdminUIFunctions.resetStyle(self, "btn_home")
            AdminUIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(AdminUIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            AdminUIFunctions.resetStyle(self, "btn_new_user")
            AdminUIFunctions.labelPage(self, "Search for User")
            btnWidget.setStyleSheet(AdminUIFunctions.selectMenu(btnWidget.styleSheet()))


    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    ## EVENT ==> MOUSE CLICK
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ## EVENT ==> KEY PRESSED
    def keyPressEvent(self, event):
        pass

    ## EVENT ==> RESIZE EVENT
    def resizeEvent(self, event):
        return super(AdminWindow, self).resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = AdminWindow()
    sys.exit(app.exec_())
