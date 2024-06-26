# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 613)
        MainWindow.setStyleSheet("")
        self.autostart = QtWidgets.QWidget(MainWindow)
        self.autostart.setObjectName("autostart")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.autostart)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 0, 351, 183))
        self.calendarWidget.setStyleSheet("font: 8pt \"MS Reference Specialty\";")
        self.calendarWidget.setObjectName("calendarWidget")
        self.checkBox = QtWidgets.QCheckBox(self.autostart)
        self.checkBox.setGeometry(QtCore.QRect(40, 110, 77, 17))
        self.checkBox.setObjectName("checkBox")
        self.start_btn = QtWidgets.QPushButton(self.autostart)
        self.start_btn.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.autostart)
        self.stop_btn.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.stop_btn.setStyleSheet("font: 8pt \"MS Reference Specialty\";\n"
"font: 8pt \"Ravie\";")
        self.stop_btn.setObjectName("stop_btn")
        self.video = QVideoWidget(self.autostart)
        self.video.setGeometry(QtCore.QRect(20, 190, 501, 311))
        self.video.setObjectName("video")
        MainWindow.setCentralWidget(self.autostart)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "memorycalendar"))
        self.checkBox.setText(_translate("MainWindow", "Автостарт"))
        self.start_btn.setText(_translate("MainWindow", "Старт"))
        self.stop_btn.setText(_translate("MainWindow", "Стоп"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
