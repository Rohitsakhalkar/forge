import sys
from .runtask import Runtask, PythonEnvironment


def main():
    commands = {
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
    