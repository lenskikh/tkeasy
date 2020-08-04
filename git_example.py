from tkeasy import *
import subprocess

title(window="main", text="Git fast push")
label(window="main",text="Small app for fast github push",row=0,column=0)

process = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

def commit(text):
    process = subprocess.Popen(["git", "commit","-m "+ text], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
    push()

def push():
    process = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
    
def info():
    text = get_info("commit")
    print(text)
    commit(text)
    
choices = ["Minor changes","Added comments",
           "Some names have been changed"]

dropdown_list(window="main",variable="commit",choices=choices,
             default="Commit",row=1,column=0)

button(window="main",text="Get Info",
       command=info,row=2,column=0)




