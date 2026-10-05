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
            "clean": cleaner.clean_history,
            "-p" : python_environment.execute,
            "run" : runtask.run_task,
            "create": file_operation.add_file,
            "delete": file_operation.delete_file,
            "sort": file_operation.sort_files,
            "list": file_operation.list_dir,
            "show" : file_operation.file_content,
            "rename": file_operation.rename,
            "copy" : file_operation.copy,
            "mkdir": file_operation.create_folder,
            "rmdir": file_operation.remove_folder, 
            "scan": executable_scanner.scan_exe,
            "app" : app.execute
        } 
        command = sys.argv[1]
        handler = commands.get(command)
        if handler is None:
            print("Invalid command")
            return
        
        args = sys.argv[2:]
        handler(*args)
    except IndexError :
        print("you have Invalid command or No command")
    
        
