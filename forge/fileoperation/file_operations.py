
from forge.database import Database 
from pathlib import Path
from datetime import datetime
import shutil

class FileOperation:

    def __init__(self):
        self.task = {}

    def execute(self,args):
        commands = {
            "create" : self.add_file,
            "delete" : self.delete_file,
            "sort" : self.sort_files,
            "list" : self.list_dir,
            "show" : self.file_content,
            "rename": self.rename,
            "copy": self.copy,
            "mkdir": self.create_folder,
            "rmdir":self.remove_folder
        }
        command = commands.get(args[0])
        if command:
            command(args)
        else:
            print("Invalid command")

    def create_folder(self, args):
        try:
            started_at = datetime.now()
            path = Path(args[1])
            if path.exists():
               print("folder Exist")
               self.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())
            else:
                Path(path).mkdir(parents = True , exist_ok = True)
                self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def remove_folder(self,args):
        try:
            started_at = datetime.now()
            path = Path(args[1])
            if any(path.iterdir()):
                print("The folder consists of:")
                for i, dir, files in path.walk():
                    print(f"root: {i}")
                    print(f"directories: {dir}")
                    print(f"files: {files}", end = "\n\n")
                confirm = input("do you want to delete all [y/n]").lower()
                if confirm == 'y':
                    shutil.rmtree(path)
                    self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else:
                    print("Terminated by user")
                    self.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())
            else:
                path.rmdir()
                self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                
        except Exception as e:
            print(f"task failed: {e}")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def add_file(self,args):
        try:
            started_at = datetime.now()
            path = Path(args[1])
            folder_name = path.parent
            file_name = path.name
            if folder_name.exists():
    
                if  Path(folder_name/file_name).exists():
                    
                    file_name = self._unique_name(args[1])
                    Path(folder_name/file_name).touch()
                    self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else:
                    Path(folder_name/file_name).touch()
                    self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
            else:
                confirm = input(f"{folder_name} doesn't exisit do you want to create [y/n]").lower()
                if confirm == 'y':
                    Path(folder_name).mkdir(parents = True, exist_ok = True)
                    Path(folder_name/file_name).touch()
                    self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else :
                    print("File creation terminated") 
                    self.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())

        except Exception as e:
            print(f"task failed: {e}")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def delete_file(self,args):
        try:   
            started_at = datetime.now()
            path = Path(args[1])
            if path.exists():
                path.unlink()
                self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
            else:
                print("No such file exist")
                self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

        except Exception as e:
            print(f"task failed: {e}")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def list_dir(self,args):
        try:
            started_at = datetime.now()
            path = Path().cwd()
            for i in path.iterdir():
                print(i.name)
            self.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def sort_files(self,args):
        print("sort files")

    def file_content(self,args):
        print("display file content")

    def _unique_name(self,filepath):

        path = Path(filepath)
        folder_path = path.parent
        filename = path.stem
        extension = path.suffix
        counter = 1
        new_file = path.name
        
        while Path(folder_path/new_file).exists():
            new_file = f"{filename}_{counter}{extension}"
            counter += 1

        return new_file

    def rename(self,args):
        print("rename")

    def copy(self,args):
        print("copy")

    def save_task(self, started_at, taskname, status, ended_at):
        duration =  ended_at - started_at
        self.task = {
            "taskname":taskname,
            "status": status,
            "started_at":str(started_at),
            "ended_at":str(ended_at),
            "duration":str(duration)
        }
        db = Database()
        db.save_history(self.task)
        