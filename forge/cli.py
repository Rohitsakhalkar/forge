import sys
from .runtask import Runtask
from .pythonenvironment import PythonEnvironment
from .clean import Cleaner
from .fileoperation import FileOperation

def main():
    commands = {
        "clean": Cleaner(),
        "-p" : PythonEnvironment(),
        "run" : Runtask(),
        "create": FileOperation(),
        "delete": FileOperation(),
        "sort": FileOperation(),
        "list": FileOperation(),
        "show" : FileOperation(),
        "rename": FileOperation(),
        "copy" : FileOperation(),
        "mkdir": FileOperation(),
        "rmdir": FileOperation() 
        
    } 
    command = sys.argv[1:]

    handler = commands.get(command[0])

    if handler is None:
        print("Invalid command")
        return
    args = sys.argv[1:]

    handler.execute(args)
    