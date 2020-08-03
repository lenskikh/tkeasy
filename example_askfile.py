#ask folder - gui widget
from tkeasy import *

title(window="main",text="Ask file")

def readname():
    print (get_info("file"))

label(window="main",text="ASK FILE",colortext="white",
      background="BLUE",row=0,column=0)

button(window="main",text="FILE BROWSER",
       command=select_file,row=1,column=0)

button(window="main",text="Print Name Of File",
       command=readname,row=2,column=0)


