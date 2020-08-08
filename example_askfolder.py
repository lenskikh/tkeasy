#ask folder - gui widget
from tkeasy import *

#root is default var of Tk
title(text="Ask Folder")
geometry(size="150x80")

def readname():
    print(get_info("folder"))

label(text="ASK FOLDER",colortext="white",
      background="green",row=0,column=0)

button(text='FOLDER BROWSER',command=select_folder,
       row=1,column=0,sticky="center")

button(text="Print Name Of Folder",
       command=readname,row=3,column=0,
       sticky="center")

app_loop()