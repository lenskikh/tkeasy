import os
import glob
from tkeasy import *

title("ListBox")

text = glob.glob("*.*")
listbox(name="listbox",row=0,column=0,text=text)

app_loop()
