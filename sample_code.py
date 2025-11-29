import os
import subprocess
user_input = input("Enter a command to run: ")
subprocess.run(user_input, shell=False)
import os
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
subprocess.call("ls -la", shell=True)
