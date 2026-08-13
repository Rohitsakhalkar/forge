from datetime import datetime
import sys
from forge.database import Database
import subprocess


class PythonEnvironment():

    def __init__(self):
        self.tasks = {}

    def execute(self, args):
        commands ={
            "install": self.install_lib,
            "uninstall": self.uninstall_lib,
            "upgrade": self.upgrade_lib
        }
        command = commands.get(args[0])
        
        if command:
            command(args)
        else:
            filename = args[0]
            self.exe_files(filename)

    def upgrade_lib(self , args):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable, "-m","pip","install","--upgrade",args[1]],check = True)
            status = "success"
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)
        except Exception as e:
            print("task failed")
            status = "Failed"
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)
            pass

    def uninstall_lib(self,args):
        try:
            started_at = datetime.now()
            confirmation = input(f"do you want to uninstall{args[1]}?  y/n ").lower()
            if confirmation ==  "y":
                result = subprocess.run([sys.executable,"-m","pip","uninstall",args[1]],check = True)
                status = "Success"
            else: 
                status = "terminated"
                print("user terminated the process")
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)

        except Exception as e:
            print("task failed")
            status = "Failed"
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)

    def install_lib(self,args):
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,"-m","pip","install",args[1]],check = True)
            status = "Success"
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)

        except Exception as e:
            status = "Failed"
            taskname = f"Executed {args}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)
            print("task failed")
            print(e)
            

    def exe_files(self, filename):
        
        try:
            started_at = datetime.now()
            subprocess.run([sys.executable,f"{filename}.py"], check=True )
            status = "Success"
            taskname = f"Executed {filename}"
            ended_at = datetime.now()
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)

        except Exception as e:
            taskname = f"Executed {filename}"
            ended_at = datetime.now()
            status = "Failed"
            duration = ended_at - started_at
            self.task_save(taskname, status, started_at, ended_at, duration)
            print("Task Failed")
            print(e)

    def task_save(self,taskname,status,started_at,ended_at,duration):
        self.task = {
            "task":taskname,
            "status":status,
            "started_at":str(started_at),
            "ended_at":str(ended_at),
            "duration": str(duration)
                    }
        db = Database()
        db.save_history(self.task)