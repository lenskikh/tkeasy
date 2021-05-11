#ask folder - gui widget
from tkeasy import *

title(text="Ask file")

def showfile():
    print (select_file())

label(text="ASK FILE",colortext="white",
      background="BLUE",row=0,column=0)

button(text="FILE BROWSER",
       command=showfile,row=1,column=0)

app_loop()
