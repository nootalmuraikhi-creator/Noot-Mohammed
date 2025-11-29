import os
import subprocess
user_input = input("Enter a command to run: ")
subprocess.run(user_input, shell=False)
import os
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
subprocess.call("ls -la", shell=True)
allowed_commands = ["ls", "pwd", "whoami"]  

user_input = input("Enter a command to run: ")

if user_input in allowed_commands:
    subprocess.run(user_input, shell=False)
else:
    print("Command not allowed!")
