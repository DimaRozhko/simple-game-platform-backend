import json
import random
import uuid
from datetime import datetime


class Domain:

    def __init__(self):
        self.R = random.randint(0, 1000)

    def do(self):
        return json.dumps({"customer_id_logged_in": str(uuid.uuid4())})

    def start_game(self, id):
        return json.dumps({
            "customer_id_logged_in": id,
            "start_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    def enrich_data_log_in(self, inputJson):
        jsonData = json.loads(inputJson)
        if jsonData["customer_id_logged_in"]:
            return json.dumps({
                "is_enriched": True,
                "operation_name": "LOG_IN",
                "data_operation": jsonData["customer_id_logged_in"],
                "result_operation": "User id=" + jsonData["customer_id_logged_in"] + " logged in",
                "customer_id_logged_in": jsonData["customer_id_logged_in"],
                "end_operation_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            })
        return inputJson

    def enrich_data_start_game(self, inputJson):
        jsonData = json.loads(inputJson)
        if jsonData["customer_id_logged_in"] and jsonData["start_time"]:
            return json.dumps({
                "is_enriched": True,
                "operation_name": "START_GAME",
                "data_operation": jsonData["start_time"],
                "result_operation": "User id=" + jsonData["customer_id_logged_in"] + " started game at " + jsonData["start_time"],
                "customer_id_logged_in": jsonData["customer_id_logged_in"],
                "start_time": jsonData["start_time"],
                "end_operation_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            })
        return inputJson
