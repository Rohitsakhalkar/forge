import json
from pathlib import Path

class Cleaner:

    def execute(self,args):
        self.clean_history()

    def clean_history(self):
        root = Path(__file__).resolve().parent
        DATABASEJSON = Path(f"{root}/database/history.json")
        data ={}
        with DATABASEJSON.open("w") as f:
            json.dump(data, f)