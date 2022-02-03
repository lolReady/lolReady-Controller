from email.mime import base
import os
import logging
from pprint import pprint
import psutil
import aiohttp
import asyncio
import websockets
import ssl
import pathlib
import json
import aioconsole

import requests


class LRCListener:
    @staticmethod
    async def start():
        self = LRCListener()
        self.sio = None
        self.room = None
        self.subscriber = []
        self.events = []

        league_client_process = None
        while True:
            for process in psutil.process_iter():
                if process.name() in ["LeagueClientUx.exe", "LeagueClientUx"]:
                    league_client_process = process
                    break

            if league_client_process:
                break

            logging.warning(
                "LeagueClient not working. Please (re)start LeagueClient")
            await asyncio.sleep(1)

        league_client_process_args = {}
        for process_arg in league_client_process.cmdline():
            if "=" in process_arg:
                key, value = process_arg[2:].split("=")
                league_client_process_args[key] = value

        self._app_username = "riot"
        self._app_name = league_client_process_args["app-name"]
        self._app_path = league_client_process_args["install-directory"]
        self._app_pid = int(league_client_process_args["app-pid"])
        self._app_port = int(league_client_process_args["app-port"])
        self._app_auth_token = league_client_process_args["remoting-auth-token"]
        self._app_url = f"{self._app_username}:{self._app_auth_token}@127.0.0.1:{self._app_port}"
        self._app_auth = aiohttp.BasicAuth(
            self._app_username, self._app_auth_token)
        self._app_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.session = aiohttp.ClientSession(
            auth=self._app_auth)
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        pem = pathlib.Path(__file__).with_name("riotgames.pem")
        self.ssl_context.load_verify_locations(pem)

        await self.create_websocket()
        print(self._app_url)
        return self

    async def create_websocket(self):
        self.ws = await websockets.connect(
            "wss://"+self._app_url, ssl=self.ssl_context)

        await self.ws.send("[5, \"OnJsonApiEvent\"]")

        async def eventLoop(self):
            async for msg in self.ws:
                try:
                    if msg:
                        if "data" in msg:
                            i = msg.index("data")
                            c = msg[i-2:-1]
                            d = json.loads(c)
                            if d["uri"] in self.events and self.room:
                                await self.sio.emit("subscribe_resp", {"room": self.room, **d})

                except websockets.exceptions.ConnectionClosed as e:
                    logging.error(str(e))

        asyncio.create_task(eventLoop(self))

    async def subscribe(self, *args, **kwargs):
        room, data = args[0].values()

        if not self.room:
            self.room = room

        for event in data:
            if event not in self.events:
                self.events.append(event)

    async def unsubscribe(self, *args, **kwargs):
        room, data = args[0].values()

        if not self.room:
            self.room = room

        for event in data:
            if event in self.events:
                del self.events[self.events.index(event)]

    async def request(self, **kwargs):
        if not self.session:
            return

        method = kwargs["method"]
        endpoint = kwargs["endpoint"]
        query = None
        data = None

        values = kwargs.keys()

        if "query" in values:
            query = kwargs["query"]

        if "data" in values:
            data = kwargs["data"][0]

        return await self.session.request(method=method, url=f"https://{self._app_url}{endpoint}{'?='+query if query else ''}", json=data, ssl=self.ssl_context)


async def run():
    global lis
    lis = await LRCListener.start()

    events = {
    }

    currently = []

    while True:
        cmd = await aioconsole.ainput(">>>")

        if "set" in cmd:
            event = cmd.split()[1]
            events[event] = True

        elif "events" in cmd:
            pprint(events)
        elif "currently" in cmd:
            pprint(currently)
        elif "del" in cmd:
            event = cmd.split()[1]
            if event in events.keys():
                events[event] = False
        else:
            print("Command not defined")

        for e in events.keys():
            if events[e] and (e not in currently):
                currently.append(e)
                await lis.ws.send(f"[5, \"{e}\"]")

            if not events[e] and (e in currently):
                i = currently.index(e)
                del currently[i]
                await lis.ws.send(f"[6, \"{e}\"]")

        await asyncio.sleep(0.5)


"""
if __name__ == "__main__":
    import aioconsole
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(start())
"""
