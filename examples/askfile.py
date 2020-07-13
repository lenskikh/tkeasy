#ask folder - gui widget
from tkeasy import *

title_size(title="Ask folder")

def readname():
    print (memory["filename"])

labels(text="ASK FILE",colortext="white",font="16",
       background="BLUE",row=0,column=0,sticky="center")

buttons(text='FILE BROWSER',command=selectfile,
        row=2,column=0,sticky="center")

buttons(text="Print Name Of File",command=readname,
        row=3,column=0,sticky="center")
