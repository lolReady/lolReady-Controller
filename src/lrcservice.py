import functools
import coloredlogs
import logging
import asyncio
import socketio

sio = socketio.AsyncClient()

host = "wss://lolready-server.herokuapp.com/"


coloredlogs.install()
logging.basicConfig(level=logging.INFO)


def showMessageOrError(argument):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            sid = sio.get_sid()
            response = args[0]
            method = argument[0]
            msg = argument[1]
            error = None

            if len(response.items()) == 1:
                error = response["error"]

            if error:
                logging.error(f"LRC_SERVICE:{method} - SID[{sid}] - {error}")
            else:
                logging.info(f"LRC_SERVICE:{method} - SID[{sid}] - {msg}")
            return await func(*args, **kwargs)
        return wrapper
    return decorator


@sio.event
async def connect(*args, **kwargs):
    logging.info(f"LRC_SERVICE:CONNECT - ESTABLISHED")


@sio.event
async def disconnect(*args, **kwargs):
    logging.info(f"LRC_SERVICE:DISCONNECT - DISCONNECTED FROM SERVER")


@sio.event
@showMessageOrError(["LOGIN", "ESTABLISHED"])
async def login_resp(*args, **kwargs):
    pass


@sio.event
@showMessageOrError(["LOGOUT", "ESTABLISHED"])
async def logout_resp(*args, **kwargs):
    pass


async def main():
    await sio.connect(host)
    await sio.emit("login", {"room": 123})
    await sio.wait()

if __name__ == "__main__":
    asyncio.run(main())
