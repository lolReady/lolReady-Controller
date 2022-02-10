import os
import sys
import logging
import coloredlogs
import easygui

from PyQt5 import QtWidgets, QtCore

import lrcgui
import lrcservice

ORIGIN_SERVER="wss://lolready-server.herokuapp.com"


def start(app):
    sys.exit(app.exec_())


if __name__ == "__main__":
    coloredlogs.install()
    logging.basicConfig(level=logging.INFO)

    app = QtWidgets.QApplication(sys.argv)
    ui = lrcgui.Ui()

    lrcservice_thread = QtCore.QThread()
    service = lrcservice.LRCService(ORIGIN_SERVER, ui)
    service.moveToThread(lrcservice_thread)
    lrcservice_thread.started.connect(service.startAsyncClient)
    lrcservice_thread.start()

    start(app)
