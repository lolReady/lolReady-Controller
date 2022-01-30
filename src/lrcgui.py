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

    def setQr(self, data):
        import qrcode
        import json
        data = json.dumps(data)
        qr = qrcode.QRCode(box_size=10, border=3)
        qr.add_data(data)
        qr.make(fit=True)
        qrfile = qr.make_image()

        qrimg = QtGui.QPixmap.fromImage(ImageQt.ImageQt(qrfile))
        qrres = QtGui.QPixmap(qrimg)
        self.ui.LRC_qr.clear()
        self.ui.LRC_qr.setPixmap(qrres)

        # TODO: remove this
        self.ui.LRC_qr.setScaledContents(True)
