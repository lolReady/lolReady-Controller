import os
import sys
import logging
import coloredlogs
import easygui

from PyQt5 import QtWidgets, QtCore

import lrcgui
import lrcservice

CLIENT_PATH = "C:\\Riot Games\\League of Legends"


def getLockfile():
    global CLIENT_PATH
    if not os.path.exists(CLIENT_PATH):
        msg = f"{CLIENT_PATH} doesn't exists"
        logging.info(msg)
        easygui.msgbox(msg)
        CLIENT_PATH = easygui.diropenbox()

    lockfile_path = CLIENT_PATH + "\\lockfile"
    while not os.path.exists(lockfile_path):
        msg = "LRC_MANAGER - Please open the League of Legends"
        logging.info(msg)
        c = easygui.boolbox(msg,
                            choices=("Retry", "Cancel"))

        if not c:
            break

    try:
        with open(lockfile_path, "r") as f:
            return dict(
                zip(["process", "pid", "port", "password", "protocol"],
                    f.read().split(":"))
            )
    except Exception as e:
        logging.error(f"LRC_MANAGER - {str(e)}")


def start(app):
    sys.exit(app.exec_())


if __name__ == "__main__":
    coloredlogs.install()
    logging.basicConfig(level=logging.INFO)

    app = QtWidgets.QApplication(sys.argv)
    ui = lrcgui.Ui()

    lrcservice_thread = QtCore.QThread()
    service = lrcservice.LRCService(os.environ["ORIGIN_SERVER"], ui)
    service.moveToThread(lrcservice_thread)
    lrcservice_thread.started.connect(service.startAsyncClient)
    lrcservice_thread.start()

    start(app)
