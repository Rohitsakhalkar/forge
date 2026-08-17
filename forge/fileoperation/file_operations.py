
from forge.database import Database 
from pathlib import Path
from datetime import datetime
import shutil

class FileOperation:

    def __init__(self):
        self.task = {}
        self.db = Database()

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
               self.db.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())
            else:
                Path(path).mkdir(parents = True , exist_ok = True)
                self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

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
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else:
                    print("Terminated by user")
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())
            else:
                path.rmdir()
                self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

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
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else:
                    Path(folder_name/file_name).touch()
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
            else:
                confirm = input(f"{folder_name} doesn't exisit do you want to create [y/n]").lower()
                if confirm == 'y':
                    Path(folder_name).mkdir(parents = True, exist_ok = True)
                    Path(folder_name/file_name).touch()
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
                else :
                    print("File creation terminated") 
                    self.db.save_task(started_at, taskname = f"Executed{args}", status = "terminated", ended_at = datetime.now())

        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def delete_file(self,args):
        try:   
            started_at = datetime.now()
            path = Path(args[1])
            if path.exists():
                path.unlink()
                self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
            else:
                print("No such file exist")
                self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def list_dir(self,args):
        try:
            started_at = datetime.now()
            path = Path().cwd()
            for i in path.iterdir():
                print(i.name)
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "Completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed{args}", status = "failed", ended_at = datetime.now())

    def sort_files(self,args):
        try:
            started_at = datetime.now()
            source_dir = Path(args[1]) if len(args)  > 1 else Path.cwd()
            file_types = {
                "Images":['.png','.jpg','.jpeg','.webp','.gif'],
                "Videos":['.mp4','.mkv','.avi'],
                "Documents":['.pdf','.docx','.txt','.pptx'],
                "Music":['.mp3','.wav']
            }
            for file in source_dir.iterdir():
                if file.is_dir():
                    continue
                extension = file.suffix.lower()
                for folder_name ,extensions in file_types.items():
                    if extension in extensions:
                        target_folder = source_dir/folder_name
                        target_folder.mkdir(exist_ok = True)
                        shutil.move(str(file),str(target_folder/file.name))
            self.db.save_task(started_at, taskname = f"Executed {args}",status = "completed",ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Executed {args}",status = "failed",ended_at = datetime.now())
            
    def file_content(self,args):
        try:
            started_at = datetime.now()
            content = Path(args[1]).read_text(encoding="utf-8")
            print(content)
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "failed", ended_at = datetime.now())

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
        try:
            started_at = datetime.now()
            Path(args[1]).rename(args[2])
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "completed", ended_at = datetime.now())
        except Exception as e:
            print(f"Task failed: {e}")
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "failed", ended_at = datetime.now())

    def copy(self,args):
        try:
            started_at = datetime.now()
            source = Path(args[1])
            destination = Path(f"{args[2]}/{source.name}")
            if source.is_dir():
                shutil.copytree(source, destination, dirs_exist_ok = True)
            else:
                shutil.copy2(args[1],args[2])
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "completed", ended_at = datetime.now())
        except Exception as e:
            print(f"task failed: {e}")
            self.db.save_task(started_at, taskname = f"Excuted {args}",status = "failed", ended_at = datetime.now())
