#ask folder - gui widget
from tkeasy import *

#root is default var of Tk
root.title("Three entries")
root.geometry("150x80")

def readname():
    print (memory["filename"])

labels(text="ASK FOLDER",background="green",row=0,column=0)

buttons(text='FOLDER BROWSER',command=selectfolder,row=2,column=0,sticky="center")

buttons(text="Print Name Of Folder",command=readname,row=3,column=0,sticky="center")
