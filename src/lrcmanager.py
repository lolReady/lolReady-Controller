import os
import sys

from PyQt5 import QtWidgets, QtCore

import lrcgui
import lrcservice


def start(app):
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = lrcgui.Ui()

    lrcservice_thread = QtCore.QThread()
    service = lrcservice.LRCService(os.environ["ORIGIN_SERVER"], ui)
    service.moveToThread(lrcservice_thread)
    lrcservice_thread.started.connect(service.startAsyncClient)
    lrcservice_thread.start()

    start(app)
