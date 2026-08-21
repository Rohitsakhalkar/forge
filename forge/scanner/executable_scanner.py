from pathlib import Path
from forge.database import Database
from datetime import datetime

class Executable:

    def __init__(self):
        self.db = Database()

    def execute(self,args):
        commands = {
             "scan": self.scan_exe
         }
        command = commands.get(args[0])
        if command:
            command()
        else:
            print("Invalid commnd")

    def scan_exe(self):
        try:
            started_at = datetime.now()
            scannable_paths ={
                "windows" : "C:/Windows",
                "users": "C:/Users",
                "program_files":  "c:/Program Files" ,
                "program_files(x86)" : "C:/Program Files (x86)",
                        }
            apps = self._apps()
            for keys, path in scannable_paths.items():
                path = Path(path)
                for root , dirs, files in path.walk():
                    for file in files:
                        full_path = root/file
                        if full_path.suffix == ".exe":
                            for app_name, exe_name in apps.items():
                                if full_path.name.lower() == exe_name.lower():
                                    self.db.save_exe_paths(app_name,full_path)
            self.db.save_task(started_at, taskname = f"Executed run scan",status = "completed",ended_at = datetime.now())
        except Exception as e:
            self.db.save_task(started_at, taskname = f"Executed run scan",status = "failed",ended_at = datetime.now())
            print(f"Task failed: {e}")

    def _apps(self):
        try:
            db = Database()
            apps = db.load_apps()
            return apps
        except Exception as e:
            print(f"task failed: {e}")         
