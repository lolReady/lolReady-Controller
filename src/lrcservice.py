from cmath import log
import os
import uuid
import asyncio
import functools
import logging
import socketio

from PyQt5 import QtCore

import lrclistener


class LRCService(QtCore.QObject, socketio.ClientNamespace):
    def __init__(self, origin, ui) -> None:
        super(LRCService, self).__init__()

        self.origin = origin
        self.ui = ui
        self.token = None

        if not os.path.exists(".token"):
            self.writeToken()
        else:
            self.readToken()

    def readToken(self):
        with open(".token", "r") as f:
            self.token = f.read()

    def writeToken(self):
        with open(".token", "w") as f:
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
            args = args[0]
            resp = await self.listener.request(**args)
            response = await resp.json()
            print(response)
            await sio.emit("ping_resp", {"room": args["room"], "data": response})

        @sio.event
        async def ping_resp(*args, **kwargs):
            pass

        @sio.event
        async def subscribe(*args, **kwargs):
            await self.listener.subscribe(*args, **kwargs)

        @sio.event
        async def subscribe_resp(*args, **kwargs):
            print(args)

        @sio.event
        async def unsubscribe(*args, **kwargs):
            await self.listener.unsubscribe(*args, **kwargs)

        @sio.event
        async def unsubscribe_resp(*args, **kwargs):
            print(args)

        async def start():
            self.listener = await lrclistener.LRCListener.start()
            self.listener.sio = sio
            await sio.connect(self.origin)
            await sio.emit("login", {"room": self.token})
            await sio.wait()

        asyncio.run(start())
