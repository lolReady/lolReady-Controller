from flask import Flask, request

from PyQt5 import QtCore

app = Flask(__name__)


class LRCServer(QtCore.QObject):
    def __init__(self, *args, **kwargs) -> None:
        super(LRCServer, self).__init__()
        self.app = Flask(__name__)
        self.ui = args[0]

        self.app.add_url_rule(
            "/", "index", self.index
        )

        self.app.add_url_rule(
            "/createqr", "createqr", self.createqr
        )

        self.app.add_url_rule(
            "/opensession", "opensession", self.opensession
        )

    def start(self):
        self.app.run()

    def index(self):
        return ""

    # TODO make this function in gui
    def createqr(self):
        import json
        import qrcode

        data = json.dumps(request.json)

        if data == "{}":
            return "Error"

        qr = qrcode.QRCode(box_size=10, border=3)
        qr.add_data(data)
        qr.make(fit=True)
        qrfile = qr.make_image()

        self.ui.setQr(qrfile)

        return "Done"

    def opensession(self):
        return "0"
