import sys
from .runtask import Runtask
from .pythonenvironment import PythonEnvironment
from .clean import Cleaner

def main():
    commands = {
        "clean": Cleaner(),
        "-p" : PythonEnvironment(),
        "run" : Runtask()
        
    } 
    command = sys.argv[1:]

    handler = commands.get(command[0])

    if handler is None:
        print("Invalid command")
        return
    args = sys.argv[2:]

    handler.execute(args)
    