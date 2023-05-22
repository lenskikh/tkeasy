import os
import glob
from tkeasy import TKeasy

gui = TKeasy()
gui.Title("ListBox")
gui.config(size="200x600")
list = glob.glob("*.*")

def show_info():
    pth = gui.listbox_item_selected("Listbox")
    gui.msg_box_warning("PATH", os.path.abspath(pth))
   
gui.listbox(height=30,width=35, padx = 5, pady = 5)
gui.listbox_insert(name= "Listbox", text = list)

gui.button(text="Get selected",command=show_info,row=1)

gui.loop()
