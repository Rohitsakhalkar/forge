from datetime import datetime
import sys
from forge.database import Database
import subprocess
import os

class PythonEnvironment():

    def __init__(self):
        self.tasks = {}

    def execute(self, args):
        commands ={
            "install": self.install_lib,
            "uninstall": self.uninstall_lib,
            "upgrade": self.upgrade_lib,
            "venv": self.create_venv
        }
        command = commands.get(args[1])
        
        if command:
            command(args)
        else:
            filename = args[1]
            self.exe_files(filename)

    def create_venv(self, args):
        try:
            path = f"{os.getcwd()}/{args[2]}"
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","venv",path],check = True)
            self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print("Task failed")
            print(e)
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())
            

    def upgrade_lib(self , args):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable, "-m","pip","install","--upgrade",args[2]],check = True)
            self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            print("task failed")
            print(e)
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def uninstall_lib(self,args):
        try:
            started_at = datetime.now()
            confirmation = input(f"do you want to uninstall{args[2]}?  y/n ").lower()
            if confirmation ==  "y":
                result = subprocess.run([sys.executable,"-m","pip","uninstall",args[1]],check = True)
                self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
            else: 
                self.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())
                print("user terminated the process")
            

        except Exception as e:
            print("task failed")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def install_lib(self,args):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","pip","install",args[2]],check = True)
            self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())
            print("task failed")
            print(e)
            

    def exe_files(self, filename):
        
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,f"{filename}.py"], check=True )
            self.save_task(started_at, taskname = f"Executed:{filename}", status = "Completed", ended_at = datetime.now())

        except Exception as e:
            self.save_task(started_at, taskname = f"Executed:{filename}", status = "failed", ended_at = datetime.now())
            print("Task Failed")
            print(e)

    def save_task(self, started_at, taskname ,status ,ended_at):
        duration = ended_at - started_at
        self.task = {
            "task":taskname,
            "status":status,
            "started_at":str(started_at),
            "ended_at":str(ended_at),
            "duration": str(duration)
                    }
        db = Database()
        db.save_history(self.task)