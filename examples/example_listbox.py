import os
import glob
from tkeasy import *

title("ListBox")
config(size="200x500")
text = glob.glob("*.*")

   
listbox(name="listbox",height=30,width=35,row=0,column=0,text=text)

app_loop()
