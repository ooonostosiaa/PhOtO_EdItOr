# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uic_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.246305 rgba(235, 197, 240, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_red = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_red.setGeometry(QtCore.QRect(30, 10, 113, 32))
        self.pushButton_red.setStyleSheet("font: 13pt \".AppleSystemUIFont\";\n"
"color: rgb(14, 29, 41);")
        self.pushButton_red.setObjectName("pushButton_red")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(MainWindow)
        self.pixmap = QPixmap('')
        self.image = QLabel(self)
        #[eq
        self.image.setGeometry(QtCore.QRect(150, 10, 740, 455))
        self.image.setPixmap(self.pixmap)
        self.label.setGeometry(QtCore.QRect(150, 10, 740, 455))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("orig.png"))
        self.label.setObjectName("label")
        self.pushButton_green = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_green.setGeometry(QtCore.QRect(30, 60, 113, 32))
        self.pushButton_green.setStyleSheet("font: 13pt \".AppleSystemUIFont\";\n"
"color: rgb(13, 23, 35);")
        self.pushButton_green.setObjectName("pushButton_green")
        self.pushButton_blue = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_blue.setGeometry(QtCore.QRect(30, 110, 113, 32))
        self.pushButton_blue.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_blue.setObjectName("pushButton_blue")
        self.pushButton_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_all.setGeometry(QtCore.QRect(30, 160, 113, 32))
        self.pushButton_all.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_all.setObjectName("pushButton_all")
        self.pushButton_bright = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bright.setGeometry(QtCore.QRect(30, 210, 113, 32))
        self.pushButton_bright.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_bright.setObjectName("pushButton_bright")
        self.pushButton_left = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_left.setGeometry(QtCore.QRect(30, 260, 113, 32))
        self.pushButton_left.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_left.setObjectName("pushButton_left")
        self.pushButton_right = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_right.setGeometry(QtCore.QRect(30, 320, 113, 32))
        self.pushButton_right.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_right.setObjectName("pushButton_right")
        self.pushButton_negative = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_negative.setGeometry(QtCore.QRect(30, 380, 113, 32))
        self.pushButton_negative.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_negative.setObjectName("pushButton_negative")
        self.pushButton_wb = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_wb.setGeometry(QtCore.QRect(30, 440, 113, 32))
        self.pushButton_wb.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_wb.setObjectName("pushButton_wb")
        self.pushButton_gray = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gray.setGeometry(QtCore.QRect(30, 490, 113, 32))
        self.pushButton_gray.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_gray.setObjectName("pushButton_gray")
        self.pushButton_sepia = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sepia.setGeometry(QtCore.QRect(180, 490, 113, 32))
        self.pushButton_sepia.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_sepia.setObjectName("pushButton_sepia")
        self.pushButton_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_contrast.setGeometry(QtCore.QRect(330, 490, 113, 32))
        self.pushButton_contrast.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_contrast.setObjectName("pushButton_contrast")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(480, 490, 113, 32))
        self.pushButton_save.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setGeometry(QtCore.QRect(630, 490, 113, 32))
        self.pushButton_download.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_download.setObjectName("pushButton_download")
        self.pushButton_orig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_orig.setGeometry(QtCore.QRect(770, 490, 113, 32))
        self.pushButton_orig.setStyleSheet("color:rgb(11, 13, 31)")
        self.pushButton_orig.setObjectName("pushButton_orig")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KotiKot"))
        self.pushButton_red.setText(_translate("MainWindow", "RED"))
        self.pushButton_green.setText(_translate("MainWindow", "GREEN"))
        self.pushButton_blue.setText(_translate("MainWindow", "BLUE"))
        self.pushButton_all.setText(_translate("MainWindow", "ALL"))
        self.pushButton_bright.setText(_translate("MainWindow", "BRIGHT"))
        self.pushButton_left.setText(_translate("MainWindow", "LEFT"))
        self.pushButton_right.setText(_translate("MainWindow", "RIGHT"))
        self.pushButton_negative.setText(_translate("MainWindow", "NEGATIVE"))
        self.pushButton_wb.setText(_translate("MainWindow", "WB"))
        self.pushButton_gray.setText(_translate("MainWindow", "GRAY"))
        self.pushButton_sepia.setText(_translate("MainWindow", "SEPIA"))
        self.pushButton_contrast.setText(_translate("MainWindow", "CONTRAST"))
        self.pushButton_save.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_download.setText(_translate("MainWindow", "DOWNLOAD"))
        self.pushButton_orig.setText(_translate("MainWindow", "ORIGINAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
