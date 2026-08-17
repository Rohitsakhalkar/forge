from datetime import datetime
from forge.database import Database


class App:
    def __init__(self):
        self.task = {}

    def execute(self,args):
        commands = {
            "add" : self.add_app,
            "delete": self.delete_app
        }
        command = commands.get(args[1])
        if command:
            command(args)
        elif args[1] == "show":
            self.show_apps()
        else:
            print("Invalid command")

    def add_app(self,args):
        try:
            started_at = datetime.now()
            appname = args[2]
            appexe = args[3]
            data = {
                "appname" : appname,
                "appexe" : appexe,
            }
            db = Database()
            db.save_apps(data)
            db.save_task(started_at, taskname = f"Executed {args}",status = "completed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            db.save_task(started_at, taskname = f"Executed {args}",status = "failed",ended_at = datetime.now())

    def delete_app(self,args):
        try:
            started_at = datetime.now()
            appname = args[2]
            db = Database()
            data = db.load_apps()
            if appname in data:
                del data[appname]
                db.save_altered_data(data)
                db.save_task(started_at, taskname = f"Executed {args}",status = "completed",ended_at = datetime.now())
            else:
                print("no app was found")
                db.save_task(started_at, taskname = f"Executed {args}",status = "failed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            db.save_task(started_at, taskname = f"Executed {args}",status = "failed",ended_at = datetime.now())


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

    