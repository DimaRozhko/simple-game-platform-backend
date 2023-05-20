import json
import time
from channels.generic.websocket import WebsocketConsumer
from admininfo.business import Domain
from send_mail_app.tasks import send_mail_message_subject_func


class OneConsumer(WebsocketConsumer):

    def send_email(self, jsonData):
        send_mail_message_subject_func("[" + jsonData["operation_name"] + "] - " + jsonData["data_operation"],
                                       jsonData["result_operation"])

    def connect(self):
        self.accept()
        D = Domain()
        for i in range(100):
            data = D.do()
            self.send(data)
            data = D.enrich_data_log_in(data)
            jsonData = json.loads(data)
            self.send_email(jsonData)
            self.send(data)
            time.sleep(2)
            data = D.start_game(json.loads(data)["customer_id_logged_in"])
            self.send(data)
            data = D.enrich_data_start_game(data)
            jsonData = json.loads(data)
            self.send_email(jsonData)
            self.send(data)
            time.sleep(5)
