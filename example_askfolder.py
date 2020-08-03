#ask folder - gui widget
from tkeasy import *

#root is default var of Tk
title(window="main",text="Ask Folder")
geometry(window="main",size="150x80")

def readname():
    print(getinfo("folder"))

label(window="main",text="ASK FOLDER",colortext="white",
      background="green",row=0,column=0)

button(window="main", text='FOLDER BROWSER',
       command=selectfolder,row=1,column=0,
       sticky="center")

button(window="main",text="Print Name Of Folder",
       command=readname,row=3,column=0,
       sticky="center")
