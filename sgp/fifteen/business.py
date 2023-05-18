#business.py

import json
#pip install random_word
# from random_word import RandomWords
import random
import uuid
from datetime import datetime


class Domain:

    def __init__(self):
        # self.R = RandomWords()
        self.R = random.randint(0, 1000)

    def do(self):
        id = str(uuid.uuid4())
        return json.dumps({"customer_id_logged_in": id})

    def start_game(self, id):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return json.dumps({
            "customer_id_logged_in": id,
            "start_time": now
        })
