import sys

from PyQt5 import QtWidgets, QtCore

import lrcgui
import lrcserver


def start(app):
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = lrcgui.Ui()

    lrcserver_thread = QtCore.QThread()

    server = lrcserver.LRCServer(window)

    server.moveToThread(lrcserver_thread)

    lrcserver_thread.started.connect(server.start)

    lrcserver_thread.start()

    start(app)
