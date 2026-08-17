import subprocess
import sys
from datetime import datetime
from forge.database import Database 
from pathlib import Path


class Runtask():
    def __init__(self):
        self.db = Database()

    def execute(self, args):
        self.run_task(args[1])


    def run_task(self, task):
        try:
            apps = self.db.load_exe_data()            
            for app, path in apps.items():
                    if task == app:
                        exe = Path(path)
                        subprocess.Popen([exe],cwd = exe.parent)

        except Exception as e:
            print("Task Failed")
            print(e)


   
