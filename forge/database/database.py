import json
from pathlib import Path

class Database():
    def __init__(self):
        self.HISTORYJSON = Path(__file__).parent/"history.json"

    def save_history(self,data):

        try:
            previous_data = self.load_history()
            task_id = max(map(int,previous_data.keys()),default = 0)
            previous_data[task_id + 1 ] = data
            with self.HISTORYJSON.open("w") as f:
                json.dump(previous_data, f, indent = 4)
        except FileNotFoundError:
            raise FileNotFoundError("must be the wind")

    def load_history(self):
        try:
            with self.HISTORYJSON.open("r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            raise FileNotFoundError("must be the wind")