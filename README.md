# Forge 

 # **Built by Sakhalkar, in search of meaning.**

Forge is a Python-based command-line automation toolkit designed to bring common development and system operations under one CLI.

It started as a simple Python environment manager and evolved into a small automation framework capable of managing Python environments, performing file operations, and launching applications directly from the terminal.



## Features

### Python Environment Management

Forge can manage Python environments without requiring you to manually remember multiple commands.

- Create virtual environments
- Install Python packages
- Upgrade packages
- Uninstall packages
- Run Python scripts inside the managed environment

Example:

```bash
forge -p venv .venv
forge -p install requests
forge -p upgrade requests
forge -p uninstall requests
forge -p run <filename.py>
```
### File Operations

 Forge provides CLI-based file management operations.

 Current operations include:

- Create files
- Delete files
- Create directories
- Remove directories
- Generate unique file names
- Perform file-related utility operations

```bash
forge create <filename>
forge delete <filename>
forge rename <filename>
forge sort <path> or current directory
forge list
forge show
forge copy <source> <distination>
forge mkdir <folder name or path>
forge rmdir <folder name or path>
```
### Application 

Forge can launch applications directly from the terminal using registered application paths.'

Save your own apps in so you can launch from terminal with appname and the extension file name

for example apps.json contains
```
{
    "chrome": "chrome.exe",
    "spotify": "spotify.exe",
    "vscode": "Code.exe",
}
```
you can add your own with a valid .exe file 

Instead of navigating through folders or the Start Menu:

```bash
forge run vscode
forge app add <application_name> <applicationname.exe>
forge delete <applcation_name>
forge show 
```


Forge resolves the configured executable and launches the application.

Application paths are stored in Forge's local database {exe.json}.

### Scanner

Forge will scan your folder {Windows,Program Files,Program Files (x86)} for executable files 

```bash
forge scan
```

this will scan the folder for executable files and store the path in the exe.json
 for example of exe.json
 ```
 {
    "vscode": "C:\\Program Files\\Microsoft VS Code\\Code.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}
```
## Technology Stack

Forge is primarily written in Python.

Core technologies and standard-library components include:

- Python
- pathlib
- subprocess
- venv
- JSON
- pyproject.toml
- CLI argument parsing

Forge intentionally relies heavily on Python's standard library wherever practical.

## Why Forge?

Modern development often involves repeatedly switching between tools and commands.

- Create an environment.
- Install dependencies.
- Run a script.
- Create some files.
- Launch an application.
- Forge aims to bring these small operations into one place.

The goal isn't to replace existing tools.
The goal is to forge a layer of automation on top of them.

## Architecture

Forge is designed as a modular Python application.
```
                    ┌──────────────┐
                    │     CLI      │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Python Environment   File Operations   Application System
        │                  │                  │
        │                  │            ┌─────┴─────┐
        │                  │            │           │
        │                  │            ▼           ▼
        │                  │        App Manager   Scanner
        │                  │            │           │
        └──────────────────┼────────────┴───────────┘
                           │
                           ▼
                       Database
                           │
                           ▼
                         JSON
```
Each module has a specific responsibility.

This allows Forge to grow without turning the entire project into a single large Python file.

## Project Structure

The project currently follows a modular structure similar to:
```
forge/
│
├── forge/
│   ├── app/
│   │    ├── __init__.py
│   │    └── app.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── exe.json
│   │   ├── history.json
│   │   └── apps.json
│   │
│   ├── fileoperations/
│   │   ├── __init__.py
│   │   └── file_operations.py
│   │
│   ├── pythonenvironment/
│   │   ├── __init__.py
│   │   └── python_environment.py
│   │
│   ├── runtask/
│   │   ├── __init__.py
│   │   └── runtask.py
│   │
│   └── scanner/
│       ├── __init__.py
│       └── executable_scanner.py
│
├── clean.py
├── cli.py
├── .gitignore   
├── pyproject.toml
└── README.md
```
## Database

Forge currently uses lightweight JSON files for local data.

One of these is:
database/exe.json
which stores executable information.

Why JSON?
For the current stage of the project, JSON provides:

- Simple structure
- Human-readable data
- No external database dependency
- Easy debugging
- Easy modification
- Simple Python integration

The database layer can later be replaced or extended if Forge's requirements grow.

## Current Limitations

Forge is still an experimental project.

Current limitations include:

- Primarily Windows-oriented functionality
- Application paths may be machine-specific
- CLI syntax is still evolving
- Error handling can be improved
- Configuration management is still basic
- Cross-platform support is limited
- The application database currently requires management of executable paths

## Contributing

Forge is currently primarily a personal development project, but ideas, bug reports, and improvements are welcome.

If you find a bug:

- Reproduce it.
- Document the command and environment.
- Describe the expected behavior.
- Describe the actual behavior.
- Open an issue.

Pull requests should preferably focus on one feature or fix at a time.

### Installation
**Requirements**

Forge is currently designed primarily for:

- Windows
- Python 3.x
- Git

Clone the repository:
```bash
git clone https://github.com/Rohitsakhalkar/forge.git
```
Navigate into the project:
```bash
cd forge
```
Create a virtual environment:
```bash
python -m venv .venv
```
Activate it on Windows:
```bash
.venv\Scripts\activate
```
Install the project dependencies:
```bash
python -m pip install -e .
```
### License

License information will be added as the project evolves.

### Author
Rohit Rajan Sakhalkar

### Forge

Forge is still being built.

V1 established the foundation.

V2 is where the machinery gets interesting.

