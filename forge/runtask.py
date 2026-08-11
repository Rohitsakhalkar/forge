import subprocess
import sys
from datetime import datetime
from .database import Database 
from pathlib import Path

class Runtask():

    def execute(self, args):
        filename = args[0]
        self.run_task(filename)


    def run_task(self, path):
        try:
            exe =Path(path)
            subprocess.Popen([exe],cwd = exe.parent)
        except Exception as e:
            print("Task Failed")
            print(e)

class PythonEnvironment():

    def __init__(self):
        self.tasks = {}

    def execute(self, args):
        commands ={
            "install": self.install_lib,
            "uninstall": self.uninstall_lib
        }
        if args[0] in commands:
             self.install_lib(args)

        else:
            filename = args[0]
            self.exe_files(filename)

    def uninstall_lib(self,args):
        try:
            
            started_at = datetime.now()
            confirmation = input(f"do you want to uninstall{args[1]}?  y/n ")
            if confirmation ==  "y":
                subprocess.run([sys.executable,"-m","pip","uninstall",args[1]],check = True)
                status = "Success"
            else: 
                status = "Failed"
                print("user terminated the process")
            task = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task = {
                "task":task,
                "status":status,
                "started_at":str(started_at),
                "ended_at":str(ended_at),
                "duration": str(duration)
            }
            db = Database()
            db.save_history(self.task)

        except Exception as e:
            print("task failed")
            status = "Failed"
            task = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task = {
                "task":task,
                "status":status,
                "started_at":str(started_at),
                "ended_at":str(ended_at),
                "duration": str(duration)
            }
            db = Database()
            db.save_history(self.task)

    def install_lib(self,args):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","pip","install",args[1]],check = True)
            status = "Success"
            task = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task = {
                "task":task,
                "status":status,
                "started_at":str(started_at),
                "ended_at":str(ended_at),
                "duration": str(duration)
                }
            db = Database()
            db.save_history(self.task)

        except Exception as e:
            print("task failed")
            status = "Failed"
            task = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task = {
                "task":task,
                "status":status,
                "started_at":str(started_at),
                "ended_at":str(ended_at),
                "duration": str(duration)
                }
            db = Database()
            db.save_history(self.task)

    def exe_files(self, filename):
        
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,f"{filename}.py"], check=True )
            status = "Success"
            taskname = f"Executed {filename}"
            ended_at = datetime.now()
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

        except Exception as e:
            taskname = f"Executed {filename}"
            ended_at = datetime.now()
            status = "Failed"
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
            print("Task Failed")
            print(e)

    def savetask(self, data):
       pass

    def loadtask(Self):
       pass