from pathlib import Path

class Executable:

     def execute(self,args):
        commands = {
             "scan": self.scan_exe
         }
        command = commands.get(args[0])
        if command:
            command()
        else:
            print("Invalid commnd")

     def scan_exe(self):
        scannable_paths ={
            "program_files":  "c:/Program Files" 
                      }
        print(scannable_paths)
        for keys, path in scannable_paths.items():
            print(keys)
            path = Path(path)
            for root , dirs, files in path.walk():
                 
                 for file in files:
                     
                     full_path = root/file
                     if full_path.suffix == ".exe":
                         if full_path.name == 'chrome.exe':
                             print(full_path)
                         
