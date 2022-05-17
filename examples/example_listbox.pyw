import os
import glob
from tkeasy import *

title("ListBox")
config(size="200x600")
text = glob.glob("*.*")

def show_info():
    pth = listbox_item_selected("listbox")
    msg_box_warning("PATH", os.path.abspath(pth))
   
listbox(name="listbox",height=30,width=35,row=1,column=0,text=text)

button(text="Get selected",command=show_info,row=0,column=0)

app_loop()
