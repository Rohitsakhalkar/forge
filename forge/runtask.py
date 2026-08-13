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


   
