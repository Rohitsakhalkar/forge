import subprocess
from forge.database import Database 
from pathlib import Path
from datetime import datetime

class Runtask():
    def __init__(self):
        self.db = Database()

    def execute(self, args):
        self.run_task(args[1])


    def run_task(self, task):
        try:
            started_at = datetime.now()
            apps = self.db.load_exe_data()            
            for app, path in apps.items():
                    if task == app:
                        exe = Path(path)
                        subprocess.Popen([exe],cwd = exe.parent)
            self.db.save_task(started_at, taskname = f"Executed run {task}",status = "completed",ended_at = datetime.now())

        except Exception as e:
            self.db.save_task(started_at, taskname = f"Executed run {task}",status = "failed",ended_at = datetime.now())
            print(f"Task Failed: {e}")


   
