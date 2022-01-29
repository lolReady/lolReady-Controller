# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/lrc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from design import lrc_assets_rc

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LRC_MainWindow(object):
    def setupUi(self, LRC_MainWindow):
        LRC_MainWindow.setObjectName("LRC_MainWindow")
        LRC_MainWindow.resize(956, 540)
        LRC_MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        LRC_MainWindow.setAutoFillBackground(False)
        self.LRC_MainWidget = QtWidgets.QWidget(LRC_MainWindow)
        self.LRC_MainWidget.setObjectName("LRC_MainWidget")
        self.LRC_MainFrame = QtWidgets.QFrame(self.LRC_MainWidget)
        self.LRC_MainFrame.setGeometry(QtCore.QRect(20, 20, 921, 451))
        self.LRC_MainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LRC_MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LRC_MainFrame.setObjectName("LRC_MainFrame")
        self.LRC_LeftFrame = QtWidgets.QFrame(self.LRC_MainFrame)
        self.LRC_LeftFrame.setGeometry(QtCore.QRect(20, 30, 361, 381))
        self.LRC_LeftFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LRC_LeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LRC_LeftFrame.setObjectName("LRC_LeftFrame")
        self.LRC_Banner = QtWidgets.QLabel(self.LRC_LeftFrame)
        self.LRC_Banner.setGeometry(QtCore.QRect(0, 0, 361, 381))
        self.LRC_Banner.setStyleSheet("border-image: url(:/lrc_assets_img/img/banner.jpg);\n"
                                      "border-top-left-radius: 50px;\n"
                                      "border-bottom-left-radius: 50px;\n"
                                      "alternate-background-color: rgb(7, 7, 7);")
        self.LRC_Banner.setText("")
        self.LRC_Banner.setObjectName("LRC_Banner")
        self.LRC_RightFrame = QtWidgets.QFrame(self.LRC_MainFrame)
        self.LRC_RightFrame.setEnabled(True)
        self.LRC_RightFrame.setGeometry(QtCore.QRect(380, 30, 521, 381))
        self.LRC_RightFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LRC_RightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LRC_RightFrame.setObjectName("LRC_RightFrame")
        self.LRC_Banner_2 = QtWidgets.QLabel(self.LRC_RightFrame)
        self.LRC_Banner_2.setGeometry(QtCore.QRect(0, 0, 521, 381))
        self.LRC_Banner_2.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                                        "border-top-right-radius: 50px;\n"
                                        "border-bottom-right-radius: 50px;\n"
                                        "")
        self.LRC_Banner_2.setText("")
        self.LRC_Banner_2.setObjectName("LRC_Banner_2")
        self.LRC_qr = QtWidgets.QLabel(self.LRC_RightFrame)
        self.LRC_qr.setGeometry(QtCore.QRect(180, 90, 181, 181))
        self.LRC_qr.setMaximumSize(QtCore.QSize(181, 181))
        self.LRC_qr.setStyleSheet("")
        self.LRC_qr.setText("")
        self.LRC_qr.setScaledContents(True)
        self.LRC_qr.setObjectName("LRC_qr")
        self.LRC_qr_header = QtWidgets.QLabel(self.LRC_RightFrame)
        self.LRC_qr_header.setGeometry(QtCore.QRect(30, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Friz Quadrata")
        font.setPointSize(23)
        font.setItalic(False)
        self.LRC_qr_header.setFont(font)
        self.LRC_qr_header.setStyleSheet("color: rgb(255, 255, 255);")
        self.LRC_qr_header.setObjectName("LRC_qr_header")
        self.LRC_qr_step1 = QtWidgets.QLabel(self.LRC_RightFrame)
        self.LRC_qr_step1.setGeometry(QtCore.QRect(20, 300, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Friz Quadrata")
        font.setPointSize(11)
        font.setItalic(False)
        self.LRC_qr_step1.setFont(font)
        self.LRC_qr_step1.setStyleSheet("color: rgb(255, 255, 255);")
        self.LRC_qr_step1.setObjectName("LRC_qr_step1")
        self.LRC_qr_step2 = QtWidgets.QLabel(self.LRC_RightFrame)
        self.LRC_qr_step2.setGeometry(QtCore.QRect(20, 330, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Friz Quadrata")
        font.setPointSize(11)
        self.LRC_qr_step2.setFont(font)
        self.LRC_qr_step2.setStyleSheet("color: rgb(255, 255, 255);")
        self.LRC_qr_step2.setObjectName("LRC_qr_step2")
        self.LRC_TitleBar = QtWidgets.QFrame(self.LRC_MainFrame)
        self.LRC_TitleBar.setGeometry(QtCore.QRect(59, 30, 801, 31))
        self.LRC_TitleBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LRC_TitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LRC_TitleBar.setObjectName("LRC_TitleBar")
        LRC_MainWindow.setCentralWidget(self.LRC_MainWidget)

        self.retranslateUi(LRC_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(LRC_MainWindow)

    def retranslateUi(self, LRC_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        LRC_MainWindow.setWindowTitle(_translate(
            "LRC_MainWindow", "LolReady - Controller"))
        self.LRC_qr_header.setText(_translate(
            "LRC_MainWindow", "To use LoLReady "))
        self.LRC_qr_step1.setText(_translate(
            "LRC_MainWindow", "1.Open LoLReady App on your phone"))
        self.LRC_qr_step2.setText(_translate(
            "LRC_MainWindow", "2.Point your phone to this screen to capture the code"))
