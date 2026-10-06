import sys
from .runtask import Runtask
from .pythonenvironment import PythonEnvironment
from .clean import Cleaner
from .fileoperation import FileOperation
from .scanner import Executable
from .app import App

def main():
    try:
        file_operation = FileOperation()
        python_environment = PythonEnvironment()
        cleaner = Cleaner()
        runtask = Runtask()
        executable_scanner = Executable()
        app = App()
        commands = {
            "clean": (cleaner.clean_history, 0),
            "-p" : (python_environment.execute, 2),
            "run" : (runtask.run_task, 1),
            "create": (file_operation.add_file, 1),
            "delete": (file_operation.delete_file, 1),
            "sort": (file_operation.sort_files, 0),
            "list": (file_operation.list_dir, 0),
            "show" : (file_operation.file_content, 1),
            "rename": (file_operation.rename, 2),
            "copy" : (file_operation.copy, 2),
            "mkdir": (file_operation.create_folder, 1),
            "rmdir": (file_operation.remove_folder, 1), 
            "scan": (executable_scanner.scan_exe, 0),
            "app" : (app.execute, 2)
        } 
        command = sys.argv[1]
        if command in commands:
            handler, needed_args = commands.get(command)
        else:
            print("Invalid command")
            return
        
        args = sys.argv[2:]
        if needed_args == len(args):
            handler(*args)
        else:
            print(f"missing argument required {needed_args} given {len(args)}")
    except IndexError :
        print("you have Invalid command or No command")
    
        
