#ask folder - gui widget
from tkeasy import *

title_size("Ask folder","")

def readname():
    print (memory["filename"])

labels("ASK FILE","white","16","BLUE",0,0,"center")

buttons(text='FILE BROWSER',command=selectfile,row=2,column=0,sticky="center")

buttons("Print Name Of File",command=readname,row=3,column=0,sticky="center")

root.mainloop()
