import os
import glob
from tkeasy import *

title("ListBox")

top_menu_demo()

text = glob.glob("*.*")
listbox(name="listbox",row=0,column=0,text=text)

app_loop()
