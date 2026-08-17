import json
from pathlib import Path

class Database():
    def __init__(self):
        self.parent = Path(__file__).parent
        self.HISTORYJSON = self.parent/"history.json"
        self.APPSJSON = self.parent/"apps.json"
        self.EXEJSON = self.parent/"exe.json"

    def save_history(self,data):

        try:
            previous_data = self.load_history()
            task_id = max(map(int,previous_data.keys()),default = 0)
            previous_data[task_id + 1 ] = data
            with self.HISTORYJSON.open("w") as f:
                json.dump(previous_data, f, indent = 4)
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name history.json")

    def load_history(self):
        try:
            with self.HISTORYJSON.open("r") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name history.json")

    def save_apps(self, data):
        try:
            previous_data = self.load_apps()
            previous_data[str(data["appname"])] = data["appexe"]
            with self.APPSJSON.open('w') as f:
                json.dump(previous_data,f, indent = 4) 
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name apps.json")

    def load_apps(self):
        try:
            with self.APPSJSON.open('r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name apps.json")

    def save_altered_data(self,data):
        try:
            with self.APPSJSON.open('w') as f:
                json.dump(data, f, indent = 4)
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name apps.json")

    def save_exe_paths(self,appname,path):
        try:
            if not self.EXEJSON.exists():
                Path(self.EXEJSON.parent).touch("exe.json")
            data = self.load_exe_data()
            data[str(appname)] = str(path)
            with self.EXEJSON.open('w') as f:
                json.dump(data, f, indent = 4)
        except Exception as e:
            # raise FileNotFoundError("create a json file in database with name exe.json")
            print(e)

    def load_exe_data(self):
        try: 
            with self.EXEJSON.open('r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            raise FileNotFoundError("create a json file in database with name exe.json")

    def save_task(self, started_at, taskname, status, ended_at):
        duration = ended_at - started_at
        self.task ={
                    "task": taskname,
                    "started_at":str(started_at),
                    "ended_at": str(ended_at),
                    "status": status,
                    "duration": str(duration)
                }
        self.save_history(self.task)