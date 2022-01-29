import sys

from PIL import ImageQt

from PyQt5 import QtWidgets, QtCore, QtGui

from design import lrc


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui = lrc.Ui_LRC_MainWindow()

        self.ui.setupUi(self)
        self.show()

    def setQr(self, qrfile):
        qrimg = QtGui.QPixmap.fromImage(ImageQt.ImageQt(qrfile))
        qrfile = QtGui.QPixmap(qrimg)
        self.ui.LRC_qr.clear()
        self.ui.LRC_qr.setPixmap(qrfile)

        # TODO: remove this
        self.ui.LRC_qr.setScaledContents(True)
