from datetime import datetime
import sys
from forge.database import Database
from pathlib import Path
import subprocess


class PythonEnvironment():

    def __init__(self):
        self.tasks = {}
        self.db = Database()

    def execute(self, command, *args):
        commands ={
            "install": self.install_lib,
            "uninstall": self.uninstall_lib,
            "upgrade": self.upgrade_lib,
            "venv": self.create_venv,
            "run" : self.exe_files
        }
        command = commands.get(command)
        
        if command:
            command(*args)
        else:
           print("Invalid command")

    def create_venv(self, path):
        try:
            path = f"{path}"
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","venv",path],check = True)
            self.db.save_task(started_at, taskname = f"Executed{path}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print("Task failed")
            print(e)
            self.db.save_task(started_at, taskname = f"Executed{path}", status = "failed", ended_at = datetime.now())
            

    def upgrade_lib(self , library):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable, "-m","pip","install","--upgrade",library],check = True)
            self.db.save_task(started_at, taskname = f"Executed{library}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            print("task failed")
            print(e)
            self.db.save_task(started_at, taskname = f"Executed{library}", status = "failed", ended_at = datetime.now())

    def uninstall_lib(self, library):
        try:
            started_at = datetime.now()
            confirmation = input(f"do you want to uninstall{library}?  y/n ").lower()
            if confirmation ==  "y":
                result = subprocess.run([sys.executable,"-m","pip","uninstall",library],check = True)
                self.db.save_task(started_at, taskname = f"Executed{library}", status = "Completed", ended_at = datetime.now())
            else: 
                self.db.save_task(started_at, taskname = f"Executed{library}", status = "terminated", ended_at = datetime.now())
                print("user terminated the process")
            

        except Exception as e:
            print("task failed")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def install_lib(self, library):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","pip","install",library],check = True)
            self.db.save_task(started_at, taskname = f"Executed{library}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            self.db.save_task(started_at, taskname = f"Executed{library}", status = "failed", ended_at = datetime.now())
            print(f"task failed: {e}")
           
            

    def exe_files(self, path):
        
        try:
            path = Path(path)
            started_at = datetime.now()
            subprocess.run([sys.executable,f"{path}"], check=True )
            self.db.save_task(started_at, taskname = f"Executed:{path}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            self.db.save_task(started_at, taskname = f"Executed:{path}", status = "failed", ended_at = datetime.now())
            print(f"Task Failed{e}")
            

