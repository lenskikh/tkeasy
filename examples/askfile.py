#ask folder - gui widget
from tkeasy import *

root.title("Ask file")
root.geometry("130x80")

def readname():
    print (memory["filename"])

labels(text="ASK FILE",colortext="white",
       background="BLUE",row=0,column=0)

button(text='FILE BROWSER',command=selectfile,
        row=2,column=0)

button(text="Print Name Of File",command=readname,
        row=3,column=0)
