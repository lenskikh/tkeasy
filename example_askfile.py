#ask folder - gui widget
from tkeasy import *

title(text="Ask file")

top_menu_demo()

def readname():
    print (get_info("file"))

label(text="ASK FILE",colortext="white",
      background="BLUE",row=0,column=0)

button(text="FILE BROWSER",
       command=select_file,row=1,column=0)

button(text="Print Name Of File",
       command=readname,row=2,column=0)

app_loop()
