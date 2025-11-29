import os
import subprocess
user_input = input("Enter a command to run: ")
os.system(user_input)
USERNAME = "Noot"  # تم تغيير "admin" إلى "Noot"
PASSWORD = "12345"
subprocess.call("ls -la", shell=True)
