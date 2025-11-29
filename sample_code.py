import os
import subprocess
user_input = input("Enter a command to run: ")
subprocess.run(user_input, shell=False)
USERNAME = "Noot"  
PASSWORD = "12345"
subprocess.call("ls -la", shell=True)
