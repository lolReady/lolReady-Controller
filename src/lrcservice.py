import os
import uuid
import asyncio
import functools
import coloredlogs
import logging
import socketio

from PyQt5 import QtCore


class LRCService(QtCore.QObject, socketio.ClientNamespace):
    def __init__(self, origin, ui) -> None:
        super(LRCService, self).__init__()
        coloredlogs.install()
        logging.basicConfig(level=logging.INFO)

        self.origin = origin
        self.ui = ui
        self.uuid = None

        if not os.path.exists(".uuid"):
            self.writeUUID()
        else:
            self.readUUID()

    def readUUID(self):
        with open(".uuid", "r") as f:
            self.uuid = f.read()

    def writeUUID(self):
        with open(".uuid", "w") as f:
            f.write(str(uuid.uuid4()))

    def startAsyncClient(self):
        sio = socketio.AsyncClient()

        def showMessageOrError(argument):
            def decorator(func):
                @functools.wraps(func)
                async def wrapper(*args, **kwargs):
                    sid = sio.get_sid()
                    data = args[0]
                    eventname = argument[0]
                    msg = argument[1]

                    log_str = f"LRC_SERVICE({sid}):{eventname}:{data['method']}:{data['action']} - "

                    if data["error"]:
                        log_str += data["error"]
                    else:
                        log_str += msg

                    logging.info(log_str)
                    return await func(*args, **kwargs)
                return wrapper
            return decorator

        @sio.event
        def connect(*args, **kwargs):
            logging.info(f"LRC_SERVICE:CONNECT - ESTABLISHED")

        @sio.event
        def disconnect(*args, **kwargs):
            logging.info(
                f"LRC_SERVICE:DISCONNECT - DISCONNECTED FROM SERVER")

        @sio.event
        def login(*args, **kwargs):
            pass

        @sio.event
        def logout(*args, **kwargs):
            pass

        @sio.event
        async def login_resp(*args, **kwargs):
            data = args[0]

            if data["error"]:
                logging.error(f"LRC_SERVICE:LOGIN_RESPONSE - {data['error']}")
                return

            logging.info(f"LRC_SERVICE:LOGIN_RESPONSE - SUCCESSFULL")
            self.ui.setQr(data["room"])

        @sio.event
        async def logout_resp(*args, **kwargs):
            pass

        @sio.event
        async def ping(*args, **kwargs):
            data = args[0]
            response = {**data}
            response["method"] = "RESPONSE"

            await sio.emit("ping_resp", response)

        @sio.event
        async def ping_resp(*args, **kwargs):
            pass

        async def start():
            await sio.connect(self.origin)
            await sio.emit("login", {"room": self.uuid})
            await sio.wait()

        asyncio.run(start())
