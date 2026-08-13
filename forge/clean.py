import json

class Cleaner:

    def execute(self,args):
        self.clean_history()

    def clean_history(self):
        data ={}
        with open("database/history.json","w") as f:
            json.dump(data, f)