from tkeasy import *
import subprocess

title(window="main", text="Git fast push")
label(window="main",text="It's small app for fast push",row=0,column=0)
process = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "commit","-m minor"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)