import json
import time
from channels.generic.websocket import WebsocketConsumer
from fifteen.business import Domain


class OneConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        D = Domain()
        for i in range(100):
            data = D.do()
            self.send(data)
            time.sleep(2)
            data = D.start_game(json.loads(data)["customer_id_logged_in"])
            self.send(data)
            time.sleep(5)
