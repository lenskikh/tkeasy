#ask folder - gui widget
from tkeasy import *

title("Ask folder")

def readname():
    print (memory["filename"])

labels("ASK FOLDER","white","16","green",0,0,"center")

buttons(text='FOLDER BROWSER',command=selectfolder,row=2,column=0,sticky="center")

buttons("Print Name Of Folder",command=readname,row=3,column=0,sticky="center")

root.mainloop()
