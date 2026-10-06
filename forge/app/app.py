from datetime import datetime
from forge.database import Database


class App:
    def __init__(self):
        self.task = {}

    def execute(self,command,*args):
        commands = {
            "add" : (self.add_app, 2),
            "delete": (self.delete_app, 1),
            "show": (self.show_apps, 0)
        }
        if command in commands:
            handler, needed_args = commands.get(command)
            if len(args) == needed_args: 
                handler(*args)
            else:
                print(f"missing argument required {needed_args} given {len}")
        else:
            print("Invalid command")

    def add_app(self,appname,appexe):
        try:
            started_at = datetime.now()
            data = {
                "appname" : appname,
                "appexe" : appexe,
            }
            db = Database()
            db.save_apps(data)
            db.save_task(started_at, taskname = f"Executed {appname,appexe}",status = "completed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            db.save_task(started_at, taskname = f"Executed {appname,appexe}",status = "failed",ended_at = datetime.now())

    def delete_app(self,appname):
        try:
            started_at = datetime.now()
            db = Database()
            data = db.load_apps()
            if appname in data:
                del data[appname]
                db.save_altered_data(data)
                db.save_task(started_at, taskname = f"Executed {appname}",status = "completed",ended_at = datetime.now())
            else:
                print("no app was found")
                db.save_task(started_at, taskname = f"Executed {appname}",status = "failed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            db.save_task(started_at, taskname = f"Executed {appname}",status = "failed",ended_at = datetime.now())


    def show_apps(self):
        try:
            started_at = datetime.now()
            db = Database()
            data = db.load_apps()
            for apps in data.keys():
                print(apps)
            db.save_task(started_at, taskname = f"Executed show apps",status = "completed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            db.save_task(started_at, taskname = f"Executed show apps", status = "failed", ended_at = datetime.now())

    